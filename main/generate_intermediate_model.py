import string
from typing import List

from spacy.tokens.doc import Doc

import main.extract_process_elements as extract
import main.find_gateway_keywords as gateways
from main import utils
from main.consts import Consts
from main.objects.svoconstruct import SvoConstruct


def generate_intermediate_model(doc: Doc, filename: str, output_directory: str):
    # elements extraction phase
    participants, svos = extract_elements_from_document(doc)

    # semantic analysis - find possible gateway relations
    gateways.find_gateway_keywords(doc, svos)

    # sort SVO in ascending order by position in sentence
    sort_svos_by_position(svos)
    with open(output_directory + "markers/" + filename.split(".")[0] + "_markers", "w") as file:
        for action in svos:
            file.write(utils.svo_gateway_keyword_print(action) + "\n")

    # generate intermediate diagram model
    conditional_gateway_started = False
    parallel_gateway_started = False
    gateway_branch_index = 0

    with open(output_directory + filename.split(".")[0] + "_intermediate_model.csv", "w") as file:
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
                    while not svo_check_validity_as_activity(action) and len(svos) > 0:
                        condition = action
                        action, svos = get_head_from_list(svos)
                    if svo_check_validity_as_activity(action):
                        add_conditional_gateway_branch(file, order, suffix, condition, action)
                    else:
                        parallel_gateway_started = False
                    gateway_branch_index += 1
                # if it's a last one SVO add it as a sequence flow
                else:
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
                while not svo_check_validity_as_activity(svo) and len(svos) > 0:
                    svo, svos = get_head_from_list(svos)
                if svo_check_validity_as_activity(svo):
                    add_parallel_gateway_branch(file, order, suffix, svo)
                else:
                    parallel_gateway_started = False
                gateway_branch_index += 1

                # Add second task in parallel
                if len(svos) > 0:
                    svo, svos = get_head_from_list(svos)

                    suffix = string.ascii_lowercase[gateway_branch_index]
                    while not svo_check_validity_as_activity(svo) and len(svos) > 0:
                        svo, svos = get_head_from_list(svos)
                    if svo_check_validity_as_activity(svo):
                        add_parallel_gateway_branch(file, order, suffix, svo)
                    else:
                        parallel_gateway_started = False
                    gateway_branch_index += 1

            # check if this SVO is a default flow of gateway
            elif svo.get_gateway_keyword() is not None \
                    and svo.get_gateway_keyword().casefold() in Consts.default_flow_keywords:
                # check if it is a default flow of conditional gateway
                if conditional_gateway_started:
                    suffix = string.ascii_lowercase[gateway_branch_index]
                    while not svo_check_validity_as_activity(svo) and len(svos) > 0:
                        svo, svos = get_head_from_list(svos)
                    if svo_check_validity_as_activity(svo):
                        add_default_flow_to_conditional_gateway(file, order, suffix, svo)
                    gateway_branch_index += 1

                # check if it is another flow of parallel gateway
                elif parallel_gateway_started:
                    suffix = string.ascii_lowercase[gateway_branch_index]
                    while not svo_check_validity_as_activity(svo) and len(svos) > 0:
                        svo, svos = get_head_from_list(svos)
                    if svo_check_validity_as_activity(svo):
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
                    while not svo_check_validity_as_activity(svo) and len(svos) > 0:
                        svo, svos = get_head_from_list(svos)
                    if svo_check_validity_as_activity(svo):
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
                while not svo_check_validity_as_activity(svo) and len(svos) > 0:
                    svo, svos = get_head_from_list(svos)
                if svo_check_validity_as_activity(svo):
                    add_sequence_flow(file, order, svo)
                else:
                    conditional_gateway_started = False

        if conditional_gateway_started and gateway_branch_index == 1:
            suffix = string.ascii_lowercase[gateway_branch_index]
            add_default_flow_pointing_to_end_event(file, order, suffix)

        order += 1
        add_end_event(file, order)


def extract_elements_from_document(doc: Doc):
    participants = []
    svos = []
    for sentence in doc.sents:
        print(sentence)
        utils.to_nltk_tree(sentence.root).pretty_print()
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
        file.write(str(order) + "," + create_activity_from_svo(action) + ",,"
                   + utils.participant_print_full_name(action.get_participant()) + ",,\n")
    else:
        file.write(str(order) + "," + create_activity_from_svo(action) + ",,,,\n")


def add_conditional_gateway_branch(file, order, suffix, condition: SvoConstruct, action: SvoConstruct):
    if condition.get_participant() is not None and not condition.get_participant().is_pronoun():
        file.write(str(order) + suffix + "1," + create_activity_from_svo(action) + "," +
                   utils.svo_print_full_name(condition) + ","
                   + utils.participant_print_full_name(condition.get_participant()) + ",,\n")
    else:
        file.write(str(order) + suffix + "1," + create_activity_from_svo(action) + "," +
                   utils.svo_print_full_name(condition) + ",,,\n")


def add_default_flow_to_conditional_gateway(file, order, suffix, action: SvoConstruct):
    if action.get_participant() is not None and not action.get_participant().is_pronoun():
        file.write(str(order) + suffix + "1," + create_activity_from_svo(action) + ",else,"
                   + utils.participant_print_full_name(action.get_participant()) + ",,\n")
    else:
        file.write(str(order) + suffix + "1," + create_activity_from_svo(action) + ",else,,,\n")


def add_parallel_gateway_branch(file, order, suffix, action: SvoConstruct):
    if action.get_participant() is not None and not action.get_participant().is_pronoun():
        file.write(str(order) + suffix + "1," + create_activity_from_svo(action) + ",,"
                   + utils.participant_print_full_name(action.get_participant()) + ",,\n")
    else:
        file.write(str(order) + suffix + "1," + create_activity_from_svo(action) + ",,,,\n")


def add_default_flow_with_end_event(file, order, suffix):
    add_default_flow_pointing_to_end_event(file, order, suffix)
    tmp_order = order + 1
    add_end_event(file, tmp_order)


def add_default_flow_pointing_to_end_event(file, order, suffix):
    tmp_order = order + 1
    file.write(str(order) + suffix + "1,goto " + str(tmp_order) + ",else,,,\n")


def add_end_event(file, order):
    file.write(str(order) + ",,,,,yes\n")


def get_head_from_list(svos: List[SvoConstruct]):
    return (lambda collection: (collection[0], collection[1:]))(svos)


def svo_check_validity_as_activity(svo: SvoConstruct):
    verb = svo.get_verb()
    if utils.svo_validate_ignorable_verb(verb):
        # Do not add this SVO as activity
        return False
    elif utils.svo_validate_replecable_verb(verb):
        # Try to find replacement for verb. If no replacement found - ignore this SVO
        replacement = utils.svo_get_verb_replacement(verb)
        if replacement is not None:
            return True
        else:
            return False
    else:
        # Neither ignorable or replaceable - passes
        return True


def create_activity_from_svo(svo: SvoConstruct):
    # Determine if activity should be created as verb-subject or verb-object
    if svo.get_object() is None or svo.get_object().pos_ == "VERB":
        return utils.svo_print_verb_subject(svo)
    else:
        return utils.svo_print_verb_object(svo)
