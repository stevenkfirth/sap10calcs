


# cd "C:\Users\cvskf\OneDrive - Loughborough University\_Git\stevenkfirth\sap10calcs\tests\sap\api_data"
# python -m validate

import sap10calcs
import os
from lxml import etree
import csv
import json


with open('validate.csv', 'w', newline = '') as f:
    csvwriter = csv.writer(f)

    csvwriter.writerow([
            'certificate_number',
            'energy_rating_scheme',
            'energy_rating_er',
            'DER_scheme',
            'DER_er',
            'PDER_scheme',
            'PDER_er',
            'Environmental_impact_scheme',
            #'Environmental_impact_er',
            'Environmental_impact_epc',
            'Energy_consumption_scheme',
            #'Energy_consumption_er',
            'Energy_consumption_epc',
            'CO2_emissions_scheme',
            #'CO2_emissions_er',
            'CO2_emissions_epc',
            'CO2_emissions_per_floor_area_scheme',
            #'CO2_emissions_per_floor_area_er',
            'CO2_emissions_per_floor_area_epc',
            'lighting_cost_scheme',
            #'lighting_cost_er',
            'lighting_cost_epc',
            'heating_cost_scheme',
            #'heating_cost_er',
            'heating_cost_epc',
            'hot_water_cost_scheme',
            #'hot_water_cost_er',
            'hot_water_cost_epc',

            
        ])

    for fn in os.listdir(os.path.join('output_data', 'energy_rating')):
        print(fn)

        if not os.path.isfile(os.path.join('output_data', 'epc', fn)):
            continue

        tree, sap_report = sap10calcs.parse_xml(os.path.join('output_data', 'sap_xml', fn.replace('.json', '.xml')))
        
        with open(os.path.join('output_data', 'energy_rating', fn)) as f1:
            j_er = json.load(f1)

        with open(os.path.join('output_data', 'epc', fn)) as f1:
            j_epc = json.load(f1)
        


        csvwriter.writerow([
            fn.replace('.json', ''),
            sap_report.energy_assessment.energy_use.energy_rating_current.value,
            j_er['sap_calculation_output_dict']['value_258'],
            f'{sap_report.energy_assessment.energy_use.der.value:.2f}' if sap_report.energy_assessment.energy_use.der is not None else 'NA',
            f'{j_er['sap_calculation_output_dict']['value_273']:.2f}',
            f'{sap_report.energy_assessment.energy_use.dper.value:.2f}' if sap_report.energy_assessment.energy_use.dper is not None else 'NA',
            f'{j_er['sap_calculation_output_dict']['value_287']:.2f}',
            f'{sap_report.energy_assessment.energy_use.environmental_impact_current.value:.2f}',
            #'{j_er['sap_calculation_output_dict']['value_274']:.2f}',
            f'{j_epc['sap_calculation_output_dict']['value_274']:.2f}',
            f'{sap_report.energy_assessment.energy_use.energy_consumption_current.value:.2f}',
            #f'{j_er['sap_calculation_output_dict']['value_287']:.2f}',
            f'{j_epc['sap_calculation_output_dict']['value_287']:.2f}',
            f'{sap_report.energy_assessment.energy_use.co2_emissions_current.value:.2f}',
            #f'{j_er['sap_calculation_output_dict']['value_272']/1000:.2f}',
            f'{j_epc['sap_calculation_output_dict']['value_272']/1000:.2f}',
            f'{sap_report.energy_assessment.energy_use.co2_emissions_current_per_floor_area.value:.2f}',
            #f'{j_er['sap_calculation_output_dict']['value_273']:.2f}',
            f'{j_epc['sap_calculation_output_dict']['value_273']:.2f}',
            f'{sap_report.energy_assessment.energy_use.lighting_cost_current.value:.2f}',
            #f'{j_er['sap_calculation_output_dict']['value_250']:.2f}',
            f'{j_epc['sap_calculation_output_dict']['value_250']:.2f}',
            f'{sap_report.energy_assessment.energy_use.heating_cost_current.value:.2f}',
            #f'{j_er['sap_calculation_output_dict']['value_240']+j_er['sap_calculation_output_dict']['value_241']+j_er['sap_calculation_output_dict']['value_242']+j_er['sap_calculation_output_dict']['value_249']+j_er['sap_calculation_output_dict']['value_251']:.2f}',
            f'{j_epc['sap_calculation_output_dict']['value_240']+j_epc['sap_calculation_output_dict']['value_241']+j_epc['sap_calculation_output_dict']['value_242']+j_epc['sap_calculation_output_dict']['value_249']+j_epc['sap_calculation_output_dict']['value_251']:.2f}',
            f'{sap_report.energy_assessment.energy_use.hot_water_cost_current.value:.2f}',
            #f'{(j_er['sap_calculation_output_dict']['value_245'] or 0) + (j_er['sap_calculation_output_dict']['value_246'] or 0) + (j_er['sap_calculation_output_dict']['value_247'] or 0) + (j_er['sap_calculation_output_dict']['value_247a'] or 0):.2f}',
            f'{(j_epc['sap_calculation_output_dict']['value_245'] or 0) + (j_epc['sap_calculation_output_dict']['value_246'] or 0) + (j_epc['sap_calculation_output_dict']['value_247'] or 0) + (j_epc['sap_calculation_output_dict']['value_247a'] or 0):.2f}',
            
        ])


        #break
                         
