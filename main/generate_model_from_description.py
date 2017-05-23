import os

import bpmn_python.bpmn_diagram_layouter as layouter
import bpmn_python.bpmn_diagram_rep as diagram
import spacy

import main.extract_elements as extract


def generate_intermediate_model(filename: str, directory: str, output_directory: str):
    ignore_verbs = ["be", "have", "do", "achieve", "start", "exist", "base"]
    conditional_words = ["if", "whether", "whereas"]
    default_flow_words = ["otherwise", "optionally"]
    parallel_words = ["while", "meanwhile", "concurrently", "meantime"]

    full_filepath = directory + filename
    nlp = spacy.load('en')

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
    for sentence in doc.sents:
        for word in sentence:
            if word.dep_ in ["mark", "advmod", "ccomp", "acl"]:
                head = word.head
                tmp_action = next((action for action in actions if action.get_position() == head.i), None)
                if tmp_action is not None:
                    tmp_action.set_marker(word.text)

    actions.sort(key=lambda action: action.get_position(), reverse=False)
    with open(output_directory + filename + "_markers", 'w') as fi1e:
        for action in actions:
            fi1e.write(action.marker_print() + "\n")

    # generate intermediate diagram model
    last_action_name = "start_event"
    conditional_gateway_started = True
    conditional_gateways = 0
    parallel_gateway_started = True
    parallel_gateways = 0
    gateway_actions = []

    with open(output_directory + filename + "_intermediate_model", 'w') as fi1e:
        while actions:
            action, actions = (lambda list: (list[0], list[1:]))(actions)
            # check if this action is a part of conditional gateway
            if action.get_marker() is not None and action.get_marker().casefold() in conditional_words:
                if parallel_gateway_started:
                    gateway_actions = []
                    parallel_gateway_started = False
                if not conditional_gateway_started:
                    conditional_gateways += 1
                    conditional_gateway_started = True
                    fi1e.write("sequence_flow:" + last_action_name + ":conditional_gateway_split" +
                               str(conditional_gateways) + "\n")
                    last_action_name = "conditional_gateway_join"
                # create pair of condition and action
                conditional_action = action
                action, actions = (lambda list: (list[0], list[1:]))(actions)
                fi1e.write("conditional_gateway:" + conditional_action.pretty_print() + ":" +
                           action.pretty_print() + "\n")
                gateway_actions.append((conditional_action, action))
            # check if this action is a part of parallel gateway
            elif action.get_marker() is not None and action.get_marker().casefold() in parallel_words:
                if conditional_gateway_started:
                    gateway_actions = []
                    conditional_gateway_started = False
                if not parallel_gateway_started:
                    parallel_gateways += 1
                    parallel_gateway_started = True
                    fi1e.write("sequence_flow:" + last_action_name + ":parallel_gateway_split" +
                               str(parallel_gateways) + "\n")
                    last_action_name = "parallel_gateway_join"
                fi1e.write("parallel_gateway:null:" + action.pretty_print() + "\n")
                gateway_actions.append(("null", action))
            # treat action as a part of sequence
            elif action.get_marker() is not None and action.get_marker().casefold() in default_flow_words:
                if parallel_gateway_started:
                    fi1e.write("parallel_gateway:default_flow:" + action.pretty_print() + "\n")
                    gateway_actions.append(("default", action))
                elif conditional_gateway_started:
                    fi1e.write("conditional_gateway:default_flow:" + action.pretty_print() + "\n")
                    gateway_actions.append(("default", action))
                # treat it like sequence flow
                else:
                    gateway_actions = []
                    if conditional_gateway_started:
                        conditional_gateway_started = False
                    if parallel_gateway_started:
                        parallel_gateway_started = False
                    # validate if action has proper actor attached
                    if action.get_actor():
                        fi1e.write("sequence_flow:" + last_action_name + ":" + action.pretty_print() + "\n")
                        last_action_name = action.pretty_print()
            else:
                gateway_actions = []
                if conditional_gateway_started:
                    conditional_gateway_started = False
                if parallel_gateway_started:
                    parallel_gateway_started = False
                # validate if action has proper actor attached
                if action.get_actor():
                    fi1e.write("sequence_flow:" + last_action_name + ":" + action.pretty_print() + "\n")
                    last_action_name = action.pretty_print()

    '''
    bpmn_graph = diagram.BpmnDiagramGraph()
    bpmn_graph.create_new_diagram_graph(diagram_name=filename)
    process_id = bpmn_graph.add_process_to_diagram()
    [source_id, _] = bpmn_graph.add_start_event_to_diagram(process_id, start_event_name="start_event")

    for action in actions:
        [target_id, _] = bpmn_graph.add_task_to_diagram(process_id, task_name=action.pretty_print())
        bpmn_graph.add_sequence_flow_to_diagram(process_id, source_id, target_id, "")
        source_id = target_id
    [end_id, _] = bpmn_graph.add_end_event_to_diagram(process_id, end_event_name="end_event")
    bpmn_graph.add_sequence_flow_to_diagram(process_id, source_id, end_id, "")
    layouter.generate_layout(bpmn_graph)
    bpmn_graph.export_xml_file(output_directory, filename + ".bpmn")
    '''
