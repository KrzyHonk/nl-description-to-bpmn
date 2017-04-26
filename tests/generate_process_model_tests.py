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

    def test_presentation_example(self):
        example_filepath = "../examples/example_phrase_seven"
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
        bpmn_graph.create_new_diagram_graph(diagram_name="presentation_example")
        process_id = bpmn_graph.add_process_to_diagram()
        [source_id, _] = bpmn_graph.add_start_event_to_diagram(process_id, start_event_name="start_event")
        for action in actions:
            [target_id, _] = bpmn_graph.add_task_to_diagram(process_id, task_name=action.pretty_print())
            bpmn_graph.add_sequence_flow_to_diagram(process_id, source_id, target_id, "")
            source_id = target_id
        [end_id, _] = bpmn_graph.add_end_event_to_diagram(process_id, end_event_name="end_event")
        bpmn_graph.add_sequence_flow_to_diagram(process_id, source_id, end_id, "")
        layouter.generate_layout(bpmn_graph)
        bpmn_graph.export_xml_file(self.output_directory, "presentation_example.bpmn")

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

    def test_model_two(self):
        example_filepath = "../models/model_2.txt"
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
        bpmn_graph.create_new_diagram_graph(diagram_name="model_2")
        process_id = bpmn_graph.add_process_to_diagram()
        [source_id, _] = bpmn_graph.add_start_event_to_diagram(process_id, start_event_name="start_event")
        for action in actions:
            [target_id, _] = bpmn_graph.add_task_to_diagram(process_id, task_name=action.pretty_print())
            bpmn_graph.add_sequence_flow_to_diagram(process_id, source_id, target_id, "")
            source_id = target_id
        [end_id, _] = bpmn_graph.add_end_event_to_diagram(process_id, end_event_name="end_event")
        bpmn_graph.add_sequence_flow_to_diagram(process_id, source_id, end_id, "")
        layouter.generate_layout(bpmn_graph)
        bpmn_graph.export_xml_file(self.output_directory, "model_2.bpmn")

    def test_model_three(self):
        example_filepath = "../models/model_3.txt"
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
        bpmn_graph.create_new_diagram_graph(diagram_name="model_3")
        process_id = bpmn_graph.add_process_to_diagram()
        [source_id, _] = bpmn_graph.add_start_event_to_diagram(process_id, start_event_name="start_event")
        for action in actions:
            [target_id, _] = bpmn_graph.add_task_to_diagram(process_id, task_name=action.pretty_print())
            bpmn_graph.add_sequence_flow_to_diagram(process_id, source_id, target_id, "")
            source_id = target_id
        [end_id, _] = bpmn_graph.add_end_event_to_diagram(process_id, end_event_name="end_event")
        bpmn_graph.add_sequence_flow_to_diagram(process_id, source_id, end_id, "")
        layouter.generate_layout(bpmn_graph)
        bpmn_graph.export_xml_file(self.output_directory, "model_3.bpmn")

    def test_model_four(self):
        example_filepath = "../models/model_4.txt"
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
        bpmn_graph.create_new_diagram_graph(diagram_name="model_4")
        process_id = bpmn_graph.add_process_to_diagram()
        [source_id, _] = bpmn_graph.add_start_event_to_diagram(process_id, start_event_name="start_event")
        for action in actions:
            [target_id, _] = bpmn_graph.add_task_to_diagram(process_id, task_name=action.pretty_print())
            bpmn_graph.add_sequence_flow_to_diagram(process_id, source_id, target_id, "")
            source_id = target_id
        [end_id, _] = bpmn_graph.add_end_event_to_diagram(process_id, end_event_name="end_event")
        bpmn_graph.add_sequence_flow_to_diagram(process_id, source_id, end_id, "")
        layouter.generate_layout(bpmn_graph)
        bpmn_graph.export_xml_file(self.output_directory, "model_4.bpmn")

    def test_model_five(self):
        example_filepath = "../models/model_5.txt"
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
        bpmn_graph.create_new_diagram_graph(diagram_name="model_5")
        process_id = bpmn_graph.add_process_to_diagram()
        [source_id, _] = bpmn_graph.add_start_event_to_diagram(process_id, start_event_name="start_event")
        for action in actions:
            [target_id, _] = bpmn_graph.add_task_to_diagram(process_id, task_name=action.pretty_print())
            bpmn_graph.add_sequence_flow_to_diagram(process_id, source_id, target_id, "")
            source_id = target_id
        [end_id, _] = bpmn_graph.add_end_event_to_diagram(process_id, end_event_name="end_event")
        bpmn_graph.add_sequence_flow_to_diagram(process_id, source_id, end_id, "")
        layouter.generate_layout(bpmn_graph)
        bpmn_graph.export_xml_file(self.output_directory, "model_5.bpmn")

    def test_model_six(self):
        example_filepath = "../models/model_6.txt"
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
        bpmn_graph.create_new_diagram_graph(diagram_name="model_6")
        process_id = bpmn_graph.add_process_to_diagram()
        [source_id, _] = bpmn_graph.add_start_event_to_diagram(process_id, start_event_name="start_event")
        for action in actions:
            [target_id, _] = bpmn_graph.add_task_to_diagram(process_id, task_name=action.pretty_print())
            bpmn_graph.add_sequence_flow_to_diagram(process_id, source_id, target_id, "")
            source_id = target_id
        [end_id, _] = bpmn_graph.add_end_event_to_diagram(process_id, end_event_name="end_event")
        bpmn_graph.add_sequence_flow_to_diagram(process_id, source_id, end_id, "")
        layouter.generate_layout(bpmn_graph)
        bpmn_graph.export_xml_file(self.output_directory, "model_6.bpmn")

    def test_model_seven(self):
        example_filepath = "../models/model_7.txt"
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
        bpmn_graph.create_new_diagram_graph(diagram_name="model_7")
        process_id = bpmn_graph.add_process_to_diagram()
        [source_id, _] = bpmn_graph.add_start_event_to_diagram(process_id, start_event_name="start_event")
        for action in actions:
            [target_id, _] = bpmn_graph.add_task_to_diagram(process_id, task_name=action.pretty_print())
            bpmn_graph.add_sequence_flow_to_diagram(process_id, source_id, target_id, "")
            source_id = target_id
        [end_id, _] = bpmn_graph.add_end_event_to_diagram(process_id, end_event_name="end_event")
        bpmn_graph.add_sequence_flow_to_diagram(process_id, source_id, end_id, "")
        layouter.generate_layout(bpmn_graph)
        bpmn_graph.export_xml_file(self.output_directory, "model_7.bpmn")

    def test_model_eight(self):
        example_filepath = "../models/model_8.txt"
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
        bpmn_graph.create_new_diagram_graph(diagram_name="model_8")
        process_id = bpmn_graph.add_process_to_diagram()
        [source_id, _] = bpmn_graph.add_start_event_to_diagram(process_id, start_event_name="start_event")
        for action in actions:
            [target_id, _] = bpmn_graph.add_task_to_diagram(process_id, task_name=action.pretty_print())
            bpmn_graph.add_sequence_flow_to_diagram(process_id, source_id, target_id, "")
            source_id = target_id
        [end_id, _] = bpmn_graph.add_end_event_to_diagram(process_id, end_event_name="end_event")
        bpmn_graph.add_sequence_flow_to_diagram(process_id, source_id, end_id, "")
        layouter.generate_layout(bpmn_graph)
        bpmn_graph.export_xml_file(self.output_directory, "model_8.bpmn")

    def test_model_nine(self):
        example_filepath = "../models/model_9.txt"
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
        bpmn_graph.create_new_diagram_graph(diagram_name="model_9")
        process_id = bpmn_graph.add_process_to_diagram()
        [source_id, _] = bpmn_graph.add_start_event_to_diagram(process_id, start_event_name="start_event")
        for action in actions:
            [target_id, _] = bpmn_graph.add_task_to_diagram(process_id, task_name=action.pretty_print())
            bpmn_graph.add_sequence_flow_to_diagram(process_id, source_id, target_id, "")
            source_id = target_id
        [end_id, _] = bpmn_graph.add_end_event_to_diagram(process_id, end_event_name="end_event")
        bpmn_graph.add_sequence_flow_to_diagram(process_id, source_id, end_id, "")
        layouter.generate_layout(bpmn_graph)
        bpmn_graph.export_xml_file(self.output_directory, "model_9.bpmn")

    def test_model_ten(self):
        example_filepath = "../models/model_10.txt"
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
        bpmn_graph.create_new_diagram_graph(diagram_name="model_10")
        process_id = bpmn_graph.add_process_to_diagram()
        [source_id, _] = bpmn_graph.add_start_event_to_diagram(process_id, start_event_name="start_event")
        for action in actions:
            [target_id, _] = bpmn_graph.add_task_to_diagram(process_id, task_name=action.pretty_print())
            bpmn_graph.add_sequence_flow_to_diagram(process_id, source_id, target_id, "")
            source_id = target_id
        [end_id, _] = bpmn_graph.add_end_event_to_diagram(process_id, end_event_name="end_event")
        bpmn_graph.add_sequence_flow_to_diagram(process_id, source_id, end_id, "")
        layouter.generate_layout(bpmn_graph)
        bpmn_graph.export_xml_file(self.output_directory, "model_10.bpmn")


if __name__ == '__main__':
    unittest.main()
