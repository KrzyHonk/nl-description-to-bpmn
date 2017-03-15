# coding=utf-8
"""
Function for extracting actors from sentence
"""
from spacy.tokens.span import Span
from spacy.tokens.token import Token
from typing import List
import main.find_conjunctions as find_conj
from main.objects.actor import Actor


def extract_actors(sentence: Span) -> List[Token]:
    output = []
    for word in sentence:
        print(word.text, word.dep_)
        if word.dep_ in ('agent', 'nsubj', 'nsubjpass'):
            # add new actor to the list and determine conjunctions
            actor = Actor(word)
            output.append(actor)
            output.append(find_conj.find_conjunctions(sentence, actor))
    return output
