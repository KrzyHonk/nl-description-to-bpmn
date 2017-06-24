class Consts(object):
    svo_descriptors_list = ["amod", "acomp", "aux", "auxpass", "neg"]
    participant_descriptors_list = ["amod", "acomp", "aux", "auxpass", "compound", "neg", "poss"]
    object_descriptors_list = ["amod", "acomp", "aux", "auxpass", "compound", "det", "neg", "poss"]
    skippable_dependencies_list = ["amod", "acomp", "aux", "auxpass", "compound", "conj",
                                   "neg", "prep", "poss", "xcomp"]
    pronoun_list = ["i", "me", "we", "us", "you", "she", "her", "he", "him", "it", "they", "them", "who", "whom",
                    "whose", "what", "which", "that"]

    conditional_keywords = ["if", "whether"]
    default_flow_keywords = ["otherwise"]
    parallel_keywords = ["while"]
    gateways_keywords = conditional_keywords + default_flow_keywords + parallel_keywords

    replaceable_verbs = ["be", "can", "do", "go", "have"]
    ignorable_verbs = ["achieve", "base", "exist", "know", "make", "need"]
    skippable_verbs = replaceable_verbs + ignorable_verbs

    message_event_verbs = ["send", "receive"]

    order_prop = "Order"
    activity_prop = "Activity"
    condition_prop = "Condition"
    who_prop = "Who"
    subprocess_prop = "Subprocess"
    terminated_prop = "Terminated"