import spacy

from main.generate_intermediate_model import generate_intermediate_model


def nlp_description_to_bpmn(filename: str, directory: str, output_directory: str):
    full_filepath = directory + filename
    nlp = spacy.load("en")

    text = open(full_filepath).read().replace("\n", " ").replace("-", "")
    doc = nlp(text)
    generate_intermediate_model(doc, filename, output_directory)
