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
        example_file = "model1.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_two(self):
        example_directory = "../models/"
        example_file = "model2.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_three(self):
        example_directory = "../models/"
        example_file = "model3.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_four(self):
        example_directory = "../models/"
        example_file = "model4.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_five(self):
        example_directory = "../models/"
        example_file = "model5.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_six(self):
        example_directory = "../models/"
        example_file = "model6.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_seven(self):
        example_directory = "../models/"
        example_file = "model7.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_eight(self):
        example_directory = "../models/"
        example_file = "model8.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_nine(self):
        example_directory = "../models/"
        example_file = "model9.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_ten(self):
        example_directory = "../models/"
        example_file = "model10.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_eleven(self):
        example_directory = "../models/"
        example_file = "model11.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_twelve(self):
        example_directory = "../models/"
        example_file = "model12.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_thirteen(self):
        example_directory = "../models/"
        example_file = "model13.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_fourteen(self):
        example_directory = "../models/"
        example_file = "model14.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_fifteen(self):
        example_directory = "../models/"
        example_file = "model15.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_sixteen(self):
        example_directory = "../models/"
        example_file = "model16.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_seventeen(self):
        example_directory = "../models/"
        example_file = "model17.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_eighteen(self):
        example_directory = "../models/"
        example_file = "model18.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_nineteen(self):
        example_directory = "../models/"
        example_file = "model19.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_twenty(self):
        example_directory = "../models/"
        example_file = "model20.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_twentyone(self):
        example_directory = "../models/"
        example_file = "model21.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_twentytwo(self):
        example_directory = "../models/"
        example_file = "model22.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_twentythree(self):
        example_directory = "../models/"
        example_file = "model23.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_twentyfour(self):
        example_directory = "../models/"
        example_file = "model24.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_twentyfive(self):
        example_directory = "../models/"
        example_file = "model25.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_twentysix(self):
        example_directory = "../models/"
        example_file = "model26.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_twentyseven(self):
        example_directory = "../models/"
        example_file = "model27.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_twentyeight(self):
        example_directory = "../models/"
        example_file = "model28.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_twentynine(self):
        example_directory = "../models/"
        example_file = "model29.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_thirty(self):
        example_directory = "../models/"
        example_file = "model30.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_thirtyone(self):
        example_directory = "../models/"
        example_file = "model31.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_thirtytwo(self):
        example_directory = "../models/"
        example_file = "model32.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_thirtythree(self):
        example_directory = "../models/"
        example_file = "model33.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_thirtyfour(self):
        example_directory = "../models/"
        example_file = "model34.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_thirtyfive(self):
        example_directory = "../models/"
        example_file = "model35.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_thirtysix(self):
        example_directory = "../models/"
        example_file = "model36.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_thirtyseven(self):
        example_directory = "../models/"
        example_file = "model37.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_thirtyeight(self):
        example_directory = "../models/"
        example_file = "model38.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_thirtynine(self):
        example_directory = "../models/"
        example_file = "model39.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_forty(self):
        example_directory = "../models/"
        example_file = "model40.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_fortyone(self):
        example_directory = "../models/"
        example_file = "model41.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_fortytwo(self):
        example_directory = "../models/"
        example_file = "model42.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)

    def test_model_fortythree(self):
        example_directory = "../models/"
        example_file = "model43.txt"
        nlp_description_to_bpmn(example_file, example_directory, self.output_directory)


if __name__ == "__main__":
    unittest.main()
