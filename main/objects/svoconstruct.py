# coding=utf-8
"""
Class for subject-verb-object constructs extracted from text
"""
from spacy.tokens.token import Token

from main.consts import Consts
from main.objects.participant import Participant
from main.objects.base_element import BaseElement


class SvoConstruct(BaseElement):
    """
    Class for subject-verb-object constructs extracted from text
    - __subject: an instance of spacy.Token class.
    - __verb: an instance of spacy.Token class.
    - __object: an instance of spacy.Token class.
    """

    def __init__(self, ident=None, subject: Token = None, verb: Token = None, new_object: Token = None,
                 position: int = 0):
        """
        Default constructor, initializes object fields with new instances.
        """
        super().__init__(ident)
        self.__subject = subject
        self.__verb = verb
        self.__object = new_object
        self.__participant = None
        self.__passive = False
        self.__position = position
        self.__gateway_keyword = None

    def get_subject(self) -> Token:
        """
        Getter for '__subject' field.
        :return: subject set as '__subject' field.
        """
        return self.__subject

    def set_subject(self, subject: Token):
        """
        Setter for '__subject' field.
        :param subject - a new subject for '__subject' field.
        """
        self.__subject = subject

    def get_verb(self) -> Token:
        """
        Getter for '__verb' field.
        :return: verb set as '__verb' field.
        """
        return self.__verb

    def set_verb(self, verb: Token):
        """
        Setter for '__verb' field.
        :param verb - a new verb for '__verb' field.
        """
        self.__verb = verb

    def get_object(self) -> Token:
        """
        Getter for '__object' field.
        :return: object set as '__object' field.
        """
        return self.__object

    def set_object(self, new_object: Token):
        """
        Setter for '__object' field.
        :param new_object - a new object for '__object' field.
        """
        self.__object = new_object

    def set_participant(self, participant: Participant):
        """
        Setter for '__participant' field.
        :param participant - a new verb for '__participant' field.
        """
        self.__participant = participant

    def get_participant(self) -> Participant:
        """
        Getter for '__participant' field.
        :return: object set as '__participant' field.
        """
        return self.__participant

    def set_passive(self, passive: bool):
        """
        Setter for '__passive' field.
        :param passive - a new verb for '__passive' field.
        """
        self.__passive = passive

    def get_passive(self) -> bool:
        """
        Getter for '__passive' field.
        :return: object set as '__passive' field.
        """
        return self.__passive

    def get_position(self) -> int:
        """
        Getter for '__position' field.
        :return: object set as '__position' field.
        """
        return self.__position

    def set_gateway_keyword(self, gateway_keyword: str):
        """
        Setter for '__gateway_keyword' field.
        :param gateway_keyword - a value of '__gateway_keyword' field.
        """
        self.__gateway_keyword = gateway_keyword

    def get_gateway_keyword(self) -> str:
        """
        Getter for '__gateway_keyword' field.
        :return: object set as '__gateway_keyword' field.
        """
        return self.__gateway_keyword

    def pretty_print(self) -> str:
        left = ""
        right = " "
        for token in self.__subject.lefts:
            if token.dep_ in Consts.participant_descriptors_set:
                left += (token.text.casefold() + " ")
        for token in self.__subject.rights:
            if token.dep_ in Consts.participant_descriptors_set:
                right += (token.text.casefold() + " ")
        subject_text = left + self.__subject.text.casefold() + right

        left = ""
        right = " "
        for token in self.__verb.lefts:
            if token.dep_ in Consts.svo_descriptors_set:
                left += (token.text.casefold() + " ")
        for token in self.__verb.rights:
            if token.dep_ in Consts.svo_descriptors_set:
                right += (token.text.casefold() + " ")
        verb_text = left + self.__verb.text.casefold() + right

        left = ""
        right = " "
        object_text = ""
        if self.__object is not None:
            for token in self.__object.lefts:
                if token.dep_ in Consts.participant_descriptors_set:
                    left += (token.text.casefold() + " ")
            for token in self.__object.rights:
                if token.dep_ in Consts.participant_descriptors_set:
                    right += (token.text.casefold() + " ")
            object_text = left + self.__object.text.casefold() + right

        return subject_text + verb_text + object_text

    def gateway_keyword_print(self) -> str:
        return "SVO: " + self.pretty_print() + " Gateway keyword: " + (self.__gateway_keyword if self.__gateway_keyword is not None else "")
