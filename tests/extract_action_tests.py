# coding=utf-8
"""
Actorsextraction tests
"""

import unittest

import spacy

import main.extract_actions as act_extr
import main.utils as utils


class SubsentenceTests(unittest.TestCase):
    def test_action_example_two(self):
        model_one_filepath = "../examples/action_example_two"
        nlp = spacy.load('en')

        text = open(model_one_filepath).read().replace("\n", " ")
        doc = nlp(text)

        outcome = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            outcome = act_extr.extract_actions(sentence)
            for action in outcome:
                print(action.pretty_print())
        self.assertEqual(len(outcome), 1, "Actors list length is incorrect")

    def test_conjunction_example_one(self):
        model_one_filepath = "../examples/conjunction_example_one"
        nlp = spacy.load('en')

        text = open(model_one_filepath).read().replace("\n", " ")
        doc = nlp(text)

        outcome = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            outcome = act_extr.extract_actions(sentence)
            for action in outcome:
                print(action.pretty_print())
        self.assertEqual(len(outcome), 1, "Actors list length is incorrect")

    def test_conjunction_example_two(self):
        # Should be spliced into two sentences
        action_example_one = "../examples/conjunction_example_two"
        nlp = spacy.load('en')

        text = open(action_example_one).read().replace("\n", " ")
        doc = nlp(text)

        outcome = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            outcome = act_extr.extract_actions(sentence)
            for action in outcome:
                print(action.pretty_print())
        self.assertEqual(len(outcome), 1, "Action list length is incorrect")


if __name__ == '__main__':
    unittest.main()
