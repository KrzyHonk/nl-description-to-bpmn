# coding=utf-8
"""
Base class for elements extracted from text
"""


class BaseElement(object):
    """
    Base class for elements extracted from text
    Fields:
    - __token: an instance of spacy.Token class.
    """

    def __init__(self, token=None):
        """
        Default constructor, initializes object fields with new instances.
        """
        self.__token = token

    def get_id(self):
        """
        Getter for '__token' field.
        :return: object set as '__token' field.
        """
        return self.__token

    def set_id(self, token):
        """
        Setter for '__token' field.
        :param token - a new object for '__token' field.
        """
        self.__token = token
