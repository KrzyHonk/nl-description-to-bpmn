# coding=utf-8
"""
Actorsextraction tests
"""

import unittest

import spacy

import main.extract_actors as act_extr
import main.utils as utils


class ActorsTests(unittest.TestCase):
    def test_example_phrase_one(self):
        filepath = "../examples/example_phrase_one"
        nlp = spacy.load('en')

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        outcome = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            outcome = act_extr.extract_actors(sentence)
            for actor in outcome:
                print(actor.pretty_print())
        self.assertEqual(len(outcome), 2, "Actors list length is incorrect")

    def test_example_phrase_two(self):
        filepath = "../examples/example_phrase_two"
        nlp = spacy.load('en')

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        outcome = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            outcome = act_extr.extract_actors(sentence)
            for actor in outcome:
                print(actor.pretty_print())
        self.assertEqual(len(outcome), 1, "Actors list length is incorrect")

    def test_example_phrase_four(self):
        filepath = "../examples/example_phrase_four"
        nlp = spacy.load('en')

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        outcome = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            outcome = act_extr.extract_actors(sentence)
            for actor in outcome:
                print(actor.pretty_print())
        self.assertEqual(len(outcome), 2, "Actors list length is incorrect")

    def test_example_phrase_five(self):
        filepath = "../examples/example_phrase_five"
        nlp = spacy.load('en')

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        outcome = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            outcome = act_extr.extract_actors(sentence)
            for actor in outcome:
                print(actor.pretty_print())
        self.assertEqual(len(outcome), 2, "Actors list length is incorrect")

    def test_example_phrase_six(self):
        filepath = "../examples/example_phrase_three"
        nlp = spacy.load('en')

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        outcome = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            outcome = act_extr.extract_actors(sentence)
            for actor in outcome:
                print(actor.pretty_print())
        self.assertEqual(len(outcome), 4, "Actors list length is incorrect")


if __name__ == '__main__':
    unittest.main()
