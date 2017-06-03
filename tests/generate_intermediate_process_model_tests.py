# coding=utf-8
"""
Sentence decomposition tests
"""

import unittest

from main.main_script import nlp_description_to_bpmn


class GenerateProcessModelTests(unittest.TestCase):
    output_directory = "./output/models-test/"

    def test_presentation_example(self):
        example_directory = "../examples/"
        example_file = "example_phrase_seven"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_one(self):
        example_directory = "../models/"
        example_file = "model1"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_two(self):
        example_directory = "../models/"
        example_file = "model2"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_three(self):
        example_directory = "../models/"
        example_file = "model3"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_four(self):
        example_directory = "../models/"
        example_file = "model4"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_five(self):
        example_directory = "../models/"
        example_file = "model5"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_six(self):
        example_directory = "../models/"
        example_file = "model6"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_seven(self):
        example_directory = "../models/"
        example_file = "model7"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_eight(self):
        example_directory = "../models/"
        example_file = "model8"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_nine(self):
        example_directory = "../models/"
        example_file = "model9"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_ten(self):
        example_directory = "../models/"
        example_file = "model10"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_eleven(self):
        example_directory = "../models/"
        example_file = "model11"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_twelve(self):
        example_directory = "../models/"
        example_file = "model12"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_thirteen(self):
        example_directory = "../models/"
        example_file = "model13"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_fourteen(self):
        example_directory = "../models/"
        example_file = "model14"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_fifteen(self):
        example_directory = "../models/"
        example_file = "model15"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_sixteen(self):
        example_directory = "../models/"
        example_file = "model16"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_seventeen(self):
        example_directory = "../models/"
        example_file = "model17"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_eighteen(self):
        example_directory = "../models/"
        example_file = "model18"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_nineteen(self):
        example_directory = "../models/"
        example_file = "model19"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_twenty(self):
        example_directory = "../models/"
        example_file = "model20"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_twentyone(self):
        example_directory = "../models/"
        example_file = "model21"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_twentytwo(self):
        example_directory = "../models/"
        example_file = "model22"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_twentythree(self):
        example_directory = "../models/"
        example_file = "model23"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_twentyfour(self):
        example_directory = "../models/"
        example_file = "model24"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_twentyfive(self):
        example_directory = "../models/"
        example_file = "model25"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_twentysix(self):
        example_directory = "../models/"
        example_file = "model26"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_twentyseven(self):
        example_directory = "../models/"
        example_file = "model27"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_twentyeight(self):
        example_directory = "../models/"
        example_file = "model28"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_twentynine(self):
        example_directory = "../models/"
        example_file = "model29"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_thirty(self):
        example_directory = "../models/"
        example_file = "model30"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_thirtyone(self):
        example_directory = "../models/"
        example_file = "model31"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_thirtytwo(self):
        example_directory = "../models/"
        example_file = "model32"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_thirtythree(self):
        example_directory = "../models/"
        example_file = "model33"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_thirtyfour(self):
        example_directory = "../models/"
        example_file = "model34"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_thirtyfive(self):
        example_directory = "../models/"
        example_file = "model35"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_thirtysix(self):
        example_directory = "../models/"
        example_file = "model36"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_thirtyseven(self):
        example_directory = "../models/"
        example_file = "model37"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_thirtyeight(self):
        example_directory = "../models/"
        example_file = "model38"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_thirtynine(self):
        example_directory = "../models/"
        example_file = "model39"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_forty(self):
        example_directory = "../models/"
        example_file = "model40"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_fortyone(self):
        example_directory = "../models/"
        example_file = "model41"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_fortytwo(self):
        example_directory = "../models/"
        example_file = "model42"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_fortythree(self):
        example_directory = "../models/"
        example_file = "model43"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)


if __name__ == "__main__":
    unittest.main()
