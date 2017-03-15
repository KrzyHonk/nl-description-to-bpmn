# coding=utf-8
"""
Actorsextraction tests
"""

import unittest

import spacy

import main.extract_actors as act_extr
import main.utils as utils


class ActorsTests(unittest.TestCase):
    def test_action_simple_example_one(self):
        # Should be spliced into two sentences
        model_one_filepath = "../examples/conjunction_example"
        nlp = spacy.load('en')

        text = open(model_one_filepath).read().replace("\n", " ")
        doc = nlp(text)

        outcome = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            outcome = act_extr.extract_actors(sentence)
        self.assertEqual(len(outcome), 1, "Subsentence list length is incorrect")


if __name__ == '__main__':
    unittest.main()