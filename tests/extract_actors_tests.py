# coding=utf-8
"""
Actorsextraction tests
"""

import unittest

import spacy

import main.extract_actors as act_extr
import main.utils as utils
import main.sentence_decompositon as decomp


class ActorsTests(unittest.TestCase):
    def test_example_phrase_one(self):
        filepath = "../examples/example_phrase_one"
        nlp = spacy.load('en')

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        actors = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            actors, actions = decomp.sentence_decomposition(sentence)
            for actor in actors:
                print(actor.pretty_print())
        self.assertEqual(len(actors), 2, "Actors list length is incorrect")

    def test_example_phrase_two(self):
        filepath = "../examples/example_phrase_two"
        nlp = spacy.load('en')

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        actors = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            actors, actions = decomp.sentence_decomposition(sentence)
            for actor in actors:
                print(actor.pretty_print())
        self.assertEqual(len(actors), 1, "Actors list length is incorrect")

    def test_example_phrase_three(self):
        filepath = "../examples/example_phrase_three"
        nlp = spacy.load('en')

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        actors = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            actors, actions = decomp.sentence_decomposition(sentence)
            for actor in actors:
                print(actor.pretty_print())
        self.assertEqual(len(actors), 4, "Actors list length is incorrect")

    def test_example_phrase_four(self):
        filepath = "../examples/example_phrase_four"
        nlp = spacy.load('en')

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        actors = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            actors, actions = decomp.sentence_decomposition(sentence)
            for actor in actors:
                print(actor.pretty_print())
        self.assertEqual(len(actors), 2, "Actors list length is incorrect")

    def test_example_phrase_five(self):
        filepath = "../examples/example_phrase_five"
        nlp = spacy.load('en')

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        actors = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            actors, actions = decomp.sentence_decomposition(sentence)
            for actor in actors:
                print(actor.pretty_print())
        self.assertEqual(len(actors), 2, "Actors list length is incorrect")


    def test_example_phrase_six(self):
        filepath = "../examples/example_phrase_six"
        nlp = spacy.load('en')

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        actors = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            actors, actions = decomp.sentence_decomposition(sentence)
            for actor in actors:
                print(actor.pretty_print())
        self.assertEqual(len(actors), 0, "Actors list length is incorrect")

    def test_example_phrase_seven(self):
        filepath = "../examples/example_phrase_seven"
        nlp = spacy.load('en')

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        actors = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            actors, actions = decomp.sentence_decomposition(sentence)
            for actor in actors:
                print(actor.pretty_print())
        self.assertEqual(len(actors), 1, "Actors list length is incorrect")


if __name__ == '__main__':
    unittest.main()
