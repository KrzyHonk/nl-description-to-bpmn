import string
from typing import List

from nltk.corpus import wordnet as wn
from spacy.tokens.doc import Doc

import main.extract_process_elements as extract
import main.find_gateway_keywords as gateways
from main.consts import Consts
from main.objects.svoconstruct import SvoConstruct


def generate_intermediate_model(doc: Doc, filename: str, output_directory: str):
    # elements extraction phase
    participants, svos = extract_elements_from_document(doc)

    # semantic analysis - find possible gateway relations
    gateways.find_gateway_keywords(doc, svos)

    # sort SVO in ascending order by position in sentence
    sort_svos_by_position(svos)
    with open(output_directory + filename + "_markers", "w") as file:
        for action in svos:
            file.write(action.gateway_keyword_print() + "\n")

    # generate intermediate diagram model
    conditional_gateway_started = False
    parallel_gateway_started = False
    gateway_branch_index = 0

    with open(output_directory + filename + "_intermediate_model", "w") as file:
        order = 0
        add_header_and_start_activity(file)

        while svos:
            svo, svos = get_head_from_list(svos)
            # check if this svo is a part of conditional gateway
            if svo.get_gateway_keyword() is not None \
                    and svo.get_gateway_keyword().casefold() in Consts.conditional_keywords:
                if parallel_gateway_started:
                    parallel_gateway_started = False
                if not conditional_gateway_started:
                    order += 1
                    conditional_gateway_started = True
                    gateway_branch_index = 0

                # create pair of condition and action
                if len(svos) > 0:
                    condition = svo
                    action, svos = get_head_from_list(svos)

                    suffix = string.ascii_lowercase[gateway_branch_index]
                    add_conditional_gateway_branch(file, order, suffix, condition, action)
                    gateway_branch_index += 1
                # if it's a last one SVO add it as a sequence flow
                else:
                    order += 1
                    add_sequence_flow(file, order, svo)

            # check if this svo is a part of parallel gateway
            elif svo.get_gateway_keyword() is not None \
                    and svo.get_gateway_keyword().casefold() in Consts.parallel_keywords:
                if conditional_gateway_started:
                    conditional_gateway_started = False
                if not parallel_gateway_started:
                    order += 1
                    parallel_gateway_started = True
                    gateway_branch_index = 0

                suffix = string.ascii_lowercase[gateway_branch_index]
                add_parallel_gateway_branch(file, order, suffix, svo)
                gateway_branch_index += 1

                # Add second task in parallel
                if len(svos) > 0:
                    svo, svos = get_head_from_list(svos)

                    suffix = string.ascii_lowercase[gateway_branch_index]
                    add_parallel_gateway_branch(file, order, suffix, svo)
                    gateway_branch_index += 1
                else:
                    order += 1
                    add_sequence_flow(file, order, svo)

            # check if this SVO is a default flow of gateway
            elif svo.get_gateway_keyword() is not None \
                    and svo.get_gateway_keyword().casefold() in Consts.default_flow_keywords:
                # check if it is a default flow of conditional gateway
                if conditional_gateway_started:
                    suffix = string.ascii_lowercase[gateway_branch_index]
                    add_default_flow_to_conditional_gateway(file, order, suffix, svo)
                    gateway_branch_index += 1

                # check if it is another flow of parallel gateway
                elif parallel_gateway_started:
                    suffix = string.ascii_lowercase[gateway_branch_index]
                    add_parallel_gateway_branch(file, order, suffix, svo)
                    gateway_branch_index += 1

                # add it as a sequence flow
                else:
                    if conditional_gateway_started:
                        conditional_gateway_started = False
                    if parallel_gateway_started:
                        parallel_gateway_started = False
                    gateway_branch_index = 0
                    order += 1
                    add_sequence_flow(file, order, svo)

            # add SVO as a task joined by sequence flow
            else:
                if conditional_gateway_started:
                    # if conditional gateway has only one flow, add default flow which leads to end event
                    if gateway_branch_index < 2:
                        suffix = string.ascii_lowercase[gateway_branch_index]
                        add_default_flow_with_end_event(file, order, suffix)
                        order += 1
                    conditional_gateway_started = False
                    gateway_branch_index = 0
                if parallel_gateway_started:
                    parallel_gateway_started = False
                    gateway_branch_index = 0
                order += 1
                add_sequence_flow(file, order, svo)

        if conditional_gateway_started and gateway_branch_index == 1:
            suffix = string.ascii_lowercase[gateway_branch_index]
            add_default_flow_pointing_to_end_event(file, order, suffix)

        order += 1
        add_end_event(file, order)


def extract_elements_from_document(doc: Doc):
    participants = []
    svos = []
    for sentence in doc.sents:
        out_participants, out_svos = extract.extract_process_elements(sentence)
        participants += out_participants
        svos += out_svos

    return participants, svos


def sort_svos_by_position(svos: List[SvoConstruct]):
    svos.sort(key=lambda elem: elem.get_position(), reverse=False)


def add_header_and_start_activity(file):
    file.write("Order,Activity,Condition,Who,Subprocess,Terminated\n")
    file.write("0,start,,,,,\n")


def add_sequence_flow(file, order, action: SvoConstruct):
    if action.get_participant() is not None and not action.get_participant().is_pronoun():
        file.write(str(order) + "," + action.pretty_print() + ",," + action.get_participant().pretty_print() + ",,\n")
    else:
        file.write(str(order) + "," + action.pretty_print() + ",,,,\n")


def add_conditional_gateway_branch(file, order, suffix, condition: SvoConstruct, action: SvoConstruct):
    if action.get_participant() is not None and not action.get_participant().is_pronoun():
        file.write(str(order) + suffix + "1," + action.pretty_print() + "," +
                   condition.pretty_print() + "," + action.get_participant().pretty_print() + ",,\n")
    else:
        file.write(str(order) + suffix + "1," + action.pretty_print() + "," +
                   condition.pretty_print() + ",,,\n")


def add_default_flow_to_conditional_gateway(file, order, suffix, action: SvoConstruct):
    if action.get_participant() is not None and not action.get_participant().is_pronoun():
        file.write(str(order) + suffix + "1," + action.pretty_print() + ",else,"
                   + action.get_participant().pretty_print() + ",,\n")
    else:
        file.write(str(order) + suffix + "1," + action.pretty_print() + ",else,,,\n")


def add_parallel_gateway_branch(file, order, suffix, action: SvoConstruct):
    if action.get_participant() is not None and not action.get_participant().is_pronoun():
        file.write(str(order) + suffix + "1," + action.pretty_print() + ",,"
                   + action.get_participant().pretty_print() + ",,\n")
    else:
        file.write(str(order) + suffix + "1," + action.pretty_print() + ",,,,\n")


def add_default_flow_with_end_event(file, order, suffix):
    add_default_flow_pointing_to_end_event(file, order, suffix)
    tmp_order = order + 1
    add_end_event(file, tmp_order)


def add_default_flow_pointing_to_end_event(file, order, suffix):
    tmp_order = order + 1
    file.write(str(order) + suffix + "1,goto " + str(tmp_order) + ",else,,,\n")


def add_end_event(file, order):
    file.write(str(order) + ",,,,,,yes\n")


def get_head_from_list(svos: List[SvoConstruct]):
    return (lambda collection: (collection[0], collection[1:]))(svos)
