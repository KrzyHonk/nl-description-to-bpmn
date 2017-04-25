# coding=utf-8
"""
Function for extracting actors from sentence
"""
from typing import List
from nltk.corpus import wordnet as wn

from spacy.tokens.span import Span

from main.objects.actor import Actor


def extract_actors(sentence: Span) -> List[Actor]:
    pronoun_set = {"I", "Me", "We", "Us", "You", "She", "Her", "He", "Him", "It", "They", "Them"}
    real_actors_terms_list = ["person", "social_group", "software_system"]
    real_actors_synonyms = []
    for term in real_actors_terms_list:
        real_actors_synonyms.extend(wn.synsets(term))
    real_actors_synonyms = set(real_actors_synonyms)

    tmp_output = []
    output = []
    for word in sentence:
        if word.dep_ in ('nsubj'):
            new_object = word
            actor = Actor(actor_token=new_object)
            if new_object.pos_ == "pron":
                actor.set_anaphora(True)
            tmp_output.append(actor)
        elif word.dep_ in ('agent'):
            for token in word.children:
                if token.dep_ in ('pobj'):
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
        if word.dep_ in ('conj'):
            for token in word.children:
                if token.dep_ in ('pobj', 'dobj', 'iobj'):
                    object = token
                    actor = Actor(actor_token=object)
                    output.append(actor)
    return output
