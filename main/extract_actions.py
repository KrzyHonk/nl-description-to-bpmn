# coding=utf-8
"""
Function for extracting actions from sentence
"""
from typing import List

from spacy.tokens.span import Span

import main.find_tokens_with_dependency as dep
from main.objects.action import Action


def extract_actions(sentence: Span) -> List[Action]:
    output = []
    for word in sentence:
        if word.dep_ in ('nsubj'):
            subject = word
            verb = word.head
            output_obj = None
            complements_list = dep.find_tokens_with_dependencies(sentence, ["acomp", "ccomp", "pcomp", "dobj", "obj", "attr"])
            if len(complements_list) > 0 and complements_list[0].head == verb:
                output_obj = complements_list[0]
                action = Action(subject=subject, verb=verb, object=output_obj)
                output.append(action)
        elif word.dep_ in ('nsubjpass'):
            # Todo sprawdzanie 'auxpass'?
            subject = word
            verb = word.head
            action = Action(subject=subject, verb=verb)
            output.append(action)
    return output
