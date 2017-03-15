# coding=utf-8
"""
Utility functions
"""
from nltk import Tree


def to_nltk_tree(node):
    if node.n_lefts + node.n_rights > 0:
        return Tree(node.orth_ + ", " + node.pos_ + ", " + node.tag_ + ", " + node.dep_, [to_nltk_tree(child) for child in node.children])
    else:
        return node.orth_ + ", " + node.pos_ + ", " + node.tag_ + ", " + node.dep_
