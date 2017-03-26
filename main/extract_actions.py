# coding=utf-8
"""
Function for extracting actions from sentence
"""
from typing import List

from spacy.tokens.span import Span
from spacy.tokens.token import Token

import main.find_tokens_with_dependency as dep
from main.objects.action import Action


def extract_actions(sentence: Span) -> List[Action]:
    output = []
    for word in sentence:
        if word.dep_ in ('nsubj'):
            subject = word
            verb = subject.head
            output_obj = None
            complements_list = dep.find_tokens_with_dependencies_for_token(verb, ["xcomp", "acomp", "ccomp", "pcomp"])
            if len(complements_list) > 0 and complements_list[0].head == verb:
                verb = complements_list[0]
                nsubj_list = dep.find_tokens_with_dependencies_for_token(verb, ["nsubj"])
                obj_list = dep.find_tokens_with_dependencies_for_token(verb, ["dobj", "obj", "pobj", "iobj"])
                if len(nsubj_list) > 0:
                    subject = nsubj_list[0]
                if len(obj_list) > 0:
                    output_obj = obj_list[0]
            action = Action(subject=subject, verb=verb, object=output_obj)
            output.append(action)
            output += extract_actions_from_conjunction(action, sentence)
        elif word.dep_ in ('dobj'):
            subject = word
            verb = subject.head
            action = Action(subject=subject, verb=verb)
            output.append(action)
            output += extract_actions_from_conjunction(action, sentence)
        elif word.dep_ in ('nsubjpass'):
            subject = word
            verb = subject.head
            action = Action(subject=subject, verb=verb)
            output.append(action)
            output += extract_actions_from_conjunction(action, sentence)
    return output


def extract_actions_from_conjunction(action: Token, sentence: Span) -> List[Action]:
    output = []
    for word in sentence:
        if word.dep_ in ('conj'):
            main_pred = word.head
            complements_list = dep.find_tokens_with_dependencies_for_token(word, ["acomp", "ccomp", "pcomp",
                                                                                  "dobj", "obj", "pobj", "attr"])
            output_obj = complements_list[0]
            for child in main_pred.children:
                if child.dep_ in ('nsubj', 'nsubjpass'):
                    subject = child
                    verb = word
                    action = Action(subject=subject, verb=verb, object=output_obj)
                    output.append(action)
    return output
