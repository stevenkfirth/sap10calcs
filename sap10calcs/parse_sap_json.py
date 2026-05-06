


from lxml import etree
import json
from .instances import SAP_Schema_19_2_0_parser
from io import StringIO, BytesIO
import copy


def parse_sap_json(
    input_file,
    input_json = None
):
    """ Parses a SAP json file and returns an SAP XML file.

    input file  - filepath to json file (downloaded from get_energy_data API)
    
    :returns: A two-item tuple containing an `lxml ElementTree <https://lxml.de/tutorial.html>`__ and the root node of the XML file (a `SAP-Report <https://stevenkfirth.github.io/sap10calcs/sap_schema_19_2_0.html#rdsap-report>`__ element).
    :rtype: (`lxml.etree.ElementTree <https://lxml.de/tutorial.html#the-elementtree-class>`__, :py:class:`sap10calcs.classes_SAP_Schema_19_2_0.SAP_Report`)

    
    """

    # load json
    if not input_json is None:
        j0 = input_json
    with open(input_file) as f:
        j0 = json.load(f)
    j = copy.deepcopy(j0)

    if not 'data' in j:
        raise Exception('No "data" key in root json.')
    #if not j['data'].get('schema_type') == 'RdSAP-Schema-19.2.0':
    #    raise Exception(f'SAP schema not equal to "SAP-Schema-19.2.0" ({j['data'].get('schema_type')})')

    # # normalise json
    # # - lists
    # if 'data' in j:
    #     if 'roofs' in j['data'] and not isinstance(j['data']['roofs'], list): j['data']['roofs'] = [j['data']['roofs']]
    #     if 'walls' in j['data'] and not isinstance(j['data']['walls'], list): j['data']['walls'] = [j['data']['walls']]
    #     if 'floors' in j['data'] and not isinstance(j['data']['floors'], list): j['data']['floors'] = [j['data']['floors']]
    #     if 'main_heating' in j['data'] and not isinstance(j['data']['main_heating'], list): j['data']['main_heating'] = [j['data']['main_heating']]
    #     if 'addendum' in j['data'] and 'addendum_numbers' in j['data']['addendum'] and not isinstance(j['data']['addendum']['addendum_numbers'], list): 
    #         j['data']['addendum']['addendum_numbers'] = [j['data']['addendum']['addendum_numbers']]
    #     if 'sap_heating' in j['data'] and 'shower_outlets' in j['data']['sap_heating'] and not isinstance(j['data']['sap_heating']['shower_outlets'], list): 
    #         j['data']['sap_heating']['shower_outlets'] = [j['data']['sap_heating']['shower_outlets']]
    #     if 'sap_heating' in j['data'] and 'main_heating_details' in j['data']['sap_heating'] and not isinstance(j['data']['sap_heating']['main_heating_details'], list): 
    #         j['data']['sap_heating']['main_heating_details'] = [j['data']['sap_heating']['main_heating_details']]
    #     if 'sap_windows' in j['data'] and not isinstance(j['data']['sap_windows'], list): j['data']['sap_windows'] = [j['data']['sap_windows']]
    #     if 'lzc_energy_sources' in j['data'] and not isinstance(j['data']['lzc_energy_sources'], list): j['data']['lzc_energy_sources'] = [j['data']['lzc_energy_sources']]
    #     if 'sap_building_parts' in j['data'] and not isinstance(j['data']['sap_building_parts'], list): j['data']['sap_building_parts'] = [j['data']['sap_building_parts']]
    #     if 'suggested_improvements' in j['data'] and not isinstance(j['data']['suggested_improvements'], list): j['data']['suggested_improvements'] = [j['data']['suggested_improvements']]
    #     if 'alternative_improvements' in j['data'] and not isinstance(j['data']['alternative_improvements'], list): j['data']['alternative_improvements'] = [j['data']['alternative_improvements']]
    #     if 'sap_energy_source' in j['data'] and 'pv_batteries' in j['data']['sap_energy_source'] and not isinstance(j['data']['sap_energy_source']['pv_batteries'], list):
    #         j['data']['sap_energy_source']['pv_batteries'] = [j['data']['sap_energy_source']['pv_batteries']]

    # # - removing unneeded keys
    #     if 'sap_heating' in j['data'] and 'shower_outlets' in j['data']['sap_heating']:
    #         for shower_outlet_index in range(len(j['data']['sap_heating']['shower_outlets'])):
    #             if 'shower_outlet' in j['data']['sap_heating']['shower_outlets'][shower_outlet_index]:
    #                 j['data']['sap_heating']['shower_outlets'][shower_outlet_index] = j['data']['sap_heating']['shower_outlets'][shower_outlet_index].pop('shower_outlet')
    #     if 'alternative_improvements' in j['data']:
    #         for alternative_improvement_index in range(len(j['data']['alternative_improvements'])):
    #             if 'improvement' in j['data']['alternative_improvements'][alternative_improvement_index]:
    #                 j['data']['alternative_improvements'][alternative_improvement_index] = j['data']['alternative_improvements'][alternative_improvement_index].pop('improvement')
    # # - values
    #     if 'sap_windows' in j['data']:
    #         for sap_window_index in range(len(j['data']['sap_windows'])):
    #             if 'window_height' in j['data']['sap_windows'][sap_window_index] and isinstance(j['data']['sap_windows'][sap_window_index]['window_height'], dict):
    #                 j['data']['sap_windows'][sap_window_index]['window_height'] = j['data']['sap_windows'][sap_window_index]['window_height']['value']
    #             if 'window_width' in j['data']['sap_windows'][sap_window_index] and isinstance(j['data']['sap_windows'][sap_window_index]['window_width'], dict):
    #                 j['data']['sap_windows'][sap_window_index]['window_width'] = j['data']['sap_windows'][sap_window_index]['window_width']['value']
    #     if 'sap_building_parts' in j['data']:
    #         for sap_building_part_index in range(len(j['data']['sap_building_parts'])):
    #             if ('floor_area' in j['data']['sap_building_parts'][sap_building_part_index] 
    #                 and isinstance(j['data']['sap_building_parts'][sap_building_part_index]['floor_area'], dict)):
    #                 j['data']['sap_building_parts'][sap_building_part_index]['floor_area'] = \
    #                     j['data']['sap_building_parts'][sap_building_part_index]['floor_area']['value']
    #             if ('glazed_perimeter' in j['data']['sap_building_parts'][sap_building_part_index] 
    #                 and isinstance(j['data']['sap_building_parts'][sap_building_part_index]['glazed_perimeter'], dict)):
    #                 j['data']['sap_building_parts'][sap_building_part_index]['glazed_perimeter'] = \
    #                     j['data']['sap_building_parts'][sap_building_part_index]['glazed_perimeter']['value']  
    #             if 'sap_room_in_roof' in j['data']['sap_building_parts'][sap_building_part_index]: 
    #                 if 'floor_area' in j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']:
    #                     if isinstance(j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['floor_area'], dict):
    #                         j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['floor_area'] = j['data']['sap_building_parts'][sap_building_part_index]['sap_room_in_roof']['floor_area']['value']
    #             if 'sap_floor_dimensions' in j['data']['sap_building_parts'][sap_building_part_index]:
    #                 for sap_floor_dimension_index in range(len(j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'])):
    #                     if ('heat_loss_perimeter' in j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index] 
    #                         and isinstance(j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index]['heat_loss_perimeter'], dict)):
    #                         j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index]['heat_loss_perimeter'] = \
    #                             j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index]['heat_loss_perimeter']['value']
    #                     if ('room_height' in j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index] 
    #                         and isinstance(j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index]['room_height'], dict)):
    #                         j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index]['room_height'] = \
    #                             j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index]['room_height']['value']
    #                     if ('total_floor_area' in j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index] 
    #                         and isinstance(j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index]['total_floor_area'], dict)):
    #                         j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index]['total_floor_area'] = \
    #                             j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index]['total_floor_area']['value']
    #                     if ('party_wall_length' in j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index] 
    #                         and isinstance(j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index]['party_wall_length'], dict)):
    #                         j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index]['party_wall_length'] = \
    #                             j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index]['party_wall_length']['value']
    #     if 'heating_cost_current' in j['data'] and isinstance(j['data']['heating_cost_current'], dict): j['data']['heating_cost_current'] = j['data']['heating_cost_current']['value']
    #     if 'heating_cost_potential' in j['data'] and isinstance(j['data']['heating_cost_potential'], dict): j['data']['heating_cost_potential'] = j['data']['heating_cost_potential']['value']
    #     if 'lighting_cost_current' in j['data'] and isinstance(j['data']['lighting_cost_current'], dict): j['data']['lighting_cost_current'] = j['data']['lighting_cost_current']['value']
    #     if 'lighting_cost_potential' in j['data'] and isinstance(j['data']['lighting_cost_potential'], dict): j['data']['lighting_cost_potential'] = j['data']['lighting_cost_potential']['value']
    #     if 'hot_water_cost_current' in j['data'] and isinstance(j['data']['hot_water_cost_current'], dict): j['data']['hot_water_cost_current'] = j['data']['hot_water_cost_current']['value']
    #     if 'hot_water_cost_potential' in j['data'] and isinstance(j['data']['hot_water_cost_potential'], dict): j['data']['hot_water_cost_potential'] = j['data']['hot_water_cost_potential']['value']
    #     if 'sap_flat_details' in j['data'] and 'unheated_corridor_length' in j['data']['sap_flat_details']:
    #         if isinstance(j['data']['sap_flat_details']['unheated_corridor_length'], dict): 
    #             j['data']['sap_flat_details']['unheated_corridor_length'] = j['data']['sap_flat_details']['unheated_corridor_length']['value']

    # # - other
    #     if 'sap_energy_source' in j['data'] and 'photovoltaic_supply' in j['data']['sap_energy_source'] and isinstance(j['data']['sap_energy_source']['photovoltaic_supply'], list):
    #         j['data']['sap_energy_source']['photovoltaic_supply'] = {'pv_arrays': j['data']['sap_energy_source']['photovoltaic_supply']}
    #     if 'sap_energy_source' in j['data'] and 'photovoltaic_supply' in j['data']['sap_energy_source'] and 'pv_arrays' in j['data']['sap_energy_source']['photovoltaic_supply']:
    #         for pv_array_index in range(len(j['data']['sap_energy_source']['photovoltaic_supply']['pv_arrays'])):
    #             if isinstance(j['data']['sap_energy_source']['photovoltaic_supply']['pv_arrays'][pv_array_index], list):
    #                 if len(j['data']['sap_energy_source']['photovoltaic_supply']['pv_arrays'][pv_array_index]) == 1:
    #                     j['data']['sap_energy_source']['photovoltaic_supply']['pv_arrays'][pv_array_index] = j['data']['sap_energy_source']['photovoltaic_supply']['pv_arrays'][pv_array_index][0]
    #                 else:
    #                     raise Exception
    #             if 'peak_power' in j['data']['sap_energy_source']['photovoltaic_supply']['pv_arrays'][pv_array_index]:
    #                 if isinstance(j['data']['sap_energy_source']['photovoltaic_supply']['pv_arrays'][pv_array_index]['peak_power'], dict):
    #                     j['data']['sap_energy_source']['photovoltaic_supply']['pv_arrays'][pv_array_index]['peak_power'] = j['data']['sap_energy_source']['photovoltaic_supply']['pv_arrays'][pv_array_index]['peak_power']['value']
    #     if 'sap_energy_source' in j['data'] and 'pv_batteries' in j['data']['sap_energy_source']:
    #         for pv_battery_index in range(len(j['data']['sap_energy_source']['pv_batteries'])):
    #             if not 'pv_battery' in j['data']['sap_energy_source']['pv_batteries'][pv_battery_index]:
    #                 j['data']['sap_energy_source']['pv_batteries'][pv_battery_index] = {'pv_battery': j['data']['sap_energy_source']['pv_batteries'][pv_battery_index]}
        


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
    <SAP-Report xmlns="https://epbr.digital.communities.gov.uk/xsd/sap">
        <Schema-Version-Original>SAP-Schema-19.1.0</Schema-Version-Original>
        <SAP-Version>10.2</SAP-Version>
    </SAP-Report>"""

    tree = etree.parse(
        StringIO(xml),
        parser = SAP_Schema_19_2_0_parser
        )
    
    # --- RdSAP-Report ---
    sap_report = tree.getroot() 

    # Schema-Version-Original
    try: 
        sap_report.add_schema_version_original().code = str(j['data'].pop('schema_version_original'))
    except KeyError: pass

    # Schema-Version-Current
    # try: 
    #     sap_report.add_schema_version_current().code = str(j['data'].pop('schema_version_current'))
    # except KeyError: pass

    # SAP-Version
    try: 
        sap_report.add_sap_version().code = str(j['data'].pop('sap_version'))
    except KeyError: pass

    # SAP-Data-Version
    try: 
        sap_report.add_sap_data_version().code = str(j['data'].pop('sap_data_version'))
    except KeyError: pass

    # PCDF-Revision-Number

    # Calculation-Software-Name

    # Calculation-Software-Version
    try: 
        sap_report.add_calculation_software_version().code = str(j['data'].pop('calculation_software_version'))
    except KeyError: pass

    # User-Interface-Name
    try: 
        sap_report.add_user_interface_name().code = str(j['data'].pop('user_interface_name'))
    except KeyError: pass
    # User-Interface-Version
    try: 
        sap_report.add_user_interface_version().code = str(j['data'].pop('user_interface_version'))
    except KeyError: pass
    #
    if True:
        # --- Report-Header ---
        report_header = sap_report.add_report_header()

        # RRN

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

        # Tenure
        try: 
            report_header.add_tenure().code = str(j['data'].pop('tenure'))
        except KeyError: pass

        # Transaction-Type
        try: 
            report_header.add_transaction_type().code = str(j['data'].pop('transaction_type'))
        except KeyError: pass

        # Seller-Commission-Report
        try: 
            report_header.add_seller_commission_report().code = str(j['data'].pop('seller_commission_report'))
        except KeyError: pass

        # Property-Type
        try: 
            report_header.add_property_type().code = str(j['data'].pop('property_type'))
        except KeyError: pass

        # Home-Inspector

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

            # Site-Reference
            try: 
                property_.add_site_reference().code = str(j['data'].pop('site_reference'))
            except KeyError: pass

            # Plot-Reference
            try: 
                property_.add_plot_reference().code = str(j['data'].pop('plot_reference'))
            except KeyError: pass

        # Region-Code
        try: 
            report_header.add_region_code().code = str(j['data'].pop('region_code'))
        except KeyError: pass
    
        # Country-Code
        try: 
            report_header.add_country_code().code = str(j['data'].pop('country_code'))
        except KeyError: pass
    
        # Related-Party-Disclosure


    if True:
        # --- Energy-Assessment ---
        energy_assessment = sap_report.add_energy_assessment()

        # Assessment-Date
        try: 
            energy_assessment.add_assessment_date().code = str(j['data'].pop('assessment_date'))
        except KeyError: pass
        
        if True:
            # --- Property-Summary ---
            property_summary = energy_assessment.add_property_summary() 

            if True:
                # --- Walls ---
                if 'walls' in j['data']:
                    c = []
                    for wall_index in range(len(j['data']['walls'])):
                        # 
                        walls = property_summary.add_walls()
                        # Description
                        try: 
                            x = j['data']['walls'][wall_index].pop('description')
                            d = walls.add_description()
                            if isinstance(x, dict):
                                d.code = str(x.get('value',''))
                                d.attrib['language'] = x.get('language', '')
                            else:
                                d.code = str(x)
                        except KeyError: pass
                        # Energy-Efficiency-Rating
                        try: 
                            walls.add_energy_efficiency_rating().code = str(j['data']['walls'][wall_index].pop('energy_efficiency_rating'))
                        except KeyError: pass
                        # Environmental-Efficiency-Rating
                        try: 
                            walls.add_environmental_efficiency_rating().code = str(j['data']['walls'][wall_index].pop('environmental_efficiency_rating'))
                        except KeyError: pass
                        #
                        if len(j['data']['walls'][wall_index]) == 0:
                            c.append(wall_index)
                        else:
                            print(etree.tostring(sap_report, pretty_print=True).decode())
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
                        # Description
                        try: 
                            x = j['data']['roofs'][roof_index].pop('description')
                            d = roof.add_description()
                            if isinstance(x, dict):
                                d.code = str(x.get('value',''))
                                d.attrib['language'] = x.get('language', '')
                            else:
                                d.code = str(x)
                        except KeyError: pass
                        # Energy-Efficiency-Rating
                        try: 
                            roof.add_energy_efficiency_rating().code = str(j['data']['roofs'][roof_index].pop('energy_efficiency_rating'))
                        except KeyError: pass
                        # Environmental-Efficiency-Rating
                        try: 
                            roof.add_environmental_efficiency_rating().code = str(j['data']['roofs'][roof_index].pop('environmental_efficiency_rating'))
                        except KeyError: pass
                        #
                        if len(j['data']['roofs'][roof_index]) == 0:
                            c.append(roof_index)
                        else:
                            print(etree.tostring(sap_report, pretty_print=True).decode())
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
                        # Description
                        try: 
                            x = j['data']['floors'][floor_index].pop('description')
                            d = floor.add_description()
                            if isinstance(x, dict):
                                d.code = str(x.get('value',''))
                                d.attrib['language'] = x.get('language', '')
                            else:
                                d.code = str(x)
                        except KeyError: pass
                        # Energy-Efficiency-Rating
                        try: 
                            floor.add_energy_efficiency_rating().code = str(j['data']['floors'][floor_index].pop('energy_efficiency_rating'))
                        except KeyError: pass
                        # Environmental-Efficiency-Rating
                        try: 
                            floor.add_environmental_efficiency_rating().code = str(j['data']['floors'][floor_index].pop('environmental_efficiency_rating'))
                        except KeyError: pass
                        #
                        if len(j['data']['floors'][floor_index]) == 0:
                            c.append(floor_index)
                        else:
                            print(etree.tostring(sap_report, pretty_print=True).decode())
                            raise Exception('j', 'data', 'floors', floor_index, list(j['data']['floors'][floor_index])[0])
                    for c1 in c[::-1]: del j['data']['floors'][c1]
                    if len(j['data']['floors']) == 0: del j['data']['floors']

            if True:
                # --- Windows ---
                if 'windows' in j['data']:
                    windows = property_summary.add_windows()
                    # Description
                    try: 
                        x = j['data']['windows'].pop('description')
                        d = windows.add_description()
                        if isinstance(x, dict):
                            d.code = str(x.get('value',''))
                            d.attrib['language'] = x.get('language', '')
                        else:
                            d.code = str(x)
                    except KeyError: pass
                    # Energy-Efficiency-Rating
                    try: 
                        windows.add_energy_efficiency_rating().code = str(j['data']['windows'].pop('energy_efficiency_rating'))
                    except KeyError: pass
                    # Environmental-Efficiency-Rating
                    try: 
                        windows.add_environmental_efficiency_rating().code = str(j['data']['windows'].pop('environmental_efficiency_rating'))
                    except KeyError: pass
                    if len(j['data']['windows']) == 0:
                        del j['data']['windows']
                    else:
                        print(etree.tostring(sap_report, pretty_print=True).decode())
                        raise Exception('j', 'data', 'windows', list(j['data']['windows'])[0])
                    
        if True:
            # --- Main-Heating ---
            if 'main_heating' in j['data']:
                c = []
                for main_heating_index in range(len(j['data']['main_heating'])):
                    # 
                    main_heating = property_summary.add_main_heating()
                    # Description
                    try: 
                        x = j['data']['main_heating'][main_heating_index].pop('description')
                        d = main_heating.add_description()
                        if isinstance(x, dict):
                            d.code = str(x.get('value',''))
                            d.attrib['language'] = x.get('language', '')
                        else:
                            d.code = str(x)
                    except KeyError: pass
                    # Energy-Efficiency-Rating
                    try: 
                        main_heating.add_energy_efficiency_rating().code = str(j['data']['main_heating'][main_heating_index].pop('energy_efficiency_rating'))
                    except KeyError: pass
                    # Environmental-Efficiency-Rating
                    try: 
                        main_heating.add_environmental_efficiency_rating().code = str(j['data']['main_heating'][main_heating_index].pop('environmental_efficiency_rating'))
                    except KeyError: pass
                    #
                    if len(j['data']['main_heating'][main_heating_index]) == 0:
                        c.append(main_heating_index)
                    else:
                        print(etree.tostring(sap_report, pretty_print=True).decode())
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
                        # Description
                        try: 
                            x = j['data']['main_heating_controls'][main_heating_controls_index].pop('description')
                            d = main_heating_controls.add_description()
                            if isinstance(x, dict):
                                d.code = str(x.get('value',''))
                                d.attrib['language'] = x.get('language', '')
                            else:
                                d.code = str(x)
                        except KeyError: pass
                        # Energy-Efficiency-Rating
                        try: 
                            main_heating_controls.add_energy_efficiency_rating().code = str(j['data']['main_heating_controls'][main_heating_controls_index].pop('energy_efficiency_rating'))
                        except KeyError: pass
                        # Environmental-Efficiency-Rating
                        try: 
                            main_heating_controls.add_environmental_efficiency_rating().code = str(j['data']['main_heating_controls'][main_heating_controls_index].pop('environmental_efficiency_rating'))
                        except KeyError: pass
                        #
                        if len(j['data']['main_heating_controls'][main_heating_controls_index]) == 0:
                            c.append(main_heating_controls_index)
                        else:
                            print(etree.tostring(sap_report, pretty_print=True).decode())
                            raise Exception('j', 'data', 'main_heating_controls', main_heating_controls_index, list(j['data']['main_heating_controls'][main_heating_controls_index])[0])
                    for c1 in c[::-1]: del j['data']['main_heating_controls'][c1]
                    if len(j['data']['main_heating_controls']) == 0: del j['data']['main_heating_controls']

            if True:
                # --- Secondary-Heating ---
                if 'secondary_heating' in j['data']:
                    secondary_heating = property_summary.add_secondary_heating()
                    # Description
                    try: 
                        x = j['data']['secondary_heating'].pop('description')
                        d = secondary_heating.add_description()
                        if isinstance(x, dict):
                            d.code = str(x.get('value',''))
                            d.attrib['language'] = x.get('language', '')
                        else:
                            d.code = str(x)
                    except KeyError: pass
                    # Energy-Efficiency-Rating
                    try: 
                        secondary_heating.add_energy_efficiency_rating().code = str(j['data']['secondary_heating'].pop('energy_efficiency_rating'))
                    except KeyError: pass
                    # Environmental-Efficiency-Rating
                    try: 
                        secondary_heating.add_environmental_efficiency_rating().code = str(j['data']['secondary_heating'].pop('environmental_efficiency_rating'))
                    except KeyError: pass
                    if len(j['data']['secondary_heating']) == 0:
                        del j['data']['secondary_heating']
                    else:
                        raise Exception('j', 'data', 'secondary_heating', list(j['data']['secondary_heating'])[0])

            if True:
                # --- Hot-Water ---
                if 'hot_water' in j['data']:
                    hot_water = property_summary.add_hot_water()
                    # Description
                    try: 
                        x = j['data']['hot_water'].pop('description')
                        d = hot_water.add_description()
                        if isinstance(x, dict):
                            d.code = str(x.get('value',''))
                            d.attrib['language'] = x.get('language', '')
                        else:
                            d.code = str(x)
                    except KeyError: pass
                    # Energy-Efficiency-Rating
                    try: 
                        hot_water.add_energy_efficiency_rating().code = str(j['data']['hot_water'].pop('energy_efficiency_rating'))
                    except KeyError: pass
                    # Environmental-Efficiency-Rating
                    try: 
                        hot_water.add_environmental_efficiency_rating().code = str(j['data']['hot_water'].pop('environmental_efficiency_rating'))
                    except KeyError: pass
                    #
                    if len(j['data']['hot_water']) == 0:
                        del j['data']['hot_water']
                    else:
                        print(etree.tostring(sap_report, pretty_print=True).decode())
                        raise Exception('j', 'data', 'hot_water', list(j['data']['hot_water'])[0])

            if True:
                # --- Lighting ---
                if 'lighting' in j['data']:
                    lighting = property_summary.add_lighting()
                    # Description
                    try: 
                        x = j['data']['lighting'].pop('description')
                        d = lighting.add_description()
                        if isinstance(x, dict):
                            d.code = str(x.get('value',''))
                            d.attrib['language'] = x.get('language', '')
                        else:
                            d.code = str(x)
                    except KeyError: pass
                    # Energy-Efficiency-Rating
                    try: 
                        lighting.add_energy_efficiency_rating().code = str(j['data']['lighting'].pop('energy_efficiency_rating'))
                    except KeyError: pass
                    # Environmental-Efficiency-Rating
                    try: 
                        lighting.add_environmental_efficiency_rating().code = str(j['data']['lighting'].pop('environmental_efficiency_rating'))
                    except KeyError: pass
                    if len(j['data']['lighting']) == 0:
                        del j['data']['lighting']
                    else:
                        print(etree.tostring(sap_report, pretty_print=True).decode())
                        raise Exception('j', 'data', 'lighting', list(j['data']['lighting'])[0])

            if True:
                # --- Air-Tightness ---
                if 'air_tightness' in j['data']:
                    air_tightness = property_summary.add_air_tightness()
                    # Description
                    try: 
                        x = j['data']['air_tightness'].pop('description')
                        d = air_tightness.add_description()
                        if isinstance(x, dict):
                            d.code = str(x.get('value',''))
                            d.attrib['language'] = x.get('language', '')
                        else:
                            d.code = str(x)
                    except KeyError: pass
                    # Energy-Efficiency-Rating
                    try: 
                        air_tightness.add_energy_efficiency_rating().code = str(j['data']['air_tightness'].pop('energy_efficiency_rating'))
                    except KeyError: pass
                    # Environmental-Efficiency-Rating
                    try: 
                        air_tightness.add_environmental_efficiency_rating().code = str(j['data']['air_tightness'].pop('environmental_efficiency_rating'))
                    except KeyError: pass
                    if len(j['data']['air_tightness']) == 0:
                        del j['data']['air_tightness']
                    else:
                        raise Exception('j', 'data', 'air_tightness', list(j['data']['air_tightness'])[0])
                    
            # Has-Fixed-Air-Conditioning
            try: 
                property_summary.add_has_fixed_air_conditioning().code = str(j['data'].pop('has_fixed_air_conditioning'))
            except KeyError: pass

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

            # Total-Floor-Area
            try: 
                property_summary.add_total_floor_area().code = str(j['data'].pop('total_floor_area'))
            except KeyError: pass

            # Multiple-Glazed-Percentage
            try: 
                property_summary.add_multiple_glazed_percentage().code = str(j['data'].pop('multiple_glazed_percentage'))
            except KeyError: pass

            # Multiple-Glazed-Percentage-NR
    #         try: 
    #             property_summary.add_multiple_glazed_Percentage_nr().code = str(j['data'].pop('multiple_glazed_Percentage_nr'))
    #         except KeyError: pass

            # Is-Zero-Carbon-Home
            try: 
                property_summary.add_is_zero_carbon_home().code = str(j['data'].pop('is_zero_carbon_home'))
            except KeyError: pass

        if True:
            # --- Energy-Use ---
            energy_use = energy_assessment.add_energy_use()

            # DER
            try: 
                energy_use.add_der().code = str(j['data'].pop('der'))
            except KeyError: pass

            # TER
            try: 
                energy_use.add_ter().code = str(j['data'].pop('ter'))
            except KeyError: pass

            # DPER
            try: 
                energy_use.add_dper().code = str(j['data'].pop('dper'))
            except KeyError: pass

            # TPER
            try: 
                energy_use.add_tper().code = str(j['data'].pop('tper'))
            except KeyError: pass

            # DFEE
            try: 
                energy_use.add_dfee().code = str(j['data'].pop('dfee'))
            except KeyError: pass

            # TFEE
            try: 
                energy_use.add_tfee().code = str(j['data'].pop('tfee'))
            except KeyError: pass

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
                    # --- Improvement ---
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

                    # # Green-Deal-Category

                    #
                    if len(j['data']['suggested_improvements'][suggested_improvements_index]) == 0:
                        c.append(suggested_improvements_index)
                    else:
                        print(etree.tostring(sap_report, pretty_print=True).decode())
                        raise Exception('j', 'data', 'suggested_improvements', suggested_improvements_index, list(j['data']['suggested_improvements'][suggested_improvements_index])[0])
                for c1 in c[::-1]: del j['data']['suggested_improvements'][c1]
                if len(j['data']['suggested_improvements']) == 0: del j['data']['suggested_improvements']



        if True:
            # --- LZC-Energy-Sources ---
            if 'lzc_energy_sources' in j['data']:
                # LZC-Energy-Source
                lzc_energy_sources = energy_assessment.add_lzc_energy_sources()
                # LZC-Energy-Source
                for lzc_energy_source_code in j['data']['lzc_energy_sources']:
                    lzc_energy_sources.add_lzc_energy_source().code = str(lzc_energy_source_code)
                del j['data']['lzc_energy_sources']

            # --- Renewable-Heat-Incentive

                # --- RHI-New-Dwelling ---

                    # Space-Heating

                    # Water-Heating

                # --- RHI-Existing-Dwelling ---

                    # Space-Heating-Existing-Dwelling

                    # Space-Heating-With-Loft-Insulation

                    # Space-Heating-With-Cavity-Insulation

                    # Space-Heating-With-Loft-And-Cavity-Insulation

                    # Water-Heating

                    # Impact-Of-Loft-Insulation

                    # Impact-Of-Cavity-Insulation

                    # Impact-Of-Solid-Wall-Insulation

            # --- Green-Deal-Package ---

                # --- Green-Deal-Improvement ---

                    # Improvement-Type

                    # Improvement-Number

                # Electricity-Saving

                # Gas-Saving

                # Other-Fuel-Saving


    #     if True:
    #         # --- Alternative-Improvements ---
    #         if 'alternative_improvements' in j['data']:
    #             alternative_improvements = energy_assessment.add_alternative_improvements()
    #             c = []
    #             for alternative_improvements_index in range(len(j['data']['alternative_improvements'])):
    #                 # --- Improvement ---
    #                 improvement = alternative_improvements.add_improvement()

    #                 # Sequence
    #                 try: 
    #                     improvement.add_sequence().code = str(j['data']['alternative_improvements'][alternative_improvements_index].pop('sequence'))
    #                 except KeyError: pass

    #                 # Improvement-Category
    #                 try: 
    #                     improvement.add_improvement_category().code = str(j['data']['alternative_improvements'][alternative_improvements_index].pop('improvement_category'))
    #                 except KeyError: pass

    #                 # Improvement-Type
    #                 try: 
    #                     improvement.add_improvement_type().code = str(j['data']['alternative_improvements'][alternative_improvements_index].pop('improvement_type'))
    #                 except KeyError: pass

    #                 # Typical-Saving
    #                 try: 
    #                     improvement.add_typical_saving().code = str(j['data']['alternative_improvements'][alternative_improvements_index].pop('typical_saving'))
    #                 except KeyError: pass

    #                 # Energy-Performance-Rating
    #                 try: 
    #                     improvement.add_energy_performance_rating().code = str(j['data']['alternative_improvements'][alternative_improvements_index].pop('energy_performance_rating'))
    #                 except KeyError: pass

    #                 # Environmental-Impact-Rating
    #                 try: 
    #                     improvement.add_environmental_impact_rating().code = str(j['data']['alternative_improvements'][alternative_improvements_index].pop('environmental_impact_rating'))
    #                 except KeyError: pass

    #                 # Improvement-Details
    #                 try: 
    #                     improvement.add_improvement_details().code = str(j['data']['alternative_improvements'][alternative_improvements_index].pop('improvement_details'))
    #                 except KeyError: pass

    #                 # Indicative-Cost
    #                 try: 
    #                     improvement.add_indicative_cost().code = str(j['data']['alternative_improvements'][alternative_improvements_index].pop('indicative_cost'))
    #                 except KeyError: pass

                    # Green-Deal-Category

    #                 #
    #                 if len(j['data']['alternative_improvements'][alternative_improvements_index]) == 0:
    #                     c.append(alternative_improvements_index)
    #                 else:
    #                     print(etree.tostring(sap_report, pretty_print=True).decode())
    #                     print(j['data']['alternative_improvements'][alternative_improvements_index])
    #                     raise Exception('j', 'data', 'alternative_improvements', alternative_improvements_index, list(j['data']['alternative_improvements'][alternative_improvements_index])[0])
    #             for c1 in c[::-1]: del j['data']['alternative_improvements'][c1]
    #             if len(j['data']['alternative_improvements']) == 0: del j['data']['alternative_improvements']


    #     if True:
    #         # --- Addendum ---
    #         if 'addendum' in j['data']:

    #             addendum = energy_assessment.add_addendum()   
                
    #             # Cavity-Fill-Recommended
    #             try: 
    #                 addendum.add_cavity_fill_recommended().code = str(j['data']['addendum'].pop('cavity_fill_recommended'))
    #             except KeyError: pass

    #             # Stone-Walls
    #             try: 
    #                 addendum.add_stone_walls().code = str(j['data']['addendum'].pop('stone_walls'))
    #             except KeyError: pass

    #             # System-Build
    #             try: 
    #                 addendum.add_system_build().code = str(j['data']['addendum'].pop('system_build'))
    #             except KeyError: pass
                
    #             # Access-Issues
    #             try: 
    #                 addendum.add_access_issues().code = str(j['data']['addendum'].pop('access_issues'))
    #             except KeyError: pass

    #             # High-Exposure
    #             try: 
    #                 addendum.add_high_exposure().code = str(j['data']['addendum'].pop('high_exposure'))
    #             except KeyError: pass

    #             # Narrow-Cavities
    #             try: 
    #                 addendum.add_narrow_cavities().code = str(j['data']['addendum'].pop('narrow_cavities'))
    #             except KeyError: pass

    #             #
    #             if len(j['data']['addendum']) == 0:
    #                 del j['data']['addendum']
    #             else:
    #                 raise Exception('j', 'data', 'addendum', list(j['data']['addendum'])[0])

    

    if True:
        # --- SAP-Data ---
        sap10_data = sap_report.add_sap10_data()

        # Data-Type
        try: 
            sap10_data.add_data_type().code = str(j['data'].pop('data_type'))
        except KeyError: pass

        if True:
            # --- SAP-Property-Details ---
            sap_property_details = sap10_data.add_sap_property_details()

#         # Property-Type
    #         try: 
    #             sap_property_details.add_property_type().code = str(j['data'].pop('property_type'))
    #         except KeyError: pass

            # Built-Form
            try: 
                sap_property_details.add_built_form().code = str(j['data'].pop('built_form'))
            except KeyError: pass

            # Living-Area
            try: 
                sap_property_details.add_living_area().code = str(j['data'].pop('living_area'))
            except KeyError: pass

            # Lowest-Storey-Area
            try: 
                sap_property_details.add_lowest_storey_area().code = str(j['data'].pop('lowest_storey_area'))
            except KeyError: pass

            # Orientation
            try: 
                sap_property_details.add_orientation().code = str(j['data'].pop('orientation'))
            except KeyError: pass

            # Conservatory-Type
            try: 
                sap_property_details.add_conservatory_type().code = str(j['data'].pop('conservatory_type'))
            except KeyError: pass  

            # Terrian-Type
            try: 
                sap_property_details.add_terrain_type().code = str(j['data'].pop('terrain_type'))
            except KeyError: pass

            # Has-Special-Feature

            # Special-Feature-Description

            # Energy-Saved-Or-Generated

            # Saved-Or-Generated-Fuel

            # Energy-Used

            # Energy-Fuel-Used

            # Is-In-Smoke-Control-Area
            try: 
                sap_property_details.add_is_in_smoke_control_area().code = str(j['data'].pop('is_in_smoke_control_area'))
            except KeyError: pass

            # Part-O-Cooling-Required

            # Cold-Water-Source
            try: 
                sap_property_details.add_cold_water_source().code = str(j['data'].pop('cold_water_source'))
            except KeyError: pass

            # Windows-Overshading
            try: 
                sap_property_details.add_windows_overshading().code = str(j['data'].pop('windows_overshading'))
            except KeyError: pass
            # Thermal-Mass-Parameter
            try: 
                sap_property_details.add_thermal_mass_parameter().code = str(j['data'].pop('thermal_mass_parameter'))
            except KeyError: pass
            # Additional-Allowable-Electricity-Generation

            # Gas-Smart-Meter-Present
            try: 
                sap_property_details.add_gas_smart_meter_present().code = str(j['data'].pop('gas_smart_meter_present'))
            except KeyError: pass

            # Electricity-Smart-Meter-Present
            try: 
                sap_property_details.add_electricity_smart_meter_present().code = str(j['data'].pop('electricity_smart_meter_present'))
            except KeyError: pass

            # Is-Dwelling-Export-Capable
            try: 
                sap_property_details.add_is_dwelling_export_capable().code = str(j['data'].pop('is_dwelling_export_capable'))
            except KeyError: pass

            # PV-Connection
            try: 
                sap_property_details.add_pv_connection().code = str(j['data'].pop('pv_connection'))
            except KeyError: pass

            # PV-Diverter
            try: 
                sap_property_details.add_pv_diverter().code = str(j['data'].pop('pv_diverter'))
            except KeyError: pass


            # Battery-Capacity
            try: 
                sap_property_details.add_battery_capacity().code = str(j['data'].pop('battery_capacity'))
            except KeyError: pass

            # Is-Wind-Turbine-Connected-To-Dwelling-Meter

            if True:
                # --- SAP-Heating ---
                if 'sap_heating' in j['data']:
                    sap_heating = sap_property_details.add_sap_heating()

                    # Water-Heating-Code
                    try: 
                        sap_heating.add_water_heating_code().code = str(j['data']['sap_heating'].pop('water_heating_code'))
                    except KeyError: pass

                    # Water-Fuel-Type
                    try: 
                        sap_heating.add_water_fuel_type().code = str(j['data']['sap_heating'].pop('water_fuel_type'))
                    except KeyError: pass

                    # Has-Hot-Water-Cylinder
                    try: 
                        sap_heating.add_has_hot_water_cylinder().code = str(j['data']['sap_heating'].pop('has_hot_water_cylinder'))
                    except KeyError: pass

                    # Secondary-Heating-Category
                    try: 
                        sap_heating.add_secondary_heating_category().code = str(j['data']['sap_heating'].pop('secondary_heating_category'))
                    except KeyError: pass

                    # Secondary-Heating-Data-Source
                    try: 
                        sap_heating.add_secondary_heating_data_source().code = str(j['data']['sap_heating'].pop('secondary_heating_data_source'))
                    except KeyError: pass

                    # Secondary-Heating-Code
                    try: 
                        sap_heating.add_secondary_heating_code().code = str(j['data']['sap_heating'].pop('secondary_heating_code'))
                    except KeyError: pass

                    # Secondary-Fuel-Type
                    try: 
                        sap_heating.add_secondary_fuel_type().code = str(j['data']['sap_heating'].pop('secondary_fuel_type'))
                    except KeyError: pass  
    
                    # Secondary-Heating-PCDF-Fuel-Index

                    # Secondary-Heating-Flue-Type
                    try: 
                        sap_heating.add_secondary_heating_flue_type().code = str(j['data']['sap_heating'].pop('secondary_heating_flue_type'))
                    except KeyError: pass  

                    # Thermal-Store
                    try: 
                        sap_heating.add_thermal_store().code = str(j['data']['sap_heating'].pop('thermal_store'))
                    except KeyError: pass

                    # Has-Fixed-Air-Conditioning
                    try: 
                        sap_heating.add_has_fixed_air_conditioning().code = str(j['data']['sap_heating'].pop('has_fixed_air_conditioning'))
                    except KeyError: pass  
    
                    # Immersion-Heating-Type
                    try: 
                        sap_heating.add_immersion_heating_type().code = str(j['data']['sap_heating'].pop('immersion_heating_type'))
                    except KeyError: pass

                    # Is-Heat-Pump-Assisted-By-Immersion
                    try: 
                        sap_heating.add_is_heat_pump_assisted_by_immersion().code = str(j['data']['sap_heating'].pop('is_heat_pump_assisted_by_immersion'))
                    except KeyError: pass

                    # Is-Heat-Pump-Installed-To-MIS
                    try: 
                        sap_heating.add_is_heat_pump_installed_to_mis().code = str(j['data']['sap_heating'].pop('is_heat_pump_installed_to_mis'))
                    except KeyError: pass 

                    # Is-Immersion-For-Summer-Use
                    try: 
                        sap_heating.add_is_immersion_for_summer_use().code = str(j['data']['sap_heating'].pop('is_immersion_for_summer_use'))
                    except KeyError: pass  

                    # Is-Secondary-Heating-HETAS-Approved
                    try: 
                        sap_heating.add_is_secondary_heating_hetas_approved().code = str(j['data']['sap_heating'].pop('is_secondary_heating_hetas_approved'))
                    except KeyError: pass  

                    # Hot-Water-Store-Manufacturer

                    # Hot-Water-Store-Model

                    # Hot-Water-Store-Commissioning-Certificate

                    # Hot-Water-Store-Installer-Engineer-Registration

                    # Hot-Water-Store-Size
                    try: 
                        sap_heating.add_hot_water_store_size().code = str(j['data']['sap_heating'].pop('hot_water_store_size'))
                    except KeyError: pass 

                    # Hot-Water-Store-Heat-Transfer-Area
                    try: 
                        sap_heating.add_hot_water_store_heat_transfer_area().code = str(j['data']['sap_heating'].pop('hot_water_store_heat_transfer_area'))
                    except KeyError: pass 

                    # Hot-Water-Store-Heat-Loss-Source
                    try: 
                        sap_heating.add_hot_water_store_heat_loss_source().code = str(j['data']['sap_heating'].pop('hot_water_store_heat_loss_source'))
                    except KeyError: pass 

                    # Hot-Water-Store-Heat-Loss
                    try: 
                        sap_heating.add_hot_water_store_heat_loss().code = str(j['data']['sap_heating'].pop('hot_water_store_heat_loss'))
                    except KeyError: pass 

                    # Hot-Water-Store-Insulation-Type
                    try: 
                        sap_heating.add_hot_water_store_insulation_type().code = str(j['data']['sap_heating'].pop('hot_water_store_insulation_type'))
                    except KeyError: pass

                    # Hot-Water-Store-Insulation-Thickness
                    try: 
                        sap_heating.add_hot_water_store_insulation_thickness().code = str(j['data']['sap_heating'].pop('hot_water_store_insulation_thickness'))
                    except KeyError: pass

                    # Is-Thermal-Store-Near-Boiler
                    try: 
                        sap_heating.add_is_thermal_store_near_boiler().code = str(j['data']['sap_heating'].pop('is_thermal_store_near_boiler'))
                    except KeyError: pass 

                    # Is-Thermal-Store-Or-CPSU-In-Airing-Cupboard
                    try: 
                        sap_heating.add_is_thermal_store_or_cpsu_in_airing_cupboard().code = str(j['data']['sap_heating'].pop('is_thermal_store_or_cpsu_in_airing_cupboard'))
                    except KeyError: pass 

                    # Has-Cylinder-Thermostat
                    try: 
                        sap_heating.add_has_cylinder_thermostat().code = str(j['data']['sap_heating'].pop('has_cylinder_thermostat'))
                    except KeyError: pass

                    # Is-Cylinder-In-Heated-Space
                    try: 
                        sap_heating.add_is_cylinder_in_heated_space().code = str(j['data']['sap_heating'].pop('is_cylinder_in_heated_space'))
                    except KeyError: pass

                    # Is-Hot-Water-Separately-Timed
                    try: 
                        sap_heating.add_is_hot_water_separately_timed().code = str(j['data']['sap_heating'].pop('is_hot_water_separately_timed'))
                    except KeyError: pass

                    # Hot-Water-Controls-Manufacturer

                    # Hot-Water-Controls-Model

                    # SAP-Community-Heating-Systems
                    try: 
                        sap_heating.add_sap_community_heating_systems().code = str(j['data']['sap_heating'].pop('sap_community_heating_systems'))
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

                                # Main-Heating-Data-Source
                                try: 
                                    main_heating.add_main_heating_data_source().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('main_heating_data_source'))
                                except KeyError: pass

                                # Main-Heating-Index-Number
                                try: 
                                    main_heating.add_main_heating_index_number().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('main_heating_index_number'))
                                except KeyError: pass

                                # Main-Heating-Manufacturer
                                try: 
                                    main_heating.add_main_heating_manufacturer().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('main_heating_manufacturer'))
                                except KeyError: pass

                                # Main-Heating-Model
                                try: 
                                    main_heating.add_main_heating_model().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('main_heating_model'))
                                except KeyError: pass

                                # Main-Heating-Commissioning-Certificate

                                # Main-Heating-Installation-Engineer

                                # Is-Condensing-Boiler
                                try: 
                                    main_heating.add_is_condensing_boiler().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('is_condensing_boiler'))
                                except KeyError: pass

                                # Condensing-Boiler-Heat-Distribution
                                try: 
                                    main_heating.add_condensing_boiler_heat_distribution().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('condensing_boiler_heat_distribution'))
                                except KeyError: pass

                                # Heat-Pump-Heat-Distribution
                                try: 
                                    main_heating.add_heat_pump_heat_distribution().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('heat_pump_heat_distribution'))
                                except KeyError: pass

                                # Gas-Or-Oil-Boiler-Type
                                try: 
                                    main_heating.add_gas_or_oil_boiler_type().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('gas_or_oil_boiler_type'))
                                except KeyError: pass

                                # Combi-Boiler-Type
                                try: 
                                    main_heating.add_combi_boiler_type().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('combi_boiler_type'))
                                except KeyError: pass

                                # Case-Heat-Emission

                                # Heat-Transfer-To-Water

                                # Solid-Fuel-Boiler-Type
                                try: 
                                    main_heating.add_solid_fuel_boiler_type().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('solid_fuel_boiler_type'))
                                except KeyError: pass

                                # Main-Heating-Code
                                try: 
                                    main_heating.add_main_heating_code().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('main_heating_code'))
                                except KeyError: pass

                                # Main-Fuel-Type
                                try: 
                                    main_heating.add_main_fuel_type().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('main_fuel_type'))
                                except KeyError: pass

                                # PCDF-Fuel-Index

                                # Main-Heating-Control
                                try: 
                                    main_heating.add_main_heating_control().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('main_heating_control'))
                                except KeyError: pass

                                # Heat-Emitter-Type
                                try: 
                                    main_heating.add_heat_emitter_type().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('heat_emitter_type'))
                                except KeyError: pass

                                # Underfloor-Heat-Emitter-Type
                                try: 
                                    main_heating.add_underfloor_heat_emitter_type().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('underfloor_heat_emitter_type'))
                                except KeyError: pass

                                # Main-Heating-Flue-Type
                                try: 
                                    main_heating.add_main_heating_flue_type().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('main_heating_flue_type'))
                                except KeyError: pass

                                # Is-Flue-Fan-Present
                                try: 
                                    main_heating.add_is_flue_fan_present().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('is_flue_fan_present'))
                                except KeyError: pass

                                # Is-Central-Heating-Pump-In-Heated-Space
                                try: 
                                    main_heating.add_is_central_heating_pump_in_heated_space().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('is_central_heating_pump_in_heated_space'))
                                except KeyError: pass

                                # Is-Oil-Pump-In-Heated-Space
                                try: 
                                    main_heating.add_is_oil_pump_in_heated_space().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('is_oil_pump_in_heated_space'))
                                except KeyError: pass

                                # Is-Interlocked-System
                                try: 
                                    main_heating.add_is_interlocked_system().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('is_interlocked_system'))
                                except KeyError: pass

                                # Has-Separate-Delayed-Start
                                try: 
                                    main_heating.add_has_separate_delayed_start().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('has_separate_delayed_start'))
                                except KeyError: pass

                                # Boiler-Fuel-Feed
                                try: 
                                    main_heating.add_boiler_fuel_feed().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('boiler_fuel_feed'))
                                except KeyError: pass

                                # Is-Main-Heating-HETAS-Approved
                                try: 
                                    main_heating.add_is_main_heating_hetas_approved().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('is_main_heating_hetas_approved'))
                                except KeyError: pass

                                # Electric-CPSU-Operating-Temperature

                                # Main-Heating-Fraction
                                try: 
                                    main_heating_fraction = j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('main_heating_fraction')
                                    main_heating.add_main_heating_fraction().code = str(float(main_heating_fraction)/100.0)
                                except KeyError: pass

                                # Burner-Control
                                try: 
                                    main_heating.add_burner_control().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('burner_control'))
                                except KeyError: pass

                                # Efficiency-Type
                                try: 
                                    main_heating.add_efficiency_type().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('efficiency_type'))
                                except KeyError: pass

                                # Main-Heating-Efficiency-Winter

                                # Main-Heating-Efficiency-Summer

                                # Main-Heating-Efficiency
                                try: 
                                    main_heating.add_main_heating_efficiency().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('main_heating_efficiency'))
                                except KeyError: pass

                                # Main-Heating-System-Type
                                try: 
                                    main_heating.add_main_heating_system_type().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('main_heating_system_type'))
                                except KeyError: pass

                                # Has-FGHRS
                                try: 
                                    main_heating.add_has_fghrs().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('has_fghrs'))
                                except KeyError: pass

                                # FGHRS-Index-Number
                                try: 
                                    main_heating.add_fghrs_index_number().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('fghrs_index_number'))
                                except KeyError: pass

                                # FGHRS-Energy-Source
                                try: 
                                    main_heating.add_fghrs_energy_source().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('fghrs_energy_source'))
                                except KeyError: pass

                                # Main-Heating-Declared-Values 
                                try: 
                                    main_heating.add_main_heating_declared_values().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('main_heating_declared_values'))
                                except KeyError: pass                                

                                
                                #
                                if 'storage_heaters' in j['data']['sap_heating']['main_heating_details'][main_heating_index]:
                                    # --- Storage-Heaters ---
                                    storage_heaters = main_heating.add_storage_heaters()
                                    storage_heaters_c = []
                                    for storage_heater_index in range(len(j['data']['sap_heating']['main_heating_details'][main_heating_index]['storage_heaters'])):
                                        # --- Storage-Heater ---
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
                                            print(etree.tostring(sap_report, pretty_print=True).decode())
                                            raise Exception('j', 'data', 'sap_heating', 'main_heating_details', main_heating_index, 'storage_heaters', storage_heater_index, 
                                                            list(j['data']['sap_heating']['main_heating_details'][main_heating_index]['storage_heaters'][storage_heater_index])[0])
                                    for c1 in storage_heaters_c[::-1]: del j['data']['sap_heating']['main_heating_details'][main_heating_index]['storage_heaters'][c1]
                                    if len(j['data']['sap_heating']['main_heating_details'][main_heating_index]['storage_heaters']) == 0: del j['data']['sap_heating']['main_heating_details'][main_heating_index]['storage_heaters']

                                # Emitter-Temperature
                                try: 
                                    main_heating.add_emitter_temperature().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('emitter_temperature'))
                                except KeyError: pass

                                # MCS-Installed-Heat-Pump
                                try: 
                                    main_heating.add_mcs_installed_heat_pump().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('mcs_installed_heat_pump'))
                                except KeyError: pass

                                # Central-Heating-Pump-Age
                                try: 
                                    main_heating.add_central_heating_pump_age().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('central_heating_pump_age'))
                                except KeyError: pass

                                # Control-Index-Number
                                try: 
                                    main_heating.add_control_index_number().code = str(j['data']['sap_heating']['main_heating_details'][main_heating_index].pop('control_index_number'))
                                except KeyError: pass

                                # Heating-Controller-Function

                                # Heating-Controller-Ecodesign-Class

                                # Heating-Controller-Manufacturer

                                # Heating-Controller-Model



                                if len(j['data']['sap_heating']['main_heating_details'][main_heating_index]) == 0:
                                    main_heating_details_c.append(main_heating_index)
                                else:
                                    print(etree.tostring(sap_report, pretty_print=True).decode())
                                    raise Exception('j', 'data', 'sap_heating', 'main_heating_details', main_heating_index, list(j['data']['sap_heating']['main_heating_details'][main_heating_index])[0])
                            for c1 in main_heating_details_c[::-1]: del j['data']['sap_heating']['main_heating_details'][c1]
                            if len(j['data']['sap_heating']['main_heating_details']) == 0: del j['data']['sap_heating']['main_heating_details']
                            

                    # SAP-Heating-Design-Water-Use

                    # Main-Heating-Systems-Interaction
                    try: 
                        sap_heating.add_main_heating_systems_interaction().code = str(j['data']['sap_heating'].pop('main_heating_systems_interaction'))
                    except KeyError: pass


                    # Secondary-Heating-Declared-Values
                    try: 
                        sap_heating.add_secondary_heating_declared_values().code = str(j['data']['sap_heating'].pop('secondary_heating_declared_values'))
                    except KeyError: pass

                    # Primary-Pipework-Insulation
                    try: 
                        sap_heating.add_primary_pipework_insulation().code = str(j['data']['sap_heating'].pop('primary_pipework_insulation'))
                    except KeyError: pass

                    if True:
                        # --- Solar-Heating-Details ---
                        if 'solar_heating_details' in j['data']['sap_heating']:
                            solar_heating_details = sap_heating.add_solar_heating_details()

                            # Solar-Heating-Collector-Manufactuer

                            # Solar-Heating-Certificate

                            # Solar-Panel-Aperture-Area
                            try: 
                                solar_heating_details.add_solar_panel_aperture_area().code = str(j['data']['sap_heating']['solar_heating_details'].pop('solar_panel_aperture_area'))
                            except KeyError: pass

                            # Solar-Panel-Collector-Type
                            try: 
                                solar_heating_details.add_solar_panel_collector_type().code = str(j['data']['sap_heating']['solar_heating_details'].pop('solar_panel_collector_type'))
                            except KeyError: pass

                            # Solar-Panel-Collector-Data-Source
                            try: 
                                solar_heating_details.add_solar_panel_collector_data_source().code = str(j['data']['sap_heating']['solar_heating_details'].pop('solar_panel_collector_data_source'))
                            except KeyError: pass

                            # Solar-Panel-Collector-Zero-Loss-Efficiency
                            try: 
                                solar_heating_details.add_solar_panel_collector_zero_loss_efficiency().code = str(j['data']['sap_heating']['solar_heating_details'].pop('solar_panel_collector_zero_loss_efficiency'))
                            except KeyError: pass

                            # Solar-Panel-Collector-Heat-Loss-Rate

                            # Solar-Panel-Collector-Linear-Heat-Loss-Coefficient
                            try: 
                                solar_heating_details.add_solar_panel_collector_linear_heat_loss_coefficient().code = str(j['data']['sap_heating']['solar_heating_details'].pop('solar_panel_collector_linear_heat_loss_coefficient'))
                            except KeyError: pass

                            # Solar-Panel-Collector-Second-Order-Heat-Loss-Coefficient
                            try: 
                                solar_heating_details.add_solar_panel_collector_second_order_heat_loss_coefficient().code = \
                                    str(j['data']['sap_heating']['solar_heating_details'].pop('solar_panel_collector_second_order_heat_loss_coefficient'))
                            except KeyError: pass

                            # Solar-Panel-Collector-Orientation
                            try: 
                                solar_heating_details.add_solar_panel_collector_orientation().code = str(j['data']['sap_heating']['solar_heating_details'].pop('solar_panel_collector_orientation'))
                            except KeyError: pass

                            # Solar-Panel-Collector-Pitch
                            try: 
                                solar_heating_details.add_solar_panel_collector_pitch().code = str(j['data']['sap_heating']['solar_heating_details'].pop('solar_panel_collector_pitch'))
                            except KeyError: pass

                            # Solar-Panel-Collector-Overshading
                            try: 
                                solar_heating_details.add_solar_panel_collector_overshading().code = str(j['data']['sap_heating']['solar_heating_details'].pop('solar_panel_collector_overshading'))
                            except KeyError: pass

                            # Has-Solar-Powered-Pump
                            try: 
                                solar_heating_details.add_has_solar_powered_pump().code = str(j['data']['sap_heating']['solar_heating_details'].pop('has_solar_powered_pump'))
                            except KeyError: pass

                            # Is-Solar-Store-Combined-Cylinder
                            try: 
                                solar_heating_details.add_is_solar_store_combined_cylinder().code = str(j['data']['sap_heating']['solar_heating_details'].pop('is_solar_store_combined_cylinder'))
                            except KeyError: pass

                            # Solar-Store-Volume
                            try: 
                                solar_heating_details.add_solar_store_volume().code = str(j['data']['sap_heating']['solar_heating_details'].pop('solar_store_volume'))
                            except KeyError: pass

                            # Collector-Loop-Efficiency
                            try: 
                                solar_heating_details.add_collector_loop_efficiency().code = str(j['data']['sap_heating']['solar_heating_details'].pop('collector_loop_efficiency'))
                            except KeyError: pass

                            # Incidence-Angle-Modifier
                            try: 
                                solar_heating_details.add_incidence_angle_modifier().code = str(j['data']['sap_heating']['solar_heating_details'].pop('incidence_angle_modifier'))
                            except KeyError: pass

                            # Is-Community-Solar
                            try: 
                                solar_heating_details.add_is_community_solar().code = str(j['data']['sap_heating']['solar_heating_details'].pop('is_community_solar'))
                            except KeyError: pass

                            # Service-Provision
                            try: 
                                solar_heating_details.add_service_provision().code = str(j['data']['sap_heating']['solar_heating_details'].pop('service_provision'))
                            except KeyError: pass

                            # Overall-Heat-Loss
                            try: 
                                solar_heating_details.add_overall_heat_loss().code = str(j['data']['sap_heating']['solar_heating_details'].pop('overall_heat_loss'))
                            except KeyError: pass

                            #
                            if len(j['data']['sap_heating']['solar_heating_details']) == 0:
                                del j['data']['sap_heating']['solar_heating_details']
                            else:
                                print(etree.tostring(sap_report, pretty_print=True).decode())
                                raise Exception('j', 'data', 'sap_heating', 'solar_heating_details', list(j['data']['sap_heating']['solar_heating_details'])[0])


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

                            # WWHRS-Efficiency1
                            try: 
                                instantaneous_wwhrs.add_wwhrs_efficiency1().code = str(j['data']['sap_heating']['instantaneous_wwhrs'].pop('wwhrs_efficiency1'))
                            except KeyError: pass

                            # WWHRS-Manufacturer1
                            try: 
                                instantaneous_wwhrs.add_wwhrs_manufacturer1().code = str(j['data']['sap_heating']['instantaneous_wwhrs'].pop('wwhrs_manufacturer1'))
                            except KeyError: pass

                            # WWHRS-Model1
                            try: 
                                instantaneous_wwhrs.add_wwhrs_model1().code = str(j['data']['sap_heating']['instantaneous_wwhrs'].pop('wwhrs_model1'))
                            except KeyError: pass

                            # WWHRS-Efficiency2
                            try: 
                                instantaneous_wwhrs.add_wwhrs_efficiency2().code = str(j['data']['sap_heating']['instantaneous_wwhrs'].pop('wwhrs_efficiency2'))
                            except KeyError: pass

                            # WWHRS-Manufacturer2
                            try: 
                                instantaneous_wwhrs.add_wwhrs_manufacturer2().code = str(j['data']['sap_heating']['instantaneous_wwhrs'].pop('wwhrs_manufacturer2'))
                            except KeyError: pass

                            # WWHRS-Model2
                            try: 
                                instantaneous_wwhrs.add_wwhrs_model2().code = str(j['data']['sap_heating']['instantaneous_wwhrs'].pop('wwhrs_model2'))
                            except KeyError: pass

                            #
                            if len(j['data']['sap_heating']['instantaneous_wwhrs']) == 0:
                                del j['data']['sap_heating']['instantaneous_wwhrs']
                            else:
                                print(etree.tostring(sap_report, pretty_print=True).decode())
                                raise Exception('j', 'data', 'sap_heating', 'instantaneous_wwhrs', list(j['data']['sap_heating']['instantaneous_wwhrs'])[0])
                    if True:
                        # --- Storage-WWHRS ---
                        if 'storage_wwhrs'in j['data']['sap_heating']:
                            storage_wwhrs = sap_heating.add_storage_wwhrs()
                            # WWHRS-Index-Number
                            try: 
                                storage_wwhrs.add_wwhrs_index_number().code = str(j['data']['sap_heating']['storage_wwhrs'].pop('wwhrs_index_number'))
                            except KeyError: pass
                            # WWHRS-Store-Volume
                            try: 
                                storage_wwhrs.add_wwhrs_store_volume().code = str(j['data']['sap_heating']['storage_wwhrs'].pop('wwhrs_store_volume'))
                            except KeyError: pass
                            # Storage-WWHRS-Efficiency

                            # Storage-WWHRS-Manufacturer
                            
                            # Storage-WWHRS-Model

                            #
                            if len(j['data']['sap_heating']['storage_wwhrs']) == 0:
                                del j['data']['sap_heating']['storage_wwhrs']
                            else:
                                print(etree.tostring(sap_report, pretty_print=True).decode())
                                raise Exception('j', 'data', 'sap_heating', 'storage_wwhrs', list(j['data']['sap_heating']['storage_wwhrs'])[0])

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

                            # Shower-Flow-Rate
                            try: 
                                shower_outlet.add_shower_flow_rate().code = str(j['data']['sap_heating']['shower_outlets'][shower_index].pop('shower_flow_rate'))
                            except KeyError: pass

                            # Shower-Power
                            try: 
                                shower_outlet.add_shower_power().code = str(j['data']['sap_heating']['shower_outlets'][shower_index].pop('shower_power'))
                            except KeyError: pass

                            # Shower-WWhrs
                            try: 
                                shower_outlet.add_shower_wwhrs().code = str(j['data']['sap_heating']['shower_outlets'][shower_index].pop('shower_wwhrs'))
                            except KeyError: pass

                            if len(j['data']['sap_heating']['shower_outlets'][shower_index]) == 0:
                                shower_outlets_c.append(shower_index)
                            else:
                                print(etree.tostring(sap_report, pretty_print=True).decode())
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

                    #
                    if len(j['data']['sap_heating']) == 0:
                        del j['data']['sap_heating']
                    else:
                        print(etree.tostring(sap_report, pretty_print=True).decode())
                        raise Exception('j', 'data', 'sap_heating', list(j['data']['sap_heating'])[0])


        if True:
            # --- SAP-Energy-Source ---
            if 'sap_energy_source' in j['data']:

                sap_energy_source = sap_property_details.add_sap_energy_source()

                # --- PV-Arrays ---
                if 'pv_arrays' in j['data']['sap_energy_source']:
                    pv_arrays = sap_energy_source.add_pv_arrays()
                    pv_arrays_c = []
                    for pv_array_index in range(len(j['data']['sap_energy_source']['pv_arrays'])):
                        # --- PV-Array ---
                        pv_array = pv_arrays.add_pv_array()
                        # Peak-Power
                        try: 
                            pv_array.add_peak_power().code = str(j['data']['sap_energy_source']['pv_arrays'][pv_array_index].pop('peak_power'))
                        except KeyError: pass
                        # Orientation
                        try: 
                            pv_array.add_orientation().code = str(j['data']['sap_energy_source']['pv_arrays'][pv_array_index].pop('orientation'))
                        except KeyError: pass
                        # Pitch
                        try: 
                            pv_array.add_pitch().code = str(j['data']['sap_energy_source']['pv_arrays'][pv_array_index].pop('pitch'))
                        except KeyError: pass
                        # Overshading
                        try: 
                            pv_array.add_overshading().code = str(j['data']['sap_energy_source']['pv_arrays'][pv_array_index].pop('overshading'))
                        except KeyError: pass

                        # MSC-Certificate
                        try: 
                            pv_array.add_mcs_certificate().code = str(j['data']['sap_energy_source']['pv_arrays'][pv_array_index].pop('mcs_certificate'))
                        except KeyError: pass

                        # MCS-Certificate-Reference
                        try: 
                            pv_array.add_mcs_certificate_reference().code = str(j['data']['sap_energy_source']['pv_arrays'][pv_array_index].pop('mcs_certificate_reference'))
                        except KeyError: pass

                        # PV-Panel-Manufacturer-Name
                        try: 
                            pv_array.add_pv_panel_manufacturer_name().code = str(j['data']['sap_energy_source']['pv_arrays'][pv_array_index].pop('pv_panel_manufacturer_name'))
                        except KeyError: pass

                        # Overshading-MCS
                        try: 
                            pv_array.add_overshading_mcs().code = str(j['data']['sap_energy_source']['pv_arrays'][pv_array_index].pop('overshading_mcs'))
                        except KeyError: pass
                                        
                        #
                        if len(j['data']['sap_energy_source']['pv_arrays'][pv_array_index]) == 0:
                            pv_arrays_c.append(pv_array_index)
                        else:
                            print(etree.tostring(sap_report, pretty_print=True).decode())
                            raise Exception('j', 'data', 'sap_energy_source', 'pv_arrays', pv_array_index, 
                                            list(j['data']['sap_energy_source']['pv_arrays'][pv_array_index])[0])
                    #    
                    for c1 in pv_arrays_c[::-1]: del j['data']['sap_energy_source']['pv_arrays'][c1]
                    if len(j['data']['sap_energy_source']['pv_arrays']) == 0: del j['data']['sap_energy_source']['pv_arrays']
                
                        

        
                # --- Wind-Turbines ---
                if 'wind_turbines' in j['data']['sap_energy_source']:
                    wind_turbines = sap_energy_source.add_wind_turbines()
                    wind_turbines_c = []
                    for wind_turbine_index in range(len(j['data']['sap_energy_source']['wind_turbines'])):
                        # --- Wind-Turbine ---
                        wind_turbine = wind_turbines.add_wind_turbine()
                        # Wind-Turbine-Manufacturer-Name

                        # Wind-Turbine-Certificate

                        # Wind-Turbine-Rotor-Diameter
                        try: 
                            wind_turbine.add_wind_turbine_rotor_diameter().code = str(j['data']['sap_energy_source']['wind_turbines'][wind_turbine_index].pop('wind_turbine_rotor_diameter'))
                        except KeyError: pass
                        # Wind-Turbine-Hub-Height
                        try: 
                            wind_turbine.add_wind_turbine_hub_height().code = str(j['data']['sap_energy_source']['wind_turbines'][wind_turbine_index].pop('wind_turbine_hub_height'))
                        except KeyError: pass
                        #                    
                        if len(j['data']['sap_energy_source']['wind_turbines'][wind_turbine_index]) == 0:
                            wind_turbines_c.append(wind_turbine_index)
                        else:
                            print(etree.tostring(sap_report, pretty_print=True).decode())
                            raise Exception('j', 'data', 'sap_energy_source', 'wind_turbines', wind_turbine_index, 
                                            list(j['data']['sap_energy_source']['wind_turbines'][wind_turbine_index])[0])
                    #    
                    for c1 in wind_turbines_c[::-1]: del j['data']['sap_energy_source']['wind_turbines'][c1]
                    if len(j['data']['sap_energy_source']['wind_turbines']) == 0: del j['data']['sap_energy_source']['wind_turbines']


                # Electricity-Tariff
                try: 
                    sap_energy_source.add_electricity_tariff().code = str(j['data']['sap_energy_source'].pop('electricity_tariff'))
                except KeyError: pass

                # Hydro-Electric-Generation

                # Hydro-Electric-Certificate

                # Hydro-Electric-Generation-Months

                # Is-Hydro-Output-Connected-To-Dwelling-Meter


                #
                if len(j['data']['sap_energy_source']) == 0:
                    del j['data']['sap_energy_source']
                else:
                    raise Exception('j', 'data', 'sap_energy_source', list(j['data']['sap_energy_source'])[0])

            if True:
                # --- SAP-Building-Parts ---
                if 'sap_building_parts' in j['data']:
                    sap_building_parts = sap_property_details.add_sap_building_parts()
                    sap_building_parts_c = []
                    for sap_building_part_index in range(len(j['data']['sap_building_parts'])):

                        
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
                        # Construction-Year
                        try: 
                            sap_building_part.add_construction_year().code = str(j['data']['sap_building_parts'][sap_building_part_index].pop('construction_year'))
                        except KeyError: pass

                        # Construction-Age-Band
                        try: 
                            sap_building_part.add_construction_age_band().code = str(j['data']['sap_building_parts'][sap_building_part_index].pop('construction_age_band'))
                        except KeyError: pass

                        # --- SAP-Openings ---
                        if 'sap_openings' in j['data']['sap_building_parts'][sap_building_part_index]:
                            sap_openings = sap_building_part.add_sap_openings()
                            sap_openings_c = []
                            for sap_opening_index in range(len(j['data']['sap_building_parts'][sap_building_part_index]['sap_openings'])):
                                # --- SAP-Opening ---
                                sap_opening = sap_openings.add_sap_opening()
                                # Name
                                try: 
                                    sap_opening.add_name().code = str(j['data']['sap_building_parts'][sap_building_part_index]['sap_openings'][sap_opening_index].pop('name'))
                                except KeyError: pass
                                # Type
                                try: 
                                    sap_opening.add_type().code = str(j['data']['sap_building_parts'][sap_building_part_index]['sap_openings'][sap_opening_index].pop('type'))
                                except KeyError: pass
                                # Location
                                try: 
                                    sap_opening.add_location().code = str(j['data']['sap_building_parts'][sap_building_part_index]['sap_openings'][sap_opening_index].pop('location'))
                                except KeyError: pass
                                # Orientation
                                try: 
                                    sap_opening.add_orientation().code = str(j['data']['sap_building_parts'][sap_building_part_index]['sap_openings'][sap_opening_index].pop('orientation'))
                                except KeyError: pass
                                # Width
                                try: 
                                    sap_opening.add_width().code = str(j['data']['sap_building_parts'][sap_building_part_index]['sap_openings'][sap_opening_index].pop('width'))
                                except KeyError: pass
                                # Height
                                try: 
                                    sap_opening.add_height().code = str(j['data']['sap_building_parts'][sap_building_part_index]['sap_openings'][sap_opening_index].pop('height'))
                                except KeyError: pass
                                # Pitch
                                try: 
                                    sap_opening.add_pitch().code = str(j['data']['sap_building_parts'][sap_building_part_index]['sap_openings'][sap_opening_index].pop('pitch'))
                                except KeyError: pass
                                #
                                if len(j['data']['sap_building_parts'][sap_building_part_index]['sap_openings'][sap_opening_index]) == 0:
                                    sap_openings_c.append(sap_opening_index)
                                else:
                                    print(etree.tostring(sap_report, pretty_print=True).decode())
                                    raise Exception('j', 'data', 'sap_building_parts', sap_building_part_index, 'sap_openings', sap_opening_index, 
                                                    list(j['data']['sap_building_parts'][sap_building_part_index]['sap_openings'][sap_opening_index])[0])
                            #    
                            for c1 in sap_openings_c[::-1]: del j['data']['sap_building_parts'][sap_building_part_index]['sap_openings'][c1]
                            if len(j['data']['sap_building_parts'][sap_building_part_index]['sap_openings']) == 0: del j['data']['sap_building_parts'][sap_building_part_index]['sap_openings']

                        # --- SAP-Roofs ---
                        if 'sap_roofs' in j['data']['sap_building_parts'][sap_building_part_index]:
                            sap_roofs = sap_building_part.add_sap_roofs()
                            sap_roofs_c = []
                            for sap_roof_index in range(len(j['data']['sap_building_parts'][sap_building_part_index]['sap_roofs'])):
                                # --- SAP-Roof ---
                                sap_roof = sap_roofs.add_sap_roof()
                                # Name
                                try: 
                                    sap_roof.add_name().code = str(j['data']['sap_building_parts'][sap_building_part_index]['sap_roofs'][sap_roof_index].pop('name'))
                                except KeyError: pass
                                # Description

                                # Roof-Type
                                try: 
                                    sap_roof.add_roof_type().code = str(j['data']['sap_building_parts'][sap_building_part_index]['sap_roofs'][sap_roof_index].pop('roof_type'))
                                except KeyError: pass
                                # Total-Roof-Area
                                try: 
                                    sap_roof.add_total_roof_area().code = str(j['data']['sap_building_parts'][sap_building_part_index]['sap_roofs'][sap_roof_index].pop('total_roof_area'))
                                except KeyError: pass
                                # U-Value
                                try: 
                                    sap_roof.add_u_value().code = str(j['data']['sap_building_parts'][sap_building_part_index]['sap_roofs'][sap_roof_index].pop('u_value'))
                                except KeyError: pass
                                # Kappa-Value
                                try: 
                                    sap_roof.add_kappa_value().code = str(j['data']['sap_building_parts'][sap_building_part_index]['sap_roofs'][sap_roof_index].pop('kappa_value'))
                                except KeyError: pass
                                #
                                if len(j['data']['sap_building_parts'][sap_building_part_index]['sap_roofs'][sap_roof_index]) == 0:
                                    sap_roofs_c.append(sap_roof_index)
                                else:
                                    print(etree.tostring(sap_report, pretty_print=True).decode())
                                    raise Exception('j', 'data', 'sap_building_parts', sap_building_part_index, 'sap_roofs', sap_roof_index, 
                                                    list(j['data']['sap_building_parts'][sap_building_part_index]['sap_roofs'][sap_roof_index])[0])
                            #    
                            for c1 in sap_roofs_c[::-1]: del j['data']['sap_building_parts'][sap_building_part_index]['sap_roofs'][c1]
                            if len(j['data']['sap_building_parts'][sap_building_part_index]['sap_roofs']) == 0: del j['data']['sap_building_parts'][sap_building_part_index]['sap_roofs']


                        if True:
                            # --- SAP-Floor-Dimensions ---
                            if 'sap_floor_dimensions' in j['data']['sap_building_parts'][sap_building_part_index]:
                                sap_floor_dimensions = sap_building_part.add_sap_floor_dimensions()
                                sap_floor_dimensions_c = []
                                for sap_floor_dimension_index in range(len(j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'])):
                                    # --- SAP-Floor-Dimension ---
                                    sap_floor_dimension = sap_floor_dimensions.add_sap_floor_dimension()
                                    # Name
                                    try: 
                                        sap_floor_dimension.add_name().code = str(j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index].pop('name'))
                                    except KeyError: pass
                                    # Storey
                                    try: 
                                        sap_floor_dimension.add_storey().code = str(j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index].pop('storey'))
                                    except KeyError: pass
                                    # Description
                                    try: 
                                        sap_floor_dimension.add_description().code = str(j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index].pop('description'))
                                    except KeyError: pass
                                    # Floor-Type
                                    try: 
                                        sap_floor_dimension.add_floor_type().code = str(j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index].pop('floor_type'))
                                    except KeyError: pass
                                    # Total-Floor-Area
                                    try: 
                                        sap_floor_dimension.add_total_floor_area().code = \
                                            str(j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index].pop('total_floor_area'))
                                    except KeyError: pass
                                    # Storey-Height
                                    try: 
                                        sap_floor_dimension.add_storey_height().code = str(j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index].pop('storey_height'))
                                    except KeyError: pass
                                    # Heat-Loss-Area
                                    try: 
                                        sap_floor_dimension.add_heat_loss_area().code = \
                                            str(j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index].pop('heat_loss_area'))
                                    except KeyError: pass
                                    # U-Value
                                    try: 
                                        sap_floor_dimension.add_u_value().code = str(j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index].pop('u_value'))
                                    except KeyError: pass
                                    # Kappa-Value
                                    try: 
                                        sap_floor_dimension.add_kappa_value().code = str(j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index].pop('kappa_value'))
                                    except KeyError: pass
                                    # Kappa-Value-From-Below
                                    try: 
                                        sap_floor_dimension.add_kappa_value_from_below().code = str(j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index].pop('kappa_value_from_below'))
                                    except KeyError: pass
                                    #
                                    if len(j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index]) == 0:
                                        sap_floor_dimensions_c.append(sap_floor_dimension_index)
                                    else:
                                        print(etree.tostring(sap_report, pretty_print=True).decode())
                                        raise Exception('j', 'data', 'sap_building_parts', sap_building_part_index, 'sap_floor_dimensions', sap_floor_dimension_index,
                                                        list(j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][sap_floor_dimension_index])[0])
                                #
                                for c1 in sap_floor_dimensions_c[::-1]: del j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions'][c1]
                                if len(j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions']) == 0: 
                                    del j['data']['sap_building_parts'][sap_building_part_index]['sap_floor_dimensions']

                        # --- SAP-Thermal-Bridges ---
                        if 'sap_thermal_bridges' in j['data']['sap_building_parts'][sap_building_part_index]:
                            sap_thermal_bridges = sap_building_part.add_sap_thermal_bridges()
                            # Thermal-Bridge-Code
                            try: 
                                sap_thermal_bridges.add_thermal_bridge_code().code = str(j['data']['sap_building_parts'][sap_building_part_index]['sap_thermal_bridges'].pop('thermal_bridge_code'))
                            except KeyError: pass    
                            # User-Defined-Y-Value
                            try: 
                                sap_thermal_bridges.add_user_defined_y_value().code = str(j['data']['sap_building_parts'][sap_building_part_index]['sap_thermal_bridges'].pop('user_defined_y_value'))
                            except KeyError: pass   
                            # Calculation-Reference
                            try: 
                                sap_thermal_bridges.add_calculation_reference().code = str(j['data']['sap_building_parts'][sap_building_part_index]['sap_thermal_bridges'].pop('calculation_reference'))
                            except KeyError: pass  
                            #
                            if 'thermal_bridges' in j['data']['sap_building_parts'][sap_building_part_index]['sap_thermal_bridges']:
                                thermal_bridges_c = []
                                for thermal_bridge_index in range(len(j['data']['sap_building_parts'][sap_building_part_index]['sap_thermal_bridges']['thermal_bridges'])):
                                    # --- SAP-Thermal-Bridge ---
                                    sap_thermal_bridge = sap_thermal_bridges.add_sap_thermal_bridge()
                                    # Thermal-Bridge-Type
                                    try: 
                                        sap_thermal_bridge.add_thermal_bridge_type().code = \
                                            str(j['data']['sap_building_parts'][sap_building_part_index]['sap_thermal_bridges']['thermal_bridges'][thermal_bridge_index].pop('thermal_bridge_type'))
                                    except KeyError: pass                                         
                                    # Length
                                    try: 
                                        sap_thermal_bridge.add_length().code = \
                                            str(j['data']['sap_building_parts'][sap_building_part_index]['sap_thermal_bridges']['thermal_bridges'][thermal_bridge_index].pop('length'))
                                    except KeyError: pass 
                                    # Psi-Value
                                    try: 
                                        sap_thermal_bridge.add_psi_value().code = \
                                            str(j['data']['sap_building_parts'][sap_building_part_index]['sap_thermal_bridges']['thermal_bridges'][thermal_bridge_index].pop('psi_value'))
                                    except KeyError: pass 
                                    # Psi-Value-Source
                                    try: 
                                        sap_thermal_bridge.add_psi_value_source().code = \
                                            str(j['data']['sap_building_parts'][sap_building_part_index]['sap_thermal_bridges']['thermal_bridges'][thermal_bridge_index].pop('psi_value_source'))
                                    except KeyError: pass 
                                    # Psi-Value-Calculation-Reference
                                    try: 
                                        sap_thermal_bridge.add_psi_value_calculation_reference().code = \
                                            str(j['data']['sap_building_parts'][sap_building_part_index]['sap_thermal_bridges']['thermal_bridges'][thermal_bridge_index].pop('psi_value_calculation_reference'))
                                    except KeyError: pass
                                    #
                                    if len(j['data']['sap_building_parts'][sap_building_part_index]['sap_thermal_bridges']['thermal_bridges'][thermal_bridge_index]) == 0:
                                        thermal_bridges_c.append(thermal_bridge_index)
                                    else:
                                        print(etree.tostring(sap_report, pretty_print=True).decode())
                                        raise Exception('j', 'data', 'sap_building_parts', sap_building_part_index, 'sap_thermal_bridges', 'thermal_bridges', thermal_bridge_index, 
                                                        list(j['data']['sap_building_parts'][sap_building_part_index]['sap_thermal_bridges']['thermal_bridges'][thermal_bridge_index])[0])
                                #    
                                for c1 in thermal_bridges_c[::-1]: del j['data']['sap_building_parts'][sap_building_part_index]['sap_thermal_bridges']['thermal_bridges'][c1]
                                if len(j['data']['sap_building_parts'][sap_building_part_index]['sap_thermal_bridges']['thermal_bridges']) == 0: 
                                    del j['data']['sap_building_parts'][sap_building_part_index]['sap_thermal_bridges']['thermal_bridges']


                            #
                            if len(j['data']['sap_building_parts'][sap_building_part_index]['sap_thermal_bridges']) == 0:
                                del j['data']['sap_building_parts'][sap_building_part_index]['sap_thermal_bridges']
                            else:
                                print(etree.tostring(sap_report, pretty_print=True).decode())
                                raise Exception('j', 'data', 'sap_building_parts', sap_building_part_index, 'sap_thermal_bridges', 
                                                list(j['data']['sap_building_parts'][sap_building_part_index]['sap_thermal_bridges'])[0])
                            

                        # --- SAP-Walls ---
                        if 'sap_walls' in j['data']['sap_building_parts'][sap_building_part_index]:
                            sap_walls = sap_building_part.add_sap_walls()
                            sap_walls_c = []
                            for sap_wall_index in range(len(j['data']['sap_building_parts'][sap_building_part_index]['sap_walls'])):
                                # --- SAP_Wall ---
                                sap_wall = sap_walls.add_sap_wall()
                                # Name
                                try: 
                                    sap_wall.add_name().code = str(j['data']['sap_building_parts'][sap_building_part_index]['sap_walls'][sap_wall_index].pop('name'))
                                except KeyError: pass                                    
                                # Description
                                try: 
                                    sap_wall.add_description().code = str(j['data']['sap_building_parts'][sap_building_part_index]['sap_walls'][sap_wall_index].pop('description'))
                                except KeyError: pass 
                                # Wall-Type
                                try: 
                                    sap_wall.add_wall_type().code = str(j['data']['sap_building_parts'][sap_building_part_index]['sap_walls'][sap_wall_index].pop('wall_type'))
                                except KeyError: pass  
                                # Total-Wall-Area
                                try: 
                                    sap_wall.add_total_wall_area().code = str(j['data']['sap_building_parts'][sap_building_part_index]['sap_walls'][sap_wall_index].pop('total_wall_area'))
                                except KeyError: pass  
                                # U-Value
                                try: 
                                    sap_wall.add_u_value().code = str(j['data']['sap_building_parts'][sap_building_part_index]['sap_walls'][sap_wall_index].pop('u_value'))
                                except KeyError: pass  
                                # Is-Curtain-Walling
                                try: 
                                    sap_wall.add_is_curtain_walling().code = str(j['data']['sap_building_parts'][sap_building_part_index]['sap_walls'][sap_wall_index].pop('is_curtain_walling'))
                                except KeyError: pass  
                                # Kappa-Value
                                try: 
                                    sap_wall.add_kappa_value().code = str(j['data']['sap_building_parts'][sap_building_part_index]['sap_walls'][sap_wall_index].pop('kappa_value'))
                                except KeyError: pass  
                                #
                                if len(j['data']['sap_building_parts'][sap_building_part_index]['sap_walls'][sap_wall_index]) == 0:
                                    sap_walls_c.append(sap_wall_index)
                                else:
                                    print(etree.tostring(sap_report, pretty_print=True).decode())
                                    raise Exception('j', 'data', 'sap_building_parts', sap_building_part_index, 'sap_walls', sap_wall_index, 
                                                    list(j['data']['sap_building_parts'][sap_building_part_index]['sap_walls'][sap_wall_index])[0])
                            #    
                            for c1 in sap_walls_c[::-1]: del j['data']['sap_building_parts'][sap_building_part_index]['sap_walls'][c1]
                            if len(j['data']['sap_building_parts'][sap_building_part_index]['sap_walls']) == 0: del j['data']['sap_building_parts'][sap_building_part_index]['sap_walls']
                        #
                        if len(j['data']['sap_building_parts'][sap_building_part_index]) == 0:
                            sap_building_parts_c.append(sap_building_part_index)
                        else:
                            print(etree.tostring(sap_report, pretty_print=True).decode())
                            raise Exception('j', 'data', 'sap_building_parts', sap_building_part_index, list(j['data']['sap_building_parts'][sap_building_part_index])[0])
                    #    
                    for c1 in sap_building_parts_c[::-1]: del j['data']['sap_building_parts'][c1]
                    if len(j['data']['sap_building_parts']) == 0: del j['data']['sap_building_parts']
            
        if True:
            # --- SAP-Opening-Types ---
            if 'sap_opening_types' in j['data']:
                sap_opening_types = sap_property_details.add_sap_opening_types()
                sap_opening_types_c = []
                for sap_opening_index in range(len(j['data']['sap_opening_types'])):
                    # --- SAP-Opening-Type ---
                    sap_opening_type = sap_opening_types.add_sap_opening_type()
                    # Name
                    try: 
                        sap_opening_type.add_name().code = str(j['data']['sap_opening_types'][sap_opening_index].pop('name'))
                    except KeyError: pass
                    # Description
                    try: 
                        sap_opening_type.add_description().code = str(j['data']['sap_opening_types'][sap_opening_index].pop('description'))
                    except KeyError: pass
                    # Data-Source
                    try: 
                        sap_opening_type.add_data_source().code = str(j['data']['sap_opening_types'][sap_opening_index].pop('data_source'))
                    except KeyError: pass
                    # Type
                    try: 
                        sap_opening_type.add_type().code = str(j['data']['sap_opening_types'][sap_opening_index].pop('type'))
                    except KeyError: pass
                    # Glazing-Type
                    try: 
                        sap_opening_type.add_glazing_type().code = str(j['data']['sap_opening_types'][sap_opening_index].pop('glazing_type'))
                    except KeyError: pass
                    # Glazing-Gap
                    try: 
                        sap_opening_type.add_glazing_gap().code = str(j['data']['sap_opening_types'][sap_opening_index].pop('glazing_gap'))
                    except KeyError: pass
                    # IsArgonFilled
                    try: 
                        sap_opening_type.add_isargonfilled().code = str(j['data']['sap_opening_types'][sap_opening_index].pop('isargonfilled'))
                    except KeyError: pass
                    # IsKryptonFilled
                    # Frame-Type
                    try: 
                        sap_opening_type.add_frame_type().code = str(j['data']['sap_opening_types'][sap_opening_index].pop('frame_type'))
                    except KeyError: pass
                    # Solar-Transmittance
                    try: 
                        sap_opening_type.add_solar_transmittance().code = str(j['data']['sap_opening_types'][sap_opening_index].pop('solar_transmittance'))
                    except KeyError: pass
                    # Frame-Factor
                    try: 
                        sap_opening_type.add_frame_factor().code = str(j['data']['sap_opening_types'][sap_opening_index].pop('frame_factor'))
                    except KeyError: pass
                    # U-Value
                    try: 
                        sap_opening_type.add_u_value().code = str(j['data']['sap_opening_types'][sap_opening_index].pop('u_value'))
                    except KeyError: pass

                    if len(j['data']['sap_opening_types'][sap_opening_index]) == 0:
                        sap_opening_types_c.append(sap_opening_index)
                    else:
                        print(etree.tostring(sap_report, pretty_print=True).decode())
                        raise Exception('j', 'data', 'sap_opening_types', sap_opening_index, list(j['data']['sap_opening_types'][sap_opening_index])[0])
                #    
                for c1 in sap_opening_types_c[::-1]: del j['data']['sap_opening_types'][c1]
                if len(j['data']['sap_opening_types']) == 0: del j['data']['sap_opening_types']
                
            

        if True:
            # --- SAP-Ventilation ---
            if 'sap_ventilation' in j['data']:
                sap_ventilation = sap_property_details.add_sap_ventilation()
                # Closed-Flues-Count
                try: 
                    sap_ventilation.add_closed_flues_count().code = str(j['data']['sap_ventilation'].pop('closed_flues_count'))
                except KeyError: pass
                # Open-Flues-Count
                try: 
                    sap_ventilation.add_open_flues_count().code = str(j['data']['sap_ventilation'].pop('open_flues_count'))
                except KeyError: pass
                # Boilers-Flues-Count
                try: 
                    sap_ventilation.add_boilers_flues_count().code = str(j['data']['sap_ventilation'].pop('boilers_flues_count'))
                except KeyError: pass
                # Other-Flues-Count
                try: 
                    sap_ventilation.add_other_flues_count().code = str(j['data']['sap_ventilation'].pop('other_flues_count'))
                except KeyError: pass
                # Open-Chimneys-Count
                try: 
                    sap_ventilation.add_open_chimneys_count().code = str(j['data']['sap_ventilation'].pop('open_chimneys_count'))
                except KeyError: pass
                # Blocked-Chimneys-Count
                try: 
                    sap_ventilation.add_blocked_chimneys_count().code = str(j['data']['sap_ventilation'].pop('blocked_chimneys_count'))
                except KeyError: pass

                # Fans-Vent-Count

                # Flueless-Gas-Fire-Count
                try: 
                    sap_ventilation.add_flueless_gas_fires_count().code = str(j['data']['sap_ventilation'].pop('flueless_gas_fires_count'))
                except KeyError: pass
                # Pressure-Test
                try: 
                    sap_ventilation.add_pressure_test().code = str(j['data']['sap_ventilation'].pop('pressure_test'))
                except KeyError: pass
        
        #         # Pressure-Test-Certificate-Number
        #         try: 
        #             sap_ventilation.add_pressure_test_certificate_number().code = str(j['data']['sap_ventilation'].pop('pressure_test_certificate_number'))
        #         except KeyError: pass

                # Air-Permeability
                try: 
                    sap_ventilation.add_air_permeability().code = str(j['data']['sap_ventilation'].pop('air_permeability'))
                except KeyError: pass
                # Ground-Floor-Type
                try: 
                    sap_ventilation.add_ground_floor_type().code = str(j['data']['sap_ventilation'].pop('ground_floor_type'))
                except KeyError: pass
                # Wall-Type
                try: 
                    sap_ventilation.add_wall_type().code = str(j['data']['sap_ventilation'].pop('wall_type'))
                except KeyError: pass
                # Has-Draught-Lobby
                try: 
                    sap_ventilation.add_has_draught_lobby().code = str(j['data']['sap_ventilation'].pop('has_draught_lobby'))
                except KeyError: pass

                # DraughtStripping
                try: 
                    sap_ventilation.add_draughtstripping().code = str(j['data']['sap_ventilation'].pop('draughtstripping'))
                except KeyError: pass

                # Sheltered-Sides-Count
                try: 
                    sap_ventilation.add_sheltered_sides_count().code = str(j['data']['sap_ventilation'].pop('sheltered_sides_count'))
                except KeyError: pass
                # Ventilation-Type
                try: 
                    sap_ventilation.add_ventilation_type().code = str(j['data']['sap_ventilation'].pop('ventilation_type'))
                except KeyError: pass
                # Mechanical-Ventilation-Data-Source
                try: 
                    sap_ventilation.add_mechanical_ventilation_data_source().code = str(j['data']['sap_ventilation'].pop('mechanical_ventilation_data_source'))
                except KeyError: pass
                # Mechanical-Vent-System-Index-Number
                try: 
                    sap_ventilation.add_mechanical_vent_system_index_number().code = str(j['data']['sap_ventilation'].pop('mechanical_vent_system_index_number'))
                except KeyError: pass

                # Mechanical-Vent-Commissioning-Certificate-Number

                # Mechanical-Vent-Installation-Engineer

                # Mechanical-Vent-System-Make-Model
                try: 
                    sap_ventilation.add_mechanical_vent_system_make_model().code = str(j['data']['sap_ventilation'].pop('mechanical_vent_system_make_model'))
                except KeyError: pass

                # Wet-Rooms-Count
                try: 
                    sap_ventilation.add_wet_rooms_count().code = str(j['data']['sap_ventilation'].pop('wet_rooms_count'))
                except KeyError: pass

                # Mechanical-Vent-Specific-Fan-Power
                try: 
                    sap_ventilation.add_mechanical_vent_specific_fan_power().code = str(j['data']['sap_ventilation'].pop('mechanical_vent_specific_fan_power'))
                except KeyError: pass

                # Mechanical-Vent-Heat-Recovery-Efficiency
                try: 
                    sap_ventilation.add_mechanical_vent_heat_recovery_efficiency().code = str(j['data']['sap_ventilation'].pop('mechanical_vent_heat_recovery_efficiency'))
                except KeyError: pass

                # Mechanical-Vent-Duct-Type
                try: 
                    sap_ventilation.add_mechanical_vent_duct_type().code = str(j['data']['sap_ventilation'].pop('mechanical_vent_duct_type'))
                except KeyError: pass

                # Mechanical-Vent-Duct-Insulation
                try: 
                    sap_ventilation.add_mechanical_vent_duct_insulation().code = str(j['data']['sap_ventilation'].pop('mechanical_vent_duct_insulation'))
                except KeyError: pass

                # Mechanical-Vent-Duct-Insulation-Level
                try: 
                    sap_ventilation.add_mechanical_vent_duct_insulation_level().code = str(j['data']['sap_ventilation'].pop('mechanical_vent_duct_insulation_level'))
                except KeyError: pass

                # Mechanical-Vent-Duct-Placement
                try: 
                    sap_ventilation.add_mechanical_vent_duct_placement().code = str(j['data']['sap_ventilation'].pop('mechanical_vent_duct_placement'))
                except KeyError: pass

                # Mechanical-Vent-Measured-Installation
                try: 
                    sap_ventilation.add_mechanical_vent_measured_installation().code = str(j['data']['sap_ventilation'].pop('mechanical_vent_measured_installation'))
                except KeyError: pass

                # Kitchen-Room-Fans-Count
                try: 
                    sap_ventilation.add_kitchen_room_fans_count().code = str(j['data']['sap_ventilation'].pop('kitchen_room_fans_count'))
                except KeyError: pass

                # Kitchen-Room-Fans-Specific-Power
                try: 
                    sap_ventilation.add_kitchen_room_fans_specific_power().code = str(j['data']['sap_ventilation'].pop('kitchen_room_fans_specific_power'))
                except KeyError: pass

                # Non-Kitchen-Room-Fans-Count
                try: 
                    sap_ventilation.add_non_kitchen_room_fans_count().code = str(j['data']['sap_ventilation'].pop('non_kitchen_room_fans_count'))
                except KeyError: pass

                # Non-Kitchen-Room-Fans-Specific-Power
                try: 
                    sap_ventilation.add_non_kitchen_room_fans_specific_power().code = str(j['data']['sap_ventilation'].pop('non_kitchen_room_fans_specific_power'))
                except KeyError: pass

                # Kitchen-Duct-Fans-Count
                try: 
                    sap_ventilation.add_kitchen_duct_fans_count().code = str(j['data']['sap_ventilation'].pop('kitchen_duct_fans_count'))
                except KeyError: pass

                # Kitchen-Duct-Fans-Specific-Power
                try: 
                    sap_ventilation.add_kitchen_duct_fans_specific_power().code = str(j['data']['sap_ventilation'].pop('kitchen_duct_fans_specific_power'))
                except KeyError: pass

                # Non-Kitchen-Duct-Fans-Count
                try: 
                    sap_ventilation.add_non_kitchen_duct_fans_count().code = str(j['data']['sap_ventilation'].pop('non_kitchen_duct_fans_count'))
                except KeyError: pass

                # Non-Kitchen-Duct-Fans-Specific-Power
                try: 
                    sap_ventilation.add_non_kitchen_duct_fans_specific_power().code = str(j['data']['sap_ventilation'].pop('non_kitchen_duct_fans_specific_power'))
                except KeyError: pass

                # Kitchen-Wall-Fans-Count
                try: 
                    sap_ventilation.add_kitchen_wall_fans_count().code = str(j['data']['sap_ventilation'].pop('kitchen_wall_fans_count'))
                except KeyError: pass

                # Kitchen-Wall-Fans-Specific-Power
                try: 
                    sap_ventilation.add_kitchen_wall_fans_specific_power().code = str(j['data']['sap_ventilation'].pop('kitchen_wall_fans_specific_power'))
                except KeyError: pass

                # Non-Kitchen-Wall-Fans-Count
                try: 
                    sap_ventilation.add_non_kitchen_wall_fans_count().code = str(j['data']['sap_ventilation'].pop('non_kitchen_wall_fans_count'))
                except KeyError: pass

                # Non-Kitchen-Wall-Fans-Specific-Power
                try: 
                    sap_ventilation.add_non_kitchen_wall_fans_specific_power().code = str(j['data']['sap_ventilation'].pop('non_kitchen_wall_fans_specific_power'))
                except KeyError: pass                

                # Extract-Fans-Count
                try: 
                    sap_ventilation.add_extract_fans_count().code = str(j['data']['sap_ventilation'].pop('extract_fans_count'))
                except KeyError: pass

                # PSV-Count
                try: 
                    sap_ventilation.add_psv_count().code = str(j['data']['sap_ventilation'].pop('psv_count'))
                except KeyError: pass

                # Is-Mechanical-Vent-Approved-Installer-Scheme
                try: 
                    sap_ventilation.add_is_mechanical_vent_approved_installer_scheme().code = str(j['data']['sap_ventilation'].pop('is_mechanical_vent_approved_installer_scheme'))
                except KeyError: pass

                # Mechanical-Vent-Ducts-Index-Number
                try: 
                    sap_ventilation.add_mechanical_vent_ducts_index_number().code = str(j['data']['sap_ventilation'].pop('mechanical_vent_ducts_index_number'))
                except KeyError: pass

                if len(j['data']['sap_ventilation']) == 0:
                    del j['data']['sap_ventilation']
                else:
                    raise Exception('j', 'data', 'sap_ventilation', list(j['data']['sap_ventilation'])[0])

        if True:
            # --- SAP-Lighting ---
            if 'sap_lighting' in j['data']:
                sap_lighting = sap_property_details.add_sap_lighting()
                # --- Fixed-Lights ---
                if len(j['data']['sap_lighting']) > 0:
                    fixed_lights = sap_lighting.add_fixed_lights()
                #
                fixed_light_c = []
                for fixed_light_index in range(len(j['data']['sap_lighting'])):
                    if isinstance(j['data']['sap_lighting'][fixed_light_index], list):
                        fixed_light_c2 = []
                        for fixed_light_index2 in range(len(j['data']['sap_lighting'][fixed_light_index])):
                            # --- Fixed-Light ---
                            fixed_light = fixed_lights.add_fixed_light()
                            # Lighting-Efficacy
                            try: 
                                fixed_light.add_lighting_efficacy().code = str(j['data']['sap_lighting'][fixed_light_index][fixed_light_index2].pop('lighting_efficacy'))
                            except KeyError: pass
                            # Lighting-Power
                            try: 
                                fixed_light.add_lighting_power().code = str(j['data']['sap_lighting'][fixed_light_index][fixed_light_index2].pop('lighting_power'))
                            except KeyError: pass
                            # Lighting-Outlets
                            try: 
                                fixed_light.add_lighting_outlets().code = str(j['data']['sap_lighting'][fixed_light_index][fixed_light_index2].pop('lighting_outlets'))
                            except KeyError: pass
                            #
                            if len(j['data']['sap_lighting'][fixed_light_index][fixed_light_index2]) == 0:
                                fixed_light_c2.append(fixed_light_index2)
                            else:
                                print(etree.tostring(sap_report, pretty_print=True).decode())
                                raise Exception('j', 'data', 'sap_lighting', fixed_light_index, fixed_light_index2, list(j['data']['sap_lighting'][fixed_light_index][fixed_light_index2])[0])
                        for c1 in fixed_light_c2[::-1]: del j['data']['sap_lighting'][fixed_light_index][c1]
                    #
                    if len(j['data']['sap_lighting'][fixed_light_index]) == 0:
                        fixed_light_c.append(fixed_light_index)
                    else:
                        print(etree.tostring(sap_report, pretty_print=True).decode())
                        raise Exception('j', 'data', 'sap_lighting', fixed_light_index, list(j['data']['sap_lighting'][fixed_light_index])[0])
                for c1 in fixed_light_c[::-1]: del j['data']['sap_lighting'][c1]
                if len(j['data']['sap_lighting']) == 0: del j['data']['sap_lighting']
                    
        if True:
            # --- SAP-Deselected-Improvements ---
            if 'sap_deselected_improvements' in j['data']:
                sap_deselected_improvements = sap_property_details.add_sap_deselected_improvements()
                sap_deselected_improvements_c = []
                for sap_deselected_improvement_index in range(len(j['data']['sap_deselected_improvements'])):
                    # Deselected-Improvement-Measure
                    sap_deselected_improvements.add_deselected_improvement_measure().code = str(j['data']['sap_deselected_improvements'][sap_deselected_improvement_index])
                    #
                del j['data']['sap_deselected_improvements']
                
        if True:
            # --- SAP-Flat-Details ---
            if 'sap_flat_details' in j['data']:
                sap_flat_details = sap_property_details.add_sap_flat_details()
                # Level
                try: 
                    sap_flat_details.add_level().code = str(j['data']['sap_flat_details'].pop('level'))
                except KeyError: pass
                # Storeys
                try: 
                    sap_flat_details.add_storeys().code = str(j['data']['sap_flat_details'].pop('storeys'))
                except KeyError: pass
                #
                if len(j['data']['sap_flat_details']) == 0:
                    del j['data']['sap_flat_details']
                else:
                    print(etree.tostring(sap_report, pretty_print=True).decode())
                    raise Exception('j', 'data', 'sap_flat_details', list(j['data']['sap_flat_details'])[0])

        if True:
            # --- SAP-Special-Features ---
            if 'sap_special_features' in j['data']:
                sap_special_features = sap_property_details.add_sap_special_features()
                sap_special_features_c = []
                for sap_special_feature_index in range(len(j['data']['sap_special_features'])):
                    # --- SAP-Special-Feature
                    sap_special_feature = sap_special_features.add_sap_special_feature()
                    # Description
                    try: 
                        sap_special_feature.add_description().code = str(j['data']['sap_special_features'][sap_special_feature_index].pop('description'))
                    except KeyError: pass
                    #
                    if 'energy_feature' in j['data']['sap_special_features'][sap_special_feature_index]:
                        # --- Energy-Feature ---
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

                        # Air-Change-Rates

                        #
                        if len(j['data']['sap_special_features'][sap_special_feature_index]['energy_feature']) == 0:
                            del j['data']['sap_special_features'][sap_special_feature_index]['energy_feature']
                        else:
                            print(etree.tostring(sap_report, pretty_print=True).decode())
                            raise Exception('j', 'data', 'sap_special_features', sap_special_feature_index, 'energy_feature', list(j['data']['sap_special_features'][sap_special_feature_index]['energy_feature'])[0])
                    #
                    if 'emissions_feature' in j['data']['sap_special_features'][sap_special_feature_index]:
                        # --- Emissions-Feature ---
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
                            print(etree.tostring(sap_report, pretty_print=True).decode())
                            raise Exception('j', 'data', 'sap_special_features', sap_special_feature_index, 'emissions_feature', list(j['data']['sap_special_features'][sap_special_feature_index]['emissions_feature'])[0])


                    #
                    if len(j['data']['sap_special_features'][sap_special_feature_index]) == 0:
                        sap_special_features_c.append(sap_special_feature_index)
                    else:
                        print(etree.tostring(sap_report, pretty_print=True).decode())
                        raise Exception('j', 'data', 'sap_special_features', sap_special_feature_index, list(j['data']['sap_special_features'][sap_special_feature_index])[0])
                for c1 in sap_special_features_c[::-1]: del j['data']['sap_special_features'][c1]
                if len(j['data']['sap_special_features']) == 0: del j['data']['sap_special_features']

        # Design-Water-Use
        try: 
            sap_property_details.add_design_water_use().code = str(j['data'].pop('design_water_use'))
        except KeyError: pass

        if True:
            # --- SAP-Cooling ---
            if 'sap_cooling' in j['data']:
                sap_cooling = sap_property_details.add_sap_cooling()
                # Cooled-Area
                try: 
                    sap_cooling.add_cooled_area().code = str(j['data']['sap_cooling'].pop('cooled_area'))
                except KeyError: pass
                # Cooling-System-Data-Source
                try: 
                    sap_cooling.add_cooling_system_data_source().code = str(j['data']['sap_cooling'].pop('cooling_system_data_source'))
                except KeyError: pass
                # Cooling-System-Class
                try: 
                    sap_cooling.add_cooling_system_class().code = str(j['data']['sap_cooling'].pop('cooling_system_class'))
                except KeyError: pass
                # System-Energy-Efficiency-Ratio
                try: 
                    sap_cooling.add_system_energy_efficiency_ratio().code = str(j['data']['sap_cooling'].pop('system_energy_efficiency_ratio'))
                except KeyError: pass
                #
                if len(j['data']['sap_cooling']) == 0:
                    del j['data']['sap_cooling']
                else:
                    print(etree.tostring(sap_report, pretty_print=True).decode())
                    raise Exception('j', 'data', 'sap_cooling', list(j['data']['sap_cooling'])[0])


    
    if len(j['data']) == 0:
        del j['data']
    else:
        print(etree.tostring(sap_report, pretty_print=True).decode())
        raise Exception('j', 'data', list(j['data'])[0])

    if len(j) > 0:
        raise Exception('j', list(j)[0])

    return tree, sap_report

    