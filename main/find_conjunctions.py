# coding=utf-8
"""
Function for finding conjunctions in sentence
"""
from spacy.tokens.span import Span
from spacy.tokens.token import Token
from typing import List


def find_conjunctions(sentence: Span, element: Token) -> List[Token]:
    for word in sentence:
        for con in word.conjuncts:
            pass

"""
Require: boolean active, Tree parsedSentence, TypedDependencies dependencies,
SpeciedElement element
1: List<SpeciedElement> result   new List<SpeciedElement>
2: for 8 TypedDependency conj 2 ndDependencies(\conj",parsedSentence,dependencies,element) do
3: xCompMatch   element instanceof Action ^ conj.governor() = ((Action)element).getXComp()
4: if conj.governor() = element ^ !partOfCop(conj.governor()) _ xCompMatch then
5: TreeGraphNode conjNode   conj.governor()
6: if xCompMatch then
7: Action newElement   ((Action)element).clone()
8: newElement.getxComp()   createAction(conjNode,dependencies)
9: else
10: if element instanceof Action then
11: Action newElement = createAction(conjNode,dependencies)
12: else
13: ExtractedObject newElement = createObject(conjNode,dependencies)
14: end if
15: end if
16: result [ newElement
17: result [ checkConjunctions(active, parsedSentence, dependencies, newElement)
18: conjunctions [ new Conjunction(conj,element,newElement)
19: end if
20: end for
21: return result
"""

"""
Algorithm 5 describes the procedure of nding and adding elements which are in a
conjunction relation. It was used within the algorithms 3,4, and 6. As it has to be able to
handle Actors, Resources, and Actions as input, it uses their common superclass Specied
Element (see 3.2) so it can be applied and used for all of them. It rst determines all
typed dependency relations with the name \conj" (line 2). Line 3 then handles Action
which have an associated open clausal complement (xcomp) and checks whether they are
the governor of a conjunction relationship. If a relation with either the element itself or
the open clausal complement of an Action as governor was found and the element is not
part of a copula relation (line 4), a new element has to be created. The check for the
copula relation has to be performed, as it is possible to create an object from the copula
element and have a conjunction assigned to it, as in this example sentence:
\Established underwriters are careful of their reputation and will not handle
a new issue [...]"
In this sentence a Resource is created from the noun phrase \careful of their reputation"
and careful is in a conjunction relationship with \handle". But this relation was already
captured during the conjunction analysis of the Action. Then, again, we make a distinction
between a match of the open clausal complement and all other cases (line 6), as
we do not want to lose the information stored in the parent-action of the open clausal
complement. Therefore, we rst create a copy of the parent object and simply replace the
xcomp element (line 7 and 8). This is necessary to create the desired actions as illustrated
by the following example.
 \The customer then has the chance to check the contract details and based on this
check may decide to either withdraw from the switch contract or conrm it."
Using algorithm 5 two activities are correctly recognized within this sentence:
1. (The customer)actor (may decide)action (to withdraw)xcomp ...
2. (The customer)actor (may decide)action (to conrm)xcomp ...
The last steps of the algorithms are to add the new element to the result set and call itself
recursively, as the new element could also be in a conjunction relation (e.g., \A and B
and C perform an action"). Furthermore, the relation between the two elements is stored
globally in a structure called Conjunctions, which is needed e.g. in algorithm 6, which is
introduced next.

"""