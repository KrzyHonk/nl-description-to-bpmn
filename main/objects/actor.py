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

    def get_object(self):
        """
        Getter for '__object' field.
        :return: object set as '__object' field.
        """
        return self.__object

    def set_object(self, object):
        """
        Setter for '__object' field.
        :param object - a new object for '__object' field.
        """
        self.__object = object

    def pretty_print(self):
        left = ""
        right = " "
        for token in self.__object.lefts:
            left += (token.text + " ")

        for token in self.__object.rights:
            right += (token.text + " ")
        return left + self.__object.text + right
