import sap10calcs
import os
import json

#%% 1 - Base case with PV
folder = "1"
if not os.path.isdir(folder): os.makedirs(folder)

# create new sap_report element
tree, sap_report = sap10calcs.create_sap_report_xml()

# postcode
report_header = sap_report.add_report_header()
property_ = report_header.add_property_()
address = property_.add_address()
postcode = address.add_postcode().value = 'LE11 3TU'

# sap10_data
sap10_data = sap_report.add_sap10_data()
sap10_data.add_data_type().value = 'new dwelling as designed'

# sap_property_details
sap_property_details = sap10_data.add_sap_property_details()
sap_property_details.add_cold_water_source().value = 'mains'
sap_property_details.add_living_area().value = 30
sap_property_details.add_windows_overshading().value = 'average or unknown'
sap_property_details.add_is_dwelling_export_capable().value = True
sap_property_details.add_pv_connection().value = "connected to dwelling's electricity meter"

# sap_building_parts
sap_building_parts = sap_property_details.add_sap_building_parts()

# sap_building_part_1
sap_building_part_1 = sap_building_parts.add_sap_building_part()
sap_building_part_1.add_building_part_number().value = 1

# sap_floor_dimensions_1
sap_floor_dimensions_1 = sap_building_part_1.add_sap_floor_dimensions()

# sap_floor_dimension_1_1
sap_floor_dimension_1_1 = sap_floor_dimensions_1.add_sap_floor_dimension()
sap_floor_dimension_1_1.add_floor_type().value = 'ground floor'
sap_floor_dimension_1_1.add_storey().value = 'Ground'
sap_floor_dimension_1_1.add_total_floor_area().value = 100
sap_floor_dimension_1_1.add_storey_height().value = 3
sap_floor_dimension_1_1.add_heat_loss_area().value = 100
sap_floor_dimension_1_1.add_u_value().value = 0.5

# sap_walls_1
sap_walls_1 = sap_building_part_1.add_sap_walls()

# sap_wall_1_1
sap_wall_1_1 = sap_walls_1.add_sap_wall()
sap_wall_1_1.add_wall_type().value = 'exposed wall'
sap_wall_1_1.add_total_wall_area().value = 120
sap_wall_1_1.add_u_value().value = 0.5
sap_wall_1_1.add_name().value = 'sap_wall_1_1'

# sap_roofs_1
sap_roofs_1 = sap_building_part_1.add_sap_roofs()

# sap_roof_1_1
sap_roof_1_1 = sap_roofs_1.add_sap_roof()
sap_roof_1_1.add_total_roof_area().value = 100
sap_roof_1_1.add_u_value().value = 0.5
sap_roof_1_1.add_roof_type().value = 'exposed roof'
sap_roof_1_1.add_name().value = 'sap_roof_1_1'

# sap_openings_1
sap_openings_1 = sap_building_part_1.add_sap_openings()

# sap_opening_1_1
sap_opening_1_1 = sap_openings_1.add_sap_opening()
sap_opening_1_1.add_type().value = 'sap_opening_type_1'
sap_opening_1_1.add_height().value = 1.5
sap_opening_1_1.add_width().value = 5
sap_opening_1_1.add_location().value = 'sap_wall_1_1'
sap_opening_1_1.add_orientation().value = 'South'

# sap_opening_types
sap_opening_types = sap_property_details.add_sap_opening_types()

# sap_opening_type_1
sap_opening_type_1 = sap_opening_types.add_sap_opening_type()
sap_opening_type_1.add_name().value = 'sap_opening_type_1'
sap_opening_type_1.add_type().value = 'window'
sap_opening_type_1.add_data_source().value = 'manufacturer declaration'
sap_opening_type_1.add_u_value().value = 1.5
sap_opening_type_1.add_glazing_type().value = 'double'

# sap_thermal_bridges
sap_thermal_bridges_1 = sap_building_part_1.add_sap_thermal_bridges()
sap_thermal_bridges_1.add_thermal_bridge_code().value = 'default'

# sap_heating
sap_heating = sap_property_details.add_sap_heating()
sap_heating.add_has_hot_water_cylinder().value = False
sap_heating.add_thermal_store().value = 'none'
sap_heating.add_secondary_heating_category().value = 'none'
sap_heating.add_water_heating_code().value = 901  # From main heating system

# main_heating_details
main_heating_details = sap_heating.add_main_heating_details()

# main_heating_1
main_heating_1 = main_heating_details.add_main_heating()
main_heating_1.add_main_heating_number().value = 1
main_heating_1.add_main_fuel_type().value = 'Gas: mains gas'
main_heating_1.add_main_heating_category().value = 'boiler with radiators or underfloor heating'
main_heating_1.add_main_heating_data_source().value = 'from SAP table'
main_heating_1.add_main_heating_code().value = 104
    # "Gas boilers (including mains gas, LPG and biogas) 1998 or later: Condensing combi with automatic ignition"
main_heating_1.add_is_central_heating_pump_in_heated_space().value = True
main_heating_1.add_main_heating_fraction().value = 1
main_heating_1.add_heat_emitter_type().value = 'radiators'
main_heating_1.add_main_heating_control().value = 2106  # "Programmer, room thermostat and TRVs"
main_heating_1.add_has_separate_delayed_start().value = False
main_heating_1.add_is_interlocked_system().value = False

# ventilation
sap_ventilation = sap_property_details.add_sap_ventilation()
sap_ventilation.add_open_chimneys_count().value = 0
sap_ventilation.add_open_flues_count().value = 0
sap_ventilation.add_closed_flues_count().value = 0
sap_ventilation.add_boilers_flues_count().value = 0
sap_ventilation.add_other_flues_count().value = 0
sap_ventilation.add_blocked_chimneys_count().value = 0
sap_ventilation.add_extract_fans_count().value = 0
sap_ventilation.add_psv_count().value = 0
sap_ventilation.add_flueless_gas_fires_count().value = 0
sap_ventilation.add_pressure_test().value = 'yes (new dwelling, design value)'
sap_ventilation.add_air_permeability().value = 3.5
sap_ventilation.add_sheltered_sides_count().value = 2
sap_ventilation.add_ventilation_type().value = 'natural with intermittent extract fans'

# SAP-Energy-Source
sap_energy_source = sap_property_details.add_sap_energy_source()
sap_energy_source.add_electricity_tariff().value = 'standard tariff'

# PV-Arrays
pv_arrays = sap_energy_source.add_pv_arrays()

# PV-Array
pv_array = pv_arrays.add_pv_array()
pv_array.add_peak_power().value = 2.5
pv_array.add_orientation().value = 'South'
pv_array.add_pitch().value = '30 degrees'
pv_array.add_overshading().value = 'modest'


tree.write(os.path.join(folder, 'in.xml'), encoding="utf-8", xml_declaration=True, pretty_print=True)

extra = {}
with open(os.path.join(folder, 'extra.json'), 'w') as f:
    json.dump(extra, f, indent = 4)


#%% 2 - Base case, double area
folder = "2"
if not os.path.isdir(folder): os.makedirs(folder)
pv_array.peak_power.value = 5
tree.write(os.path.join(folder, 'in.xml'), encoding="utf-8", xml_declaration=True, pretty_print=True)
extra = {}
with open(os.path.join(folder, 'extra.json'), 'w') as f:
    json.dump(extra, f, indent = 4)
