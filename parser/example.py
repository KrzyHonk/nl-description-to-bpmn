import spacy
from spacy.attrs import *
from os import walk

from nltk import Tree

def to_nltk_tree(node):
    if node.n_lefts + node.n_rights > 0:
        return Tree(node.orth_, [to_nltk_tree(child) for child in node.children])
    else:
        return node.orth_

def parse_test():
    # Load files list
    models_directory = "../models/"
    model_files = []
    for (dirpath, dirnames, filenames) in walk(models_directory):
        model_files.extend(filenames)
        break

    print("Filenames: ", model_files)

    # Load English tokenizer, tagger, parser, NER and word vectors
    nlp = spacy.load('en')

    for file in model_files:
        # Process a document, of any size
        text = open(models_directory + file).read().replace("\n","")
        doc = nlp(unicode(text,encoding="utf-8"))

        # All strings mapped to integers, for easy export to numpy
        np_array = doc.to_array([LOWER, POS, ENT_TYPE, IS_ALPHA])

        for s in doc.sents:
            print(s)

        [to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]

parse_test()