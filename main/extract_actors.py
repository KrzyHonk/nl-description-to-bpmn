# coding=utf-8
"""
Function for extracting actors from sentence
"""
from typing import List

from spacy.tokens.span import Span
from spacy.tokens.token import Token

from main.objects.actor import Actor


def extract_actors(sentence: Span) -> List[Token]:
    output = []
    for word in sentence:
        if word.dep_ in ('agent', 'nsubj', 'nsubjpass'):
            object = word
            actor = Actor(object=object)
            output.append(actor)
            # output.append(find_conj.find_conjunctions(sentence, actor))
    return output
