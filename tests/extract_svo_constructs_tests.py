# coding=utf-8
"""
Actorsextraction tests
"""

import unittest

import spacy

import main.extract_elements as extract
import main.utils as utils


class SubsentenceTests(unittest.TestCase):
    def test_example_phrase_one(self):
        filepath = "../examples/example_phrase_one"
        nlp = spacy.load('en')

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        actions = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            actors, actions = extract.extract_elements(sentence)
            for action in actions:
                print(action.pretty_print())
        self.assertEqual(len(actions), 2, "Action list length is incorrect")

    def test_example_phrase_two(self):
        filepath = "../examples/example_phrase_two"
        nlp = spacy.load('en')

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        actions = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            actors, actions = extract.extract_elements(sentence)
            for action in actions:
                print(action.pretty_print())
        self.assertEqual(len(actions), 1, "Action list length is incorrect")

    def test_example_phrase_three(self):
        filepath = "../examples/example_phrase_three"
        nlp = spacy.load('en')

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        actions = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            actors, actions = extract.extract_elements(sentence)
            for action in actions:
                print(action.pretty_print())
        self.assertEqual(len(actions), 4, "Action list length is incorrect")

    def test_example_phrase_four(self):
        filepath = "../examples/example_phrase_four"
        nlp = spacy.load('en')

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        actions = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            actors, actions = extract.extract_elements(sentence)
            for action in actions:
                print(action.pretty_print())
        self.assertEqual(len(actions), 1, "Action list length is incorrect")

    def test_example_phrase_five(self):
        filepath = "../examples/example_phrase_five"
        nlp = spacy.load('en')

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        actions = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            actors, actions = extract.extract_elements(sentence)
            for action in actions:
                print(action.pretty_print())
        self.assertEqual(len(actions), 2, "Action list length is incorrect")

    def test_example_phrase_six(self):
        filepath = "../examples/example_phrase_six"
        nlp = spacy.load('en')

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        actions = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            actors, actions = extract.extract_elements(sentence)
            for action in actions:
                print(action.pretty_print())
        self.assertEqual(len(actions), 1, "Action list length is incorrect")

    def test_example_phrase_seven(self):
        filepath = "../examples/example_phrase_seven"
        nlp = spacy.load('en')

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        actions = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            actors, actions = extract.extract_elements(sentence)
            for action in actions:
                print(action.pretty_print())
        self.assertEqual(len(actions), 2, "Action list length is incorrect")

    def test_example_phrase_eight(self):
        filepath = "../examples/example_phrase_eight"
        nlp = spacy.load('en')

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        actions = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            actors, actions = extract.extract_elements(sentence)
            for action in actions:
                print(action.pretty_print())
        self.assertEqual(len(actions), 3, "Action list length is incorrect")


if __name__ == '__main__':
    unittest.main()
