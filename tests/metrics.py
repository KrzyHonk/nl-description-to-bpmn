import unittest

import bpmn_python.bpmn_diagram_rep as diagram
import bpmn_python.bpmn_diagram_metrics as metrics


class GenerateProcessModelTests(unittest.TestCase):
    hand_made_models = "./input/bpmn/"
    generated_models = "./output/bpmn/"

    def test_thesis_models(self):
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
            "model23"
        ]

        '''
            "model24",
            "model25",
            "model26",
            "model27",
            "model28",
            "model29",
            "model30",
            "model31",
            "model32",
            "model33",
            "model34",
            "model35",
            "model36",
            "model37",
            "model38",
            "model39",
            "model40",
            "model41",
            "model42",
            "model43",
            "model44",
            "model45"
        '''
        with open("./output/metrics", "w") as file:
            # write header
            file.write("Model name,NOA metric - handmade model,NOAC metric - handmade model,"
                       "Coefficient of network complexity metric - handmade model,"
                       "Average gateway degree metric - handmade model,"
                       "Gateway Heterogenity metric - handmade model,"
                       "NOA metric - generated model,NOAC metric - generated model,"
                       "Coefficient of network complexity metric - generated model,"
                       "Average gateway degree metric - generated model,"
                       "Gateway Heterogenity metric - generated model\n")

            for model_name in names:
                print(model_name)
                hand_made_bpmn = diagram.BpmnDiagramGraph()
                hand_made_bpmn.load_diagram_from_xml_file(self.hand_made_models + model_name + ".bpmn")
                hand_made_noa = metrics.NOA_metric(hand_made_bpmn)
                hand_made_noac = metrics.NOAC_metric(hand_made_bpmn)
                hand_made_coeff = metrics.CoefficientOfNetworkComplexity_metric(hand_made_bpmn)
                # hand_made_avg = metrics.AverageGatewayDegree_metric(hand_made_bpmn)
                hand_made_avg = 0
                hand_made_heter = metrics.GatewayHeterogenity_metric(hand_made_bpmn)

                generated_bpmn = diagram.BpmnDiagramGraph()
                generated_bpmn.load_diagram_from_xml_file(self.generated_models + model_name + ".bpmn")
                generated_noa = metrics.NOA_metric(generated_bpmn)
                generated_noac = metrics.NOAC_metric(generated_bpmn)
                generated_coeff = metrics.CoefficientOfNetworkComplexity_metric(generated_bpmn)
                # TODO temporary - metrics script does not work with zero gateways
                # generated_avg = metrics.AverageGatewayDegree_metric(generated_bpmn)
                generated_avg = 0
                generated_heter = metrics.GatewayHeterogenity_metric(generated_bpmn)

                file.write(model_name + "," + str(hand_made_noa) + "," + str(hand_made_noac) + ","
                           + str(hand_made_coeff) + "," + str(hand_made_avg) + "," + str(hand_made_heter) + "," +
                           str(generated_noa) + "," + str(generated_noac) + "," + str(generated_coeff) + "," +
                           str(generated_avg) + "," + str(generated_heter) + "\n")

if __name__ == "__main__":
    unittest.main()
