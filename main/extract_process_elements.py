# coding=utf-8
"""
Function for extracting elements from sentence
"""
from typing import List

from spacy.tokens.span import Span
from spacy.tokens.token import Token

from main.extract_participants import extract_participants
from main.extract_svo_constructs import extract_svo_constructs


def extract_process_elements(sentence: Span) -> (List[Token], List[Token]):
    participants = extract_participants(sentence)
    svos = extract_svo_constructs(sentence, participants)

    return participants, svos
