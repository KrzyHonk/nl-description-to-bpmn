from typing import List

from spacy.tokens.doc import Doc

from main.objects.svoconstruct import SvoConstruct


def find_gateway_keywords(doc: Doc, svos: List[SvoConstruct]):
    """
    Method that finds potential gateways

    :param doc: SpaCy's Doc object
    :param svos: List of SvoConstruct objects
    """
    for sentence in doc.sents:
        for word in sentence:
            if word.dep_ in ["mark", "advmod", "ccomp", "acl"]:
                head = word.head
                tmp_svo = next((svo for svo in svos if svo.get_position() == head.i), None)
                if tmp_svo is not None:
                    tmp_svo.set_gateway_keyword(word.text)
    return svos
