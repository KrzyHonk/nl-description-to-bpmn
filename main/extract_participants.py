# coding=utf-8
"""
Function for extracting participants from sentence
"""
from typing import List

from nltk.corpus import wordnet as wn
from spacy.tokens.span import Span

from main.objects.participant import Participant


def extract_participants(sentence: Span) -> List[Participant]:
    participant_keywords_list = {"atm", "crm", "crs", "office", "provisioning", "secretary", "support"}
    participant_hypernyms_list = {"facility", "group", "organization", "person", "service", "system"}
    participants_base_keywords_synonyms = []
    for term in participant_hypernyms_list:
        participants_base_keywords_synonyms.extend(wn.synsets(term))
    participants_base_keywords_synonyms = set(participants_base_keywords_synonyms)

    tmp_output = []
    output = []
    for word in sentence:
        if word.dep_ in {"nsubj", "nsubjpass"}:
            participant = Participant(participant_token=word)
            if word.pos_ == "pron":
                participant.set_pronoun(True)
            tmp_output.append(participant)
        elif word.dep_ == "agent":
            for child in word.children:
                if child.dep_ == "pobj":
                    participant = Participant(participant_token=child)
                    if child.pos_ == "pron":
                        participant.set_pronoun(True)
                    tmp_output.append(participant)

    # Check if possible participant is a part of conjunction
    for word in sentence:
        if word.dep_ == "conj":
            for child in word.children:
                if child.dep_ in {"pobj", "dobj", "iobj", "attr"}:
                    participant = Participant(participant_token=child)
                    if child.pos_ == "pron":
                        participant.set_pronoun(True)
                    tmp_output.append(participant)

    # Check if Participant is an acceptable entity
    for participant in tmp_output:
        participant_text = participant.get_participant_token().text

        insert_flag = False
        # Check whether participant is a pronoun
        if participant.is_pronoun():
            insert_flag = True

        if insert_flag is False:
            # Analyze participant hypernyms, in search for one of base keywords
            insert_flag = analyze_participants_hypernyms(participant_text, participants_base_keywords_synonyms)

        if insert_flag is False:
            # Check if participant is one of keywords
            insert_flag = validate_participant_text_against_keyword_list(participant_text, participant_keywords_list)
        if insert_flag:
            output.append(participant)

    return output


def analyze_participants_hypernyms(participant_text: str, participants_base_keywords_synonyms):
    participant_synonyms = wn.synsets(participant_text)
    for participant_synonym in participant_synonyms:
        participant_hypernyms = participant_synonym.hypernyms()
        while len(participant_hypernyms) > 0:
            participant_hypernym = participant_hypernyms.pop()
            if participant_hypernym in participants_base_keywords_synonyms:
                return True
            participant_hypernyms.extend(participant_hypernym.hypernyms())
    return False


def validate_participant_text_against_keyword_list(participant_text, participant_keywords_list):
    for participant_keyword in participant_keywords_list:
        if participant_text.casefold() == participant_keyword.casefold():
            return True
    return False