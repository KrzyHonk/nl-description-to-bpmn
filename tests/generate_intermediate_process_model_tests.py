# coding=utf-8
"""
Sentence decomposition tests
"""
import os
import unittest

from main.main_script import nlp_description_to_bpmn
import bpmn_python.bpmn_diagram_rep as diagram
import bpmn_python.bpmn_diagram_layouter as layouter


class GenerateProcessModelTests(unittest.TestCase):
    output_directory = "./output/"
    output_directory_bpmn = "./output/bpmn/"

    def test_example_phrases(self):
        example_directory = "../examples/"
        examples = [
            "example_phrase_one",
            "example_phrase_two",
            "example_phrase_three",
            "example_phrase_four",
            "example_phrase_five",
            "example_phrase_six",
            "example_phrase_seven",
            "example_phrase_eight"
        ]
        for example_file in examples:
            nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

            bpmn_graph = diagram.BpmnDiagramGraph()
            bpmn_graph.load_diagram_from_csv_file(os.path.abspath(self.output_directory +
                                                                  example_file + "_intermediate_model.csv"))
            layouter.generate_layout(bpmn_graph)
            bpmn_graph.export_xml_file_no_di(self.output_directory_bpmn, example_file + "_no_di.bpmn")
            bpmn_graph.export_xml_file(self.output_directory_bpmn, example_file + ".bpmn")

    def test_thesis_models(self):
        example_directory = "../models/"
        examples = [
            "model1",
            "model2",
            "model3",
            "model4",
            "model5",
            "model6",
            "model7",
            "model8",
            "model9",
            "model10",
            "model11",
            "model12",
            "model13",
            "model14",
            "model15",
            "model16",
            "model17",
            "model18",
            "model19",
            "model20",
            "model21",
            "model22",
            "model23",
            "model24",
            "model25",
            "model26",
            "model27",
            "model28",
            "model29",
            "model30",
            "model31",
            "model32",
            "model33",
            "model34",
            "model35",
            "model36",
            "model37",
            "model38",
            "model39",
            "model40",
            "model41",
            "model42",
            "model43"
        ]
        for example_file in examples:
            nlp_description_to_bpmn(example_file + ".txt", example_directory, self.output_directory)

            bpmn_graph = diagram.BpmnDiagramGraph()
            bpmn_graph.load_diagram_from_csv_file(os.path.abspath(self.output_directory +
                                                                  example_file + "_intermediate_model.csv"))
            layouter.generate_layout(bpmn_graph)
            bpmn_graph.export_xml_file_no_di(self.output_directory_bpmn, example_file + "_no_di.bpmn")
            bpmn_graph.export_xml_file(self.output_directory_bpmn, example_file + ".bpmn")

if __name__ == "__main__":
    unittest.main()
