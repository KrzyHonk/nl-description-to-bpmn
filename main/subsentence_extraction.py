# coding=utf-8
"""
Subsentence decomposition function
"""
from typing import List

from spacy.tokens.span import Span


def subsentence_extraction(sentence: Span) -> List[Span]:
    output_sentences = []

    for word in sentence:
        if word.dep_ in ('csubj', 'csubjpass', 'xcomp', 'ccomp', 'advcl', 'acl'):
            output_sentences.append(sentence[word.left_edge.i: word.right_edge.i + 1])

    return output_sentences
