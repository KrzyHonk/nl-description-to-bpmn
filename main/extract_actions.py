# coding=utf-8
"""
Function for extracting actions from sentence
"""
from spacy.tokens.span import Span
import main.find_tokens_with_dependency as dep
import main.find_conjunctions as find_conj
from typing import List


def extract_actions(sentence: Span) -> List[Span]:
    output = []
    for word in sentence:
        print(word.text, word.dep_)
        if word.dep_ == 'nsubj':
            governor = word.head
            acomp = dep.find_tokens_with_dependencies(sentence, ["acomp", "ccomp", "pcomp"])
            if acomp == governor:
                main_predicate = acomp
        elif word.dep_ in ('dobj', 'nsubjpass'):
            main_predicate = word
        # TODO add action
        # output.append()
            output.append(find_conj.find_conjunctions(sentence, main_predicate))
    return output

"""
Algorithm 4 Determine Actions
Require: boolean active, Tree parsedSentence, TypedDependencies dependencies
1: List<Action> result   new List<Action>
2: if active then
3: TypedDependency nsubj   ndDependency(\nsubj", parsedSentence, dependencies)
4: if nsubj 6=  then
5: TreeGraphNode mainPredicate   nsubj.governor()
6: TypedDependency cop   ndDependency(\cop", parsedSentence, dependencies)
7: if cop.governor() = mainPredicate then
8: TreeGraphNode mainPredicate   cop.dependent()
9: end if
10: else
11: TypedDependency dobj   ndDependency(\dobj", parsedSentence, dependencies)
12: TreeGraphNode mainPredicate   dobj.governor()
13: end if
14: else
15: TypedDependency nsubjpass   ndDependency(\nsubjpass", parsedSentence, dependencies)
16: TreeGraphNode mainPredicate   nsubjpass.governor()
17: end if
18: Action action   createAction(mainPredicate, dependencies)
19: checkSubSentences(action,dependencies)
20: result [ action
21: result [ checkConjunctions(action,active,dependencies)
22: return result
"""