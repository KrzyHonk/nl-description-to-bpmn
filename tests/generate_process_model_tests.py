# coding=utf-8
"""
Sentence decomposition tests
"""

import unittest

import spacy

import bpmn_python.bpmn_diagram_rep as diagram
import bpmn_python.bpmn_diagram_layouter as layouter
import main.sentence_decompositon as decomp


class GenerateProcessModelTests(unittest.TestCase):
    output_directory = "./output/models-test/"

    def test_model_one(self):
        example_filepath = "../models/model_1.txt"
        nlp = spacy.load('en')

        text = open(example_filepath).read().replace("\n", " ")
        doc = nlp(text)

        actors = []
        actions = []
        for sentence in doc.sents:
            out_actors, out_actions = decomp.sentence_decomposition(sentence)
            actors += out_actors
            actions += out_actions

        bpmn_graph = diagram.BpmnDiagramGraph()
        bpmn_graph.create_new_diagram_graph(diagram_name="model_1")
        process_id = bpmn_graph.add_process_to_diagram()
        [source_id, _] = bpmn_graph.add_start_event_to_diagram(process_id, start_event_name="start_event")
        for action in actions:
            [target_id, _] = bpmn_graph.add_task_to_diagram(process_id, task_name=action.pretty_print())
            bpmn_graph.add_sequence_flow_to_diagram(process_id, source_id, target_id, "")
            source_id = target_id
        [end_id, _] = bpmn_graph.add_end_event_to_diagram(process_id, end_event_name="end_event")
        bpmn_graph.add_sequence_flow_to_diagram(process_id, source_id, end_id, "")
        layouter.generate_layout(bpmn_graph)
        bpmn_graph.export_xml_file(self.output_directory, "model_1.bpmn")


if __name__ == '__main__':
    unittest.main()
