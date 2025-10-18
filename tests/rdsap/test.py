import sap10calcs
import json
import os
import math
from io import StringIO

local = True

url_rdsap = 'http://127.0.0.1:8000/calc/rdsap10' if local else 'https://netzeroapis.com/calc/rdsap10'
url_sap = 'http://127.0.0.1:8000/calc/sap10' if local else 'https://netzeroapis.com/calc/sap10'

def run_test(dir_, test):
    ""
    id_ = test['id']
    name = test['name']
    answers = test['answers']
    folder = os.path.join(dir_, id_)
    fp_in = os.path.join(folder, 'in.xml')
    fp_extra = os.path.join(folder, 'extra.json')
    fp_in_display = os.path.join(folder, 'in__display.xml')
    fp_response = os.path.join(folder, 'response.json')
    fp_xml = os.path.join(folder, 'out.xml')
    fp_xml_display = os.path.join(folder, 'out__display.xml')

    tree, rdsap_report = sap10calcs.parse_rdsap_xml(fp_in)
    with open(fp_in_display, 'w') as f: f.write(rdsap_report.display())  

    with open(fp_extra) as f:
        extra = json.load(f)
    
    response = sap10calcs.rdsap(
        input_file = fp_in,
        auth_token = None,
        url = url_rdsap
    )

    with open(fp_response, 'w') as f:
        json.dump(response, f, indent = 4)

    if response['rdsap_calculation_success'] == False:
        raise Exception(f'{response['rdsap_calculation_error_traceback']}[RDSAP: {id_}] ')

    tree, sap_report = sap10calcs.parse_xml(StringIO(response['sap_xml']))  
    tree.write(fp_xml, encoding="utf-8", xml_declaration=True, pretty_print=True)
    with open(fp_xml_display, 'w') as f: f.write(sap_report.display())  

    output_dict = response['rdsap_calculation_output_dict']

    for answer in answers:
        xpath = answer['xpath']
        value = answer['value']
        value2 = tree.xpath(xpath, namespaces = {'sap': 'https://epbr.digital.communities.gov.uk/xsd/sap'})[0].value
        if isinstance(value, str):
            if not value == value2: 
                raise Exception(xpath, value, value2)
        else:
        
            if not math.isclose(value, value2, rel_tol=0.01):  # 1%
                raise Exception(xpath, value, value2)
            
    # sap
    fp_in = fp_xml
    dir_sap = os.path.join(folder, 'sap')
    if not os.path.isdir(dir_sap): os.makedirs(dir_sap)
    fp_out = os.path.join(dir_sap, 'out.json')

    response = sap10calcs.calculate(
        input_file = fp_in,
        auth_token = None,
        url = url_sap
    )

    with open(fp_out, 'w') as f:
        json.dump(response, f, indent = 4)

    if response['sap_calculation_success'] == False:
        raise Exception(f'{response['sap_calculation_error_traceback']}[SAP: {id_}] ')




def run_tests(dir_):
    ""
    fp_in = os.path.join(dir_, 'manifest.json')

    if os.path.isfile(fp_in):

        with open(fp_in) as f:
            manifest = json.load(f)

        tests = manifest['tests']

        for test in tests:

            run_test(dir_, test)
            

if __name__ == '__main__':

    subdirs = [x for x in os.listdir() if os.path.isdir(x)]

    for subdir in subdirs:

        run_tests(subdir)
        
