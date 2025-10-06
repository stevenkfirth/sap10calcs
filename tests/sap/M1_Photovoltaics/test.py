import sap10calcs
import json
import os
import math

local = True

with open('manifest.json') as f:
    manifest = json.load(f)

tests = manifest['tests']

for test in tests:
    id_ = test['id']
    name = test['name']
    description = test['description']
    folder = id_
    answers = test['answers']
    fp_in = os.path.join(folder, 'in.xml')
    fp_extra = os.path.join(folder, 'extra.json')
    fp_response = os.path.join(folder, 'response.json')
    fp_answer = os.path.join(folder, 'answer.json')

    with open(fp_extra) as f:
        extra = json.load(f)
    
    response = sap10calcs.calculate(
        input_file = fp_in,
        extra = extra,
        auth_token = None,
        url = 'http://127.0.0.1:8000/calc/sap10' if local else 'https://netzeroapis.com/calc/sap10'
    )

    with open(fp_response, 'w') as f:
        json.dump(response, f, indent = 4)

    output_dict = response['sap_calculation_output_dict']

    for answer in answers:
        key = answer['key']
        value = answer['value']
        value2 = output_dict[key]
        if not math.isclose(value, value2, rel_tol=0.01):  # 1%
            raise Exception(key, value, value2)
