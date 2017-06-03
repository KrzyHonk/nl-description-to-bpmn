# coding=utf-8
"""
Utility functions
"""
from nltk import Tree


def to_nltk_tree(node):
    if node.n_lefts + node.n_rights > 0:
        return Tree("Text: " + node.orth_ + ", POS: " + node.pos_ + ", TAG: " + node.tag_ + ", DEP: " + node.dep_,
                    [to_nltk_tree(child) for child in node.children])
    else:
        return "Text: " + node.orth_ + ", POS: " + node.pos_ + ", TAG: " + node.tag_ + ", DEP: " + node.dep_
