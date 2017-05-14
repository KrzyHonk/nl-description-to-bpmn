# coding=utf-8
"""
Actorsextraction tests
"""

import unittest

import spacy

import main.extract_elements as extract
import main.utils as utils


class ActorsTests(unittest.TestCase):
    def test_example_phrase_one(self):
        filepath = "../examples/example_phrase_one"
        nlp = spacy.load('en')

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        actors = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            tmp_actors, actions = extract.extract_elements(sentence)
            actors.extend(tmp_actors)
            for actor in tmp_actors:
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
            actors, actions = extract.extract_elements(sentence)
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
            actors, actions = extract.extract_elements(sentence)
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
            actors, actions = extract.extract_elements(sentence)
            for actor in actors:
                print(actor.pretty_print())
        self.assertEqual(len(actors), 3, "Actors list length is incorrect")

    def test_example_phrase_five(self):
        filepath = "../examples/example_phrase_five"
        nlp = spacy.load('en')

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        actors = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            actors, actions = extract.extract_elements(sentence)
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
            actors, actions = extract.extract_elements(sentence)
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
            actors, actions = extract.extract_elements(sentence)
            for actor in actors:
                print(actor.pretty_print())
        self.assertEqual(len(actors), 1, "Actors list length is incorrect")

    def test_example_phrase_eight(self):
        filepath = "../examples/example_phrase_eight"
        nlp = spacy.load('en')

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        actors = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            actors, actions = extract.extract_elements(sentence)
            for actor in actors:
                print(actor.pretty_print())
        self.assertEqual(len(actors), 2, "Actors list length is incorrect")


if __name__ == '__main__':
    unittest.main()
