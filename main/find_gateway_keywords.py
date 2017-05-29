from typing import List

from spacy.tokens.doc import Doc

from main.consts import Consts
from main.objects.svoconstruct import SvoConstruct


def find_gateway_keywords(doc: Doc, svos: List[SvoConstruct]):
    """
    Method that finds potential gateways

    :param doc: SpaCy's Doc object
    :param svos: List of SvoConstruct objects
    """
    for sentence in doc.sents:
        for word in sentence:
            if word.text.casefold() in Consts.gateways_keywords:
                head = word.head
                svo = next((svo for svo in svos if svo.get_verb().i == head.i), None)
                if svo is not None:
                    svo.set_gateway_keyword(word.text)
