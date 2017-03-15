# coding=utf-8
"""
Function for finding all tokens with given dependency
"""
from spacy.tokens.span import Span
from spacy.tokens.token import Token
from typing import List


def find_tokens_with_dependencies(sentence: Span, dependencies: List[str]) -> List[Token]:
    output = []
    for word in sentence:
        if word.dep_ in dependencies:
            output.append(word)
    return output
