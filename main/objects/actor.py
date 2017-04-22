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

    def __init__(self, ident=None, object: Token = None):
        """
        Default constructor, initializes object fields with new instances.
        """
        super().__init__(ident)
        self.__object = object
        self.__anaphora = False

    def get_object(self):
        """
        Getter for '__object' field.
        :return: object set as '__object' field.
        """
        return self.__object

    def set_object(self, new_object):
        """
        Setter for '__object' field.
        :param new_object - a new object for '__object' field.
        """
        self.__object = new_object

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
        for token in self.__object.lefts:
            left += (token.text + " ")

        for token in self.__object.rights:
            right += (token.text + " ")
        return left + self.__object.text + right
