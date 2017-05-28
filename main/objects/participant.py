# coding=utf-8
"""
Class for participants extracted from text
"""
from spacy.tokens.token import Token

from main.consts import Consts
from main.objects.base_element import BaseElement


class Participant(BaseElement):
    """
    Class for participants extracted from text
    """

    def __init__(self, ident=None, participant_token: Token = None):
        """
        Default constructor, initializes object fields with new instances.
        """
        super().__init__(ident)
        self.__participant_token = participant_token
        self.__pronoun = False

    def get_participant_token(self) -> Token:
        """
        Getter for '__participant_token' field.
        :return: object set as '__participant_token' field.
        """
        return self.__participant_token

    def set_participant_token(self, participant_token: Token):
        """
        Setter for '__participant_token' field.
        :param participant_token - a new object for '__participant_token' field.
        """
        self.__participant_token = participant_token

    def is_pronoun(self) -> bool:
        """
        Getter for '__pronoun' field.
        :return: value of '__pronoun' field.
        """
        return self.__pronoun

    def set_pronoun(self, pronoun: bool):
        """
        Setter for '__pronoun' field.
        :param pronoun - a new value of '__pronoun' field.
        """
        self.__pronoun = pronoun

    def pretty_print(self) -> str:
        left = ""
        right = " "
        for token in self.__participant_token.lefts:
            if token.dep_ in Consts.participant_descriptors_set:
                left += (token.text.casefold() + " ")

        for token in self.__participant_token.rights:
            if token.dep_ in Consts.participant_descriptors_set:
                right += (token.text.casefold() + " ")
        return left + self.__participant_token.text.casefold() + right
