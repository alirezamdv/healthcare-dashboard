import json


def change_evidence_and_update(net, node_id, outcome_id):
    if outcome_id is not None:
        net.set_evidence(node_id, outcome_id)
    else:
        net.clear_evidence(node_id)
    net.update_beliefs()


def sort_dictionary(dictionary, reverse=False):
    """
    :param dictionary: dictionary to be sorted
    :return: sorted dictionary
    """
    return {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1], reverse=reverse)}


def json_parser(jsonstring):
    try:
        symptoms = json.loads(jsonstring)
        return symptoms
    except json.decoder.JSONDecodeError as e:
        raise ("Invalid JSON", e)
