# 2 - Base case with room in roof type 1

import sap10calcs
import os
import json

# 1 - Base
id_ = '1_base'
if not os.path.isdir(id_): os.makedirs(id_)

dir_in = '../1_base_case/1_detached'
tree, rdsap_report = sap10calcs.parse_rdsap_xml(os.path.join(dir_in, 'in.xml'))

sap_building_part = rdsap_report.sap_data.sap_property_details.sap_building_parts.sap_building_part[0]
sap_room_in_roof = sap_building_part.add_sap_room_in_roof()
sap_room_in_roof.add_floor_area().value = 80
sap_room_in_roof.add_construction_age_band().value = 'England and Wales: 1991-1995; Scotland: 1992-1998; Northern Ireland: 1992-1999'
room_in_roof_type_1 = sap_room_in_roof.add_room_in_roof_type_1()
room_in_roof_type_1.add_gable_wall_length_1().value = 8
room_in_roof_type_1.add_gable_wall_type_1().value = 'exposed'
room_in_roof_type_1.add_gable_wall_length_2().value = 8
room_in_roof_type_1.add_gable_wall_type_2().value = 'exposed'


tree.write(os.path.join(id_, 'in.xml'), encoding="utf-8", xml_declaration=True, pretty_print=True)

extra = {}
with open(os.path.join(id_, 'extra.json'), 'w') as f: json.dump(extra, f, indent = 4)




