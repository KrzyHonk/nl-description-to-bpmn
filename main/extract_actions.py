# coding=utf-8
"""
Function for extracting actions from sentence
"""
from typing import List

from spacy.tokens.span import Span

import main.find_tokens_with_dependency as dep
from main.objects.action import Action
from main.objects.actor import Actor


def extract_actions(sentence: Span, actors: List[Actor]) -> List[Action]:
    tmp_output = []
    root = sentence.root
    nsubj_list = dep.find_tokens_with_dependencies_for_token_in_subtree(root, ["nsubj"])
    dobj_list = dep.find_tokens_with_dependencies_for_token_in_subtree(root, ["dobj", "pobj"])
    nsubjpass_list = dep.find_tokens_with_dependencies_for_token_in_subtree(root, ["nsubjpass"])
    if len(nsubj_list) > 0:
        for token in nsubj_list:
            output_obj = None
            subject = token
            verb = subject.head
            complements_list = dep.find_tokens_with_dependencies_for_token_in_subtree(verb, ["xcomp", "acomp", "ccomp",
                                                                                             "pcomp"])
            for complement in complements_list:
                if complement.head == verb:
                    output_obj = complement
            action = Action(subject=subject, verb=verb, new_object=output_obj)
            tmp_output.append(action)
    elif len(dobj_list) > 0:
        for token in dobj_list:
            subject = token
            verb = subject.head
            action = Action(subject=subject, verb=verb)
            tmp_output.append(action)
    elif len(nsubjpass_list) > 0:
        for token in nsubjpass_list:
            subject = token
            verb = subject.head
            action = Action(subject=subject, verb=verb)
            tmp_output.append(action)
    tmp_output += extract_actions_from_conjunction(sentence)

    # Check if extracted action can be assigned to verified actor
    output = set()
    for action in tmp_output:
        for actor in actors:
            if actor.get_object() == action.get_subject():
                output.add(action)

    return output


def extract_actions_from_conjunction(sentence: Span) -> List[Action]:
    output = []
    for word in sentence:
        if word.dep_ in ('conj'):
            main_pred = word.head
            complements_list = dep.find_tokens_with_dependencies_for_token_in_subtree(word, ["acomp", "ccomp", "pcomp",
                                                                                             "xcomp", "dobj", "obj",
                                                                                             "pobj", "attr"])
            for complement in complements_list:
                output_obj = complement
                for child in main_pred.children:
                    if child.dep_ in ('nsubj', 'nsubjpass'):
                        subject = child
                        verb = word
                        action = Action(subject=subject, verb=verb, new_object=output_obj)
                        output.append(action)
    return output
