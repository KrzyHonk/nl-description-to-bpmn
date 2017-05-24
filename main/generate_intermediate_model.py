import string

import spacy

import main.extract_elements as extract
import main.find_gateway_keywords as gateways
from main.objects.action import Action
from nltk.corpus import wordnet as wn


def generate_intermediate_model(filename: str, directory: str, output_directory: str):
    conditional_words = ["if", "whether", "whereas"]
    default_flow_words = ["otherwise", "optionally"]
    parallel_words = ["while", "meanwhile", "concurrently", "meantime"]

    full_filepath = directory + filename
    nlp = spacy.load("en")

    text = open(full_filepath).read().replace("\n", " ")
    doc = nlp(text)

    # elements extraction phase
    actors = []
    actions = []
    for sentence in doc.sents:
        out_actors, out_actions = extract.extract_elements(sentence)
        actors += out_actors
        actions += out_actions

    # semantic analysis - find possible gateway relations
    actions = gateways.find_gateway_keywords(doc, actions)

    actions.sort(key=lambda action: action.get_position(), reverse=False)
    with open(output_directory + filename + "_markers", "w") as fi1e:
        for action in actions:
            fi1e.write(action.marker_print() + "\n")

    # generate intermediate diagram model
    last_action_name = "start_event"
    conditional_gateway_started = True
    parallel_gateway_started = True
    alphabet_suffix_index = 1

    with open(output_directory + filename + "_intermediate_model", "w") as fi1e:
        order = 0
        fi1e.write("Order,Activity,Condition,Who,Subprocess,Terminated\n")
        fi1e.write(str(order) + ",start,,,,,\n")
        while actions:
            action, actions = (lambda list: (list[0], list[1:]))(actions)
            # check if this action is a part of conditional gateway
            if action.get_marker() is not None and action.get_marker().casefold() in conditional_words:
                if parallel_gateway_started:
                    parallel_gateway_started = False
                if not conditional_gateway_started:
                    order += 1
                    conditional_gateway_started = True
                    alphabet_suffix_index = 1

                # create pair of condition and action
                conditional_action = action
                action, actions = (lambda list: (list[0], list[1:]))(actions)

                suffix = string.ascii_lowercase[alphabet_suffix_index]
                fi1e.write(str(order) + suffix + "1," + action.pretty_print() + "," + conditional_action.pretty_print()
                           + ",,,\n")
                alphabet_suffix_index += 1
            # check if this action is a part of parallel gateway
            elif action.get_marker() is not None and action.get_marker().casefold() in parallel_words:
                if conditional_gateway_started:
                    conditional_gateway_started = False
                if not parallel_gateway_started:
                    order += 1
                    parallel_gateway_started = True
                    alphabet_suffix_index = 1
                suffix = string.ascii_lowercase[alphabet_suffix_index]
                fi1e.write(str(order) + suffix + "1," + action.pretty_print() + ",,,,\n")
                alphabet_suffix_index += 1
            # treat action as a part of sequence
            elif action.get_marker() is not None and action.get_marker().casefold() in default_flow_words:
                if parallel_gateway_started:
                    suffix = string.ascii_lowercase[alphabet_suffix_index]
                    fi1e.write(str(order) + suffix + "1," + action.pretty_print() + ",,,,\n")
                elif conditional_gateway_started:
                    suffix = string.ascii_lowercase[alphabet_suffix_index]
                    fi1e.write(str(order) + suffix + "1," + action.pretty_print() + ",else,,,\n")
                # treat it like sequence flow
                else:
                    if conditional_gateway_started:
                        conditional_gateway_started = False
                        alphabet_suffix_index = 1
                    if parallel_gateway_started:
                        parallel_gateway_started = False
                        alphabet_suffix_index = 1
                    # validate if action has proper actor attached
                    if action.get_actor() and validate_action_no_ignored_verb(action):
                        order += 1
                        fi1e.write(str(order) + "," + action.pretty_print() + ",,,,\n")
            else:
                if conditional_gateway_started:
                    conditional_gateway_started = False
                    alphabet_suffix_index = 1
                if parallel_gateway_started:
                    parallel_gateway_started = False
                    alphabet_suffix_index = 1
                # validate if action has proper actor attached
                if action.get_actor() and validate_action_no_ignored_verb(action):
                    order += 1
                    fi1e.write(str(order) + "," + action.pretty_print() + ",,,,\n")


def validate_action_no_ignored_verb(action: Action) -> bool:
    ignore_verbs = ["be", "have", "do", "achieve", "start", "exist", "base"]

    base_verb = wn.morphy(action.get_verb().text, wn.VERB)
    if base_verb is not None and base_verb.casefold() not in ignore_verbs:
        return True
    else:
        return False
