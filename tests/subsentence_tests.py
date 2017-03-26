# coding=utf-8
"""
Subsentence extraction tests
"""

import unittest

import spacy

import main.subsentence_extraction as decomp


class SubsentenceTests(unittest.TestCase):
    def test_simple_subsentence_example_one(self):
        # Should be spliced into two sentences
        model_one_filepath = "../examples/example_phrase_one"
        nlp = spacy.load('en')

        text = open(model_one_filepath).read().replace("\n", " ")
        doc = nlp(text)

        outcome = []
        for sentence in doc.sents:
            outcome = decomp.subsentence_extraction(sentence)
        self.assertEqual(len(outcome), 1, "Subsentence list length is incorrect")

    def test_complex_subsentence_example_one(self):
        # Should be spliced into two sentences
        model_one_filepath = "../examples/example_phrase_three"
        nlp = spacy.load('en')

        text = open(model_one_filepath).read().replace("\n", " ")
        doc = nlp(text)

        outcome = []
        for sentence in doc.sents:
            outcome = decomp.subsentence_extraction(sentence)
        self.assertEqual(len(outcome), 2, "Subsentence list length is incorrect")


if __name__ == '__main__':
    unittest.main()
