import string

import spacy
from nltk.corpus import wordnet as wn

import main.extract_process_elements as extract
import main.find_gateway_keywords as gateways
from main.objects.svoconstruct import SvoConstruct


def generate_intermediate_model(filename: str, directory: str, output_directory: str):
    conditional_words = ["if", "whether", "whereas", "whenever"]
    default_flow_words = ["otherwise", "optionally"]
    parallel_words = ["while", "meanwhile", "concurrently", "meantime"]

    full_filepath = directory + filename
    nlp = spacy.load("en")

    text = open(full_filepath).read().replace("\n", " ")
    doc = nlp(text)

    # elements extraction phase
    actors = []
    svos = []
    for sentence in doc.sents:
        out_actors, out_svos = extract.extract_process_elements(sentence)
        actors += out_actors
        svos += out_svos

    # semantic analysis - find possible gateway relations
    svos = gateways.find_gateway_keywords(doc, svos)
    svos.sort(key=lambda svo: svo.get_position(), reverse=False)
    '''
    with open(output_directory + filename + "_gateway_keywords", "w") as fi1e:
        for svo in svos:
            fi1e.write(svo.gateway_keyword_print() + "\n")
    '''

    # generate intermediate diagram model
    conditional_gateway_started = False
    parallel_gateway_started = False
    alphabet_suffix_index = 0

    with open(output_directory + filename + "_intermediate_model", "w") as fi1e:
        order = 0
        fi1e.write("Order,Activity,Condition,Who,Subprocess,Terminated\n")
        fi1e.write(str(order) + ",start,,,,,\n")
        while svos:
            svo, svos = (lambda list: (list[0], list[1:]))(svos)
            # check if this svo is a part of conditional gateway
            if svo.get_gateway_keyword() is not None and svo.get_gateway_keyword().casefold() in conditional_words:
                if parallel_gateway_started:
                    parallel_gateway_started = False
                if not conditional_gateway_started:
                    order += 1
                    conditional_gateway_started = True
                    alphabet_suffix_index = 0

                # create pair of condition and action
                condition = svo
                svo, svos = (lambda list: (list[0], list[1:]))(svos)

                suffix = string.ascii_lowercase[alphabet_suffix_index]

                if svo.get_actor() is not None and not svo.get_actor().is_anaphora():
                    fi1e.write(str(order) + suffix + "1," + svo.pretty_print() + "," +
                               condition.pretty_print() + "," + svo.get_actor().pretty_print() + ",,\n")
                else:
                    fi1e.write(str(order) + suffix + "1," + svo.pretty_print() + "," +
                               condition.pretty_print() + ",,,\n")

                alphabet_suffix_index += 1
            # check if this svo is a part of parallel gateway
            elif svo.get_gateway_keyword() is not None and svo.get_gateway_keyword().casefold() in parallel_words:
                if conditional_gateway_started:
                    conditional_gateway_started = False
                if not parallel_gateway_started:
                    order += 1
                    parallel_gateway_started = True
                    alphabet_suffix_index = 0
                suffix = string.ascii_lowercase[alphabet_suffix_index]
                if svo.get_actor() is not None and not svo.get_actor().is_anaphora():
                    fi1e.write(str(order) + suffix + "1," + svo.pretty_print() + ",,"
                               + svo.get_actor().pretty_print() + ",,\n")
                else:
                    fi1e.write(str(order) + suffix + "1," + svo.pretty_print() + ",,,,\n")
                alphabet_suffix_index += 1
                # Get the second task in parallel
                svo, svos = (lambda list: (list[0], list[1:]))(svos)
                suffix = string.ascii_lowercase[alphabet_suffix_index]
                if svo.get_actor() is not None and not svo.get_actor().is_anaphora():
                    fi1e.write(str(order) + suffix + "1," + svo.pretty_print() + ",,"
                               + svo.get_actor().pretty_print() + ",,\n")
                else:
                    fi1e.write(str(order) + suffix + "1," + svo.pretty_print() + ",,,,\n")
                alphabet_suffix_index += 1
            # treat task as a part of sequence
            elif svo.get_gateway_keyword() is not None and svo.get_gateway_keyword().casefold() in default_flow_words:
                # check if it is a default flow of gateway
                if parallel_gateway_started:
                    suffix = string.ascii_lowercase[alphabet_suffix_index]
                    if svo.get_actor() is not None and not svo.get_actor().is_anaphora():
                        fi1e.write(str(order) + suffix + "1," + svo.pretty_print() + ",,"
                                   + svo.get_actor().pretty_print() + ",,\n")
                    else:
                        fi1e.write(str(order) + suffix + "1," + svo.pretty_print() + ",,,,\n")
                    alphabet_suffix_index += 1
                elif conditional_gateway_started:
                    suffix = string.ascii_lowercase[alphabet_suffix_index]
                    if svo.get_actor() is not None and not svo.get_actor().is_anaphora():
                        fi1e.write(str(order) + suffix + "1," + svo.pretty_print() + ",else,"
                                   + svo.get_actor().pretty_print() + ",,\n")
                    else:
                        fi1e.write(str(order) + suffix + "1," + svo.pretty_print() + ",else,,,\n")
                    alphabet_suffix_index += 1
                # treat it like sequence flow
                else:
                    if conditional_gateway_started:
                        conditional_gateway_started = False
                        alphabet_suffix_index = 0
                    if parallel_gateway_started:
                        parallel_gateway_started = False
                        alphabet_suffix_index = 0
                    # validate if svo has proper actor attached
                    if svo.get_actor() and validate_svo_no_ignored_verb(svo):
                        order += 1
                        if svo.get_actor() is not None and not svo.get_actor().is_anaphora():
                            fi1e.write(str(order) + "," + svo.pretty_print() + ",," +
                                       svo.get_actor().pretty_print() + ",,\n")
                        else:
                            fi1e.write(str(order) + "," + svo.pretty_print() + ",,,,\n")
            else:
                if conditional_gateway_started:
                    # if conditional gateway has only one flow, add default flow which leads to end event
                    if alphabet_suffix_index < 2:
                        suffix = string.ascii_lowercase[alphabet_suffix_index]
                        tmp_order = order + 1
                        fi1e.write(str(order) + suffix + "1,goto " + str(tmp_order) + ",else,,,\n")
                        order = tmp_order
                        fi1e.write(str(order) + ",,,,,,yes\n")
                    conditional_gateway_started = False
                    alphabet_suffix_index = 0
                if parallel_gateway_started:
                    parallel_gateway_started = False
                    alphabet_suffix_index = 0
                # validate if svo has proper actor attached
                if svo.get_actor() and validate_svo_no_ignored_verb(svo):
                    if svo.get_actor() is not None and not svo.get_actor().is_anaphora():
                        order += 1
                        fi1e.write(str(order) + "," + svo.pretty_print() + ",," +
                                   svo.get_actor().pretty_print() + ",,\n")
                    else:
                        order += 1
                        fi1e.write(str(order) + "," + svo.pretty_print() + ",,,,\n")
        if conditional_gateway_started and alphabet_suffix_index < 2:
            suffix = string.ascii_lowercase[alphabet_suffix_index]
            tmp_order = order + 1
            fi1e.write(str(order) + suffix + "1,goto " + str(tmp_order) + ",else,,,\n")
        order += 1
        fi1e.write(str(order) + ",,,,,,yes\n")


def validate_svo_no_ignored_verb(svo: SvoConstruct) -> bool:
    ignore_verbs = ["be", "have", "do", "achieve", "start", "exist", "base"]

    base_verb = wn.morphy(svo.get_verb().text, wn.VERB)
    if base_verb is not None and base_verb.casefold() not in ignore_verbs:
        return True
    else:
        return False
