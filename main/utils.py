# coding=utf-8
"""
Utility functions
"""
from nltk import Tree
from nltk.corpus import wordnet as wn
from spacy.tokens.token import Token

from main.consts import Consts
from main.objects.participant import Participant
from main.objects.svoconstruct import SvoConstruct


def to_nltk_tree(node):
    if node.n_lefts + node.n_rights > 0:
        return Tree("Text: " + node.orth_ + ", POS: " + node.pos_ + ", TAG: " + node.tag_ + ", DEP: " + node.dep_,
                    [to_nltk_tree(child) for child in node.children])
    else:
        return "Text: " + node.orth_ + ", POS: " + node.pos_ + ", TAG: " + node.tag_ + ", DEP: " + node.dep_


def participant_print_full_name(participant: Participant):
    left = ""
    right = " "
    for token in participant.get_participant_token().lefts:
        if token.dep_ in Consts.participant_descriptors_list:
            left += (token.text.casefold().capitalize() + " ")

    for token in participant.get_participant_token().rights:
        if token.dep_ in Consts.participant_descriptors_list:
            right += (token.text.casefold().capitalize() + " ")
    return left + participant.get_participant_token().text.casefold().capitalize() + right


def svo_print_full_name(svo: SvoConstruct):
    left = ""
    right = " "
    for token in svo.get_subject().lefts:
        if token.dep_ in Consts.participant_descriptors_list:
            left += (token.text.casefold().capitalize() + " ")
    for token in svo.get_subject().rights:
        if token.dep_ in Consts.participant_descriptors_list:
            right += (token.text.casefold().capitalize() + " ")
    subject_text = left + svo.get_subject().text.casefold().capitalize() + right

    left = ""
    right = " "
    for token in svo.get_verb().lefts:
        if token.dep_ in Consts.svo_descriptors_list:
            left += (token.text.casefold() + " ")
    for token in svo.get_verb().rights:
        if token.dep_ in Consts.svo_descriptors_list:
            right += (token.text.casefold() + " ")
    verb_text = left + svo.get_verb().text.casefold() + right

    left = ""
    right = " "
    object_text = ""
    if svo.get_object() is not None:
        for token in svo.get_object().lefts:
            if token.dep_ in Consts.participant_descriptors_list:
                left += (token.text.casefold() + " ")
        for token in svo.get_object().rights:
            if token.dep_ in Consts.participant_descriptors_list:
                right += (token.text.casefold() + " ")
        object_text = left + svo.get_object().text.casefold() + right

    return subject_text + verb_text + object_text


def activity_verb_object_order(svo: SvoConstruct):
    base_verb_form = svo_get_verb_base_form(svo.get_verb())

    left = ""
    right = " "
    for token in svo.get_object().lefts:
        if token.dep_ in Consts.object_descriptors_list:
            left += (token.text.casefold().capitalize() + " ")
    for token in svo.get_object().rights:
        if token.dep_ in Consts.object_descriptors_list:
            right += (token.text.casefold().capitalize() + " ")
    object_text = left + svo.get_object().text.casefold().capitalize() + right

    if base_verb_form in Consts.message_event_verbs:
        return "message " + base_verb_form.capitalize() + " " + object_text
    else:
        return base_verb_form.capitalize() + " " + object_text


def activity_verb_subject_order(svo: SvoConstruct):
    base_verb_form = svo_get_verb_base_form(svo.get_verb())

    if svo.get_subject().text in Consts.pronoun_list:
        subject_text =""
    else:
        left = ""
        right = " "
        for token in svo.get_subject().lefts:
            if token.dep_ in Consts.participant_descriptors_list:
                left += (token.text.casefold().capitalize() + " ")
        for token in svo.get_subject().rights:
            if token.dep_ in Consts.participant_descriptors_list:
                right += (token.text.casefold().capitalize() + " ")
        subject_text = left + svo.get_subject().text.casefold().capitalize() + right

    if base_verb_form in Consts.message_event_verbs:
        return "message " + base_verb_form.capitalize() + " " + subject_text
    else:
        return base_verb_form.capitalize() + " " + subject_text


def svo_gateway_keyword_print(svo: SvoConstruct) -> str:
    return "SVO: " + svo_print_full_name(svo) + " Gateway keyword: " + \
           (svo.get_gateway_keyword() if svo.get_gateway_keyword() is not None else "")


def svo_get_verb_base_form(verb: Token):
    base_verb = None
    if svo_validate_skippable_verb(verb):
        for child in verb.children:
            if child.pos_ is "VERB" and not svo_validate_skippable_verb(child):
                base_verb = wn.morphy(child.text, wn.VERB)
                if base_verb is None:
                    base_verb = child.text
                break
    else:
        base_verb = wn.morphy(verb.text.casefold(), wn.VERB)

    if base_verb is not None:
        return base_verb
    else:
        return verb.text.casefold()


def svo_validate_skippable_verb(verb: Token) -> bool:
    skippable_verbs = Consts.skippable_verbs

    base_verb = wn.morphy(verb.text, wn.VERB)
    if base_verb is not None and base_verb.casefold() in skippable_verbs:
        return True
    else:
        return False


def svo_validate_replecable_verb(verb: Token) -> bool:
    replaceable_verbs = Consts.skippable_verbs

    base_verb = wn.morphy(verb.text, wn.VERB)
    if base_verb is not None and base_verb.casefold() in replaceable_verbs:
        return True
    else:
        return False


def svo_validate_ignorable_verb(verb: Token) -> bool:
    ignore_verbs = Consts.ignorable_verbs

    base_verb = wn.morphy(verb.text, wn.VERB)
    if base_verb is not None and base_verb.casefold() in ignore_verbs:
        return True
    else:
        return False


def svo_get_verb_replacement(verb: Token):
    verb_replacement = None
    for child in verb.children:
        if child.pos_ is "VERB" and not svo_validate_skippable_verb(child):
            verb_replacement = wn.morphy(child.text, wn.VERB)
            if verb_replacement is None:
                verb_replacement = child.text
            break
    return verb_replacement
