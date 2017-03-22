# coding=utf-8
"""
Class for actions extracted from text
"""
from spacy.tokens.token import Token

from main.objects.base_element import BaseElement


class Action(BaseElement):
    """
    Class for actions extracted from text
    - __subject: an instance of spacy.Token class.
    - __verb: an instance of spacy.Token class.
    - __object: an instance of spacy.Token class.
    """

    def __init__(self, ident=None, subject: Token = None, verb: Token = None, object: Token = None):
        """
        Default constructor, initializes object fields with new instances.
        """
        super().__init__(ident)
        self.__subject = subject
        self.__verb = verb
        self.__object = object

    def get_subject(self):
        """
        Getter for '__subject' field.
        :return: subject set as '__subject' field.
        """
        return self.__subject

    def set_subject(self, subject):
        """
        Setter for '__subject' field.
        :param subject - a new subject for '__subject' field.
        """
        self.__subject = subject

    def get_verb(self):
        """
        Getter for '__verb' field.
        :return: verb set as '__verb' field.
        """
        return self.__verb

    def set_verb(self, verb):
        """
        Setter for '__verb' field.
        :param verb - a new verb for '__verb' field.
        """
        self.__verb = verb

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
        return self.__subject.text + " " + self.__verb.text + " " + \
               ("" if self.__object == None else self.__object.text)
