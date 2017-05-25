# coding=utf-8
"""
Function for extracting actors from sentence
"""
from typing import List
from nltk.corpus import wordnet as wn

from spacy.tokens.span import Span

from main.consts import Consts
from main.objects.actor import Actor


def extract_actors(sentence: Span) -> List[Actor]:
    pronoun_set = {"I", "Me", "We", "Us", "You", "She", "Her", "He", "Him", "It", "They", "Them"}
    actors_keywords_set = {"provisioning", "service", "support", "office", "officer", "master", "masters", "assembler",
                           "acme", "accounting", "secretary", "office", "registry", "head", "storehouse", "atm", "crs",
                           "company", "garage", "kitchen", "department", "ec", "sp", "mpo", "mpoo", "mpon", "msp",
                           "mspo", "mspn", "go", "pu", "ip", "inq" "sp", "pu", "go", "detector"}
    real_actors_terms_list = ["person", "social_group", "software_system"]
    real_actors_synonyms = []
    for term in real_actors_terms_list:
        real_actors_synonyms.extend(wn.synsets(term))
    real_actors_synonyms = set(real_actors_synonyms)

    tmp_output = []
    output = []
    for word in sentence:
        if word.dep_ in Consts.subjects_set:
            new_object = word
            actor = Actor(actor_token=new_object)
            if new_object.pos_ == "pron":
                actor.set_anaphora(True)
            tmp_output.append(actor)
        elif word.dep_ == "agent":
            for token in word.children:
                if token.dep_ == "pobj":
                    new_object = token
                    actor = Actor(actor_token=new_object)
                    if new_object.pos_ == "pron":
                        actor.set_anaphora(True)
                    tmp_output.append(actor)
    tmp_output += extract_actors_from_conjunction(sentence)

    # Check if Actor is an acceptable entity
    for actor in tmp_output:
        actor_text = actor.get_actor_token().text

        flag = False
        # Check whether actor is a pronoun
        for pronoun in pronoun_set:
            if actor_text.casefold() == pronoun.casefold():
                flag = True
                actor.set_anaphora(True)

        for actor_keyword in actors_keywords_set:
            if actor_text.casefold() == actor_keyword.casefold():
                flag = True

        if flag is False:
            # Analyze actor hypernyms
            actor_synonyms = wn.synsets(actor_text)
            for actor_synonym in actor_synonyms:
                actor_hypernyms = actor_synonym.hypernyms()
                while flag is False and len(actor_hypernyms) > 0:
                    actor_hypernym = actor_hypernyms.pop()
                    if actor_hypernym in real_actors_synonyms:
                        flag = True
                    actor_hypernyms.extend(actor_hypernym.hypernyms())
        if flag:
            output.append(actor)

    return output


def extract_actors_from_conjunction(sentence: Span) -> List[Actor]:
    output = []
    for word in sentence:
        if word.dep_ == "conj":
            for token in word.children:
                if token.dep_ in ("pobj", "dobj", "iobj", "attr"):
                    actor = Actor(actor_token=token)
                    output.append(actor)
    return output
