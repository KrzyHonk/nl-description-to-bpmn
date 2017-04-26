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
    nsubjpass_list = dep.find_tokens_with_dependencies_for_token_in_subtree(root, ["nsubjpass"])
    if len(nsubj_list) > 0:
        for token in nsubj_list:
            output_obj = None
            subject = token
            verb = subject.head
            objects_list = dep.find_tokens_with_dependencies_for_token_in_subtree(verb,
                                                                                  ["dobj", "iobj", "pobj", "attr"])
            for complement in objects_list:
                if complement.head == verb:
                    output_obj = complement
            action = Action(subject=subject, verb=verb, new_object=output_obj)
            tmp_output.append(action)
    if len(nsubjpass_list) > 0:
        for token in nsubjpass_list:
            subject = token
            verb = subject.head
            action = Action(subject=subject, verb=verb)
            action.set_passive(True)
            tmp_output.append(action)
    tmp_output += extract_actions_from_conjunction(sentence)

    # Check if extracted action can be assigned to verified actor
    output = set()
    for action in tmp_output:
        if action.get_passive():
            output.add(action)
        else:
            for actor in actors:
                if actor.get_actor_token() == action.get_subject():
                    output.add(action)
    return output


def extract_actions_from_conjunction(sentence: Span) -> List[Action]:
    output = []
    for word in sentence:
        if word.dep_ in ('conj'):
            conj_verb = word
            output_object = None
            for child in conj_verb.children:
                if child.dep_ in ["dobj", "iobj", "attr"]:
                    output_object = child

            subject = None
            token = conj_verb
            while token.head is not None and subject is None:
                for child in token.children:
                    if child.dep_ in ('nsubj', 'nsubjpass'):
                        subject = child
                if subject is None:
                    token = token.head

            if subject is not None:
                action = Action(subject=subject, verb=conj_verb, new_object=output_object)
                output.append(action)
    return output
