# coding=utf-8
"""
Function for extracting participants from sentence
"""
from typing import List

from nltk.corpus import wordnet as wn
from spacy.tokens.span import Span

from main.consts import Consts
from main.objects.participant import Participant


def extract_participants(sentence: Span) -> List[Participant]:
    pronoun_set = ("I", "Me", "We", "Us", "You", "She", "Her", "He", "Him", "It", "They", "Them", "who", "whom",
                   "whose", "what", "which", "that")
    participant_keywords_set = {"atm", "crm", "crs", "office", "officer", "post", "process", "task", "provisioning", "service",
                                 "secretary", "support", "storehouse"}
    participant_hypernyms_list = {"group", "organization", "person", "service", "system"}
    participants_base_keywords_synonyms = []
    for term in participant_hypernyms_list:
        participants_base_keywords_synonyms.extend(wn.synsets(term))
    participants_base_keywords_synonyms = set(participants_base_keywords_synonyms)

    tmp_output = []
    output = []
    for word in sentence:
        if word.dep_ in ("nsubj", "nsubjpass"):
            new_object = word
            participant = Participant(participant_token=new_object)
            if new_object.pos_ == "pron":
                participant.set_pronoun(True)
            tmp_output.append(participant)
        elif word.dep_ == "agent":
            for token in word.children:
                if token.dep_ == "pobj":
                    new_object = token
                    participant = Participant(participant_token=new_object)
                    if new_object.pos_ == "pron":
                        participant.set_pronoun(True)
                    tmp_output.append(participant)

    # Check if possible participant is a part of conjunction
    for word in sentence:
        if word.dep_ == "conj":
            for token in word.children:
                if token.dep_ in ("pobj", "dobj", "iobj", "attr"):
                    participant = Participant(participant_token=token)
                    tmp_output.append(participant)

    # Check if Participant is an acceptable entity
    for participant in tmp_output:
        participant_text = participant.get_participant_token().text

        flag = False
        # Check whether participant is a pronoun
        for pronoun in pronoun_set:
            if participant_text.casefold() == pronoun.casefold():
                flag = True
                participant.set_pronoun(True)

        if flag is False:
            # Analyze participant hypernyms, in search of one of base keywords
            participant_synonyms = wn.synsets(participant_text)
            for participant_synonym in participant_synonyms:
                participant_hypernyms = participant_synonym.hypernyms()
                while flag is False and len(participant_hypernyms) > 0:
                    participant_hypernym = participant_hypernyms.pop()
                    if participant_hypernym in participants_base_keywords_synonyms:
                        flag = True
                    participant_hypernyms.extend(participant_hypernym.hypernyms())

        if flag is False:
            # Check if participant is one of keywords
            for participant_keyword in participant_keywords_set:
                if participant_text.casefold() == participant_keyword.casefold():
                    flag = True
        if flag:
            output.append(participant)

    return output
