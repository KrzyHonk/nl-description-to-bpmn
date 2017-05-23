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
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_one(self):
        example_directory = "../models/"
        example_file = "model_1"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_two(self):
        example_directory = "../models/"
        example_file = "model_2"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_three(self):
        example_directory = "../models/"
        example_file = "model_3"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_four(self):
        example_directory = "../models/"
        example_file = "model_4"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_five(self):
        example_directory = "../models/"
        example_file = "model_5"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_six(self):
        example_directory = "../models/"
        example_file = "model_6"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_seven(self):
        example_directory = "../models/"
        example_file = "model_7"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_eight(self):
        example_directory = "../models/"
        example_file = "model_8"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_nine(self):
        example_directory = "../models/"
        example_file = "model_9"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_ten(self):
        example_directory = "../models/"
        example_file = "model_10"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_eleven(self):
        example_directory = "../models/"
        example_file = "model_11"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_twelve(self):
        example_directory = "../models/"
        example_file = "model_12"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_thirteen(self):
        example_directory = "../models/"
        example_file = "model_13"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_fourteen(self):
        example_directory = "../models/"
        example_file = "model_14"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_fifteen(self):
        example_directory = "../models/"
        example_file = "model_15"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_sixteen(self):
        example_directory = "../models/"
        example_file = "model_16"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_seventeen(self):
        example_directory = "../models/"
        example_file = "model_17"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_eighteen(self):
        example_directory = "../models/"
        example_file = "model_18"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_nineteen(self):
        example_directory = "../models/"
        example_file = "model_19"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_twenty(self):
        example_directory = "../models/"
        example_file = "model_20"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_twentyone(self):
        example_directory = "../models/"
        example_file = "model_21"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_twentytwo(self):
        example_directory = "../models/"
        example_file = "model_22"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_twentythree(self):
        example_directory = "../models/"
        example_file = "model_23"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_twentyfour(self):
        example_directory = "../models/"
        example_file = "model_24"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_twentyfive(self):
        example_directory = "../models/"
        example_file = "model_25"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_twentysix(self):
        example_directory = "../models/"
        example_file = "model_26"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_twentyseven(self):
        example_directory = "../models/"
        example_file = "model_27"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_twentyeight(self):
        example_directory = "../models/"
        example_file = "model_28"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_twentynine(self):
        example_directory = "../models/"
        example_file = "model_29"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_thirty(self):
        example_directory = "../models/"
        example_file = "model_30"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_thirtyone(self):
        example_directory = "../models/"
        example_file = "model_31"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_thirtytwo(self):
        example_directory = "../models/"
        example_file = "model_32"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_thirtythree(self):
        example_directory = "../models/"
        example_file = "model_33"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_thirtyfour(self):
        example_directory = "../models/"
        example_file = "model_34"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_thirtyfive(self):
        example_directory = "../models/"
        example_file = "model_35"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_thirtysix(self):
        example_directory = "../models/"
        example_file = "model_36"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_thirtyseven(self):
        example_directory = "../models/"
        example_file = "model_37"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_thirtyeight(self):
        example_directory = "../models/"
        example_file = "model_38"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_thirtynine(self):
        example_directory = "../models/"
        example_file = "model_39"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_forty(self):
        example_directory = "../models/"
        example_file = "model_40"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_fortyone(self):
        example_directory = "../models/"
        example_file = "model_41"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_fortytwo(self):
        example_directory = "../models/"
        example_file = "model_42"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)

    def test_model_fortythree(self):
        example_directory = "../models/"
        example_file = "model_43"
        generate.generate_intermediate_model(example_file, example_directory, self.output_directory)


if __name__ == '__main__':
    unittest.main()
