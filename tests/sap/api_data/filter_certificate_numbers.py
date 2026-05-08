
# cd "C:\Users\cvskf\OneDrive - Loughborough University\_Git\stevenkfirth\sap10calcs\tests\sap\api_data"
# python -m filter_certificate_numbers


import sap10calcs
import os
from lxml import etree
import json

result = {}

for i, fn in enumerate(os.listdir(os.path.join('output_data', 'sap_xml'))):

    if i < 0: continue

    if i%100 == 0: print(i, end = ' ', flush = True)

    cn = fn.replace('.json', '')
    tree, sap_report = sap10calcs.parse_xml(os.path.join('output_data', 'sap_xml', fn))

    try:
        property_type = sap_report.sap10_data.sap_property_details.property_type.value
    except AttributeError:
        property_type = None

    

    result.setdefault(property_type, {})
    

    #break

with open(os.path.join('output_data', 'certificate_numbers', 'cn.json'), 'w') as f:
    json.dump(result, f, indent = 4)
