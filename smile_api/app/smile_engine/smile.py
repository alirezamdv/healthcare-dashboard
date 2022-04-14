import pysmile
from .license import smile_license
from . import utils


class SmileEngine:
    """
    """

    def __init__(self, disease="dengue"):
        if disease == "dengue":
            xdsl_path = "/app/smile_engine/xdsls/den.xdsl"
            print(xdsl_path)
            self.outcome = "den_outcome"
        self.net = pysmile.Network()
        self.net.read_file(xdsl_path)

    def predict(self, json_input):

        symptoms = utils.json_parser(json_input)
        excluded = []
        for node in range(len(self.net.get_all_nodes())):
            if self.net.get_node_name(node) != self.outcome:
                node_name = self.net.get_node_name(node)
            # it just works with Model, without Model: if node_name not in symptoms.keys():
            if not symptoms[node_name]:
                excluded.append(node_name)
            else:
                utils.change_evidence_and_update(self.net, node_name, symptoms[node_name])

        self.net.update_beliefs()

        out = {"s1": (self.net.get_node_value(self.outcome))[0], "s0": (self.net.get_node_value(self.outcome))[1]}
        out["s1"] = 0 if round(out["s1"], 2) <= 0 else out["s1"]
        out["s0"] = 0 if round(out["s0"], 2) <= 0 else out["s0"]
        if len(excluded) > 0:
            out["impact_of_missing_inputs"] = self.max_difference_4each(excluded, out)
        print(out, excluded)
        return out

    def max_difference_4each(self, symptoms, out):
        rank = {}
        for i in range(len(symptoms)):
            outcome_ids = self.net.get_outcome_ids(symptoms[i])
            for j in range(len(outcome_ids)):
                net = self.net
                utils.change_evidence_and_update(net, symptoms[i], outcome_ids[j])
                out2 = {"s1": (net.get_node_value(self.outcome))[0],
                        "s0": (net.get_node_value(self.outcome))[1]}
                out2["s1"] = 0 if round(out2["s1"], 2) <= 0 else out2["s1"]
                out2["s0"] = 0 if round(out2["s0"], 2) <= 0 else out2["s0"]
                s1_diff = abs(round(out["s1"], 4) - round(out2["s1"], 4))
                s0_diff = abs(round(out["s0"], 4) - round(out2["s0"], 4))
                rank[symptoms[i]] = s1_diff if s1_diff > s0_diff else s0_diff

        return utils.sort_dictionary(rank, True)
