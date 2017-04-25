# coding=utf-8
"""
Class for actors extracted from text
"""
from spacy.tokens.token import Token

from main.objects.base_element import BaseElement


class Actor(BaseElement):
    """
    Class for actors extracted from text
    """

    def __init__(self, ident=None, actor_token: Token = None):
        """
        Default constructor, initializes object fields with new instances.
        """
        super().__init__(ident)
        self.__actor_token = actor_token
        self.__anaphora = False

    def get_actor_token(self):
        """
        Getter for '__actor_token' field.
        :return: object set as '__actor_token' field.
        """
        return self.__actor_token

    def set_actor_token(self, actor_token):
        """
        Setter for '__actor_token' field.
        :param actor_token - a new object for '__actor_token' field.
        """
        self.__actor_token = actor_token

    def get_anaphora(self):
        """
        Getter for '__anaphora' field.
        :return: value of '__anaphora' field.
        """
        return self.__anaphora

    def set_anaphora(self, anaphora):
        """
        Setter for '__anaphora' field.
        :param anaphora - a new value of '__anaphora' field.
        """
        self.__anaphora = anaphora

    def pretty_print(self):
        left = ""
        right = " "
        for token in self.__actor_token.lefts:
            left += (token.text + " ")

        for token in self.__actor_token.rights:
            right += (token.text + " ")
        return left + self.__actor_token.text + right
