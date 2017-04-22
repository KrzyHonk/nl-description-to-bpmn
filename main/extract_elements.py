# coding=utf-8
"""
Function for extracting elements from sentence
"""
from typing import List

from spacy.tokens.span import Span
from spacy.tokens.token import Token

from main.extract_actions import extract_actions
from main.extract_actors import extract_actors


def extract_elements(sentence: Span) -> (List[Token], List[Token]):
    actors = extract_actors(sentence)
    actions = extract_actions(sentence, actors)

    return actors, actions
