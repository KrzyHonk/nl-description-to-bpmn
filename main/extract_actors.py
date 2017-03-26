# coding=utf-8
"""
Function for extracting actors from sentence
"""
from typing import List

from spacy.tokens.span import Span

from main.objects.actor import Actor


def extract_actors(sentence: Span) -> List[Actor]:
    output = []
    for word in sentence:
        if word.dep_ in ('nsubj'):
            object = word
            actor = Actor(object=object)
            output.append(actor)
        elif word.dep_ in ('agent'):
            for token in word.children:
                if token.dep_ in ('pobj'):
                    object = token
                    actor = Actor(object=object)
                    output.append(actor)
    output += extract_actors_from_conjunction(sentence)
    return output


def extract_actors_from_conjunction(sentence: Span) -> List[Actor]:
    output = []
    for word in sentence:
        if word.dep_ in ('conj'):
            for token in word.children:
                if token.dep_ in ('pobj', 'dobj', 'iobj'):
                    object = token
                    actor = Actor(object=object)
                    output.append(actor)
    return output
