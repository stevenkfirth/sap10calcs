
# cd "C:\Users\cvskf\OneDrive - Loughborough University\_Git\stevenkfirth\sap10calcs\tests\sap\api_data"
# python -m main

# #--- launch local browser
# #[ANACONDA PROMPT]
# cd "C:\Users\cvskf\OneDrive - Loughborough University\_Git\stevenkfirth\sap10_heroku"
# conda activate sap10_heroku
# set DATABASE_URL=postgresql://postgres:postgres@localhost:5432
# uvicorn app.main:app --reload

# code "input_data\json_indented\0000-5142-0322-4301-3263.json"

import sap10calcs
import os
from lxml import etree
import json
import logging
from io import StringIO

logging.basicConfig(filename='main.log', level=logging.INFO, 
                    #filemode = 'w'
                    )

local = True
url_sap = 'http://127.0.0.1:8000/calc/sap10' if local else 'https://netzeroapis.com/calc/sap10'

for i, fn in enumerate(os.listdir(os.path.join('input_data', 'json_indented'))):

    if i < 95173: continue

    print(i, fn)

    with open(os.path.join('input_data', 'json_indented', fn)) as f: 
        j = json.load(f)
        
    try:
        tree_sap, sap_report = sap10calcs.parse_sap_json(
            os.path.join('input_data', 'json_indented', fn)
        )
    except Exception as err:
        if str(err).startswith('SAP schema not equal to "SAP-Schema-19.2.0"'):
            print((i, fn, str(err)))
            logging.error(f'{i}, {fn}, {str(err)}')
            continue
        else:
            with open('rdsap.json', 'w') as f: json.dump(j, f, indent = 4)
            print(i, fn)
            raise err
        
    continue

    response_rdsap = sap10calcs.rdsap(
        input_lxml = rdsap_report,
        auth_token = None,
        url = url_rdsap
    )

    if response_rdsap['rdsap_calculation_success'] == False:
        msg = response_rdsap['rdsap_calculation_error_message']
        if (
            msg.startswith('The text value of the Window-Wall-Type XML element is incorrect')
            or msg.startswith('The text value of the Wall-Thickness XML element is incorrect ("0")')
            or msg.startswith('The text value of the Measurement-Type XML element is incorrect (current value is "2")')
            or msg.startswith('The text value of the Room-Height XML element is incorrect ("0.0")')
            or msg.startswith('The Description XML element is missing. This is a child element of the [0] SAP-Special-Feature XML element.')
            or msg.startswith('The Energy-Feature XML element is missing.')
            or msg.startswith('The Emissions-Feature XML element is missing.')
            or msg.startswith('The text value of the Wall-Area XML element is incorrect ("0.0").')
            or msg.startswith('The text value of the Cylinder-Size XML element is incorrect (actual size included in Solar-Water-Heating-Details).')
        ):  
            print(i, fn, response_rdsap['rdsap_calculation_error_message'])
            logging.error(f'{i}, {fn}, {response_rdsap['rdsap_calculation_error_message']}')
        else:
            with open('rdsap.json', 'w') as f: json.dump(j, f, indent = 4)
            with open('rdsap.xml', 'w') as f: f.write(etree.tostring(rdsap_report, pretty_print=True).decode())
            with open('rdsap__display.xml', 'w') as f: f.write(rdsap_report.display())
            with open('rdsap_response.json', 'w') as f: json.dump(response_rdsap, f, indent = 4)
            raise Exception(response_rdsap['rdsap_calculation_error_traceback'])
        
    #continue

    tree_sap, sap_report = sap10calcs.parse_xml(StringIO(response_rdsap['sap_xml'])) 
    response_sap = sap10calcs.calculate(
        input_lxml = sap_report,
        auth_token = None,
        url = url_sap
    )
    if response_sap['sap_calculation_success'] == False:
        with open('rdsap.json', 'w') as f: json.dump(j, f, indent = 4)
        with open('rdsap.xml', 'w') as f: f.write(etree.tostring(rdsap_report, pretty_print=True).decode())
        with open('rdsap__display.xml', 'w') as f: f.write(rdsap_report.display())
        with open('rdsap_response.json', 'w') as f: json.dump(response_rdsap, f, indent = 4)
        with open('sap.xml', 'w') as f: f.write(etree.tostring(sap_report, pretty_print=True).decode())
        with open('sap__display.xml', 'w') as f: f.write(sap_report.display())
        with open('sap_response.json', 'w') as f: json.dump(response_sap, f, indent = 4)
        raise Exception(response_sap['sap_calculation_error_traceback'])


    #break

    #fn_out = os.path.join('output_data', 'rdsap_xml_display', fn.replace('.json', '__display.xml'))
    #with open(fn_out, 'w') as f: f.write(root.display())

    #print(etree.tostring(root, pretty_print=True).decode())

    #break



