# coding=utf-8
"""
Function for finding all tokens with given dependency
"""
from typing import List

from spacy.tokens.span import Span
from spacy.tokens.token import Token


def find_tokens_with_dependencies_in_sentence(sentence: Span, dependencies: List[str]) -> List[Token]:
    output = []
    for word in sentence:
        if word.dep_ in dependencies:
            output.append(word)
    return output


def find_tokens_with_dependencies_for_token(token: Token, dependencies: List[str]) -> List[Token]:
    output = []
    for word in token.subtree:
        if word.dep_ in dependencies:
            output.append(word)
    return output
