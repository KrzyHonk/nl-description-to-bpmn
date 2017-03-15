# coding=utf-8
"""
Function for extracting elements from sentence
"""
from spacy.tokens.span import Span
from typing import List


def extract_elements(sentence: Span) -> List[Span]:
    pass

"""
Require: Tree parsedSentence, TypedDependencies dependencies
1: boolean active   isActive(parsedSentence,dependencies)
2: List<Actor> actors   determineActors(active,sentence,dependencies)
3: List<Action> rawActions   determineActions(active,sentence,dependencies)
4: removeExampleSentences(actions)
5: List<Action> actionsWithObject   new List<Action>
6: for 8 Action action 2 rawActions do
7: List<ExtractedObject> objects   determineObject(active,sentence,dependencies, action)
8: lterSpeciers(action,objects,actors)
9: if jobjectsj > 0 then
10: for 8 ExtractedObject object 2 objetcs do
11: actionsWithObject [ (action+object)
12: end for
13: else
14: actionsWithObject [ rawActions
15: end if
16: end for
17: List<Action> nalActions   new List<Action>
18: for 8 Action action 2 actionsWithObject do
19: if jactorsj > 0 then
20: for 8 Actor actor 2 actors do
21: nalActions [ (actor+action)
22: end for
23: else
24: nalActions [ actionsWithObject
25: end if
26: end for
27: addToWorldModel(nalActions)
"""