# if fn in [
#         '0019-3058-6202-9146-5200.json',  # RdSAPInputFileError: The text value of the Window-Wall-Type XML element is incorrect (current value is "common wall 1 Only include for RR Type 2.")). There is no "common wall 1 Only include for RR Type 2." in the [2] Building-Part XML element.
#         '0024-1203-3406-7631-1900.json',  # RdSAPInputFileError - a floor height of 0
#         '0024-1205-4506-1612-1404.json',  # RdSAPInputFileError - window location given as Alternative Wall 1, but this wall doesn't exist
#         '0025-2200-1006-0526-1200.json',  # RdSAPInputFileError: The text value of the Window-Wall-Type XML element is incorrect (current value is "Roof of Room in Roof")). There is no "Roof of Room in Roof" in the [0] Building-Part XML element.
#         '0026-0203-9406-0639-8704.json',  # RdSAPInputFileError: The text value of the Measurement-Type XML element is incorrect (current value is "2"). Flats and Maisonettes should always be measured internally so the value should be "Internal". 
#         '0027-0207-6606-9605-0014.json',  # RdSAPInputFileError: The text value of the Window-Wall-Type XML element is incorrect (current value is "common wall 2 Only include for RR Type 2.")). There is no "common wall 2 Only include for RR Type 2." in the [0] Building-Part XML element.
#         '0028-0203-2406-1108-2404.json',  # RdSAPInputFileError: The text value of the Window-Wall-Type XML element is incorrect (current value is "Alternative wall 1")). There is no "Alternative wall 1" in the [2] Building-Part XML element.
#         '0036-2022-1500-0172-9292.json',  # RdSAPInputFileError: The text value of the Window-Wall-Type XML element is incorrect (current value is "common wall 1 Only include for RR Type 2.")). There is no "common wall 1 Only include for RR Type 2." in the [1] Building-Part XML element. 
#         '0036-2922-2500-0181-8202.json',  # RdSAPInputFileError: The text value of the Wall-Thickness XML element is incorrect ("0"). The value should be a number greater than 0. 
#         '0036-9429-7500-0868-8222.json',  # RdSAPInputFileError: The text value of the Wall-Thickness XML element is incorrect ("0"). The value should be a number greater than 0.
#         '0051-3058-0202-0316-8204.json',  # RdSAPInputFileError: The text value of the Window-Wall-Type XML element is incorrect (current value is "common wall 1 Only include for RR Type 2.")). There is no "common wall 1 Only include for RR Type 2." in the [0] Building-Part XML element. 
#         '0059-3058-2202-9066-8204.json',  # RdSAPInputFileError: The text value of the Window-Wall-Type XML element is incorrect (current value is "common wall 1 Only include for RR Type 2.")). There is no "common wall 1 Only include for RR Type 2." in the [0] Building-Part XML element. 
#         '0070-3058-4202-7476-6200.json',  # RdSAPInputFileError: The text value of the Window-Wall-Type XML element is incorrect (current value is "common wall 1 Only include for RR Type 2.")). There is no "common wall 1 Only include for RR Type 2." in the [0] Building-Part XML element.
#         '0099-3009-7202-8206-4200.json',  # RdSAPInputFileError: The text value of the Window-Wall-Type XML element is incorrect (current value is "common wall 2 Only include for RR Type 2.")). There is no "common wall 2 Only include for RR Type 2." in the [0] Building-Part XML element. 
#         '0136-2122-4100-0122-1202.json',  # RdSAPInputFileError: The text value of the Window-Wall-Type XML element is incorrect (current value is "common wall 1 Only include for RR Type 2.")). There is no "common wall 1 Only include for RR Type 2." in the [0] Building-Part XML element.
#         '0136-6922-9500-0471-8202.json',  # RdSAPInputFileError: The text value of the Wall-Thickness XML element is incorrect ("0"). The value should be a number greater than 0.
#         '0141-3058-4202-8256-7204.json',  # RdSAPInputFileError: The text value of the Wall-Thickness XML element is incorrect ("0"). The value should be a number greater than 0.
#         '0143-3058-3202-5106-8204.json',  # RdSAPInputFileError: The text value of the Wall-Thickness XML element is incorrect ("0"). The value should be a number greater than 0.
#         '0148-3058-3202-4266-7200.json',  # RdSAPInputFileError: The text value of the Window-Wall-Type XML element is incorrect (current value is "common wall 1 Only include for RR Type 2.")). There is no "common wall 1 Only include for RR Type 2." in the [0] Building-Part XML element. 
#         # ... now dealt with below for window-wall-type
#         ]:
#         continue


