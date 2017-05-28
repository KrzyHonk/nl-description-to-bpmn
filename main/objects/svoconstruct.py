# coding=utf-8
"""
Class for subject-verb-object constructs extracted from text
"""
from spacy.tokens.token import Token

from main.consts import Consts
from main.objects.actor import Actor
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
        self.__actor = None
        self.__passive = False
        self.__position = position
        self.__marker = None

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

    def set_actor(self, actor: Actor):
        """
        Setter for '__actor' field.
        :param actor - a new verb for '__actor' field.
        """
        self.__actor = actor

    def get_actor(self) -> Actor:
        """
        Getter for '__actor' field.
        :return: object set as '__actor' field.
        """
        return self.__actor

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

    def set_marker(self, marker: str):
        """
        Setter for '__marker' field.
        :param marker - a value of '__marker' field.
        """
        self.__marker = marker

    def get_marker(self) -> str:
        """
        Getter for '__marker' field.
        :return: object set as '__marker' field.
        """
        return self.__marker

    def pretty_print(self) -> str:
        left = ""
        right = " "
        for token in self.__subject.lefts:
            if token.dep_ in Consts.actor_descriptors_set:
                left += (token.text.casefold() + " ")
        for token in self.__subject.rights:
            if token.dep_ in Consts.actor_descriptors_set:
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
                if token.dep_ in Consts.actor_descriptors_set:
                    left += (token.text.casefold() + " ")
            for token in self.__object.rights:
                if token.dep_ in Consts.actor_descriptors_set:
                    right += (token.text.casefold() + " ")
            object_text = left + self.__object.text.casefold() + right

        return subject_text + verb_text + object_text

    def marker_print(self) -> str:
        return "SVO: " + self.pretty_print() + " Marker: " + (self.__marker if self.__marker is not None else "")
