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
    root = sentence.root
    nsubj_list = dep.find_tokens_with_dependencies_for_token_in_subtree(root, ["nsubj"])
    dobj_list = dep.find_tokens_with_dependencies_for_token_in_subtree(root, ["dobj"])
    nsubjpass_list = dep.find_tokens_with_dependencies_for_token_in_subtree(root, ["nsubjpass"])
    if len(nsubj_list) > 0:
        for word in nsubj_list:
            output_obj = None
            subject = word
            verb = subject.head
            complements_list = dep.find_tokens_with_dependencies_for_token_in_subtree(verb, ["xcomp", "acomp", "ccomp",
                                                                                             "pcomp"])
            for complement in complements_list:
                if complement.head == verb:
                    output_obj = complement
            action = Action(subject=subject, verb=verb, object=output_obj)
            output.append(action)
    elif len(dobj_list) > 0:
        for word in dobj_list:
            subject = word
            verb = subject.head
            action = Action(subject=subject, verb=verb)
            output.append(action)
    elif len(nsubjpass_list) > 0:
        for word in nsubjpass_list:
            subject = word
            verb = subject.head
            action = Action(subject=subject, verb=verb)
            output.append(action)
    output += extract_actions_from_conjunction(sentence)
    return output


def extract_actions_from_conjunction(sentence: Span) -> List[Action]:
    output = []
    for word in sentence:
        if word.dep_ in ('conj'):
            main_pred = word.head
            complements_list = dep.find_tokens_with_dependencies_for_token_in_subtree(word, ["acomp", "ccomp", "pcomp",
                                                                                             "dobj", "obj", "pobj",
                                                                                             "attr"])
            for complement in complements_list:
                output_obj = complements_list[0]
                for child in main_pred.children:
                    if child.dep_ in ('nsubj', 'nsubjpass'):
                        subject = child
                        verb = word
                        action = Action(subject=subject, verb=verb, object=output_obj)
                        output.append(action)
    return output
