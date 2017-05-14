# coding=utf-8
"""
Sentence decomposition tests
"""

import unittest

import bpmn_python.bpmn_diagram_layouter as layouter
import bpmn_python.bpmn_diagram_rep as diagram
import main.generate_model_from_description as generate
import spacy

import main.extract_elements as extract


class GenerateProcessModelTests(unittest.TestCase):
    output_directory = "./output/models-test/"

    def test_presentation_example(self):
        example_directory = "../examples/"
        example_file = "example_phrase_seven"
        generate.generate_model(example_file, example_directory, self.output_directory)

    def test_model_one(self):
        example_directory = "../models/"
        example_file = "model_1"
        generate.generate_model(example_file, example_directory, self.output_directory)

    def test_model_two(self):
        example_directory = "../models/"
        example_file = "model_2"
        generate.generate_model(example_file, example_directory, self.output_directory)

    def test_model_three(self):
        example_directory = "../models/"
        example_file = "model_3"
        generate.generate_model(example_file, example_directory, self.output_directory)

    def test_model_four(self):
        example_directory = "../models/"
        example_file = "model_4"
        generate.generate_model(example_file, example_directory, self.output_directory)

    def test_model_five(self):
        example_directory = "../models/"
        example_file = "model_5"
        generate.generate_model(example_file, example_directory, self.output_directory)

    def test_model_six(self):
        example_directory = "../models/"
        example_file = "model_6"
        generate.generate_model(example_file, example_directory, self.output_directory)

    def test_model_seven(self):
        example_directory = "../models/"
        example_file = "model_7"
        generate.generate_model(example_file, example_directory, self.output_directory)

    def test_model_eight(self):
        example_directory = "../models/"
        example_file = "model_8"
        generate.generate_model(example_file, example_directory, self.output_directory)

    def test_model_nine(self):
        example_directory = "../models/"
        example_file = "model_9"
        generate.generate_model(example_file, example_directory, self.output_directory)

    def test_model_ten(self):
        example_directory = "../models/"
        example_file = "model_10"
        generate.generate_model(example_file, example_directory, self.output_directory)


if __name__ == '__main__':
    unittest.main()
