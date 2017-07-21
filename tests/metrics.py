import unittest

import bpmn_python.bpmn_diagram_metrics as metrics
import bpmn_python.bpmn_diagram_rep as diagram


class GenerateProcessModelTests(unittest.TestCase):
    hand_made_models = "./input/bpmn/"
    generated_models = "./output/bpmn/"

    def test_thesis_models(self):
        format_three_dec = "{0:.3f}"
        format_two_dec = "{0:.2f}"
        names = [
            "model1",
            "model2",
            "model3",
            "model4",
            "model5",
            "model6",
            "model7",
            "model8",
            "model9",
            "model10",
            "model11",
            "model12",
            "model13",
            "model14",
            "model15",
            "model16",
            "model17",
            "model18",
            "model19",
            "model20",
            "model21",
            "model22",
            "model23",
            "model24",
            "model25",
            "model26",
            "model27",
            "model28",
            "model29",
            "model30",
            "model31",
            "model32"
        ]

        with open("./output/metrics_part1.csv", "w") as file_one:
            with open("./output/metrics_part2.csv", "w") as file_two:
                with open("./output/metrics_min_max.csv", "w") as file_three:
                    # write header
                    file_one.write("Model name,NOA-H,NOA-G,NOA-diff,NOA-prop,NOC-H,NOC-G,NOC-diff,NOC-prop\n")
                    file_two.write("Model name,CNC-H,CNC-G,CNC-diff,Avg-H,Avg-G,Avg-diff,Heter-H,Heter-G,Heter-diff\n")
                    counter = 1

                    noa_max_diff = None
                    noa_max_diff_index = 0
                    noa_max_prop = None
                    noa_max_prop_index = 0
                    noa_min_diff = None
                    noa_min_diff_index = 0
                    noa_min_prop = None
                    noa_min_prop_index = 0
                    noa_sum = 0

                    noc_max_diff = None
                    noc_max_diff_index = 0
                    noc_max_prop = None
                    noc_max_prop_index = 0
                    noc_min_diff = None
                    noc_min_diff_index = 0
                    noc_min_prop = None
                    noc_min_prop_index = 0
                    noc_sum = 0

                    cnc_max = None
                    cnc_max_diff = None
                    cnc_max_index = 0
                    cnc_min = None
                    cnc_min_diff = None
                    cnc_min_index = 0
                    cnc_diff_sum = 0

                    avg_max_diff = None
                    avg_max_index = 0
                    avg_min_diff = None
                    avg_min_index = 0
                    avg_diff_sum = 0

                    heter_max_diff = None
                    heter_max_index = 0
                    heter_min_diff = None
                    heter_min_index = 0

                    for model_name in names:
                        print(model_name)
                        hand_made_bpmn = diagram.BpmnDiagramGraph()
                        hand_made_bpmn.load_diagram_from_xml_file(self.hand_made_models + model_name + ".bpmn")
                        hand_made_noa = metrics.NOA_metric(hand_made_bpmn)
                        hand_made_noc = metrics.NOAC_metric(hand_made_bpmn) - hand_made_noa
                        hand_made_cnc = metrics.CoefficientOfNetworkComplexity_metric(hand_made_bpmn)
                        if metrics.all_gateways_count(hand_made_bpmn) > 0:
                            hand_made_avg = metrics.AverageGatewayDegree_metric(hand_made_bpmn)
                        else:
                            hand_made_avg = 0
                        hand_made_heter = int(metrics.GatewayHeterogenity_metric(hand_made_bpmn))

                        gen_bpmn = diagram.BpmnDiagramGraph()
                        gen_bpmn.load_diagram_from_xml_file(self.generated_models + model_name + ".bpmn")
                        gen_noa = metrics.NOA_metric(gen_bpmn)
                        gen_noc = metrics.NOAC_metric(gen_bpmn) - gen_noa
                        gen_cnc = metrics.CoefficientOfNetworkComplexity_metric(gen_bpmn)
                        if cnc_max is None:
                            cnc_max = gen_cnc
                        elif cnc_max < gen_cnc:
                            cnc_max = gen_cnc
                        if cnc_min is None:
                            cnc_min = gen_cnc
                        elif cnc_min > gen_cnc:
                            cnc_min = gen_cnc
                        if metrics.all_gateways_count(gen_bpmn) > 0:
                            gen_avg = metrics.AverageGatewayDegree_metric(gen_bpmn)
                        else:
                            gen_avg = 0
                        gen_heter = int(metrics.GatewayHeterogenity_metric(gen_bpmn))

                        noa_diff = hand_made_noa - gen_noa
                        noa_prop = (noa_diff * 100.0) / hand_made_noa
                        noa_sum += noa_prop
                        if noa_max_diff is None:
                            noa_max_diff = noa_diff
                            noa_max_diff_index = counter
                        elif noa_diff > noa_max_diff:
                            noa_max_diff = noa_diff
                            noa_max_diff_index = counter
                        if noa_max_prop is None:
                            noa_max_prop = noa_diff
                            noa_max_prop_index = counter
                        elif noa_prop > noa_max_prop:
                            noa_max_prop = noa_prop
                            noa_max_prop_index = counter
                        if noa_min_diff is None:
                            noa_min_diff = noa_diff
                            noa_min_diff_index = counter
                        elif noa_diff < noa_min_diff:
                            noa_min_diff = noa_diff
                            noa_min_diff_index = counter
                        if noa_min_prop is None:
                            noa_min_prop = noa_diff
                            noa_min_prop_index = counter
                        elif noa_prop < noa_min_prop:
                            noa_min_prop = noa_prop
                            noa_min_prop_index = counter

                        noc_diff = hand_made_noc - gen_noc
                        noc_prop = (noc_diff * 100.0) / hand_made_noc
                        noc_sum += noc_prop
                        if noc_max_diff is None:
                            noc_max_diff = noc_diff
                            noc_max_diff_index = counter
                        elif noc_diff > noc_max_diff:
                            noc_max_diff = noc_diff
                            noc_max_diff_index = counter
                        if noc_max_prop is None:
                            noc_max_prop = noc_prop
                            noc_max_prop_index = counter
                        elif noc_prop > noc_max_prop:
                            noc_max_prop = noc_prop
                            noc_max_prop_index = counter
                        if noc_min_diff is None:
                            noc_min_diff = noc_diff
                            noc_min_diff_index = counter
                        elif noc_diff < noc_min_diff:
                            noc_min_diff = noc_diff
                            noc_min_diff_index = counter
                        if noc_min_prop is None:
                            noc_min_prop = noc_prop
                            noc_min_prop_index = counter
                        elif noc_prop < noc_min_prop:
                            noc_min_prop = noc_prop
                            noc_min_prop_index = counter

                        cnc_diff = hand_made_cnc - gen_cnc
                        cnc_diff_sum += cnc_diff
                        if cnc_max_diff is None:
                            cnc_max_diff = cnc_diff
                        elif cnc_diff > cnc_max_diff:
                            cnc_max_diff = cnc_diff
                            cnc_max_index = counter
                        if cnc_min_diff is None:
                            cnc_min_diff = cnc_diff
                        elif cnc_diff < cnc_min_diff:
                            cnc_min_diff = cnc_diff
                            cnc_min_index = counter

                        avg_diff = hand_made_avg - gen_avg
                        avg_diff_sum += avg_diff
                        if avg_max_diff is None:
                            avg_max_diff = avg_diff
                        elif avg_diff > avg_max_diff:
                            avg_max_diff = avg_diff
                            avg_max_index = counter
                        if avg_min_diff is None:
                            avg_min_diff = avg_diff
                        elif avg_diff < avg_min_diff:
                            avg_min_diff = avg_diff
                            avg_min_index = counter

                        heter_diff = hand_made_heter - gen_heter
                        if heter_max_diff is None:
                            heter_max_diff = heter_diff
                        elif heter_diff > heter_max_diff:
                            heter_max_diff = heter_diff
                            heter_max_index = counter
                        if heter_min_diff is None:
                            heter_min_diff = heter_diff
                        elif heter_diff < heter_min_diff:
                            heter_min_diff = heter_diff
                            heter_min_index = counter

                        file_one.write("Model " + str(counter) + "," + str(hand_made_noa) + "," + str(gen_noa) + ","
                                       + str(noa_diff) + "," + format_two_dec.format(noa_prop) + "\%,"
                                       + str(hand_made_noc) + "," + str(gen_noc) + "," + str(noc_diff) + ","
                                       + format_two_dec.format(noc_prop) + "\%\n")
                        file_two.write("Model " + str(counter) + "," + format_three_dec.format(hand_made_cnc) + ","
                                       + format_three_dec.format(gen_cnc) + "," + format_three_dec.format(cnc_diff)
                                       + "," + format_three_dec.format(hand_made_avg) + ","
                                       + format_three_dec.format(gen_avg) + "," + format_three_dec.format(avg_diff)
                                       + "," + str(hand_made_heter) + "," + str(gen_heter) + "," + str(heter_diff)
                                       + "\n")
                        counter += 1

                    file_three.write(
                        "CNC metric: avg=" + format_three_dec.format(cnc_diff_sum / counter)
                        + ", min=" + format_three_dec.format(cnc_min_diff)
                        + ", model: " + str(cnc_min_index)
                        + ", max=" + format_three_dec.format(cnc_max_diff)
                        + ", model: " + str(cnc_max_index)
                        + ", global min: " + format_three_dec.format(cnc_min)
                        + ", global max: " + format_three_dec.format(cnc_max) + "\n")
                    file_three.write(
                        "Average Gateway Degree metric: avg=" + format_three_dec.format(avg_diff_sum / counter)
                        + ", min=" + format_three_dec.format(avg_min_diff)
                        + ", model: " + str(avg_min_index)
                        + ", max=" + format_three_dec.format(avg_max_diff)
                        + ", model: " + str(avg_max_index) + "\n")
                    file_three.write(
                        "Gateway Heterogenity metric: "
                        + "min=" + str(heter_min_diff)
                        + ", model: " + str(heter_min_index)
                        + ", max=" + str(heter_max_diff)
                        + ", model: " + str(heter_max_index) + "\n")
                    file_three.write(
                        "NOA metric (diff): "
                        + "min=" + str(noa_min_diff)
                        + ", model: " + str(noa_min_diff_index)
                        + ", max=" + str(noa_max_diff)
                        + ", model: " + str(noa_max_diff_index) + "\n")
                    file_three.write(
                        "NOA metric (prop): "
                        + "min=" + format_two_dec.format(noa_min_prop)
                        + ", model: " + str(noa_min_prop_index)
                        + ", max=" + format_two_dec.format(noa_max_prop)
                        + ", model: " + str(noa_max_prop_index)
                        + ", average: " + format_two_dec.format(noa_sum / counter) + "\n")
                    file_three.write(
                        "NOC metric (diff): "
                        + "min=" + str(noc_min_diff)
                        + ", model: " + str(noc_min_diff_index)
                        + ", max=" + str(noc_max_diff)
                        + ", model: " + str(noc_max_diff_index) + "\n")
                    file_three.write(
                        "NOC metric (prop): "
                        + "min=" + format_two_dec.format(noc_min_prop)
                        + ", model: " + str(noc_min_prop_index)
                        + ", max=" + format_two_dec.format(noc_max_prop)
                        + ", model: " + str(noc_max_prop_index)
                        + ", average: " + format_two_dec.format(noc_sum / counter) + "\n")



if __name__ == "__main__":
    unittest.main()
