
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

    if i < 26014: continue

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
            with open('sap.json', 'w') as f: json.dump(j, f, indent = 4)
            print(i, fn)
            raise err
        
    with open(os.path.join('output_data', 'sap_xml', fn.replace('.json', '.xml')), 'w') as f: f.write(etree.tostring(sap_report, pretty_print=True).decode())
    with open('sap__display.xml', 'w') as f: f.write(sap_report.display())

    # ignore cases
    flag = False
    # no data
    if len(sap_report.sap10_data.sap_property_details) == 0:
        continue
    # - heat pumps or community heating
    for main_heating in sap_report.sap10_data.sap_property_details.sap_heating.main_heating_details:
        if main_heating.main_heating_category.code in ['4', '5', '6', '7', '9']:
            flag = True
        if main_heating.heat_pump_heat_distribution is not None:
            flag = True
    if flag: continue
    
    # energy_rating
    response_sap = sap10calcs.calculate(
        input_lxml = sap_report,
        calculation_method='Energy rating',
        auth_token = None,
        url = url_sap
    )
    if response_sap['sap_calculation_success'] == False:
        if (
            response_sap['sap_calculation_error_message'].startswith('The text value of a Storey-Height XML element is incorrect ("0.0").')
            or response_sap['sap_calculation_error_message'].startswith('PV diverter calculations still to be implemented. Please request this.')
            or response_sap['sap_calculation_error_message'].startswith('G6, 7b, p66, FGHRS, storage combi boiler')
            or response_sap['sap_calculation_error_message'].startswith('Table D1')
            or response_sap['sap_calculation_error_message'].startswith('A SAP-Opening-Type XML element with the name')
            or response_sap['sap_calculation_error_message'].startswith('The Hot-Water-Storage-Size XML element is missing.')
            or response_sap['sap_calculation_error_message'].startswith('The Efficiency XML element is missing. This is the child element of the Secondary-Heating-Declared-Values XML element.')
            or response_sap['sap_calculation_error_message'].startswith('The value of the Has-Hot-Water-Cylinder XML element is incorrect')
            or response_sap['sap_calculation_error_message'].startswith('table_12a_high_rate_fraction')
            or response_sap['sap_calculation_error_message'].startswith('The Hot-Water-Store-Insulation-Thickness XML element is missing.')
            or response_sap['sap_calculation_error_message'].startswith('The value of the FGHRS-Index-Number XML element')
            or response_sap['sap_calculation_error_message'].startswith('The text value of a U_Value XML element is incorrect ("0.0").')
            or response_sap['sap_calculation_error_message'].startswith('The Water-Fuel-Type XML element is missing.')
            or response_sap['sap_calculation_error_message'].startswith('SAP cooling is still to be implemented in the API.')
            or response_sap['sap_calculation_error_message'].startswith('A Is-Central-Heating-Pump-In-Heated-Space XML element is missing.')
            or response_sap['sap_calculation_error_message'].startswith('A Heat-Emitter-Type XML element is missing.')
            or response_sap['sap_calculation_error_message'].startswith('has_thermal_store_or_CPSU_separate_timer_for_heating_the_store')
            or response_sap['sap_calculation_error_message'].startswith('type_of_water_storage')
            or response_sap['sap_calculation_error_message'].startswith('Proportion of solar heating to water heating')
            or response_sap['sap_calculation_error_message'].startswith('space_heating_main_system_2_other_fuel_price')
            or response_sap['sap_calculation_error_message'].startswith('The Ground-Floor-Type XML element is missing.')
            or response_sap['sap_calculation_error_message'].startswith('table_6b')
            or response_sap['sap_calculation_error_message'].startswith('get_water_heating_fuel_category')
            or response_sap['sap_calculation_error_message'].startswith('get_responsiveness')
            or response_sap['sap_calculation_error_message'].startswith('G5, 7a, p66, FGHRS, combi boiler, keep hot facility')
            or response_sap['sap_calculation_error_message'].startswith('A Main-Fuel-Type XML element is missing.')
            or response_sap['sap_calculation_error_message'].startswith('get_table_9_Th2__NA')
            or response_sap['sap_calculation_error_message'].startswith('table_371 referred to with control_index_number')
            or response_sap['sap_calculation_error_message'].startswith('The value of a Main-Fuel-Type XML element')  # ...does not match the fuel used by the specified heating system.
            or response_sap['sap_calculation_error_message'].startswith('is_storage_and_direct_acting_system')
            or response_sap['sap_calculation_error_message'].startswith('The value of the Has-Hot-Water-Cylinder XML element should be True')
            or response_sap['sap_calculation_error_message'].startswith('value_241a - Space heating - main system 2 (electric off-peak tariff), High-rate fraction')
            or fn == '0300-3346-7180-2225-7015.json'
            or fn == '0310-3650-5030-2274-8845.json'
            or fn == '0320-3597-1050-2625-5901.json'
            or fn == '0330-3563-6090-2125-8961.json'
            ):
            print((i, fn, response_sap['sap_calculation_error_message']))
            logging.error(f'{i}, {fn}, {response_sap['sap_calculation_error_message']}')
            continue
        with open('sap.json', 'w') as f: json.dump(j, f, indent = 4)
        with open('sap.xml', 'w') as f: f.write(etree.tostring(sap_report, pretty_print=True).decode())
        with open('sap__display.xml', 'w') as f: f.write(sap_report.display())
        with open('sap_response.json', 'w') as f: json.dump(response_sap, f, indent = 4)
        raise Exception(response_sap['sap_calculation_error_traceback'])
    with open(os.path.join('output_data', 'energy_rating', fn), 'w') as f: json.dump(response_sap, f, indent = 4)

    # epc
    response_sap = sap10calcs.calculate(
        input_lxml = sap_report,
        calculation_method='EPC costs, emissions and primary energy',
        auth_token = None,
        url = url_sap,
        year = sap_report.report_header.completion_date.value.year,
        month = sap_report.report_header.completion_date.value.month,
        day = sap_report.report_header.completion_date.value.day,
    )
    if response_sap['sap_calculation_success'] == False:
        if (
            'the Postcode XML element is not valid' in response_sap['sap_calculation_error_message']
        ):
            print((i, fn, response_sap['sap_calculation_error_message']))
            logging.error(f'{i}, {fn}, {response_sap['sap_calculation_error_message']}')
            continue
        with open('sap.json', 'w') as f: json.dump(j, f, indent = 4)
        with open('sap.xml', 'w') as f: f.write(etree.tostring(sap_report, pretty_print=True).decode())
        with open('sap__display.xml', 'w') as f: f.write(sap_report.display())
        with open('sap_response.json', 'w') as f: json.dump(response_sap, f, indent = 4)
        raise Exception(response_sap['sap_calculation_error_traceback'])
    with open(os.path.join('output_data', 'epc', fn), 'w') as f: json.dump(response_sap, f, indent = 4)
    

    #fn_out = os.path.join('output_data', 'rdsap_xml_display', fn.replace('.json', '__display.xml'))
    #with open(fn_out, 'w') as f: f.write(root.display())

    #print(etree.tostring(root, pretty_print=True).decode())

    



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


