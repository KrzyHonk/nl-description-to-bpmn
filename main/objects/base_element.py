# coding=utf-8
"""
Base class for elements extracted from text
"""


class BaseElement(object):
    """
    Base class for elements extracted from text
    Fields:
    - __ident: a string value.
    """

    def __init__(self, ident: str = None):
        """
        Default constructor, initializes object fields with new instances.
        """
        self.__ident = ident

    def get_ident(self):
        """
        Getter for '__ident' field.
        :return: object set as '__ident' field.
        """
        return self.__ident

    def set_ident(self, ident):
        """
        Setter for '__ident' field.
        :param ident - a new object for '__ident' field.
        """
        self.__ident = ident
