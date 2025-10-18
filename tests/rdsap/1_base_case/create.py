import sap10calcs
import os
import json

#%% 1 - detached
folder = "1_detached"
if not os.path.isdir(folder): os.makedirs(folder)

# create new rdsap_report element
tree, rdsap_report = sap10calcs.create_rdsap_report_xml() 

# report_header
report_header = rdsap_report.add_report_header()
report_header.add_country_code().value = 'England'

# sap_data
sap_data = rdsap_report.add_sap_data()

# sap_property_details
sap_property_details = sap_data.add_sap_property_details()
sap_property_details.add_property_type().value = 'House'
sap_property_details.add_built_form().value = 'Detached'
sap_property_details.add_extensions_count().value = 0
sap_property_details.add_habitable_room_count().value = 1
sap_property_details.add_heated_room_count().value = 1
sap_property_details.add_low_energy_fixed_lighting_bulbs_count().value = 0
sap_property_details.add_incandescent_fixed_lighting_bulbs_count().value = 0
sap_property_details.add_measurement_type().value = 'Internal'
sap_property_details.add_solar_water_heating().value = 'No'
sap_property_details.add_pressure_test().value = 'yes - measured at 50 Pa'
sap_property_details.add_air_permeability().value = 0
sap_property_details.add_mechanical_ventilation().value = 'natural'
sap_property_details.add_conservatory_type().value = 'no conservatory'
sap_property_details.add_door_count().value = 0
sap_property_details.add_percent_draughtproofed().value = 0

# sap_heating
sap_heating = sap_property_details.add_sap_heating()
sap_heating.add_water_heating_fuel().value = 'electricity (not community)'
sap_heating.add_water_heating_code().value = 909  # Electric instantaneous at point of use
sap_heating.add_immersion_heating_type().value = 'not applicable'
sap_heating.add_cylinder_size().value = 'No Cylinder'
sap_heating.add_has_fixed_air_conditioning().value = False

# main_heating_details
main_heating_details = sap_heating.add_main_heating_details()

# main_heating_1
main_heating_1 = main_heating_details.add_main_heating()
main_heating_1.add_main_heating_number().value = 1
main_heating_1.add_main_heating_category().value = 'room heaters'
main_heating_1.add_main_fuel_type().value = 'electricity (not community)'
main_heating_1.add_main_heating_control().value = 2699  # None
main_heating_1.add_main_heating_data_source().value = 'SAP Table'
main_heating_1.add_sap_main_heating_code().value = 691  
    # Panel, convector or radiant heaters
main_heating_1.add_boiler_flue_type().value = 'room-sealed'
main_heating_1.add_heat_emitter_type().value = 'radiators'
main_heating_1.add_main_heating_fraction().value = 1
main_heating_1.add_has_fghrs().value = 'No'

# sap_energy_source
sap_energy_source = sap_property_details.add_sap_energy_source()
sap_energy_source.add_meter_type().value = 'Single'
sap_energy_source.add_mains_gas().value = 'mains gas available in the property'
sap_energy_source.add_electricity_smart_meter_present().value = False
sap_energy_source.add_gas_smart_meter_present().value = False
sap_energy_source.add_is_dwelling_export_capable().value = False
sap_energy_source.add_wind_turbines_count().value = 0
sap_energy_source.add_wind_turbines_terrain_type().value = 'not recorded'
sap_energy_source.add_pv_connection().value = 'not applicable (FGHRS or no PV)'

# photovoltaic_supply
photovoltaic_supply = sap_energy_source.add_photovoltaic_supply()
photovoltaic_supply.add_none_or_no_details().add_percent_roof_area().value = 0

# sap_building_parts
sap_building_parts = sap_property_details.add_sap_building_parts()

# sap_building_part_1
sap_building_part_1 = sap_building_parts.add_sap_building_part()
sap_building_part_1.add_building_part_number().value = 1
sap_building_part_1.add_construction_age_band().value = \
    'England and Wales: 1991-1995; Scotland: 1992-1998; Northern Ireland: 1992-1999'
sap_building_part_1.add_floor_u_value().value = 1.0
sap_building_part_1.add_floor_heat_loss().value = 'Ground floor'
sap_building_part_1.add_roof_construction().value = 'Pitched (slates or tiles), access to loft'
sap_building_part_1.add_roof_u_value().value = 1.0
sap_building_part_1.add_roof_insulation_location().value = 'Joists'
sap_building_part_1.add_wall_construction().value = 'cavity'
sap_building_part_1.add_wall_dry_lined().value = 'No'
sap_building_part_1.add_wall_u_value().value = 1.0
sap_building_part_1.add_wall_insulation_type().value = 'filled cavity'
sap_building_part_1.add_wall_thickness_measured().value = 'No'
sap_building_part_1.add_party_wall_construction().value = \
    'not applicable (detached property or no party wall in this building part)'

# sap_floor_dimensions_1
sap_floor_dimensions_1 = sap_building_part_1.add_sap_floor_dimensions()

# sap_floor_dimension_1_1
sap_floor_dimension_1_1 = sap_floor_dimensions_1.add_sap_floor_dimension()
sap_floor_dimension_1_1.add_heat_loss_perimeter().value = 40
sap_floor_dimension_1_1.add_room_height().value = 3
sap_floor_dimension_1_1.add_total_floor_area().value = 100
sap_floor_dimension_1_1.add_floor().value = 'lowest occupied'
sap_floor_dimension_1_1.add_floor_construction().value = 'suspended timber'
sap_floor_dimension_1_1.add_floor_insulation().value = 'as built'
sap_floor_dimension_1_1.add_party_wall_length().value = 0

tree.write(os.path.join(folder, 'in.xml'), encoding="utf-8", xml_declaration=True, pretty_print=True)

extra = {}
with open(os.path.join(folder, 'extra.json'), 'w') as f:
    json.dump(extra, f, indent = 4)


