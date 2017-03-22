# coding=utf-8
"""
Sentence decomposition tests
"""

import unittest

import spacy

import main.sentence_decompositon as decomp
from main import utils


class SentenceDecompositionTests(unittest.TestCase):
    def test_model_one(self):
        example_filepath = "../models/model_1.txt"
        nlp = spacy.load('en')

        text = open(example_filepath).read().replace("\n", " ")
        doc = nlp(text)

        for sentence in doc.sents:
            actors, actions = decomp.sentence_decomposition(sentence)
            for actor in actors:
                print("ACTOR:", actor.pretty_print())
            for action in actions:
                print("ACTION:", action.pretty_print())


if __name__ == '__main__':
    unittest.main()
