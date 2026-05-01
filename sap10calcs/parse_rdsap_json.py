


from lxml import etree
import json
from .instances import RdSAP_Schema_21_0_1_parser
from io import StringIO, BytesIO
import copy


def parse_rdsap_json(
    input_file,
    input_json = None
):
    """ Parses a RdSAP json file and returns an RdSAP XML file.

    input file  - filepath to json file (downloaded from get_energy_data API)
    
    :returns: A two-item tuple containing an `lxml ElementTree <https://lxml.de/tutorial.html>`__ and the root node of the XML file (a `RdSAP-Report <https://stevenkfirth.github.io/sap10calcs/rdsap_schema_21_0_0.html#rdsap-report>`__ element).
    :rtype: (`lxml.etree.ElementTree <https://lxml.de/tutorial.html#the-elementtree-class>`__, :py:class:`sap10calcs.classes_RdSAP_Schema_21_0_0.RdSAP_Report`)

    
    """

    # load json
    if not input_json is None:
        j0 = input_json
    with open(input_file) as f:
        j0 = json.load(f)
    j = copy.deepcopy(j0)

    if not 'data' in j:
        raise Exception('No "data" key in root json.')
    if not j['data'].get('schema_type') == 'RdSAP-Schema-21.0.1':
        raise Exception(f'RdSAP schema not equal to "RdSAP-Schema-21.0.1" ({j['data'].get('schema_type')})')

    # normalise json
    # - lists
    if 'data' in j:
        if 'roofs' in j['data'] and not isinstance(j['data']['roofs'], list): j['data']['roofs'] = [j['data']['roofs']]
        if 'walls' in j['data'] and not isinstance(j['data']['walls'], list): j['data']['walls'] = [j['data']['walls']]
        if 'floors' in j['data'] and not isinstance(j['data']['floors'], list): j['data']['floors'] = [j['data']['floors']]
        if 'main_heating' in j['data'] and not isinstance(j['data']['main_heating'], list): j['data']['main_heating'] = [j['data']['main_heating']]
        if 'addendum' in j['data'] and 'addendum_numbers' in j['data']['addendum'] and not isinstance(j['data']['addendum']['addendum_numbers'], list): 
            j['data']['addendum']['addendum_numbers'] = [j['data']['addendum']['addendum_numbers']]
        if 'sap_heating' in j['data'] and 'shower_outlets' in j['data']['sap_heating'] and not isinstance(j['data']['sap_heating']['shower_outlets'], list): 
            j['data']['sap_heating']['shower_outlets'] = [j['data']['sap_heating']['shower_outlets']]
        if 'sap_heating' in j['data'] and 'main_heating_details' in j['data']['sap_heating'] and not isinstance(j['data']['sap_heating']['main_heating_details'], list): 
            j['data']['sap_heating']['main_heating_details'] = [j['data']['sap_heating']['main_heating_details']]
        if 'sap_windows' in j['data'] and not isinstance(j['data']['sap_windows'], list): j['data']['sap_windows'] = [j['data']['sap_windows']]
        if 'lzc_energy_sources' in j['data'] and not isinstance(j['data']['lzc_energy_sources'], list): j['data']['lzc_energy_sources'] = [j['data']['lzc_energy_sources']]
        if 'sap_building_parts' in j['data'] and not isinstance(j['data']['sap_building_parts'], list): j['data']['sap_building_parts'] = [j['data']['sap_building_parts']]
        if 'suggested_improvements' in j['data'] and not isinstance(j['data']['suggested_improvements'], list): j['data']['suggested_improvements'] = [j['data']['suggested_improvements']]
        if 'alternative_improvements' in j['data'] and not isinstance(j['data']['alternative_improvements'], list): j['data']['alternative_improvements'] = [j['data']['alternative_improvements']]
        if 'sap_energy_source' in j['data'] and 'pv_batteries' in j['data']['sap_energy_source'] and not isinstance(j['data']['sap_energy_source']['pv_batteries'], list):
            j['data']['sap_energy_source']['pv_batteries'] = [j['data']['sap_energy_source']['pv_batteries']]

    # - removing unneeded keys
        if 'sap_heating' in j['data'] and 'shower_outlets' in j['data']['sap_heating']:
            for shower_outlet_index in range(len(j['data']['sap_heating']['shower_outlets'])):
                if 'shower_outlet' in j['data']['sap_heating']['shower_outlets'][shower_outlet_index]:
                    j['data']['sap_heating']['shower_outlets'][shower_outlet_index] = j['data']['sap_heating']['shower_outlets'][shower_outlet_index].pop('shower_outlet')
        if 'alternative_improvements' in j['data']:
            for alternative_improvement_index in range(len(j['data']['alternative_improvements'])):
                if 'improvement' in j['data']['alternative_improvements'][alternative_improvement_index]:
                    j['data']['alternative_improvements'][alternative_improvement_index] = j['data']['alternative_improvements'][alternative_improvement_index].pop('improvement')
    # - values
        if 'sap_windows' in j['data']:
            for sap_window_index in range(len(j['data']['sap_windows'])):
                if 'window_height' in j['data']['sap_windows'][sap_window_index] and isinstance(j['data']['sap_windows'][sap_window_index]['window_height'], dict):
                    j['data']['sap_windows'][sap_window_index]['window_height'] = j['data']['sap_windows'][sap_window_index]['window_height']['value']
                if 'window_width' in j['data']['sap_windows'][sap_window_index] and isinstance(j['data']['sap_windows'][sap_window_index]['window_width'], dict):
                    j['data']['sap_windows'][sap_window_index]['window_width'] = j['data']['sap_windows'][sap_window_index]['window_width']['value']
        if 'sap_building_parts' in j['data']:
            for sap_building_part_index in range(len(j['data']['sap_building_parts'])):
                if ('floor_area' in j['data']['sap_building_parts'][sap_building_part_index] 
                    and isinstance(j['data']['sap_building_parts'][sap_building_part_index]['floor_area'], dict)):
                    j['data']['sap_building_parts'][sap_building_part_index]['floor_area'] = \
                        j['data']['sap_building_parts'][sap_building_part_index]['floor_area']['value']
                if ('glazed_perimeter' in j['data']['sap_building_parts'][sap_building_part_index] 
                    and isinstance(j['data']['sap_building_parts'][sap_building_part_index]['glazed_perimeter'], dict)):
                    j['data']['sap_building_parts'][sap_building_part_index]['glazed_perimeter'] = \
                        j['data']['sap_building_parts'][sap_building_part_index]['glazed_perimeter']['value']  
                if 'sap_room_in_roof' in j['data']['sap_building_parts'][sap_building_part_index]: 
                    if 'floor_area' in j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']:
                        if isinstance(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['floor_area'], dict):
                            j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['floor_area'] = j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['floor_area']['value']
                if 'sap_floor_dimensions' in j['data']['sap_building_parts'][sap_building_part_index]:
                    for sap_floor_dimension_index in range(len(j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'])):
                        if ('heat_loss_perimeter' in j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index] 
                            and isinstance(j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index]['heat_loss_perimeter'], dict)):
                            j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index]['heat_loss_perimeter'] = \
                                j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index]['heat_loss_perimeter']['value']
                        if ('room_height' in j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index] 
                            and isinstance(j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index]['room_height'], dict)):
                            j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index]['room_height'] = \
                                j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index]['room_height']['value']
                        if ('total_floor_area' in j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index] 
                            and isinstance(j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index]['total_floor_area'], dict)):
                            j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index]['total_floor_area'] = \
                                j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index]['total_floor_area']['value']
                        if ('party_wall_length' in j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index] 
                            and isinstance(j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index]['party_wall_length'], dict)):
                            j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index]['party_wall_length'] = \
                                j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index]['party_wall_length']['value']
        if 'heating_cost_current' in j['data'] and isinstance(j['data']['heating_cost_current'], dict): j['data']['heating_cost_current'] = j['data']['heating_cost_current']['value']
        if 'heating_cost_potential' in j['data'] and isinstance(j['data']['heating_cost_potential'], dict): j['data']['heating_cost_potential'] = j['data']['heating_cost_potential']['value']
        if 'lighting_cost_current' in j['data'] and isinstance(j['data']['lighting_cost_current'], dict): j['data']['lighting_cost_current'] = j['data']['lighting_cost_current']['value']
        if 'lighting_cost_potential' in j['data'] and isinstance(j['data']['lighting_cost_potential'], dict): j['data']['lighting_cost_potential'] = j['data']['lighting_cost_potential']['value']
        if 'hot_water_cost_current' in j['data'] and isinstance(j['data']['hot_water_cost_current'], dict): j['data']['hot_water_cost_current'] = j['data']['hot_water_cost_current']['value']
        if 'hot_water_cost_potential' in j['data'] and isinstance(j['data']['hot_water_cost_potential'], dict): j['data']['hot_water_cost_potential'] = j['data']['hot_water_cost_potential']['value']
        if 'sap_flat_details' in j['data'] and 'unheated_corridor_length' in j['data']['sap_flat_details']:
            if isinstance(j['data']['sap_flat_details']['unheated_corridor_length'], dict): 
                j['data']['sap_flat_details']['unheated_corridor_length'] = j['data']['sap_flat_details']['unheated_corridor_length']['value']

    # - other
        if 'sap_energy_source' in j['data'] and 'photovoltaic_supply' in j['data']['sap_energy_source'] and isinstance(j['data']['sap_energy_source']['photovoltaic_supply'], list):
            j['data']['sap_energy_source']['photovoltaic_supply'] = {'pv_arrays': j['data']['sap_energy_source']['photovoltaic_supply']}
        if 'sap_energy_source' in j['data'] and 'photovoltaic_supply' in j['data']['sap_energy_source'] and 'pv_arrays' in j['data']['sap_energy_source']['photovoltaic_supply']:
            for pv_array_index in range(len(j['data']['sap_energy_source']['photovoltaic_supply']['pv_arrays'])):
                if isinstance(j['data']['sap_energy_source']['photovoltaic_supply']['pv_arrays'][pv_array_index], list):
                    if len(j['data']['sap_energy_source']['photovoltaic_supply']['pv_arrays'][pv_array_index]) == 1:
                        j['data']['sap_energy_source']['photovoltaic_supply']['pv_arrays'][pv_array_index] = j['data']['sap_energy_source']['photovoltaic_supply']['pv_arrays'][pv_array_index][0]
                    else:
                        raise Exception
                if 'peak_power' in j['data']['sap_energy_source']['photovoltaic_supply']['pv_arrays'][pv_array_index]:
                    if isinstance(j['data']['sap_energy_source']['photovoltaic_supply']['pv_arrays'][pv_array_index]['peak_power'], dict):
                        j['data']['sap_energy_source']['photovoltaic_supply']['pv_arrays'][pv_array_index]['peak_power'] = j['data']['sap_energy_source']['photovoltaic_supply']['pv_arrays'][pv_array_index]['peak_power']['value']
        if 'sap_energy_source' in j['data'] and 'pv_batteries' in j['data']['sap_energy_source']:
            for pv_battery_index in range(len(j['data']['sap_energy_source']['pv_batteries'])):
                if not 'pv_battery' in j['data']['sap_energy_source']['pv_batteries'][pv_battery_index]:
                    j['data']['sap_energy_source']['pv_batteries'][pv_battery_index] = {'pv_battery': j['data']['sap_energy_source']['pv_batteries'][pv_battery_index]}
        


    # remove JSON values that don't parse to the RdSAP XML (no equivalent XML elements available)
    if 'error' in j['data']: del j['data']['error']
    if 'created_at' in j['data']: del j['data']['created_at']
    if 'schema_type' in j['data']: del j['data']['schema_type']
    if 'uprn_source' in j['data']: del j['data']['uprn_source']
    if 'assessment_type' in j['data']: del j['data']['assessment_type']
    if 'current_energy_efficiency_band' in j['data']: del j['data']['current_energy_efficiency_band']
    if 'potential_energy_efficiency_band' in j['data']: del j['data']['potential_energy_efficiency_band']

    # create new rdsap xml
    xml = """
    <RdSAP-Report xmlns="https://epbr.digital.communities.gov.uk/xsd/rdsap">
        <Schema-Version-Original>RdSAP-Schema-21.0.0</Schema-Version-Original>
        <SAP-Version>10.2</SAP-Version>
    </RdSAP-Report>"""

    tree = etree.parse(
        StringIO(xml),
        parser = RdSAP_Schema_21_0_1_parser
        )
    
    # --- RdSAP-Report ---
    rdsap_report = tree.getroot() 

    # Calculation-Software-Version
    try: 
        rdsap_report.add_calculation_software_version().code = str(j['data'].pop('calculation_software_version'))
    except KeyError: pass

    # Schema-Version-Original
    try: 
        rdsap_report.add_schema_version_original().code = str(j['data'].pop('schema_version_original'))
    except KeyError: pass

    # Schema-Version-Current
    try: 
        rdsap_report.add_schema_version_current().code = str(j['data'].pop('schema_version_current'))
    except KeyError: pass

    # SAP-Version
    try: 
        rdsap_report.add_sap_version().code = str(j['data'].pop('sap_version'))
    except KeyError: pass

    


    if True:
        # --- Energy-Assessment ---
        energy_assessment = rdsap_report.add_energy_assessment()

        
        if True:
            # --- Property-Summary ---
            property_summary = energy_assessment.add_property_summary() 

            if True:
                # --- Wall ---
                if 'walls' in j['data']:
                    c = []
                    for wall_index in range(len(j['data']['walls'])):
                        # 
                        wall = property_summary.add_wall()
                        # description
                        try: 
                            wall.add_description().code = str(j['data']['walls'][wall_index].pop('description'))
                        except KeyError: pass
                        # energy_efficiency_rating
                        try: 
                            wall.add_energy_efficiency_rating().code = str(j['data']['walls'][wall_index].pop('energy_efficiency_rating'))
                        except KeyError: pass
                        # environmental_efficiency_rating
                        try: 
                            wall.add_environmental_efficiency_rating().code = str(j['data']['walls'][wall_index].pop('environmental_efficiency_rating'))
                        except KeyError: pass
                        #
                        if len(j['data']['walls'][wall_index]) == 0:
                            c.append(wall_index)
                        else:
                            print(etree.tostring(rdsap_report, pretty_print=True).decode())
                            raise Exception('j', 'data', 'walls', wall_index, list(j['data']['walls'][wall_index])[0])
                    for c1 in c[::-1]: del j['data']['walls'][c1]
                    if len(j['data']['walls']) == 0: del j['data']['walls']

            if True:
                # --- Roof ---
                if 'roofs' in j['data']:
                    c = []
                    for roof_index in range(len(j['data']['roofs'])):
                        # 
                        roof = property_summary.add_roof()
                        # description
                        try: 
                            roof.add_description().code = str(j['data']['roofs'][roof_index].pop('description'))
                        except KeyError: pass
                        # energy_efficiency_rating
                        try: 
                            roof.add_energy_efficiency_rating().code = str(j['data']['roofs'][roof_index].pop('energy_efficiency_rating'))
                        except KeyError: pass
                        # environmental_efficiency_rating
                        try: 
                            roof.add_environmental_efficiency_rating().code = str(j['data']['roofs'][roof_index].pop('environmental_efficiency_rating'))
                        except KeyError: pass
                        #
                        if len(j['data']['roofs'][roof_index]) == 0:
                            c.append(roof_index)
                        else:
                            print(etree.tostring(rdsap_report, pretty_print=True).decode())
                            raise Exception('j', 'data', 'roofs', roof_index, list(j['data']['roofs'][roof_index])[0])
                    for c1 in c[::-1]: del j['data']['roofs'][c1]
                    if len(j['data']['roofs']) == 0: del j['data']['roofs']

            if True:
            # --- Floor ---
                if 'floors' in j['data']:
                    c = []
                    for floor_index in range(len(j['data']['floors'])):
                        # 
                        floor = property_summary.add_floor()
                        # description
                        try: 
                            floor.add_description().code = str(j['data']['floors'][floor_index].pop('description'))
                        except KeyError: pass
                        # energy_efficiency_rating
                        try: 
                            floor.add_energy_efficiency_rating().code = str(j['data']['floors'][floor_index].pop('energy_efficiency_rating'))
                        except KeyError: pass
                        # environmental_efficiency_rating
                        try: 
                            floor.add_environmental_efficiency_rating().code = str(j['data']['floors'][floor_index].pop('environmental_efficiency_rating'))
                        except KeyError: pass
                        #
                        if len(j['data']['floors'][floor_index]) == 0:
                            c.append(floor_index)
                        else:
                            print(etree.tostring(rdsap_report, pretty_print=True).decode())
                            raise Exception('j', 'data', 'floors', floor_index, list(j['data']['floors'][floor_index])[0])
                    for c1 in c[::-1]: del j['data']['floors'][c1]
                    if len(j['data']['floors']) == 0: del j['data']['floors']

            if True:
                # --- Window ---
                if 'window' in j['data']:
                    window = property_summary.add_window()
                    # description
                    try: 
                        window.add_description().code = str(j['data']['window'].pop('description'))
                    except KeyError: pass
                    # energy_efficiency_rating
                    try: 
                        window.add_energy_efficiency_rating().code = str(j['data']['window'].pop('energy_efficiency_rating'))
                    except KeyError: pass
                    # environmental_efficiency_rating
                    try: 
                        window.add_environmental_efficiency_rating().code = str(j['data']['window'].pop('environmental_efficiency_rating'))
                    except KeyError: pass
                    if len(j['data']['window']) == 0:
                        del j['data']['window']
                    else:
                        raise Exception('j', 'data', 'window', list(j['data']['window'])[0])


            if True:
                # --- Air-Tightness ---
                if 'air_tightness' in j['data']:
                    air_tightness = property_summary.add_air_tightness()
                    # description
                    try: 
                        air_tightness.add_description().code = str(j['data']['air_tightness'].pop('description'))
                    except KeyError: pass
                    # energy_efficiency_rating
                    try: 
                        air_tightness.add_energy_efficiency_rating().code = str(j['data']['air_tightness'].pop('energy_efficiency_rating'))
                    except KeyError: pass
                    # environmental_efficiency_rating
                    try: 
                        air_tightness.add_environmental_efficiency_rating().code = str(j['data']['air_tightness'].pop('environmental_efficiency_rating'))
                    except KeyError: pass
                    if len(j['data']['air_tightness']) == 0:
                        del j['data']['air_tightness']
                    else:
                        raise Exception('j', 'data', 'air_tightness', list(j['data']['air_tightness'])[0])
                    
            if True:
                # --- Main-Heating ---
                if 'main_heating' in j['data']:
                    c = []
                    for main_heating_index in range(len(j['data']['main_heating'])):
                        # 
                        main_heating = property_summary.add_main_heating()
                        # description
                        try: 
                            main_heating.add_description().code = str(j['data']['main_heating'][main_heating_index].pop('description'))
                        except KeyError: pass
                        # energy_efficiency_rating
                        try: 
                            main_heating.add_energy_efficiency_rating().code = str(j['data']['main_heating'][main_heating_index].pop('energy_efficiency_rating'))
                        except KeyError: pass
                        # environmental_efficiency_rating
                        try: 
                            main_heating.add_environmental_efficiency_rating().code = str(j['data']['main_heating'][main_heating_index].pop('environmental_efficiency_rating'))
                        except KeyError: pass
                        #
                        if len(j['data']['main_heating'][main_heating_index]) == 0:
                            c.append(main_heating_index)
                        else:
                            print(etree.tostring(rdsap_report, pretty_print=True).decode())
                            raise Exception('j', 'data', 'main_heating', main_heating_index, list(j['data']['main_heating'][main_heating_index])[0])
                    for c1 in c[::-1]: del j['data']['main_heating'][c1]
                    if len(j['data']['main_heating']) == 0: del j['data']['main_heating']

            if True:
                # --- Main-Heating-Controls ---
                if 'main_heating_controls' in j['data']:
                    c = []
                    for main_heating_controls_index in range(len(j['data']['main_heating_controls'])):
                        # 
                        main_heating_controls = property_summary.add_main_heating_controls()
                        # description
                        try: 
                            main_heating_controls.add_description().code = str(j['data']['main_heating_controls'][main_heating_controls_index].pop('description'))
                        except KeyError: pass
                        # energy_efficiency_rating
                        try: 
                            main_heating_controls.add_energy_efficiency_rating().code = str(j['data']['main_heating_controls'][main_heating_controls_index].pop('energy_efficiency_rating'))
                        except KeyError: pass
                        # environmental_efficiency_rating
                        try: 
                            main_heating_controls.add_environmental_efficiency_rating().code = str(j['data']['main_heating_controls'][main_heating_controls_index].pop('environmental_efficiency_rating'))
                        except KeyError: pass
                        #
                        if len(j['data']['main_heating_controls'][main_heating_controls_index]) == 0:
                            c.append(main_heating_controls_index)
                        else:
                            print(etree.tostring(rdsap_report, pretty_print=True).decode())
                            raise Exception('j', 'data', 'main_heating_controls', main_heating_controls_index, list(j['data']['main_heating_controls'][main_heating_controls_index])[0])
                    for c1 in c[::-1]: del j['data']['main_heating_controls'][c1]
                    if len(j['data']['main_heating_controls']) == 0: del j['data']['main_heating_controls']


            if True:
                # --- Hot-Water ---
                if 'hot_water' in j['data']:
                    hot_water = property_summary.add_hot_water()
                    # description
                    try: 
                        hot_water.add_description().code = str(j['data']['hot_water'].pop('description'))
                    except KeyError: pass
                    # energy_efficiency_rating
                    try: 
                        hot_water.add_energy_efficiency_rating().code = str(j['data']['hot_water'].pop('energy_efficiency_rating'))
                    except KeyError: pass
                    # environmental_efficiency_rating
                    try: 
                        hot_water.add_environmental_efficiency_rating().code = str(j['data']['hot_water'].pop('environmental_efficiency_rating'))
                    except KeyError: pass
                    if len(j['data']['hot_water']) == 0:
                        del j['data']['hot_water']
                    else:
                        raise Exception('j', 'data', 'hot_water', list(j['data']['hot_water'])[0])

            if True:
                # --- Lighting ---
                if 'lighting' in j['data']:
                    lighting = property_summary.add_lighting()
                    # description
                    try: 
                        lighting.add_description().code = str(j['data']['lighting'].pop('description'))
                    except KeyError: pass
                    # energy_efficiency_rating
                    try: 
                        lighting.add_energy_efficiency_rating().code = str(j['data']['lighting'].pop('energy_efficiency_rating'))
                    except KeyError: pass
                    # environmental_efficiency_rating
                    try: 
                        lighting.add_environmental_efficiency_rating().code = str(j['data']['lighting'].pop('environmental_efficiency_rating'))
                    except KeyError: pass
                    if len(j['data']['lighting']) == 0:
                        del j['data']['lighting']
                    else:
                        raise Exception('j', 'data', 'lighting', list(j['data']['lighting'])[0])

            if True:
                # --- Secondary-Heating ---
                if 'secondary_heating' in j['data']:
                    secondary_heating = property_summary.add_secondary_heating()
                    # description
                    try: 
                        secondary_heating.add_description().code = str(j['data']['secondary_heating'].pop('description'))
                    except KeyError: pass
                    # energy_efficiency_rating
                    try: 
                        secondary_heating.add_energy_efficiency_rating().code = str(j['data']['secondary_heating'].pop('energy_efficiency_rating'))
                    except KeyError: pass
                    # environmental_efficiency_rating
                    try: 
                        secondary_heating.add_environmental_efficiency_rating().code = str(j['data']['secondary_heating'].pop('environmental_efficiency_rating'))
                    except KeyError: pass
                    if len(j['data']['secondary_heating']) == 0:
                        del j['data']['secondary_heating']
                    else:
                        raise Exception('j', 'data', 'secondary_heating', list(j['data']['secondary_heating'])[0])

            # Has-Hot-Water-Cylinder
            try: 
                property_summary.add_has_hot_water_cylinder().code = str(j['data'].pop('has_hot_water_cylinder'))
            except KeyError: pass

            # Has-Heated-Separate-Conservatory
            try: 
                property_summary.add_has_heated_separate_conservatory().code = str(j['data'].pop('has_heated_separate_conservatory'))
            except KeyError: pass

            # Dwelling-Type
            try: 
                property_summary.add_dwelling_type().code = str(j['data'].pop('dwelling_type'))
            except KeyError: pass

            # # Total-Floor-Area
            try: 
                property_summary.add_total_floor_area().code = str(j['data'].pop('total_floor_area'))
            except KeyError: pass

            # Has-Fixed-Air-Conditioning
            try: 
                property_summary.add_has_fixed_air_conditioning().code = str(j['data'].pop('has_fixed_air_conditioning'))
            except KeyError: pass

            # Multiple-Glazed-Proportion
            try: 
                property_summary.add_multiple_glazed_proportion().code = str(j['data'].pop('multiple_glazed_proportion'))
            except KeyError: pass

            # Multiple-Glazed-Proportion-NR
            try: 
                property_summary.add_multiple_glazed_proportion_nr().code = str(j['data'].pop('multiple_glazed_proportion_nr'))
            except KeyError: pass

        if True:
            # --- Energy-Use ---
            energy_use = energy_assessment.add_energy_use()

            # Energy-Rating-Current
            try: 
                energy_use.add_energy_rating_current().code = str(j['data'].pop('energy_rating_current'))
            except KeyError: pass

            # Energy-Rating-Potential
            try: 
                energy_use.add_energy_rating_potential().code = str(j['data'].pop('energy_rating_potential'))
            except KeyError: pass

            # Energy-Rating-Average
            try: 
                energy_use.add_energy_rating_average().code = str(j['data'].pop('energy_rating_average'))
            except KeyError: pass

            # Environmental-Impact-Current
            try: 
                energy_use.add_environmental_impact_current().code = str(j['data'].pop('environmental_impact_current'))
            except KeyError: pass

            # Environmental-Impact-Potential
            try: 
                energy_use.add_environmental_impact_potential().code = str(j['data'].pop('environmental_impact_potential'))
            except KeyError: pass

            # Energy-Consumption-Current
            try: 
                energy_use.add_energy_consumption_current().code = str(j['data'].pop('energy_consumption_current'))
            except KeyError: pass

            # Energy-Consumption-Potential
            try: 
                energy_use.add_energy_consumption_potential().code = str(j['data'].pop('energy_consumption_potential'))
            except KeyError: pass

            # CO2-Emissions-Current
            try: 
                energy_use.add_co2_emissions_current().code = str(j['data'].pop('co2_emissions_current'))
            except KeyError: pass

            # CO2-Emissions-Current-Per-Floor-Area
            try: 
                energy_use.add_co2_emissions_current_per_floor_area().code = str(j['data'].pop('co2_emissions_current_per_floor_area'))
            except KeyError: pass

            # CO2-Emissions-Potential
            try: 
                energy_use.add_co2_emissions_potential().code = str(j['data'].pop('co2_emissions_potential'))
            except KeyError: pass

            # Lighting-Cost-Current
            try: 
                energy_use.add_lighting_cost_current().code = str(j['data'].pop('lighting_cost_current'))
            except KeyError: pass

            # Lighting-Cost-Potential
            try: 
                energy_use.add_lighting_cost_potential().code = str(j['data'].pop('lighting_cost_potential'))
            except KeyError: pass

            # Heating-Cost-Current
            try: 
                energy_use.add_heating_cost_current().code = str(j['data'].pop('heating_cost_current'))
            except KeyError: pass

            # Heating-Cost-Potential
            try: 
                energy_use.add_heating_cost_potential().code = str(j['data'].pop('heating_cost_potential'))
            except KeyError: pass

            # Hot-Water-Cost-Current
            try: 
                energy_use.add_hot_water_cost_current().code = str(j['data'].pop('hot_water_cost_current'))
            except KeyError: pass

            # Hot-Water-Cost-Potential
            try: 
                energy_use.add_hot_water_cost_potential().code = str(j['data'].pop('hot_water_cost_potential'))
            except KeyError: pass

        if True:
            # --- Suggested-Improvements ---
            if 'suggested_improvements' in j['data']:
                suggested_improvements = energy_assessment.add_suggested_improvements()
                c = []
                for suggested_improvements_index in range(len(j['data']['suggested_improvements'])):
                    improvement = suggested_improvements.add_improvement()

                    # Sequence
                    try: 
                        improvement.add_sequence().code = str(j['data']['suggested_improvements'][suggested_improvements_index].pop('sequence'))
                    except KeyError: pass

                    # Improvement-Category
                    try: 
                        improvement.add_improvement_category().code = str(j['data']['suggested_improvements'][suggested_improvements_index].pop('improvement_category'))
                    except KeyError: pass

                    # Improvement-Type
                    try: 
                        improvement.add_improvement_type().code = str(j['data']['suggested_improvements'][suggested_improvements_index].pop('improvement_type'))
                    except KeyError: pass

                    # Typical-Saving
                    try: 
                        improvement.add_typical_saving().code = str(j['data']['suggested_improvements'][suggested_improvements_index].pop('typical_saving'))
                    except KeyError: pass

                    # Energy-Performance-Rating
                    try: 
                        improvement.add_energy_performance_rating().code = str(j['data']['suggested_improvements'][suggested_improvements_index].pop('energy_performance_rating'))
                    except KeyError: pass

                    # Environmental-Impact-Rating
                    try: 
                        improvement.add_environmental_impact_rating().code = str(j['data']['suggested_improvements'][suggested_improvements_index].pop('environmental_impact_rating'))
                    except KeyError: pass

                    # Improvement-Details
                    try: 
                        improvement.add_improvement_details().code = str(j['data']['suggested_improvements'][suggested_improvements_index].pop('improvement_details'))
                    except KeyError: pass

                    # Indicative-Cost
                    try: 
                        improvement.add_indicative_cost().code = str(j['data']['suggested_improvements'][suggested_improvements_index].pop('indicative_cost'))
                    except KeyError: pass

                    #
                    if len(j['data']['suggested_improvements'][suggested_improvements_index]) == 0:
                        c.append(suggested_improvements_index)
                    else:
                        print(etree.tostring(rdsap_report, pretty_print=True).decode())
                        raise Exception('j', 'data', 'suggested_improvements', suggested_improvements_index, list(j['data']['suggested_improvements'][suggested_improvements_index])[0])
                for c1 in c[::-1]: del j['data']['suggested_improvements'][c1]
                if len(j['data']['suggested_improvements']) == 0: del j['data']['suggested_improvements']



        if True:
            # --- LZC-Energy-Sources ---
            if 'lzc_energy_sources' in j['data']:
                lzc_energy_sources = energy_assessment.add_lzc_energy_sources()
                # LZC-Energy-Source
                for lzc_energy_source_code in j['data']['lzc_energy_sources']:
                    lzc_energy_sources.add_lzc_energy_source().code = str(lzc_energy_source_code)
                del j['data']['lzc_energy_sources']


        if True:
            # --- Addendum ---
            if 'addendum' in j['data']:

                addendum = energy_assessment.add_addendum()

                # Addendum-Number
                if 'addendum_numbers' in j['data']['addendum']:
                    for addendum_number_code in j['data']['addendum']['addendum_numbers']:
                        addendum.add_addendum_number().code = str(addendum_number_code)
                    del j['data']['addendum']['addendum_numbers']
                
                # Cavity-Fill-Recommended
                try: 
                    addendum.add_cavity_fill_recommended().code = str(j['data']['addendum'].pop('cavity_fill_recommended'))
                except KeyError: pass

                # Stone-Walls
                try: 
                    addendum.add_stone_walls().code = str(j['data']['addendum'].pop('stone_walls'))
                except KeyError: pass

                # System-Build
                try: 
                    addendum.add_system_build().code = str(j['data']['addendum'].pop('system_build'))
                except KeyError: pass
                
                # Access-Issues
                try: 
                    addendum.add_access_issues().code = str(j['data']['addendum'].pop('access_issues'))
                except KeyError: pass

                # High-Exposure
                try: 
                    addendum.add_high_exposure().code = str(j['data']['addendum'].pop('high_exposure'))
                except KeyError: pass

                # Narrow-Cavities
                try: 
                    addendum.add_narrow_cavities().code = str(j['data']['addendum'].pop('narrow_cavities'))
                except KeyError: pass

                #
                if len(j['data']['addendum']) == 0:
                    del j['data']['addendum']
                else:
                    raise Exception('j', 'data', 'addendum', list(j['data']['addendum'])[0])

        if True:
            # --- Renewable-Heat-Incentive ---
            if 'renewable_heat_incentive' in j['data']:
                renewable_heat_incentive = energy_assessment.add_renewable_heat_incentive()

                # Space-Heating-Existing-Dwelling
                try: 
                    renewable_heat_incentive.add_space_heating_existing_dwelling().code = str(j['data']['renewable_heat_incentive'].pop('space_heating_existing_dwelling'))
                except KeyError: pass

                # Water-Heating
                try: 
                    renewable_heat_incentive.add_water_heating().code = str(j['data']['renewable_heat_incentive'].pop('water_heating'))
                except KeyError: pass

                if len(j['data']['renewable_heat_incentive']) == 0:
                    del j['data']['renewable_heat_incentive']
                else:
                    raise Exception('j', 'data', 'renewable_heat_incentive', list(j['data']['renewable_heat_incentive'])[0])

        if True:
            # --- Alternative-Improvements ---
            if 'alternative_improvements' in j['data']:
                alternative_improvements = energy_assessment.add_alternative_improvements()
                c = []
                for alternative_improvements_index in range(len(j['data']['alternative_improvements'])):
                    # --- Improvement ---
                    improvement = alternative_improvements.add_improvement()

                    # Sequence
                    try: 
                        improvement.add_sequence().code = str(j['data']['alternative_improvements'][alternative_improvements_index].pop('sequence'))
                    except KeyError: pass

                    # Improvement-Category
                    try: 
                        improvement.add_improvement_category().code = str(j['data']['alternative_improvements'][alternative_improvements_index].pop('improvement_category'))
                    except KeyError: pass

                    # Improvement-Type
                    try: 
                        improvement.add_improvement_type().code = str(j['data']['alternative_improvements'][alternative_improvements_index].pop('improvement_type'))
                    except KeyError: pass

                    # Typical-Saving
                    try: 
                        improvement.add_typical_saving().code = str(j['data']['alternative_improvements'][alternative_improvements_index].pop('typical_saving'))
                    except KeyError: pass

                    # Energy-Performance-Rating
                    try: 
                        improvement.add_energy_performance_rating().code = str(j['data']['alternative_improvements'][alternative_improvements_index].pop('energy_performance_rating'))
                    except KeyError: pass

                    # Environmental-Impact-Rating
                    try: 
                        improvement.add_environmental_impact_rating().code = str(j['data']['alternative_improvements'][alternative_improvements_index].pop('environmental_impact_rating'))
                    except KeyError: pass

                    # Improvement-Details
                    try: 
                        improvement.add_improvement_details().code = str(j['data']['alternative_improvements'][alternative_improvements_index].pop('improvement_details'))
                    except KeyError: pass

                    # Indicative-Cost
                    try: 
                        improvement.add_indicative_cost().code = str(j['data']['alternative_improvements'][alternative_improvements_index].pop('indicative_cost'))
                    except KeyError: pass

                    #
                    if len(j['data']['alternative_improvements'][alternative_improvements_index]) == 0:
                        c.append(alternative_improvements_index)
                    else:
                        print(etree.tostring(rdsap_report, pretty_print=True).decode())
                        print(j['data']['alternative_improvements'][alternative_improvements_index])
                        raise Exception('j', 'data', 'alternative_improvements', alternative_improvements_index, list(j['data']['alternative_improvements'][alternative_improvements_index])[0])
                for c1 in c[::-1]: del j['data']['alternative_improvements'][c1]
                if len(j['data']['alternative_improvements']) == 0: del j['data']['alternative_improvements']


    if True:
        # --- SAP-Data ---
        sap_data = rdsap_report.add_sap_data()

        if True:
            # --- SAP-Property-Details
            sap_property_details = sap_data.add_sap_property_details()

            # Built-Form
            try: 
                sap_property_details.add_built_form().code = str(j['data'].pop('built_form'))
            except KeyError: pass

            # Extensions-Count
            try: 
                sap_property_details.add_extensions_count().code = str(j['data'].pop('extensions_count'))
            except KeyError: pass

            # Habitable-Room-Count
            try: 
                sap_property_details.add_habitable_room_count().code = str(j['data'].pop('habitable_room_count'))
            except KeyError: pass
    
            # Heated-Room-Count
            try: 
                sap_property_details.add_heated_room_count().code = str(j['data'].pop('heated_room_count'))
            except KeyError: pass

            # Low-Energy-Fixed-Lighting-Bulbs-Count
            try: 
                sap_property_details.add_low_energy_fixed_lighting_bulbs_count().code = str(j['data'].pop('low_energy_fixed_lighting_bulbs_count'))
            except KeyError: pass

            # Incandescent-Fixed-Lighting-Bulbs-Count
            try: 
                sap_property_details.add_incandescent_fixed_lighting_bulbs_count().code = str(j['data'].pop('incandescent_fixed_lighting_bulbs_count'))
            except KeyError: pass

            # LED-Fixed-Lighting-Bulbs-Count
            try: 
                sap_property_details.add_led_fixed_lighting_bulbs_count().code = str(j['data'].pop('led_fixed_lighting_bulbs_count'))
            except KeyError: pass

            # CFL-Fixed-Lighting-Bulbs-Count
            try: 
                sap_property_details.add_cfl_fixed_lighting_bulbs_count().code = str(j['data'].pop('cfl_fixed_lighting_bulbs_count'))
            except KeyError: pass

            # Measurement-Type
            try: 
                sap_property_details.add_measurement_type().code = str(j['data'].pop('measurement_type'))
            except KeyError: pass

            # Property-Type
            try: 
                sap_property_details.add_property_type().code = str(j['data'].pop('property_type'))
            except KeyError: pass

            # Solar-Water-Heating
            try: 
                sap_property_details.add_solar_water_heating().code = str(j['data'].pop('solar_water_heating'))
            except KeyError: pass
    
            # Wet-Rooms-Count
            try: 
                sap_property_details.add_wet_rooms_count().code = str(j['data'].pop('wet_rooms_count'))
            except KeyError: pass

            # Pressure-Test
            try: 
                sap_property_details.add_pressure_test().code = str(j['data'].pop('pressure_test'))
            except KeyError: pass

            # Pressure-Test-Certificate-Number
            try: 
                sap_property_details.add_pressure_test_certificate_number().code = str(j['data'].pop('pressure_test_certificate_number'))
            except KeyError: pass

            # Air-Permeability
            try: 
                sap_property_details.add_air_permeability().code = str(j['data'].pop('air_permeability'))
            except KeyError: pass

            # Has-Draught-Lobby
            try: 
                sap_property_details.add_has_draught_lobby().code = str(j['data'].pop('has_draught_lobby'))
            except KeyError: pass

            # Open-Chimneys-Count
            try: 
                sap_property_details.add_open_chimneys_count().code = str(j['data'].pop('open_chimneys_count'))
            except KeyError: pass

            # Blocked-Chimneys-Count
            try: 
                sap_property_details.add_blocked_chimneys_count().code = str(j['data'].pop('blocked_chimneys_count'))
            except KeyError: pass

            # Open-Flues-Count
            try: 
                sap_property_details.add_open_flues_count().code = str(j['data'].pop('open_flues_count'))
            except KeyError: pass

            # Closed-Flues-Count
            try: 
                sap_property_details.add_closed_flues_count().code = str(j['data'].pop('closed_flues_count'))
            except KeyError: pass

            # Boilers-Flues-Count
            try: 
                sap_property_details.add_boilers_flues_count().code = str(j['data'].pop('boilers_flues_count'))
            except KeyError: pass

            # Other-Flues-Count
            try: 
                sap_property_details.add_other_flues_count().code = str(j['data'].pop('other_flues_count'))
            except KeyError: pass

            # Extract-Fans-Count
            try: 
                sap_property_details.add_extract_fans_count().code = str(j['data'].pop('extract_fans_count'))
            except KeyError: pass

            # PSV-Count
            try: 
                sap_property_details.add_psv_count().code = str(j['data'].pop('psv_count'))
            except KeyError: pass

            # Flueless-Gas-Fire-Count
            try: 
                sap_property_details.add_flueless_gas_fires_count().code = str(j['data'].pop('flueless_gas_fires_count'))
            except KeyError: pass

            # Mechanical-Ventilation-Index-Number
            try: 
                sap_property_details.add_mechanical_ventilation_index_number().code = str(j['data'].pop('mechanical_ventilation_index_number'))
            except KeyError: pass
             
            # Mechanical-Ventilation
            try: 
                sap_property_details.add_mechanical_ventilation().code = str(j['data'].pop('mechanical_ventilation'))
            except KeyError: pass

            # Mechanical-Vent-Duct-Type
            try: 
                sap_property_details.add_mechanical_vent_duct_type().code = str(j['data'].pop('mechanical_vent_duct_type'))
            except KeyError: pass

            # Mechanical-Vent-Duct-Placement
            try: 
                sap_property_details.add_mechanical_vent_duct_placement().code = str(j['data'].pop('mechanical_vent_duct_placement'))
            except KeyError: pass

            # Mechanical-Vent-Duct-Insulation
            try: 
                sap_property_details.add_mechanical_vent_duct_insulation().code = str(j['data'].pop('mechanical_vent_duct_insulation'))
            except KeyError: 
                sap_property_details.add_mechanical_vent_duct_insulation().code = '1'  # not insulated

            # Mechanical-Vent-Duct-Insulation-Level
            try: 
                sap_property_details.add_mechanical_vent_duct_insulation_level().code = str(j['data'].pop('mechanical_vent_duct_insulation_level'))
            except KeyError: 
                sap_property_details.add_mechanical_vent_duct_insulation_level().code = '1'  # level 1

            # Mechanical-Vent-Measured-Installation
            try: 
                sap_property_details.add_mechanical_vent_measured_installation().code = str(j['data'].pop('mechanical_vent_measured_installation'))
            except KeyError: pass

            # Is-Mechanical-Vent-Approved-Installer-Scheme
            try: 
                sap_property_details.add_is_mechanical_vent_approved_installer_scheme().code = str(j['data'].pop('is_mechanical_vent_approved_installer_scheme'))
            except KeyError: pass

            # Kitchen-Rooms-Fans-Count
            try: 
                sap_property_details.add_kitchen_room_fans_count().code = str(j['data'].pop('kitchen_room_fans_count'))
            except KeyError: 
                sap_property_details.add_kitchen_room_fans_count().code = '0'

            # Non-Kitchen-Rooms-Fans-Count
            try: 
                sap_property_details.add_non_kitchen_room_fans_count().code = str(j['data'].pop('non_kitchen_room_fans_count'))
            except KeyError: 
                sap_property_details.add_non_kitchen_room_fans_count().code = '0'

            # Kitchen-Duct-Fans-Count
            try: 
                sap_property_details.add_kitchen_duct_fans_count().code = str(j['data'].pop('kitchen_duct_fans_count'))
            except KeyError: 
                sap_property_details.add_kitchen_duct_fans_count().code = '0'

            # Non-Kitchen-Duct-Fans-Count
            try: 
                sap_property_details.add_non_kitchen_duct_fans_count().code = str(j['data'].pop('non_kitchen_duct_fans_count'))
            except KeyError: 
                sap_property_details.add_non_kitchen_duct_fans_count().code = '0'

            # Kitchen-Walls-Fans-Count
            try: 
                sap_property_details.add_kitchen_wall_fans_count().code = str(j['data'].pop('kitchen_wall_fans_count'))
            except KeyError: 
                sap_property_details.add_kitchen_wall_fans_count().code = '0'

            # Non-Kitchen-Walls-Fans-Count
            try: 
                sap_property_details.add_non_kitchen_wall_fans_count().code = str(j['data'].pop('non_kitchen_wall_fans_count'))
            except KeyError: 
                sap_property_details.add_non_kitchen_wall_fans_count().code = '0'

            # Non-Kitchen-Walls-Fans-Count
            try: 
                sap_property_details.add_non_kitchen_duct_fans_count().code = str(j['data'].pop('non_kitchen_duct_fans_count'))
            except KeyError: pass
             
            # Conservatory-Type
            try: 
                sap_property_details.add_conservatory_type().code = str(j['data'].pop('conservatory_type'))
            except KeyError: pass  
    
            if True:
                # --- SAP-Heating ---
                if 'sap_heating' in j['data']:
                    sap_heating = sap_property_details.add_sap_heating()

                    # Secondary-Fuel-Type
                    try: 
                        sap_heating.add_secondary_fuel_type().code = str(j['data']['sap_heating'].pop('secondary_fuel_type'))
                    except KeyError: pass  ## ['38']:  # NOTE: CODE NOT IN XML SCHEMA - IS THIS A VERSION ISSUE?
    
                    # Water-Heating-Fuel
                    try: 
                        sap_heating.add_water_heating_fuel().code = str(j['data']['sap_heating'].pop('water_heating_fuel'))
                    except KeyError: pass
    
                    # Secondary-Heating-Type
                    try: 
                        sap_heating.add_secondary_heating_type().code = str(j['data']['sap_heating'].pop('secondary_heating_type'))
                    except KeyError: pass

                    # Water-Heating-Code
                    try: 
                        sap_heating.add_water_heating_code().code = str(j['data']['sap_heating'].pop('water_heating_code'))
                    except KeyError: pass

                    # Immersion-Heating-Type
                    try: 
                        sap_heating.add_immersion_heating_type().code = str(j['data']['sap_heating'].pop('immersion_heating_type'))
                    except KeyError: pass

                    # Cylinder-Size
                    try: 
                        sap_heating.add_cylinder_size().code = str(j['data']['sap_heating'].pop('cylinder_size'))
                    except KeyError: pass

                    # Cylinder-Size-Measured
                    try: 
                        sap_heating.add_cylinder_size_measured().code = str(j['data']['sap_heating'].pop('cylinder_size_measured'))
                    except KeyError: pass
                
                    # Cylinder-Insulation-Type
                    try: 
                        sap_heating.add_cylinder_insulation_type().code = str(j['data']['sap_heating'].pop('cylinder_insulation_type'))
                    except KeyError: pass

                    # Cylinder-Heat-Loss
                    try: 
                        sap_heating.add_cylinder_heat_loss().code = str(j['data']['sap_heating'].pop('cylinder_heat_loss'))
                    except KeyError: pass

                    # Cylinder-Insulation-Thickness
                    try: 
                        sap_heating.add_cylinder_insulation_thickness().code = str(j['data']['sap_heating'].pop('cylinder_insulation_thickness'))
                    except KeyError: pass

                    # Cylinder-Thermostat
                    try: 
                        sap_heating.add_cylinder_thermostat().code = str(j['data']['sap_heating'].pop('cylinder_thermostat'))
                    except KeyError: pass
    
                    # Has-Fixed-Air-Conditioning
                    try: 
                        sap_heating.add_has_fixed_air_conditioning().code = str(j['data']['sap_heating'].pop('has_fixed_air_conditioning'))
                    except KeyError: pass  
    
                    if True:
                        # --- Main-Heating-Details ---
                            if 'main_heating_details' in j['data']['sap_heating']:
                                main_heating_details = sap_heating.add_main_heating_details()
                                main_heating_details_c = []
                                for main_heating_index in range(len(j['data']['sap_heating']['main_heating_details'])):
                                    # --- Main-Heating ---
                                    main_heating = main_heating_details.add_main_heating()

                                    # Main-Heating-Number
                                    try: 
                                        main_heating.add_main_heating_number().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('main_heating_number'))
                                    except KeyError: pass

                                    # Main-Heating-Category
                                    try: 
                                        main_heating.add_main_heating_category().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('main_heating_category'))
                                    except KeyError: pass

                                    # Main-Fuel-Type
                                    try: 
                                        main_heating.add_main_fuel_type().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('main_fuel_type'))
                                    except KeyError: pass

                                    # Main-Heating-Control
                                    try: 
                                        main_heating.add_main_heating_control().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('main_heating_control'))
                                    except KeyError: pass

                                    # Main-Heating-Index-Number
                                    try: 
                                        main_heating.add_main_heating_index_number().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('main_heating_index_number'))
                                    except KeyError: pass

                                    # Main-Heating-Data-Source
                                    try: 
                                        main_heating.add_main_heating_data_source().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('main_heating_data_source'))
                                    except KeyError: pass

                                    # SAP-Main-Heating-Code
                                    try: 
                                        main_heating.add_sap_main_heating_code().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('sap_main_heating_code'))
                                    except KeyError: pass

                                    # Has-FGHRS
                                    try: 
                                        main_heating.add_has_fghrs().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('has_fghrs'))
                                    except KeyError: pass

                                    # FGHRS-Index-Number
                                    try: 
                                        main_heating.add_fghrs_index_number().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('fghrs_index_number'))
                                    except KeyError: pass

                                    # Boiler-Flue-Type
                                    try: 
                                        main_heating.add_boiler_flue_type().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('boiler_flue_type'))
                                    except KeyError: pass

                                    # Fan-Flue-Present
                                    try: 
                                        main_heating.add_fan_flue_present().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('fan_flue_present'))
                                    except KeyError: pass

                                    # Heat-Emitter-Type
                                    try: 
                                        main_heating.add_heat_emitter_type().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('heat_emitter_type'))
                                    except KeyError: pass

                                    # Main-Heating-Fraction
                                    try: 
                                        main_heating_fraction = j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('main_heating_fraction')
        
                                        main_heating.add_main_heating_fraction().code = str(float(main_heating_fraction)/100.0)
                                    except KeyError: pass

                                    # Emitter-Temperature
                                    try: 
                                        main_heating.add_emitter_temperature().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('emitter_temperature'))
                                    except KeyError: pass

                                    # Compensating-Controller-Index-Number
                                    try: 
                                        main_heating.add_compensating_controller_index_number().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('compensating_controller_index_number'))
                                    except KeyError: pass

                                    # TTZC-Index-Number
                                    try: 
                                        main_heating.add_ttzc_index_number().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('ttzc_index_number'))
                                    except KeyError: pass

                                    # Community-Heat-Sub-Network-Name
                                    try: 
                                        main_heating.add_community_heat_sub_network_name().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('community_heat_sub_network_name'))
                                    except KeyError: pass

                                    # Community-Heat-CHP-Electricity-Generation
                                    try: 
                                        main_heating.add_community_heat_chp_electricity_generation().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('community_heat_chp_electricity_generation'))
                                    except KeyError: pass

                                    if True:
                                        # --- Storage-Heater ---
                                        if 'storage_heaters' in j['data']['sap_heating']['main_heating_details'][main_heating_index]:
                                            storage_heaters = main_heating.add_storage_heaters()
                                            storage_heaters_c = []
                                            for storage_heater_index in range(len(j['data']['sap_heating']['main_heating_details'][main_heating_index]['storage_heaters'])):
                                                storage_heater = storage_heaters.add_storage_heater()

                                                # Number-Of-Heaters
                                                try: 
                                                    storage_heater.add_number_of_heaters().code = \
                                                        str(j['data']['sap_heating']['main_heating_details'][main_heating_index]['storage_heaters'][storage_heater_index].pop('number_of_heaters'))
                                                except KeyError: pass

                                                # Index-Number
                                                try: 
                                                    storage_heater.add_index_number().code = \
                                                        str(j['data']['sap_heating']['main_heating_details'][main_heating_index]['storage_heaters'][storage_heater_index].pop('index_number'))
                                                except KeyError: pass

                                                # High-Heat-Retention
                                                try: 
                                                    storage_heater.add_high_heat_retention().code = \
                                                        str(j['data']['sap_heating']['main_heating_details'][main_heating_index]['storage_heaters'][storage_heater_index].pop('high_heat_retention'))
                                                except KeyError: pass

                                                #
                                                if len(j['data']['sap_heating']['main_heating_details'][main_heating_index]['storage_heaters'][storage_heater_index]) == 0:
                                                    storage_heaters_c.append(storage_heater_index)
                                                else:
                                                    print(etree.tostring(rdsap_report, pretty_print=True).decode())
                                                    raise Exception('j', 'data', 'sap_heating', 'main_heating_details', main_heating_index, 'storage_heaters', storage_heater_index, 
                                                                    list(j['data']['sap_heating']['main_heating_details'][main_heating_index]['storage_heaters'][storage_heater_index])[0])
                                            for c1 in storage_heaters_c[::-1]: del j['data']['sap_heating']['main_heating_details'][main_heating_index]['storage_heaters'][c1]
                                            if len(j['data']['sap_heating']['main_heating_details'][main_heating_index]['storage_heaters']) == 0: del j['data']['sap_heating']['main_heating_details'][main_heating_index]['storage_heaters']


    #                                 elif k3 == 'storage_heaters':  # 0000-4241-0922-8599-3963.json
    #                                     storage_heaters = main_heating.add_storage_heaters()
    #                                     for index2 in range(len(v3)):
    #                                         for k4, v4 in v3[index2].items():
    #                                             storage_heater = storage_heaters.add_storage_heater()
    #                                             if k4 == 'index_number':
    #                                                 storage_heater.add_index_number().code = str(v4)
    #                                             elif k4 == 'number_of_heaters':
    #                                                 storage_heater.add_number_of_heaters().code = str(v4)
    #                                             elif k4 == 'high_heat_retention':
    #                                                 storage_heater.add_high_heat_retention().code = str(v4)
    #                                             else:
    #                                                 raise Exception(f'{input_file} {k0} {k1} {k2} {index} {k3} {index2} {k4}')

                                    # Community-Heat-Distribution-Type
                                    try: 
                                        main_heating.add_community_heat_distribution_type().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('community_heat_distribution_type'))
                                    except KeyError: pass

                                    # MCS-Installed-Heat-Pump
                                    try: 
                                        main_heating.add_mcs_installed_heat_pump().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('mcs_installed_heat_pump'))
                                    except KeyError: pass

                                    # Central-Heating-Pump-Age
                                    try: 
                                        main_heating.add_central_heating_pump_age().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('central_heating_pump_age'))
                                    except KeyError: pass

                                    if len(j['data']['sap_heating']['main_heating_details'][main_heating_index]) == 0:
                                        main_heating_details_c.append(main_heating_index)
                                    else:
                                        print(etree.tostring(rdsap_report, pretty_print=True).decode())
                                        raise Exception('j', 'data', 'sap_heating', 'main_heating_details', main_heating_index, list(j['data']['sap_heating']['main_heating_details'][main_heating_index])[0])
                                for c1 in main_heating_details_c[::-1]: del j['data']['sap_heating']['main_heating_details'][c1]
                                if len(j['data']['sap_heating']['main_heating_details']) == 0: del j['data']['sap_heating']['main_heating_details']
                                
                    if True:
                        # --- Solar-Water-Heating-Details ---
                        if 'solar_water_heating_details' in j['data']['sap_heating']:
                            solar_water_heating_details = sap_heating.add_solar_water_heating_details()

                            # Solar-Panel-Collector-Data-Source
                            try: 
                                solar_water_heating_details.add_solar_panel_collector_data_source().code = str(j['data']['sap_heating']['solar_water_heating_details'].pop('solar_panel_collector_data_source'))
                            except KeyError: pass

                            # Solar-Panel-Collector-Orientation
                            try: 
                                solar_water_heating_details.add_solar_panel_collector_orientation().code = str(j['data']['sap_heating']['solar_water_heating_details'].pop('solar_panel_collector_orientation'))
                            except KeyError: pass

                            # Solar-Panel-Collector-Pitch
                            try: 
                                solar_water_heating_details.add_solar_panel_collector_pitch().code = str(j['data']['sap_heating']['solar_water_heating_details'].pop('solar_panel_collector_pitch'))
                            except KeyError: pass

                            # Solar-Panel-Collector-Overshading
                            try: 
                                solar_water_heating_details.add_solar_panel_collector_overshading().code = str(j['data']['sap_heating']['solar_water_heating_details'].pop('solar_panel_collector_overshading'))
                            except KeyError: pass

                            # Solar-Water-Pump
                            try: 
                                solar_water_heating_details.add_solar_water_pump().code = str(j['data']['sap_heating']['solar_water_heating_details'].pop('solar_water_pump'))
                            except KeyError: pass

                            # Store-Volume-Details-Known
                            try: 
                                solar_water_heating_details.add_store_volume_details_known().code = str(j['data']['sap_heating']['solar_water_heating_details'].pop('store_volume_details_known'))
                            except KeyError: pass

                            if True:
                                # --- Solar-Collector-Details ---
                                if 'solar_collector_details' in j['data']['sap_heating']['solar_water_heating_details']:
                                    solar_collector_details = solar_water_heating_details.add_solar_collector_details()

                                    # Aperture-Area
                                    try: 
                                        solar_collector_details.add_aperture_area().code = str(j['data']['sap_heating']['solar_water_heating_details']['solar_collector_details'].pop('aperture_area'))
                                    except KeyError: pass

                                    # Collector-Type
                                    try: 
                                        solar_collector_details.add_collector_type().code = str(j['data']['sap_heating']['solar_water_heating_details']['solar_collector_details'].pop('collector_type'))
                                    except KeyError: pass

                                    # Zero-Loss-Efficiency
                                    try: 
                                        solar_collector_details.add_zero_loss_efficiency().code = str(j['data']['sap_heating']['solar_water_heating_details']['solar_collector_details'].pop('zero_loss_efficiency'))
                                    except KeyError: pass

                                    # Linear-Heat-Loss-Coefficient
                                    try: 
                                        solar_collector_details.add_linear_heat_loss_coefficient().code = \
                                            str(j['data']['sap_heating']['solar_water_heating_details']['solar_collector_details'].pop('linear_heat_loss_coefficient'))
                                    except KeyError: pass

                                    # Second-Order-Heat-Loss-Coefficient
                                    try: 
                                        solar_collector_details.add_second_order_heat_loss_coefficient().code = \
                                            str(j['data']['sap_heating']['solar_water_heating_details']['solar_collector_details'].pop('second_order_heat_loss_coefficient'))
                                    except KeyError: pass

                                    #
                                    if len(j['data']['sap_heating']['solar_water_heating_details']['solar_collector_details']) == 0:
                                        del j['data']['sap_heating']['solar_water_heating_details']['solar_collector_details']
                                    else:
                                        print(etree.tostring(rdsap_report, pretty_print=True).decode())
                                        raise Exception('j', 'data', 'sap_heating', 'solar_water_heating_details', 'solar_collector_details', 
                                                        list(j['data']['sap_heating']['solar_water_heating_details']['solar_collector_details'])[0])

                            if True:
                                # --- Solar-Volume-Details ---
                                if 'solar_volume_details' in j['data']['sap_heating']['solar_water_heating_details']:
                                    solar_volume_details = solar_water_heating_details.add_solar_volume_details()

                                    # Total-Store-Volume
                                    try: 
                                        solar_volume_details.add_total_store_volume().code = str(j['data']['sap_heating']['solar_water_heating_details']['solar_volume_details'].pop('total_store_volume'))
                                    except KeyError: pass

                                    # Total-Dedicated-Volume
                                    try: 
                                        solar_volume_details.add_dedicated_solar_volume().code = str(j['data']['sap_heating']['solar_water_heating_details']['solar_volume_details'].pop('dedicated_solar_volume'))
                                    except KeyError: pass

                                    # Combined-Cylinder
                                    try: 
                                        solar_volume_details.add_combined_cylinder().code = str(j['data']['sap_heating']['solar_water_heating_details']['solar_volume_details'].pop('combined_cylinder'))
                                    except KeyError: pass

                                    #
                                    if len(j['data']['sap_heating']['solar_water_heating_details']['solar_volume_details']) == 0:
                                        del j['data']['sap_heating']['solar_water_heating_details']['solar_volume_details']
                                    else:
                                        print(etree.tostring(rdsap_report, pretty_print=True).decode())
                                        raise Exception('j', 'data', 'sap_heating', 'solar_water_heating_details', 'solar_volume_details', 
                                                        list(j['data']['sap_heating']['solar_water_heating_details']['solar_volume_details'])[0])

                            # Shower-Types
                            try: 
                                solar_water_heating_details.add_shower_types().code = str(j['data']['sap_heating']['solar_water_heating_details'].pop('shower_types'))
                            except KeyError: pass

                            # Collector-Loop-Efficiency
                            try: 
                                solar_water_heating_details.add_collector_loop_efficiency().code = str(j['data']['sap_heating']['solar_water_heating_details'].pop('collector_loop_efficiency'))
                            except KeyError: pass

                            # Incidence-Angle-Modifier
                            try: 
                                solar_water_heating_details.add_incidence_angle_modifier().code = str(j['data']['sap_heating']['solar_water_heating_details'].pop('incidence_angle_modifier'))
                            except KeyError: pass

                            # Is-Community-Solar
                            try: 
                                solar_water_heating_details.add_is_community_solar().code = str(j['data']['sap_heating']['solar_water_heating_details'].pop('is_community_solar'))
                            except KeyError: pass

                            # Service-Provision
                            try: 
                                solar_water_heating_details.add_service_provision().code = str(j['data']['sap_heating']['solar_water_heating_details'].pop('service_provision'))
                            except KeyError: pass

                            #
                            if len(j['data']['sap_heating']['solar_water_heating_details']) == 0:
                                del j['data']['sap_heating']['solar_water_heating_details']
                            else:
                                print(etree.tostring(rdsap_report, pretty_print=True).decode())
                                raise Exception('j', 'data', 'sap_heating', 'solar_water_heating_details', list(j['data']['sap_heating']['solar_water_heating_details'])[0])

                    if True:
                        # --- Instantaneous-WWHRS ---
                        if 'instantaneous_wwhrs' in j['data']['sap_heating']:
                            instantaneous_wwhrs = sap_heating.add_instantaneous_wwhrs()

                            # WWHRS-Index-Number1
                            try: 
                                instantaneous_wwhrs.add_wwhrs_index_number1().code = str(j['data']['sap_heating']['instantaneous_wwhrs'].pop('wwhrs_index_number1'))
                            except KeyError: pass

                            # WWHRS-Index-Number2
                            try: 
                                instantaneous_wwhrs.add_wwhrs_index_number2().code = str(j['data']['sap_heating']['instantaneous_wwhrs'].pop('wwhrs_index_number2'))
                            except KeyError: pass

                            #
                            if len(j['data']['sap_heating']['instantaneous_wwhrs']) == 0:
                                del j['data']['sap_heating']['instantaneous_wwhrs']
                            else:
                                print(etree.tostring(rdsap_report, pretty_print=True).decode())
                                raise Exception('j', 'data', 'sap_heating', 'instantaneous_wwhrs', list(j['data']['sap_heating']['instantaneous_wwhrs'])[0])

                    # Shower-Outlets
                    if 'shower_outlets'in j['data']['sap_heating']:
                        shower_outlets = sap_heating.add_shower_outlets()
                        shower_outlets_c = []
                        for shower_index in range(len(j['data']['sap_heating']['shower_outlets'])):
                            # --- Shower-Outlet ---
                            shower_outlet = shower_outlets.add_shower_outlet()

                            # Shower-Outlet-Type
                            try: 
                                shower_outlet.add_shower_outlet_type().code = str(j['data']['sap_heating']['shower_outlets'][shower_index].pop('shower_outlet_type'))
                            except KeyError: pass

                            # Shower-WWhrs
                            try: 
                                shower_outlet.add_shower_wwhrs().code = str(j['data']['sap_heating']['shower_outlets'][shower_index].pop('shower_wwhrs'))
                            except KeyError: pass

                            if len(j['data']['sap_heating']['shower_outlets'][shower_index]) == 0:
                                shower_outlets_c.append(shower_index)
                            else:
                                print(etree.tostring(rdsap_report, pretty_print=True).decode())
                                raise Exception('j', 'data', 'sap_heating', 'shower_outlets', shower_index, list(j['data']['sap_heating']['shower_outlets'][shower_index])[0])
                                
                        for c1 in shower_outlets_c[::-1]: del j['data']['sap_heating']['shower_outlets'][c1]
                        if len(j['data']['sap_heating']['shower_outlets']) == 0: del j['data']['sap_heating']['shower_outlets']

                    # Number-Baths
                    try: 
                        sap_heating.add_number_baths().code = str(j['data']['sap_heating'].pop('number_baths'))
                    except KeyError: pass

                    # Number-Baths-WWHRS
                    try: 
                        sap_heating.add_number_baths_wwhrs().code = str(j['data']['sap_heating'].pop('number_baths_wwhrs'))
                    except KeyError: pass

                    # Community-DHW-Disribution-Type
                    try: 
                        sap_heating.add_community_dhw_distribution_type().code = str(j['data']['sap_heating'].pop('community_dhw_distribution_type'))
                    except KeyError: pass
                         
                    # Community-DHW-CHP-Electricity-Generation
                    try: 
                        sap_heating.add_community_dhw_chp_electricity_generation().code = str(j['data']['sap_heating'].pop('community_dhw_chp_electricity_generation'))
                    except KeyError: pass

                    #
                    if len(j['data']['sap_heating']) == 0:
                        del j['data']['sap_heating']
                    else:
                        raise Exception('j', 'data', 'sap_heating', list(j['data']['sap_heating'])[0])

            if True:
                # --- SAP-Energy-Source ---
                if 'sap_energy_source' in j['data']:
                    sap_energy_source = sap_property_details.add_sap_energy_source()

                    # Meter-Type
                    try: 
                        sap_energy_source.add_meter_type().code = str(j['data']['sap_energy_source'].pop('meter_type'))
                    except KeyError: pass

                    # Mains-Gas
                    try: 
                        sap_energy_source.add_mains_gas().code = str(j['data']['sap_energy_source'].pop('mains_gas'))
                    except KeyError: pass

                    # Electricity-Smart-Meter-Present
                    try: 
                        sap_energy_source.add_electricity_smart_meter_present().code = str(j['data']['sap_energy_source'].pop('electricity_smart_meter_present'))
                    except KeyError: pass

                    # Gas-Smart-Meter-Present
                    try: 
                        sap_energy_source.add_gas_smart_meter_present().code = str(j['data']['sap_energy_source'].pop('gas_smart_meter_present'))
                    except KeyError: pass

                    # Is-Dwelling-Export-Capable
                    try: 
                        sap_energy_source.add_is_dwelling_export_capable().code = str(j['data']['sap_energy_source'].pop('is_dwelling_export_capable'))
                    except KeyError: pass

                    # Wind-Turbine-Count
                    try: 
                        sap_energy_source.add_wind_turbines_count().code = str(j['data']['sap_energy_source'].pop('wind_turbines_count'))
                    except KeyError: pass

                    # Wind-Turbine-Terrian-Type
                    try: 
                        sap_energy_source.add_wind_turbines_terrain_type().code = str(j['data']['sap_energy_source'].pop('wind_turbines_terrain_type'))
                    except KeyError: pass

                    if True:
                        # --- Wind-Turbine-Details
                        if 'wind_turbine_details' in j['data']['sap_energy_source']:
                            wind_turbine_details = sap_energy_source.add_wind_turbine_details()

                            # Rotor-Diameter
                            try: 
                                wind_turbine_details.add_rotor_diameter().code = str(j['data']['sap_energy_source']['wind_turbine_details'].pop('rotor_diameter'))
                            except KeyError: pass

                            # Hub-Height
                            try: 
                                wind_turbine_details.add_hub_height().code = str(j['data']['sap_energy_source']['wind_turbine_details'].pop('hub_height'))
                            except KeyError: pass

                            #
                            if len(j['data']['sap_energy_source']['wind_turbine_details']) == 0:
                                del j['data']['sap_energy_source']['wind_turbine_details']
                            else:
                                print(etree.tostring(rdsap_report, pretty_print=True).decode())
                                raise Exception('j', 'data', 'sap_energy_source', 'wind_turbine_details', list(j['data']['sap_energy_source']['wind_turbine_details'])[0])

                    if True:
                        # --- Photovoltaic-Supply ---
                        if 'photovoltaic_supply' in j['data']['sap_energy_source']:
                            photovoltaic_supply = sap_energy_source.add_photovoltaic_supply()
                            if True:
                                # --- PV-Arrays ---
                                if 'pv_arrays' in j['data']['sap_energy_source']['photovoltaic_supply']:
                                    c = []
                                    for pv_array_index in range(len(j['data']['sap_energy_source']['photovoltaic_supply']['pv_arrays'])):
                                        pv_arrays = photovoltaic_supply.add_pv_arrays()
                                        pv_array = pv_arrays.add_pv_array()

                                        # Peak-Power
                                        try: 
                                            pv_array.add_peak_power().code = str(j['data']['sap_energy_source']['photovoltaic_supply']['pv_arrays'][pv_array_index].pop('peak_power'))
                                        except KeyError: pass

                                        # Orientation
                                        try: 
                                            pv_array.add_orientation().code = str(j['data']['sap_energy_source']['photovoltaic_supply']['pv_arrays'][pv_array_index].pop('orientation'))
                                        except KeyError: pass

                                        # Pitch
                                        try: 
                                            pv_array.add_pitch().code = str(j['data']['sap_energy_source']['photovoltaic_supply']['pv_arrays'][pv_array_index].pop('pitch'))
                                        except KeyError: pass

                                        # Overshading
                                        try: 
                                            pv_array.add_overshading().code = str(j['data']['sap_energy_source']['photovoltaic_supply']['pv_arrays'][pv_array_index].pop('overshading'))
                                        except KeyError: pass
                                        
                                        #
                                        if len(j['data']['sap_energy_source']['photovoltaic_supply']['pv_arrays'][pv_array_index]) == 0:
                                            c.append(pv_array_index)
                                        else:
                                            print(etree.tostring(rdsap_report, pretty_print=True).decode())
                                            raise Exception('j', 'data', 'sap_energy_source', 'photovoltaic_supply', 'pv_arrays', pv_array_index, 
                                                            list(j['data']['sap_energy_source']['photovoltaic_supply']['pv_arrays'][pv_array_index])[0])
                                    for c1 in c[::-1]: del j['data']['sap_energy_source']['photovoltaic_supply']['pv_arrays'][c1]
                                    if len(j['data']['sap_energy_source']['photovoltaic_supply']['pv_arrays']) == 0: del j['data']['sap_energy_source']['photovoltaic_supply']['pv_arrays']

                                # --- None-Or-No-Details ---
                                if 'none_or_no_details' in j['data']['sap_energy_source']['photovoltaic_supply']:
                                    none_or_no_details = photovoltaic_supply.add_none_or_no_details()
                                    # Percent-Roof-Area
                                    try: 
                                        none_or_no_details.add_percent_roof_area().code = str(j['data']['sap_energy_source']['photovoltaic_supply']['none_or_no_details'].pop('percent_roof_area'))
                                    except KeyError: pass

                                    #
                                    if len(j['data']['sap_energy_source']['photovoltaic_supply']['none_or_no_details']) == 0:
                                        del j['data']['sap_energy_source']['photovoltaic_supply']['none_or_no_details']
                                    else:
                                        raise Exception('j', 'data', 'sap_energy_source', 'photovoltaic_supply', 'none_or_no_details', 
                                                        list(j['data']['sap_energy_source']['photovoltaic_supply']['none_or_no_details'])[0])

                            #
                            if len(j['data']['sap_energy_source']['photovoltaic_supply']) == 0:
                                del j['data']['sap_energy_source']['photovoltaic_supply']
                            else:
                                print(etree.tostring(rdsap_report, pretty_print=True).decode())
                                raise Exception('j', 'data', 'sap_energy_source', 'photovoltaic_supply', list(j['data']['sap_energy_source']['photovoltaic_supply'])[0])

                    # PV-Connection
                    try: 
                        sap_energy_source.add_pv_connection().code = str(j['data']['sap_energy_source'].pop('pv_connection'))
                    except KeyError: pass

                    # PV-Diverter
                    try: 
                        sap_energy_source.add_pv_diverter().code = str(j['data']['sap_energy_source'].pop('pv_diverter'))
                    except KeyError: pass

                    # PV-Battery-Count
                    try: 
                        sap_energy_source.add_pv_battery_count().code = str(j['data']['sap_energy_source'].pop('pv_battery_count'))
                    except KeyError: pass

                    if True:
                        # --- PV-Batteries ---
                        if 'pv_batteries' in j['data']['sap_energy_source']:
                            pv_batteries = sap_energy_source.add_pv_batteries()
                            pv_batteries_c = []
                            for pv_battery_index in range(len(j['data']['sap_energy_source']['pv_batteries'])):
                                
                                # --- PV-Battery ---
                                if 'pv_battery' in j['data']['sap_energy_source']['pv_batteries'][pv_battery_index]:
                                    pv_battery = pv_batteries.add_pv_battery()

                                    # Battery-Capacity
                                    try: 
                                        pv_battery.add_battery_capacity().code = str(j['data']['sap_energy_source']['pv_batteries'][pv_battery_index]['pv_battery'].pop('battery_capacity'))
                                    except KeyError: pass

                                    #
                                    if len(j['data']['sap_energy_source']['pv_batteries'][pv_battery_index]['pv_battery']) == 0:
                                        del j['data']['sap_energy_source']['pv_batteries'][pv_battery_index]['pv_battery']
                                    else:
                                        raise Exception('j', 'data', 'sap_energy_source', 'pv_batteries', pv_battery_index, 'pv_battery', 
                                                        list(j['data']['sap_energy_source']['pv_batteries'][pv_battery_index]['pv_battery'])[0])

                                #
                                if len(j['data']['sap_energy_source']['pv_batteries'][pv_battery_index]) == 0:
                                    pv_batteries_c.append(pv_battery_index)
                                else:
                                    print(etree.tostring(rdsap_report, pretty_print=True).decode())
                                    raise Exception('j', 'data', 'sap_energy_source', 'pv_batteries', pv_battery_index, list(j['data']['sap_energy_source']['pv_batteries'][pv_battery_index])[0])
                            for c1 in pv_batteries_c[::-1]: del j['data']['sap_energy_source']['pv_batteries'][c1]
                            if len(j['data']['sap_energy_source']['pv_batteries']) == 0: del j['data']['sap_energy_source']['pv_batteries']

                    # Hydro-Electric-Generation
                    try: 
                        sap_energy_source.add_hydro_electric_generation().code = str(j['data']['sap_energy_source'].pop('hydro_electric_generation'))
                    except KeyError: pass

                    # Is-Hydro-Output-Connected-To-Dwelling-Meter
                    try: 
                        sap_energy_source.add_is_hydro_output_connected_to_dwelling_meter().code = str(j['data']['sap_energy_source'].pop('is_hydro_output_connected_to_dwelling_meter'))
                    except KeyError: pass

                    #
                    if len(j['data']['sap_energy_source']) == 0:
                        del j['data']['sap_energy_source']
                    else:
                        raise Exception('j', 'data', 'sap_energy_source', list(j['data']['sap_energy_source'])[0])

            if True:
                # --- SAP-Building-Parts ---
                if 'sap_building_parts' in j['data']:
                    sap_building_parts = sap_property_details.add_sap_building_parts()
                    c = []
                    for sap_building_part_index in range(len(j['data']['sap_building_parts'])):

                        if 'identifier' in j['data']['sap_building_parts'][sap_building_part_index]:
                            # --- SAP-Building-Part ---
                            sap_building_part = sap_building_parts.add_sap_building_part()

                            # Building-Part-Number
                            try: 
                                sap_building_part.add_building_part_number().code = str(j['data']['sap_building_parts'][sap_building_part_index].pop('building_part_number'))
                            except KeyError: pass

                            # Identifier
                            try: 
                                sap_building_part.add_identifier().code = str(j['data']['sap_building_parts'][sap_building_part_index].pop('identifier'))
                            except KeyError: pass

                            # Construction-Age-Band
                            try: 
                                sap_building_part.add_construction_age_band().code = str(j['data']['sap_building_parts'][sap_building_part_index].pop('construction_age_band'))
                            except KeyError: pass

                            if True:
                                # --- SAP-Floor-Dimensions ---
                                if 'sap_floor_dimensions' in j['data']['sap_building_parts'][sap_building_part_index]:
                                    sap_floor_dimensions = sap_building_part.add_sap_floor_dimensions()
                                    sap_floor_dimensions_c = []
                                    for sap_floor_dimension_index in range(len(j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'])):
                                        sap_floor_dimension = sap_floor_dimensions.add_sap_floor_dimension()

                                        # Heat-Loss-Perimeter
                                        try: 
                                            sap_floor_dimension.add_heat_loss_perimeter().code = \
                                                str(j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index].pop('heat_loss_perimeter'))
                                        except KeyError: pass

                                        # Room-Height
                                        try: 
                                            sap_floor_dimension.add_room_height().code = \
                                                str(j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index].pop('room_height'))
                                        except KeyError: pass

                                        # Total-Floor-Area
                                        try: 
                                            sap_floor_dimension.add_total_floor_area().code = \
                                                str(j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index].pop('total_floor_area'))
                                        except KeyError: pass

                                        # Floor
                                        try: 
                                            sap_floor_dimension.add_floor().code = \
                                                str(j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index].pop('floor'))
                                        except KeyError: pass

                                        # Floor-Construction
                                        try: 
                                            sap_floor_dimension.add_floor_construction().code = \
                                                str(j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index].pop('floor_construction'))
                                        except KeyError: pass

                                        # Floor-Insulation
                                        try: 
                                            sap_floor_dimension.add_floor_insulation().code = \
                                                str(j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index].pop('floor_insulation'))
                                        except KeyError: pass

                                        # Party-Wall-Length
                                        try: 
                                            sap_floor_dimension.add_party_wall_length().code = \
                                                str(j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index].pop('party_wall_length'))
                                        except KeyError: pass

                                        #
                                        if len(j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index]) == 0:
                                            sap_floor_dimensions_c.append(sap_floor_dimension_index)
                                        else:
                                            raise Exception('j', 'data', 'sap_building_parts', sap_building_part_index, 'sap_floor_dimensions', sap_floor_dimension_index,
                                                            list(j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index])[0])
                                    #
                                    for c1 in sap_floor_dimensions_c[::-1]: del j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][c1]
                                    if len(j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions']) == 0: 
                                        del j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions']

                            # Floor-U-Value
                            try: 
                                sap_building_part.add_floor_u_value().code = str(j['data']['sap_building_parts'][sap_building_part_index].pop('floor_u_value'))
                            except KeyError: pass

                            # Floor-Insulation-Thickness
                            try: 
                                sap_building_part.add_floor_insulation_thickness().code = str(j['data']['sap_building_parts'][sap_building_part_index].pop('floor_insulation_thickness'))
                            except KeyError: pass

                            # Floor-Heat-Loss
                            try: 
                                sap_building_part.add_floor_heat_loss().code = str(j['data']['sap_building_parts'][sap_building_part_index].pop('floor_heat_loss'))
                            except KeyError: pass

                            # Roof-Construction
                            try: 
                                sap_building_part.add_roof_construction().code = str(j['data']['sap_building_parts'][sap_building_part_index].pop('roof_construction'))
                            except KeyError: pass

                            # Roof-Insulation-Location
                            try: 
                                sap_building_part.add_roof_insulation_location().code = str(j['data']['sap_building_parts'][sap_building_part_index].pop('roof_insulation_location'))
                            except KeyError: pass

                            # Roof-U-Value
                            try: 
                                sap_building_part.add_roof_u_value().code = str(j['data']['sap_building_parts'][sap_building_part_index].pop('roof_u_value'))
                            except KeyError: pass

                            # Roof-Insulation-Thickness
                            try: 
                                sap_building_part.add_roof_insulation_thickness().code = str(j['data']['sap_building_parts'][sap_building_part_index].pop('roof_insulation_thickness'))
                            except KeyError: pass

                            # Rafter-Insulation-Thickness
                            try: 
                                sap_building_part.add_rafter_insulation_thickness().code = str(j['data']['sap_building_parts'][sap_building_part_index].pop('rafter_insulation_thickness'))
                            except KeyError: pass

                            # Flat-Roof-Insulation-Thickness
                            try: 
                                sap_building_part.add_flat_roof_insulation_thickness().code = str(j['data']['sap_building_parts'][sap_building_part_index].pop('flat_roof_insulation_thickness'))
                            except KeyError: pass

                            # Sloping-Ceiling-Insulation-Thickness
                            try: 
                                sap_building_part.add_sloping_ceiling_insulation_thickness().code = str(j['data']['sap_building_parts'][sap_building_part_index].pop('sloping_ceiling_insulation_thickness'))
                            except KeyError: pass

                            # Wall-Construction
                            try: 
                                sap_building_part.add_wall_construction().code = str(j['data']['sap_building_parts'][sap_building_part_index].pop('wall_construction'))
                            except KeyError: pass

                            # Wall-Insulation-Type
                            try: 
                                sap_building_part.add_wall_insulation_type().code = str(j['data']['sap_building_parts'][sap_building_part_index].pop('wall_insulation_type'))
                            except KeyError: pass

                            # Wall-Thickness-Measured
                            try: 
                                sap_building_part.add_wall_thickness_measured().code = str(j['data']['sap_building_parts'][sap_building_part_index].pop('wall_thickness_measured'))
                            except KeyError: pass

                            # Wall-Thickness
                            try: 
                                sap_building_part.add_wall_thickness().code = str(j['data']['sap_building_parts'][sap_building_part_index].pop('wall_thickness'))
                            except KeyError: pass

                            # Wall-Dry-Lined
                            try: 
                                sap_building_part.add_wall_dry_lined().code = str(j['data']['sap_building_parts'][sap_building_part_index].pop('wall_dry_lined'))
                            except KeyError: pass

                            # Wall-U-Value
                            try: 
                                sap_building_part.add_wall_u_value().code = str(j['data']['sap_building_parts'][sap_building_part_index].pop('wall_u_value'))
                            except KeyError: pass

                            # Wall-Insulation-Thickness
                            try: 
                                sap_building_part.add_wall_insulation_thickness().code = str(j['data']['sap_building_parts'][sap_building_part_index].pop('wall_insulation_thickness'))
                            except KeyError: pass

                            # Wall-Insulation-Thickness-Measured
                            try: 
                                sap_building_part.add_wall_insulation_thickness_measured().code = str(j['data']['sap_building_parts'][sap_building_part_index].pop('wall_insulation_thickness_measured'))
                            except KeyError: pass

                            # Wall-Insulation-Thermal-Conductivity
                            try: 
                                sap_building_part.add_wall_insulation_thermal_conductivity().code = str(j['data']['sap_building_parts'][sap_building_part_index].pop('wall_insulation_thermal_conductivity'))
                            except KeyError: pass

                            if True:
                                # --- SAP-Room-In-Roof ---
                                if 'sap_room_in_roof' in j['data']['sap_building_parts'][sap_building_part_index]:
                                    sap_room_in_roof = sap_building_part.add_sap_room_in_roof()

                                    # Floor-Area
                                    try: 
                                        sap_room_in_roof.add_floor_area().code = str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof'].pop('floor_area'))
                                    except KeyError: pass

                                    # Construction-Age-Band
                                    try: 
                                        sap_room_in_roof.add_construction_age_band().code = str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof'].pop('construction_age_band'))
                                    except KeyError: pass

                                    if True:
                                        # --- Room-In-Roof-Details ---
                                        if 'room_in_roof_details' in j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']:
                                            room_in_roof_details = sap_room_in_roof.add_room_in_roof_details()

                                            # Flat-Ceiling-Length-1
                                            try: 
                                                room_in_roof_details.add_flat_ceiling_length_1().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('flat_ceiling_length_1'))
                                            except KeyError: pass

                                            # Flat-Ceiling-Height-1
                                            try: 
                                                room_in_roof_details.add_flat_ceiling_height_1().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('flat_ceiling_height_1'))
                                            except KeyError: pass

                                            # Flat-Ceiling-U-Value-1
                                            try: 
                                                room_in_roof_details.add_flat_ceiling_u_value_1().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('flat_ceiling_u_value_1'))
                                            except KeyError: pass

                                            # Flat-Ceiling-Insulation-Thickness-1
                                            try: 
                                                room_in_roof_details.add_flat_ceiling_insulation_thickness_1().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('flat_ceiling_insulation_thickness_1'))
                                            except KeyError: pass

                                            # Flat-Ceiling-Insulation-Type-1
                                            try: 
                                                room_in_roof_details.add_flat_ceiling_insulation_type_1().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('flat_ceiling_insulation_type_1'))
                                            except KeyError: pass

                                            # Flat-Ceiling-Insulation-Location-1
                                            try: 
                                                room_in_roof_details.add_flat_ceiling_insulation_location_1().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('flat_ceiling_insulation_location_1'))
                                            except KeyError: pass

                                            # Flat-Ceiling-Length-2
                                            try: 
                                                room_in_roof_details.add_flat_ceiling_length_2().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('flat_ceiling_length_2'))
                                            except KeyError: pass

                                            # Flat-Ceiling-Height-2
                                            try: 
                                                room_in_roof_details.add_flat_ceiling_height_2().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('flat_ceiling_height_2'))
                                            except KeyError: pass

                                            # Flat-Ceiling-U-Value-2
                                            try: 
                                                room_in_roof_details.add_flat_ceiling_u_value_2().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('flat_ceiling_u_value_2'))
                                            except KeyError: pass

                                            # Flat-Ceiling-Insulation-Thickness-2
                                            try: 
                                                room_in_roof_details.add_flat_ceiling_insulation_thickness_2().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('flat_ceiling_insulation_thickness_2'))
                                            except KeyError: pass

                                            # Flat-Ceiling-Insulation-Type-2
                                            try: 
                                                room_in_roof_details.add_flat_ceiling_insulation_type_2().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('flat_ceiling_insulation_type_2'))
                                            except KeyError: pass

                                            # Flat-Ceiling-Insulation-Location-2
                                            try: 
                                                room_in_roof_details.add_flat_ceiling_insulation_location_2().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('flat_ceiling_insulation_location_2'))
                                            except KeyError: pass

                                            # Stud-Wall-Length-1
                                            try: 
                                                room_in_roof_details.add_stud_wall_length_1().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('stud_wall_length_1'))
                                            except KeyError: pass

                                            # Stud-Wall-Height-1
                                            try: 
                                                room_in_roof_details.add_stud_wall_height_1().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('stud_wall_height_1'))
                                            except KeyError: pass

                                            # Stud-Wall-U-Value-1
                                            try: 
                                                room_in_roof_details.add_stud_wall_u_value_1().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('stud_wall_u_value_1'))
                                            except KeyError: pass

                                            # Stud-Wall-Insulation-Thickness-1
                                            try: 
                                                room_in_roof_details.add_stud_wall_insulation_thickness_1().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('stud_wall_insulation_thickness_1'))
                                            except KeyError: pass

                                            # Stud-Wall-Insulation-Type-1
                                            try: 
                                                room_in_roof_details.add_stud_wall_insulation_type_1().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('stud_wall_insulation_type_1'))
                                            except KeyError: pass

                                            # Stud-Wall-Length-2
                                            try: 
                                                room_in_roof_details.add_stud_wall_length_2().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('stud_wall_length_2'))
                                            except KeyError: pass

                                            # Stud-Wall-Height-2
                                            try: 
                                                room_in_roof_details.add_stud_wall_height_2().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('stud_wall_height_2'))
                                            except KeyError: pass

                                            # Stud-Wall-U-Value-2
                                            try: 
                                                room_in_roof_details.add_stud_wall_u_value_2().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('stud_wall_u_value_2'))
                                            except KeyError: pass

                                            # Stud-Wall-Insulation-Thickness-2
                                            try: 
                                                room_in_roof_details.add_stud_wall_insulation_thickness_2().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('stud_wall_insulation_thickness_2'))
                                            except KeyError: pass

                                            # Stud-Wall-Insulation-Type-2
                                            try: 
                                                room_in_roof_details.add_stud_wall_insulation_type_2().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('stud_wall_insulation_type_2'))
                                            except KeyError: pass

                                            # Slope-Length-1
                                            try: 
                                                room_in_roof_details.add_slope_length_1().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('slope_length_1'))
                                            except KeyError: pass

                                            # Slope-Height-1
                                            try: 
                                                room_in_roof_details.add_slope_height_1().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('slope_height_1'))
                                            except KeyError: pass

                                            # Slope-U-Value-1
                                            try: 
                                                room_in_roof_details.add_slope_u_value_1().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('slope_u_value_1'))
                                            except KeyError: pass

                                            # Slope-Insulation-Thickness-1
                                            try: 
                                                room_in_roof_details.add_slope_insulation_thickness_1().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('slope_insulation_thickness_1'))
                                            except KeyError: pass

                                            # Slope-Insulation-Type-1
                                            try: 
                                                room_in_roof_details.add_slope_insulation_type_1().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('slope_insulation_type_1'))
                                            except KeyError: pass

                                            # Slope-Length-2
                                            try: 
                                                room_in_roof_details.add_slope_length_2().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('slope_length_2'))
                                            except KeyError: pass

                                            # Slope-Height-2
                                            try: 
                                                room_in_roof_details.add_slope_height_2().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('slope_height_2'))
                                            except KeyError: pass

                                            # Slope-U-Value-2
                                            try: 
                                                room_in_roof_details.add_slope_u_value_2().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('slope_u_value_2'))
                                            except KeyError: pass

                                            # Slope-Insulation-Thickness-2
                                            try: 
                                                room_in_roof_details.add_slope_insulation_thickness_2().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('slope_insulation_thickness_2'))
                                            except KeyError: pass

                                            # Slope-Insulation-Type-2
                                            try: 
                                                room_in_roof_details.add_slope_insulation_type_2().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('slope_insulation_type_2'))
                                            except KeyError: pass

                                            # Gable-Wall-Type-1
                                            try: 
                                                room_in_roof_details.add_gable_wall_type_1().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('gable_wall_type_1'))
                                            except KeyError: pass

                                            # Gable-Wall-Length-1
                                            try: 
                                                room_in_roof_details.add_gable_wall_length_1().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('gable_wall_length_1'))
                                            except KeyError: pass

                                            # Gable-Wall-Height-1
                                            try: 
                                                room_in_roof_details.add_gable_wall_height_1().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('gable_wall_height_1'))
                                            except KeyError: pass

                                            # Gable-Wall-U-Value-1
                                            try: 
                                                room_in_roof_details.add_gable_wall_u_value_1().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('gable_wall_u_value_1'))
                                            except KeyError: pass

                                            # Gable-Wall-Type-2
                                            try: 
                                                room_in_roof_details.add_gable_wall_type_2().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('gable_wall_type_2'))
                                            except KeyError: pass

                                            # Gable-Wall-Length-2
                                            try: 
                                                room_in_roof_details.add_gable_wall_length_2().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('gable_wall_length_2'))
                                            except KeyError: pass

                                            # Gable-Wall-Height-2
                                            try: 
                                                room_in_roof_details.add_gable_wall_height_2().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('gable_wall_height_2'))
                                            except KeyError: pass

                                            # Gable-Wall-U-Value-2
                                            try: 
                                                room_in_roof_details.add_gable_wall_u_value_2().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('gable_wall_u_value_2'))
                                            except KeyError: pass

                                            # Common-Wall-Length-1
                                            try: 
                                                room_in_roof_details.add_common_wall_length_1().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('common_wall_length_1'))
                                            except KeyError: pass

                                            # Common-Wall-Height-1
                                            try: 
                                                room_in_roof_details.add_common_wall_height_1().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('common_wall_height_1'))
                                            except KeyError: pass

                                            # Common-Wall-U-Value-1
                                            try: 
                                                room_in_roof_details.add_common_wall_u_value_1().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('common_wall_u_value_1'))
                                            except KeyError: pass

                                            # Common-Wall-Length-2
                                            try: 
                                                room_in_roof_details.add_common_wall_length_2().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('common_wall_length_2'))
                                            except KeyError: pass

                                            # Common-Wall-Height-2
                                            try: 
                                                room_in_roof_details.add_common_wall_height_2().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('common_wall_height_2'))
                                            except KeyError: pass

                                            # Common-Wall-U-Value-2
                                            try: 
                                                room_in_roof_details.add_common_wall_u_value_2().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'].pop('common_wall_u_value_2'))
                                            except KeyError: pass

                                            #
                                            if len(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details']) == 0:
                                                del j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details']
                                            else:
                                                raise Exception('j', 'data', 'sap_building_parts', sap_building_part_index, 'sap_room_in_roof', 'room_in_roof_details',
                                                                list(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_details'])[0])
                                            

                                    if True:
                                        # --- Room-In-Roof-Type-1 ---
                                        if 'room_in_roof_type_1' in j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']:
                                            room_in_roof_type_1 = sap_room_in_roof.add_room_in_roof_type_1()

                                            # Gable-Wall-Length-1
                                            try: 
                                                room_in_roof_type_1.add_gable_wall_length_1().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_type_1'].pop('gable_wall_length_1'))
                                            except KeyError: pass

                                            # Gable-Wall-Type-1
                                            try: 
                                                room_in_roof_type_1.add_gable_wall_type_1().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_type_1'].pop('gable_wall_type_1'))
                                            except KeyError: pass

                                            # Gable-Wall-Length-2
                                            try: 
                                                room_in_roof_type_1.add_gable_wall_length_2().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_type_1'].pop('gable_wall_length_2'))
                                            except KeyError: pass

                                            # Gable-Wall-Type-2
                                            try: 
                                                room_in_roof_type_1.add_gable_wall_type_2().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_type_1'].pop('gable_wall_type_2'))
                                            except KeyError: pass

                                            #
                                            if len(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_type_1']) == 0:
                                                del j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_type_1']
                                            else:
                                                raise Exception('j', 'data', 'sap_building_parts', sap_building_part_index, 'sap_room_in_roof', 'room_in_roof_type_1',
                                                                list(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_type_1'])[0])
                                            
                                    if True:
                                        # --- Room-In-Roof-Type-2 ---
                                        if 'room_in_roof_type_2' in j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']:
                                            room_in_roof_type_2 = sap_room_in_roof.add_room_in_roof_type_2()

                                            # Gable-Wall-Length-1
                                            try: 
                                                room_in_roof_type_2.add_gable_wall_length_1().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_type_2'].pop('gable_wall_length_1'))
                                            except KeyError: pass

                                            # Gable-Wall-Height-1
                                            try: 
                                                room_in_roof_type_2.add_gable_wall_height_1().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_type_2'].pop('gable_wall_height_1'))
                                            except KeyError: pass

                                            # Gable-Wall-Type-1
                                            try: 
                                                room_in_roof_type_2.add_gable_wall_type_1().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_type_2'].pop('gable_wall_type_1'))
                                            except KeyError: pass

                                            # Gable-Wall-Length-2
                                            try: 
                                                room_in_roof_type_2.add_gable_wall_length_2().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_type_2'].pop('gable_wall_length_2'))
                                            except KeyError: pass

                                            # Gable-Wall-Height-2
                                            try: 
                                                room_in_roof_type_2.add_gable_wall_height_2().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_type_2'].pop('gable_wall_height_2'))
                                            except KeyError: pass

                                            # Gable-Wall-Type-2
                                            try: 
                                                room_in_roof_type_2.add_gable_wall_type_2().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_type_2'].pop('gable_wall_type_2'))
                                            except KeyError: pass

                                            # Common-Wall-Length-1
                                            try: 
                                                room_in_roof_type_2.add_common_wall_length_1().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_type_2'].pop('common_wall_length_1'))
                                            except KeyError: pass

                                            # Common-Wall-Height-1
                                            try: 
                                                room_in_roof_type_2.add_common_wall_height_1().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_type_2'].pop('common_wall_height_1'))
                                            except KeyError: pass

                                            # Common-Wall-Length-2
                                            try: 
                                                room_in_roof_type_2.add_common_wall_length_2().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_type_2'].pop('common_wall_length_2'))
                                            except KeyError: pass

                                            # Common-Wall-Height-2
                                            try: 
                                                room_in_roof_type_2.add_common_wall_height_2().code = \
                                                    str(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_type_2'].pop('common_wall_height_2'))
                                            except KeyError: pass

                                            #
                                            if len(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_type_2']) == 0:
                                                del j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_type_2']
                                            else:
                                                raise Exception('j', 'data', 'sap_building_parts', sap_building_part_index, 'sap_room_in_roof', 'room_in_roof_type_2',
                                                                list(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['room_in_roof_type_2'])[0])
                                            
                                    #
                                    if len(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']) == 0:
                                        del j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']
                                    else:
                                        print(etree.tostring(rdsap_report, pretty_print=True).decode())
                                        raise Exception('j', 'data', 'sap_building_parts', sap_building_part_index, 'sap_room_in_roof', 
                                                        list(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof'])[0])


                            if True:
                                # --- SAP-Alternative-Wall-1 ---
                                if 'sap_alternative_wall_1' in j['data']['sap_building_parts'][sap_building_part_index]:
                                    sap_alternative_wall_1 = sap_building_part.add_sap_alternative_wall_1()

                                    # Wall-Construction
                                    try: 
                                        sap_alternative_wall_1.add_wall_construction().code = \
                                            str(j['data']['sap_building_parts'][sap_building_part_index]['sap_alternative_wall_1'].pop('wall_construction'))
                                    except KeyError: pass

                                    # Wall-Insulation-Type
                                    try: 
                                        sap_alternative_wall_1.add_wall_insulation_type().code = \
                                            str(j['data']['sap_building_parts'][sap_building_part_index]['sap_alternative_wall_1'].pop('wall_insulation_type'))
                                    except KeyError: pass

                                    # Wall-Area
                                    try: 
                                        sap_alternative_wall_1.add_wall_area().code = \
                                            str(j['data']['sap_building_parts'][sap_building_part_index]['sap_alternative_wall_1'].pop('wall_area'))
                                    except KeyError: pass

                                    # Wall-Thickness-Measured
                                    try: 
                                        sap_alternative_wall_1.add_wall_thickness_measured().code = \
                                            str(j['data']['sap_building_parts'][sap_building_part_index]['sap_alternative_wall_1'].pop('wall_thickness_measured'))
                                    except KeyError: pass

                                    # Wall-Thickness
                                    try: 
                                        sap_alternative_wall_1.add_wall_thickness().code = \
                                            str(j['data']['sap_building_parts'][sap_building_part_index]['sap_alternative_wall_1'].pop('wall_thickness'))
                                    except KeyError: pass

                                    # Wall-U-Value
                                    try: 
                                        sap_alternative_wall_1.add_wall_u_value().code = \
                                            str(j['data']['sap_building_parts'][sap_building_part_index]['sap_alternative_wall_1'].pop('wall_u_value'))
                                    except KeyError: pass

                                    # Wall-Insulation-Thickness
                                    try: 
                                        sap_alternative_wall_1.add_wall_insulation_thickness().code = \
                                            str(j['data']['sap_building_parts'][sap_building_part_index]['sap_alternative_wall_1'].pop('wall_insulation_thickness'))
                                    except KeyError: pass

                                    # Wall-Insulation-Thickness-Measured
                                    try: 
                                        sap_alternative_wall_1.add_wall_insulation_thickness_measured().code = \
                                            str(j['data']['sap_building_parts'][sap_building_part_index]['sap_alternative_wall_1'].pop('wall_insulation_thickness_measured'))
                                    except KeyError: pass

                                    # Wall-Insulation-Thermal-Conductivity
                                    try: 
                                        sap_alternative_wall_1.add_wall_insulation_thermal_conductivity().code = \
                                            str(j['data']['sap_building_parts'][sap_building_part_index]['sap_alternative_wall_1'].pop('wall_insulation_thermal_conductivity'))
                                    except KeyError: pass

                                    # Wall-Dry-Lined
                                    try: 
                                        sap_alternative_wall_1.add_wall_dry_lined().code = \
                                            str(j['data']['sap_building_parts'][sap_building_part_index]['sap_alternative_wall_1'].pop('wall_dry_lined'))
                                    except KeyError: pass

                                    # Sheltered-Wall
                                    try: 
                                        sap_alternative_wall_1.add_sheltered_wall().code = \
                                            str(j['data']['sap_building_parts'][sap_building_part_index]['sap_alternative_wall_1'].pop('sheltered_wall'))
                                    except KeyError: pass

                                    #
                                    if len(j['data']['sap_building_parts'][sap_building_part_index]['sap_alternative_wall_1']) == 0:
                                        del j['data']['sap_building_parts'][sap_building_part_index]['sap_alternative_wall_1']
                                    else:
                                        print(etree.tostring(rdsap_report, pretty_print=True).decode())
                                        raise Exception('j', 'data', 'sap_building_parts', sap_building_part_index, 'sap_alternative_wall_1', 
                                                        list(j['data']['sap_building_parts'][sap_building_part_index]['sap_alternative_wall_1'])[0])


                            if True:
                                # --- SAP-Alternative-Wall-2 ---
                                if 'sap_alternative_wall_2' in j['data']['sap_building_parts'][sap_building_part_index]:
                                    sap_alternative_wall_2 = sap_building_part.add_sap_alternative_wall_2()

                                    # Wall-Construction
                                    try: 
                                        sap_alternative_wall_2.add_wall_construction().code = \
                                            str(j['data']['sap_building_parts'][sap_building_part_index]['sap_alternative_wall_2'].pop('wall_construction'))
                                    except KeyError: pass

                                    # Wall-Insulation-Type
                                    try: 
                                        sap_alternative_wall_2.add_wall_insulation_type().code = \
                                            str(j['data']['sap_building_parts'][sap_building_part_index]['sap_alternative_wall_2'].pop('wall_insulation_type'))
                                    except KeyError: pass

                                    # Wall-Area
                                    try: 
                                        sap_alternative_wall_2.add_wall_area().code = \
                                            str(j['data']['sap_building_parts'][sap_building_part_index]['sap_alternative_wall_2'].pop('wall_area'))
                                    except KeyError: pass

                                    # Wall-Thickness-Measured
                                    try: 
                                        sap_alternative_wall_2.add_wall_thickness_measured().code = \
                                            str(j['data']['sap_building_parts'][sap_building_part_index]['sap_alternative_wall_2'].pop('wall_thickness_measured'))
                                    except KeyError: pass

                                    # Wall-Insulation-Thermal-Conductivity
                                    try: 
                                        sap_alternative_wall_2.add_wall_insulation_thermal_conductivity().code = \
                                            str(j['data']['sap_building_parts'][sap_building_part_index]['sap_alternative_wall_2'].pop('wall_insulation_thermal_conductivity'))
                                    except KeyError: pass

                                    # Wall-Thickness
                                    try: 
                                        sap_alternative_wall_2.add_wall_thickness().code = \
                                            str(j['data']['sap_building_parts'][sap_building_part_index]['sap_alternative_wall_2'].pop('wall_thickness'))
                                    except KeyError: pass

                                    # Wall-Insulation-Thickness
                                    try: 
                                        sap_alternative_wall_2.add_wall_insulation_thickness().code = \
                                            str(j['data']['sap_building_parts'][sap_building_part_index]['sap_alternative_wall_2'].pop('wall_insulation_thickness'))
                                    except KeyError: pass

                                    # Wall-Insulation-Thickness-Measured
                                    try: 
                                        sap_alternative_wall_2.add_wall_insulation_thickness_measured().code = \
                                            str(j['data']['sap_building_parts'][sap_building_part_index]['sap_alternative_wall_2'].pop('wall_insulation_thickness_measured'))
                                    except KeyError: pass

                                    # Wall-Dry-Lined
                                    try: 
                                        sap_alternative_wall_2.add_wall_dry_lined().code = \
                                            str(j['data']['sap_building_parts'][sap_building_part_index]['sap_alternative_wall_2'].pop('wall_dry_lined'))
                                    except KeyError: pass

                                    # Sheltered-Wall
                                    try: 
                                        sap_alternative_wall_2.add_sheltered_wall().code = \
                                            str(j['data']['sap_building_parts'][sap_building_part_index]['sap_alternative_wall_2'].pop('sheltered_wall'))
                                    except KeyError: pass

                                    #
                                    if len(j['data']['sap_building_parts'][sap_building_part_index]['sap_alternative_wall_2']) == 0:
                                        del j['data']['sap_building_parts'][sap_building_part_index]['sap_alternative_wall_2']
                                    else:
                                        print(etree.tostring(rdsap_report, pretty_print=True).decode())
                                        raise Exception('j', 'data', 'sap_building_parts', sap_building_part_index, 'sap_alternative_wall_2', 
                                                        list(j['data']['sap_building_parts'][sap_building_part_index]['sap_alternative_wall_2'])[0])

                            # Party-Wall-Construction
                            try: 
                                sap_building_part.add_party_wall_construction().code = str(j['data']['sap_building_parts'][sap_building_part_index].pop('party_wall_construction'))
                            except KeyError: pass

                        else:
                            # --- SAP-Integral-Conservatory ---
                            sap_integral_conservatory = sap_building_parts.add_sap_integral_conservatory()

                            # Double-Glazed
                            try: 
                                sap_integral_conservatory.add_double_glazed().code = str(j['data']['sap_building_parts'][sap_building_part_index].pop('double_glazed'))
                            except KeyError: pass

                            # Floor-Area
                            try: 
                                sap_integral_conservatory.add_floor_area().code = str(j['data']['sap_building_parts'][sap_building_part_index].pop('floor_area'))
                            except KeyError: pass

                            # Room-Height
                            try: 
                                sap_integral_conservatory.add_room_height().code = str(j['data']['sap_building_parts'][sap_building_part_index].pop('room_height'))
                            except KeyError: pass

                            # Glazed-Perimeter
                            try: 
                                sap_integral_conservatory.add_glazed_perimeter().code = str(j['data']['sap_building_parts'][sap_building_part_index].pop('glazed_perimeter'))
                            except KeyError: pass

                        #
                        if len(j['data']['sap_building_parts'][sap_building_part_index]) == 0:
                            c.append(sap_building_part_index)
                        else:
                            print(etree.tostring(rdsap_report, pretty_print=True).decode())
                            raise Exception('j', 'data', 'sap_building_parts', sap_building_part_index, list(j['data']['sap_building_parts'][sap_building_part_index])[0])
                    for c1 in c[::-1]: del j['data']['sap_building_parts'][c1]
                    if len(j['data']['sap_building_parts']) == 0: del j['data']['sap_building_parts']

            if True:
                # --- SAP-Flat-Details ---
                if 'sap_flat_details' in j['data']:
                    sap_flat_details = sap_property_details.add_sap_flat_details()

                    # Flat-Location
                    try: 
                        code = str(j['data']['sap_flat_details'].pop('flat_location'))
                        if len(str(code)) == 1: code = f'0{code}'  # left padding zeros
                        sap_flat_details.add_flat_location().code = code
                    except KeyError: pass

                    # Storey-Count
                    try: 
                        sap_flat_details.add_storey_count().code = str(j['data']['sap_flat_details'].pop('storey_count'))
                    except KeyError: pass

                    # Level
                    try: 
                        sap_flat_details.add_level().code = str(j['data']['sap_flat_details'].pop('level'))
                    except KeyError: pass

                    # Top-Storey
                    try: 
                        sap_flat_details.add_top_storey().code = str(j['data']['sap_flat_details'].pop('top_storey'))
                    except KeyError: pass

                    # Heat-Loss-Corridor
                    try: 
                        sap_flat_details.add_heat_loss_corridor().code = str(j['data']['sap_flat_details'].pop('heat_loss_corridor'))
                    except KeyError: pass

                    # Unheated-Corridor-Length
                    try: 
                        sap_flat_details.add_unheated_corridor_length().code = str(j['data']['sap_flat_details'].pop('unheated_corridor_length'))
                    except KeyError: pass

                    if len(j['data']['sap_flat_details']) == 0:
                        del j['data']['sap_flat_details']
                    else:
                        raise Exception('j', 'data', 'sap_flat_details', list(j['data']['sap_flat_details'])[0])

            if True:
                # --- SAP-Windows ---
                if 'sap_windows' in j['data']:
                    sap_windows = sap_property_details.add_sap_windows()
                    c = []
                    for sap_window_index in range(len(j['data']['sap_windows'])):

                        # --- SAP-Window ---
                        sap_window = sap_windows.add_sap_window()

                        # Window-Location
                        try: 
                            sap_window.add_window_location().code = str(j['data']['sap_windows'][sap_window_index].pop('window_location'))
                        except KeyError: pass

                        # Window-Height
                        try: 
                            sap_window.add_window_height().code = str(j['data']['sap_windows'][sap_window_index].pop('window_height'))
                        except KeyError: pass


                        # Window-Width
                        try: 
                            sap_window.add_window_width().code = str(j['data']['sap_windows'][sap_window_index].pop('window_width'))
                        except KeyError: pass

                        # Draught-Proofed
                        try: 
                            sap_window.add_draught_proofed().code = str(j['data']['sap_windows'][sap_window_index].pop('draught_proofed'))
                        except KeyError: pass

                        # Glazing-Type
                        try: 
                            sap_window.add_glazing_type().code = str(j['data']['sap_windows'][sap_window_index].pop('glazing_type'))
                        except KeyError: pass

                        # Window-Type
                        try: 
                            sap_window.add_window_type().code = str(j['data']['sap_windows'][sap_window_index].pop('window_type'))
                        except KeyError: pass

                        # Orientation
                        try: 
                            sap_window.add_orientation().code = str(j['data']['sap_windows'][sap_window_index].pop('orientation'))
                        except KeyError: pass
                        
                        if True:
                            # --- Window-Transmission-Details ---
                            if 'window_transmission_details' in j['data']['sap_windows'][sap_window_index]:
                                window_transmission_details = sap_window.add_window_transmission_details()

                                # Data-Source
                                try: 
                                    window_transmission_details.add_data_source().code = str(j['data']['sap_windows'][sap_window_index]['window_transmission_details'].pop('data_source'))
                                except KeyError: pass

                                # U-Value
                                try: 
                                    window_transmission_details.add_u_value().code = str(j['data']['sap_windows'][sap_window_index]['window_transmission_details'].pop('u_value'))
                                except KeyError: pass

                                # Solar-Transmittance
                                try: 
                                    window_transmission_details.add_solar_transmittance().code = str(j['data']['sap_windows'][sap_window_index]['window_transmission_details'].pop('solar_transmittance'))
                                except KeyError: pass

                                #
                                if len(j['data']['sap_windows'][sap_window_index]['window_transmission_details']) == 0:
                                    del j['data']['sap_windows'][sap_window_index]['window_transmission_details']
                                else:
                                    raise Exception('j', 'data', 'sap_windows', sap_window_index, 'window_transmission_details', 
                                                    list(j['data']['sap_windows'][sap_window_index]['window_transmission_details'])[0])
    
                        # PVC-Frame
                        try: 
                            sap_window.add_pvc_frame().code = str(j['data']['sap_windows'][sap_window_index].pop('pvc_frame'))
                        except KeyError: pass

                        # Glazing-Gap
                        try: 
                            sap_window.add_glazing_gap().code = str(j['data']['sap_windows'][sap_window_index].pop('glazing_gap'))
                        except KeyError: pass

                        # Frame-Factor
                        try: 
                            sap_window.add_frame_factor().code = str(j['data']['sap_windows'][sap_window_index].pop('frame_factor'))
                        except KeyError: pass
    
                        # Window-Wall-Type
                        try: 
                            sap_window.add_window_wall_type().code = str(j['data']['sap_windows'][sap_window_index].pop('window_wall_type'))
                        except KeyError: pass
    
                        # Permenant-Shutters-Present
                        try: 
                            sap_window.add_permanent_shutters_present().code = str(j['data']['sap_windows'][sap_window_index].pop('permanent_shutters_present'))
                        except KeyError: pass

                        # Permenant-Shutters-Insulated
                        try: 
                            sap_window.add_permanent_shutters_insulated().code = str(j['data']['sap_windows'][sap_window_index].pop('permanent_shutters_insulated'))
                        except KeyError: pass

                        if len(j['data']['sap_windows'][sap_window_index]) == 0:
                            c.append(sap_window_index)
                        else:
                            print(etree.tostring(rdsap_report, pretty_print=True).decode())
                            raise Exception('j', 'data', 'sap_windows', sap_window_index, list(j['data']['sap_windows'][sap_window_index])[0])
                    for c1 in c[::-1]: del j['data']['sap_windows'][c1]
                    if len(j['data']['sap_windows']) == 0: del j['data']['sap_windows']

            if True:
                # --- SAP-Deselected-Improvements ---
                if 'sap_deselected_improvements' in j['data']:
                    sap_deselected_improvements = sap_property_details.add_sap_deselected_improvements()
                    for code in j['data']['sap_deselected_improvements']:
                        sap_deselected_improvements.add_deselected_improvement_measure().code = str(code)
                    del j['data']['sap_deselected_improvements']

            # Door-Count
            try: 
                sap_property_details.add_door_count().code = str(j['data'].pop('door_count'))
            except KeyError: pass  

            # Insulated-Door-Count
            try: 
                sap_property_details.add_insulated_door_count().code = str(j['data'].pop('insulated_door_count'))
            except KeyError: pass  

            # Insulated-Door-U-Value
            try: 
                sap_property_details.add_insulated_door_u_value().code = str(j['data'].pop('insulated_door_u_value'))
            except KeyError: pass  

            # Draughtproofed-Door-Count
            try: 
                sap_property_details.add_draughtproofed_door_count().code = str(j['data'].pop('draughtproofed_door_count'))
            except KeyError: pass  

            # Percent-Draughtproofed
            try: 
                sap_property_details.add_percent_draughtproofed().code = str(j['data'].pop('percent_draughtproofed'))
            except KeyError: pass  
    
            if True:
                # --- SAP-Special-Features ---
                if 'sap_special_features' in j['data']:
                    sap_special_features = sap_property_details.add_sap_special_features()
                    sap_special_features_c = []
                    for sap_special_feature_index in range(len(j['data']['sap_special_features'])):

                        if True:
                            # --- SAP-Special-Feature ---
                            sap_special_feature = sap_special_features.add_sap_special_feature()

                            # Description
                            try: 
                                sap_special_feature.add_description().code = str(j['data']['sap_special_features'][sap_special_feature_index].pop('description'))
                            except KeyError: pass
                        
                            if True:
                                # --- Energy-Feature
                                if 'energy_feature' in j['data']['sap_special_features'][sap_special_feature_index]:
                                    energy_feature = sap_special_feature.add_energy_feature()

                                    # Energy-Saved-Or-Generated
                                    try: 
                                        energy_feature.add_energy_saved_or_generated().code = str(j['data']['sap_special_features'][sap_special_feature_index]['energy_feature'].pop('energy_saved_or_generated'))
                                    except KeyError: pass

                                    # Saved-Or-Generated-Fuel
                                    try: 
                                        energy_feature.add_saved_or_generated_fuel().code = str(j['data']['sap_special_features'][sap_special_feature_index]['energy_feature'].pop('saved_or_generated_fuel'))
                                    except KeyError: pass

                                    # Energy-Used
                                    try: 
                                        energy_feature.add_energy_used().code = str(j['data']['sap_special_features'][sap_special_feature_index]['energy_feature'].pop('energy_used'))
                                    except KeyError: pass

                                    # Energy-Used-Fuel
                                    try: 
                                        energy_feature.add_energy_used_fuel().code = str(j['data']['sap_special_features'][sap_special_feature_index]['energy_feature'].pop('energy_used_fuel'))
                                    except KeyError: pass

                                    #
                                    if len(j['data']['sap_special_features'][sap_special_feature_index]['energy_feature']) == 0:
                                        del j['data']['sap_special_features'][sap_special_feature_index]['energy_feature']
                                    else:
                                        print(etree.tostring(rdsap_report, pretty_print=True).decode())
                                        raise Exception('j', 'data', 'sap_special_features', sap_special_feature_index, 'energy_feature', 
                                                        list(j['data']['sap_special_features'][sap_special_feature_index]['energy_feature'])[0])

                            if True:
                                # --- Emissions-Feature
                                if 'emissions_feature' in j['data']['sap_special_features'][sap_special_feature_index]:
                                    emissions_feature = sap_special_feature.add_emissions_feature()

                                    # Emissions-Saved
                                    try: 
                                        emissions_feature.add_emissions_saved().code = str(j['data']['sap_special_features'][sap_special_feature_index]['emissions_feature'].pop('emissions_saved'))
                                    except KeyError: pass

                                    # Emissions-Created
                                    try: 
                                        emissions_feature.add_emissions_created().code = str(j['data']['sap_special_features'][sap_special_feature_index]['emissions_feature'].pop('emissions_created'))
                                    except KeyError: pass

                                    #
                                    if len(j['data']['sap_special_features'][sap_special_feature_index]['emissions_feature']) == 0:
                                        del j['data']['sap_special_features'][sap_special_feature_index]['emissions_feature']
                                    else:
                                        print(etree.tostring(rdsap_report, pretty_print=True).decode())
                                        raise Exception('j', 'data', 'sap_special_features', sap_special_feature_index, 'emissions_feature', 
                                                        list(j['data']['sap_special_features'][sap_special_feature_index]['emissions_feature'])[0])

                            #
                            if len(j['data']['sap_special_features'][sap_special_feature_index]) == 0:
                                sap_special_features_c.append(sap_special_feature_index)
                            else:
                                print(etree.tostring(rdsap_report, pretty_print=True).decode())
                                raise Exception('j', 'data', 'sap_special_features', sap_special_feature_index, list(j['data']['sap_special_features'][sap_special_feature_index])[0])
        
                    for c1 in sap_special_features_c[::-1]: del j['data']['sap_special_features'][c1]
                    if len(j['data']['sap_special_features']) == 0: del j['data']['sap_special_features']

    if True:
        # --- Report-Header ---
        report_header = rdsap_report.add_report_header()

        # Inspection-Date
        try: 
            report_header.add_inspection_date().code = str(j['data'].pop('inspection_date'))
        except KeyError: pass

        # Report-Type
        try: 
            report_header.add_report_type().code = str(j['data'].pop('report_type'))
        except KeyError: pass

        # Completion-Date
        try: 
            report_header.add_completion_date().code = str(j['data'].pop('completion_date'))
        except KeyError: pass
    
        # Registration-Date
        try: 
            report_header.add_registration_date().code = str(j['data'].pop('registration_date'))
        except KeyError: pass

        # Status
        try: 
            report_header.add_status().code = str(j['data'].pop('status'))
        except KeyError: pass
        
        # Language-Code
        try: 
            report_header.add_language_code().code = str(j['data'].pop('language_code'))
        except KeyError: pass
    
        # Property-Type
        try: 
            report_header.add_property_type().code = sap_property_details.property_type.code
        except KeyError: pass
    
        # Region-Code
        try: 
            report_header.add_region_code().code = str(j['data'].pop('region_code'))
        except KeyError: pass
    
        # Country-Code
        try: 
            report_header.add_country_code().code = str(j['data'].pop('country_code'))
        except KeyError: pass
    
        # Transaction-Type
        try: 
            report_header.add_transaction_type().code = str(j['data'].pop('transaction_type'))
        except KeyError: pass

        # Tenure
        try: 
            report_header.add_tenure().code = str(j['data'].pop('tenure'))
        except KeyError: pass

        if True: 
            # --- Property ---
            property_ = report_header.add_property_()

            if True:
                # --- Address ---
                address = property_.add_address()

                # Address-Line-1
                try: 
                    address.add_address_line_1().code = str(j['data'].pop('address_line_1'))
                except KeyError: pass
   
                # Address-Line-2
                try: 
                    address.add_address_line_2().code = str(j['data'].pop('address_line_2'))
                except KeyError: pass
    
                # Address-Line-3
                try: 
                    address.add_address_line_3().code = str(j['data'].pop('address_line_3'))
                except KeyError: pass
    
                # Postcode
                try: 
                    address.add_postcode().code = str(j['data'].pop('postcode'))
                except KeyError: pass

                # Post-Town
                try: 
                    address.add_post_town().code = str(j['data'].pop('post_town'))
                except KeyError: pass
    
            # UPRN
            try: 
                property_.add_uprn().code = str(j['data'].pop('uprn'))
            except KeyError: pass

    if len(j['data']) == 0:
        del j['data']
    else:
        print(etree.tostring(rdsap_report, pretty_print=True).decode())
        raise Exception('j', 'data', list(j['data'])[0])

    if len(j) > 0:
        raise Exception('j', list(j)[0])

    return tree, rdsap_report

    