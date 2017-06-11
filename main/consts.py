class Consts(object):
    svo_descriptors_set = ["amod", "acomp", "aux", "auxpass", "neg"]
    participant_descriptors_set = ["amod", "acomp", "aux", "auxpass", "compound", "neg", "poss"]
    skippable_dependencies_set = ["amod", "acomp", "aux", "auxpass", "compound", "conj", "neg", "poss", "xcomp"]

    conditional_keywords = ["if", "whether"]
    default_flow_keywords = ["otherwise"]
    parallel_keywords = ["while"]
    gateways_keywords = conditional_keywords + default_flow_keywords + parallel_keywords

    replaceable_verbs = ["be", "can", "do", "go", "have", "go"]
    ignorable_verbs = ["achieve", "base", "by", "exist", "know", "make", "need"]
    skippable_verbs = replaceable_verbs + ignorable_verbs
