# coding=utf-8
"""
Class for actions extracted from text
"""
from spacy.tokens.token import Token

from main.objects.actor import Actor
from main.objects.base_element import BaseElement


class Action(BaseElement):
    """
    Class for actions extracted from text
    - __subject: an instance of spacy.Token class.
    - __verb: an instance of spacy.Token class.
    - __object: an instance of spacy.Token class.
    """

    def __init__(self, ident=None, subject: Token = None, verb: Token = None, new_object: Token = None):
        """
        Default constructor, initializes object fields with new instances.
        """
        super().__init__(ident)
        self.__subject = subject
        self.__verb = verb
        self.__object = new_object
        self.__actor = None

    def get_subject(self):
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

    def get_verb(self):
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

    def get_object(self):
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

    def set_actor(self, actor: Actor):
        """
        Setter for '__actor' field.
        :param actor - a new verb for '__actor' field.
        """
        self.__actor = actor

    def get_actor(self):
        """
        Getter for '__actor' field.
        :return: object set as '__actor' field.
        """
        return self.__actor


    def find_complement(self):
        """
        Find child token in complement relationship.
        """
        return None

    def pretty_print(self):
        verb_text = ""
        for token in self.__verb.subtree:
            if token.dep_ in ["aux", "auxpass", "neg"] and token.head == self.__verb:
                verb_text += (token.text + " ")
        verb_text += self.__verb.text
        return self.__subject.text + " " + verb_text + " " + \
               ("" if self.__object == None else self.__object.text)
