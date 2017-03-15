# coding=utf-8
import os

from setuptools import setup


def read(fname):
    """
    Utility function to read the README file. Used for the long_description.
    :param fname:
    :return:
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="nl-description-to-bpmn",
    version="0.1.0",
    author="Krzysztof Honkisz",
    # author_email = "honkiszkrzystof@gmail.com",
    description=(""),
    license="GNU GENERAL PUBLIC LICENSE",
    keywords=["bpmn", "xml"],
    url="https://github.com/KrzyHonk/nl-description-to-bpmn",
    download_url="https://github.com/KrzyHonk/nl-description-to-bpmn/tarball/0.1.0",
    packages=['main'],
    install_requires=[
        'spacy',
    ],
    long_description=read('README.md'),
)
