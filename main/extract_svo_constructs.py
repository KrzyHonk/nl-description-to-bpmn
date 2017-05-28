# coding=utf-8
"""
Function for extracting svos from sentence
"""
from typing import List

from spacy.tokens.span import Span
from spacy.tokens.token import Token

import main.find_tokens_with_dependency as dep
from main.objects.svoconstruct import SvoConstruct
from main.objects.actor import Actor
from main.consts import Consts


def extract_svo_constructs(sentence: Span, actors: List[Actor]) -> List[SvoConstruct]:
    tmp_output = []
    root = sentence.root
    nsubj_list = dep.find_tokens_with_dependencies_for_token_in_subtree(root, ["nsubj"])
    nsubjpass_list = dep.find_tokens_with_dependencies_for_token_in_subtree(root, ["nsubjpass"])
    if len(nsubj_list) > 0:
        for token in nsubj_list:
            subject = token
            verb = subject.head
            output_obj = find_token_in_ancestors(verb, Consts.objects_set)

            svo = SvoConstruct(subject=subject, verb=verb, new_object=output_obj, position=verb.i)
            insert_flag = True
            if len(tmp_output) > 0:
                for tmp_svo in tmp_output:
                    if svo.get_subject() == tmp_svo.get_subject() \
                            and svo.get_verb() == tmp_svo.get_verb() \
                            and svo.get_object() == tmp_svo.get_object():
                        insert_flag = False
                if insert_flag:
                    tmp_output.append(svo)
            else:
                tmp_output.append(svo)
    if len(nsubjpass_list) > 0:
        for token in nsubjpass_list:
            subject = token
            verb = subject.head
            svo = SvoConstruct(subject=subject, verb=verb, position=verb.i)
            svo.set_passive(True)
            insert_flag = True
            if len(tmp_output) > 0:
                # Check if svo wasn't already discovered
                for tmp_svo in tmp_output:
                    if svo.get_subject() == tmp_svo.get_subject() \
                            and svo.get_verb() == tmp_svo.get_verb() \
                            and svo.get_object() == tmp_svo.get_object():
                        insert_flag = False
                if insert_flag:
                    tmp_output.append(svo)
            else:
                tmp_output.append(svo)
    extract_svos_from_conjunction(sentence, tmp_output)

    # Check if extracted svo can be assigned to verified actor
    for svo in tmp_output:
        for actor in actors:
            if actor.get_actor_token() == svo.get_subject():
                svo.set_actor(actor)
    return tmp_output


def extract_svos_from_conjunction(sentence: Span, tmp_output: List[SvoConstruct]) -> List[SvoConstruct]:
    for word in sentence:
        if word.dep_ == "conj":
            conj_verb = word
            output_object = find_token_in_ancestors(conj_verb, Consts.objects_set)

            subject = None
            token = conj_verb
            while token is not None and subject is None:
                subject = find_token_in_ancestors(token, Consts.subjects_set)
                if token.dep_ == "ROOT":
                    break
                if subject is None:
                    token = token.head

            if subject is not None:
                svo = SvoConstruct(subject=subject, verb=conj_verb, new_object=output_object, position=conj_verb.i)
                if len(tmp_output) > 0:
                    insert_flag = True
                    for tmp_svo in tmp_output:
                        if svo.get_subject() == tmp_svo.get_subject() \
                                and svo.get_verb() == tmp_svo.get_verb() \
                                and svo.get_object() == tmp_svo.get_object():
                            insert_flag = False
                    if insert_flag:
                        tmp_output.append(svo)
                else:
                    tmp_output.append(svo)


def find_token_in_ancestors(token: Token, dependencies_set):
    for child in token.children:
        if child.dep_ in dependencies_set:
            return child
        elif child.dep_ in Consts.actor_descriptors_set:
            for grandchild in child.children:
                output = find_token_in_ancestors(grandchild, dependencies_set)
                if output is not None:
                    return output
    return None