# coding=utf-8
"""
Subsentence decomposition function
"""
from typing import List

from spacy.tokens.span import Span


def subsentence_extraction(sentence: Span) -> List[Span]:
    output_sentences = []

    for word in sentence:
        if (word.dep_ in ("csubj", "csubjpass", "xcomp", "ccomp", "advcl", "acl", "conj", "cc"))\
                or word.dep_ == "punct" and word.text != ".":
            new_sentence = sentence[word.left_edge.i: word.right_edge.i + 1]
            output_sentences.append(new_sentence)
            break

    return output_sentences
