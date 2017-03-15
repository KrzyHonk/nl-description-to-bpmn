# coding=utf-8
"""
Sentence decomposition function
"""
from spacy.tokens.span import Span
import spacy

import main.extract_elements as elem_extr
import main.subsentence_extraction as subsent


def sentence_decomposition(sentence: Span):
    """

    :param sentence:
    """
    subsentences_list = subsent.subsentence_extraction(sentence)

    if len(subsentences_list) == 0:
        elem_extr.extract_elements(sentence)
    else:
        tmp_sentence = sentence[0:sentence.end]
        for subsentence in subsentences_list:
            rest = [x for x in tmp_sentence if x not in subsentence]
            tmp_sentence = rest

        # Extract the reminder of processed sentence and add it to the list
        sentence_rest = ""
        for word in tmp_sentence:
            sentence_rest += (" " + word.text)

        nlp = spacy.load('en')
        doc = nlp(sentence_rest)
        for s in doc.sents:
            subsentences_list.append(s)

        for subsentence in subsentences_list:
            elem_extr.extract_elements(subsentence)
