import os

import bpmn_python.bpmn_diagram_layouter as layouter
import bpmn_python.bpmn_diagram_rep as diagram
import spacy

import main.extract_elements as extract


def generate_model(filename: str, directory: str, output_directory: str):
    ignore_verbs = ["be", "have", "do", "achieve", "start", "exist", "base"]
    conditional_words = ["if", "whether", "whereas", "otherwise", "optionally"]
    conditional_phrases = ["in case of", "in the case of", "in case", "for the case"]
    parallel_phrases = ["while", "meanwhile", "concurrently", "meantime"]
    sequence_phrases = ["then", "after", "afterward", "subsequently", "thus"]

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

            '''
            if word.dep_ in ["prep", "relcl"]:
                head = word.head
                tmp_action = next((action for action in actions if action.get_position() == head.i), None)
                if tmp_action is not None:
                    tmp_action.set_marker(word.text)
            '''

    with open(output_directory + filename + "_markers", 'w') as fi1e:
        for action in actions:
            fi1e.write(action.marker_print() + os.linesep)

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
