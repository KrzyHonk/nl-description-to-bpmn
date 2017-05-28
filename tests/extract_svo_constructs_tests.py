# coding=utf-8
"""
SVO (subject-verb-object) construct extraction tests
"""

import unittest

import spacy

import main.extract_process_elements as extract
import main.utils as utils


class SubsentenceTests(unittest.TestCase):
    def test_example_phrase_one(self):
        filepath = "../examples/example_phrase_one"
        nlp = spacy.load("en")

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        svos = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            actors, svos = extract.extract_process_elements(sentence)
            for svo in svos:
                print(svo.pretty_print())
        self.assertEqual(len(svos), 2, "SVO list length is incorrect")

    def test_example_phrase_two(self):
        filepath = "../examples/example_phrase_two"
        nlp = spacy.load("en")

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        svos = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            actors, svos = extract.extract_process_elements(sentence)
            for svo in svos:
                print(svo.pretty_print())
        self.assertEqual(len(svos), 1, "SVO list length is incorrect")

    def test_example_phrase_three(self):
        filepath = "../examples/example_phrase_three"
        nlp = spacy.load("en")

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        svos = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            actors, svos = extract.extract_process_elements(sentence)
            for svo in svos:
                print(svo.pretty_print())
        self.assertEqual(len(svos), 4, "SVO list length is incorrect")

    def test_example_phrase_four(self):
        filepath = "../examples/example_phrase_four"
        nlp = spacy.load("en")

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        svos = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            actors, svos = extract.extract_process_elements(sentence)
            for svo in svos:
                print(svo.pretty_print())
        self.assertEqual(len(svos), 2, "SVO list length is incorrect")

    def test_example_phrase_five(self):
        filepath = "../examples/example_phrase_five"
        nlp = spacy.load("en")

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        svos = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            actors, svos = extract.extract_process_elements(sentence)
            for svo in svos:
                print(svo.pretty_print())
        self.assertEqual(len(svos), 2, "SVO list length is incorrect")

    def test_example_phrase_six(self):
        filepath = "../examples/example_phrase_six"
        nlp = spacy.load("en")

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        svos = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            actors, svos = extract.extract_process_elements(sentence)
            for svo in svos:
                print(svo.pretty_print())
        self.assertEqual(len(svos), 1, "SVO list length is incorrect")

    def test_example_phrase_seven(self):
        filepath = "../examples/example_phrase_seven"
        nlp = spacy.load("en")

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        svos = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            actors, svos = extract.extract_process_elements(sentence)
            for svo in svos:
                print(svo.pretty_print())
        self.assertEqual(len(svos), 2, "SVO list length is incorrect")

    def test_example_phrase_eight(self):
        filepath = "../examples/example_phrase_eight"
        nlp = spacy.load("en")

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        svos = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            actors, svos = extract.extract_process_elements(sentence)
            for svo in svos:
                print(svo.pretty_print())
        self.assertEqual(len(svos), 3, "SVO list length is incorrect")


if __name__ == "__main__":
    unittest.main()
