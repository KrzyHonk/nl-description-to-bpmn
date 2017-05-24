from typing import List

from spacy.tokens.doc import Doc

from main.objects.action import Action


def find_gateway_keywords(doc: Doc, actions: List[Action]):
    """
    Method that finds potential gateways

    :param doc: SpaCy's Doc object
    :param actions: List of Action objects
    """
    for sentence in doc.sents:
        for word in sentence:
            if word.dep_ in ["mark", "advmod", "ccomp", "acl"]:
                head = word.head
                tmp_action = next((action for action in actions if action.get_position() == head.i), None)
                if tmp_action is not None:
                    tmp_action.set_marker(word.text)
    return actions
