# coding=utf-8
"""
Participants extraction tests
"""

import unittest

import spacy

import main.extract_process_elements as extract
import main.utils as utils


class ParticipantsTests(unittest.TestCase):
    def test_example_phrase_one(self):
        filepath = "../examples/example_phrase_one"
        nlp = spacy.load("en")

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        participants = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            tmp_participants, svos = extract.extract_process_elements(sentence)
            participants.extend(tmp_participants)
            for participant in tmp_participants:
                print(utils.participant_print_full_name(participant))
        self.assertEqual(len(participants), 1, "Participants list length is incorrect")

    def test_example_phrase_two(self):
        filepath = "../examples/example_phrase_two"
        nlp = spacy.load("en")

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        participants = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            participants, svos = extract.extract_process_elements(sentence)
            for participant in participants:
                print(utils.participant_print_full_name(participant))
        self.assertEqual(len(participants), 1, "Participants list length is incorrect")

    def test_example_phrase_three(self):
        filepath = "../examples/example_phrase_three"
        nlp = spacy.load("en")

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        participants = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            participants, svos = extract.extract_process_elements(sentence)
            for participant in participants:
                print(utils.participant_print_full_name(participant))
        self.assertEqual(len(participants), 2, "Participants list length is incorrect")

    def test_example_phrase_four(self):
        filepath = "../examples/example_phrase_four"
        nlp = spacy.load("en")

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        participants = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            participants, svos = extract.extract_process_elements(sentence)
            for participant in participants:
                print(utils.participant_print_full_name(participant))
        self.assertEqual(len(participants), 2, "Participants list length is incorrect")

    def test_example_phrase_five(self):
        filepath = "../examples/example_phrase_five"
        nlp = spacy.load("en")

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        participants = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            participants, svos = extract.extract_process_elements(sentence)
            for participant in participants:
                print(utils.participant_print_full_name(participant))
        self.assertEqual(len(participants), 1, "Participants list length is incorrect")

    def test_example_phrase_six(self):
        filepath = "../examples/example_phrase_six"
        nlp = spacy.load("en")

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        participants = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            participants, svos = extract.extract_process_elements(sentence)
            for participant in participants:
                print(utils.participant_print_full_name(participant))
        self.assertEqual(len(participants), 0, "Participants list length is incorrect")

    def test_example_phrase_seven(self):
        filepath = "../examples/example_phrase_seven"
        nlp = spacy.load("en")

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        participants = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            participants, svos = extract.extract_process_elements(sentence)
            for participant in participants:
                print(utils.participant_print_full_name(participant))
        self.assertEqual(len(participants), 1, "Participants list length is incorrect")

    def test_example_phrase_eight(self):
        filepath = "../examples/example_phrase_eight"
        nlp = spacy.load("en")

        text = open(filepath).read().replace("\n", " ")
        doc = nlp(text)

        participants = []
        for sentence in doc.sents:
            [utils.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
            participants, svos = extract.extract_process_elements(sentence)
            for participant in participants:
                print(utils.participant_print_full_name(participant))
        self.assertEqual(len(participants), 2, "Participants list length is incorrect")


if __name__ == "__main__":
    unittest.main()
