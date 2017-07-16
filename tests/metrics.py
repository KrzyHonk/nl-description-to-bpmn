import math
import unittest

import bpmn_python.bpmn_diagram_metrics as metrics
import bpmn_python.bpmn_diagram_rep as diagram


class GenerateProcessModelTests(unittest.TestCase):
    hand_made_models = "./input/bpmn/"
    generated_models = "./output/bpmn/"

    def test_thesis_models(self):
        format_string = "{0:.3f}"
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
            "model31"
        ]

        with open("./output/metrics_part1.csv", "w") as file_one:
            with open("./output/metrics_part2.csv", "w") as file_two:
                # write header
                file_one.write("Model name,NOA-H,NOA-G,NOA-diff,NOA-prop,NOAC-H,NOAC-G,NOAC-diff,NOAC-prop\n")
                file_two.write("Model name,CNC-H,CNC-G,CNC-diff,Avg-H,Avg-G,Avg-diff,Heter-H,Heter-G,Heter-diff\n")
                counter = 1

                for model_name in names:
                    print(model_name)
                    hand_made_bpmn = diagram.BpmnDiagramGraph()
                    hand_made_bpmn.load_diagram_from_xml_file(self.hand_made_models + model_name + ".bpmn")
                    hand_made_noa = metrics.NOA_metric(hand_made_bpmn)
                    hand_made_noac = metrics.NOAC_metric(hand_made_bpmn)
                    hand_made_coeff = metrics.CoefficientOfNetworkComplexity_metric(hand_made_bpmn)
                    if metrics.all_gateways_count(hand_made_bpmn) > 0:
                        hand_made_avg = metrics.AverageGatewayDegree_metric(hand_made_bpmn)
                    else:
                        hand_made_avg = 0
                    hand_made_heter = metrics.GatewayHeterogenity_metric(hand_made_bpmn)

                    gen_bpmn = diagram.BpmnDiagramGraph()
                    gen_bpmn.load_diagram_from_xml_file(self.generated_models + model_name + ".bpmn")
                    gen_noa = metrics.NOA_metric(gen_bpmn)
                    gen_noac = metrics.NOAC_metric(gen_bpmn)
                    gen_coeff = metrics.CoefficientOfNetworkComplexity_metric(gen_bpmn)
                    if metrics.all_gateways_count(gen_bpmn) > 0:
                        gen_avg = metrics.AverageGatewayDegree_metric(gen_bpmn)
                    else:
                        gen_avg = 0
                    gen_heter = metrics.GatewayHeterogenity_metric(gen_bpmn)

                    noa_abs = int(math.fabs(hand_made_noa - gen_noa))
                    noa_prop = (noa_abs * 100.0) / hand_made_noa
                    noac_abs = int(math.fabs(hand_made_noac - gen_noac))
                    noac_prop = (noac_abs * 100.0) / hand_made_noac
                    coeff_abs = math.fabs(hand_made_coeff - gen_coeff)
                    avg_abs = math.fabs(hand_made_avg - gen_avg)
                    heter_abs = math.fabs(hand_made_heter - gen_heter)

                    file_one.write("Model " + str(counter) + ","
                                   + str(hand_made_noa) + "," + str(gen_noa) + "," + str(noa_abs) + ","
                                   + format_string.format(noa_prop) + "," + str(hand_made_noac) + "," +
                                   str(gen_noac) + "," + str(noac_abs) + "," + format_string.format(noac_prop) + "\n")
                    file_two.write("Model " + str(counter) + ","
                                   + format_string.format(hand_made_coeff) + "," + format_string.format(gen_coeff) + ","
                                   + format_string.format(coeff_abs) + "," + format_string.format(hand_made_avg) + ","
                                   + format_string.format(gen_avg) + "," + format_string.format(avg_abs) + ","
                                   + format_string.format(hand_made_heter) + "," + format_string.format(gen_heter) + ","
                                   + format_string.format(heter_abs) + "\n")
                    counter += 1


if __name__ == "__main__":
    unittest.main()
