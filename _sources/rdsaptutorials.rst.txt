.. _rdsap10_tutorials:

RdSAP10 Tutorials
=================

.. _running_a_rdsap10_calculation:

Running a RdSAP10 calculation
-----------------------------

An RdSAP10 calculation can be run using:

.. code-block:: Python

   import sap10calcs
   result = sap10calcs.rdsap(
       input_file = 'my_rdsap10_file.xml',
       auth_token = None
   )

This uses the :py:func:`sap10calcs.rdsap` function:

- ``input_file`` is an RdSAP10 XML file provided by the user and stored on the local computer.
- ``auth_token`` is an authorization token for the remote API service provided by the user (see `here <https://netzeroapis.com/redoc#section/Authorization>`__ for details).
- ``result`` is a Python dictionary which contains the final RdSAP calculated values (such as energy consumption and the SAP rating), the intermediate calculations and any error messages.

In practice, I would use this in a wider function that also saves the complete output of the :py:func:`sap10calcs.rdsap` function, saves the final SAP10 XML file (ready for use in :py:func:`sap10calcs.calculate`) and prints out any error message. This might look like:

..  code-block:: Python

    import sap10calcs
    import json
    from io import StringIO
    
    def run_rdsap(
        fp_in,  # filepath to the input RdSAP10 XML file.
        fp_out_json,  # filepath for the output from the sap10calcs.rdsap function.
        fp_out_xml,  # filepath for the final SAP10 XML file.
        auth_token = None
        ):
        ""
        # run RdSAP engine
        result = sap10calcs.rdsap(
            input_file = fp_in, 
            auth_token = auth_token
        )
    
        # save full output - useful for fixing errors...
        with open(fp_out_json, 'w') as f: json.dump(result, f, indent = 4)
    
        # print error message if present
        if not result['rdsap_calculation_error_traceback'] is None:
            print('\n', result['rdsap_calculation_error_traceback'])
        else:
            # save SAP10 XML file
            tree, sap_report = sap10calcs.parse_xml(StringIO(result['sap_xml']))
            tree.write(fp_out_xml, encoding="utf-8", xml_declaration=True, pretty_print=True)
    
        return result
    
    run_rdsap('my_rdsap10_file.xml', 'rdsap_result.json', 'my_sap10_file.xml') 

The SAP10 XML file is returned as a string in the ``result`` dictionary. So this is converted into a file-like object using `StringIO <https://docs.python.org/3/library/io.html#io.StringIO>`__ before being read using the :py:func:`sap10calcs.parse_xml` function.

The ``tree`` variable is a standard `lxml ElementTree <https://lxml.de/tutorial.html>`__. The ``write`` method from the lxml package is used to save the XML to a local file.


.. _editing_an_existing_rdsap_xml_file:

Editing an existing RdSAP XML input file
----------------------------------------

This code uses the :py:func:`sap10calcs.parse_rsdap_xml` function to read an RdSAP XML file. It then updates the country code and the number of doors, and saves the XML file with a new name.

.. code-block:: Python

   import sap10calcs
   tree, rdsap_report = sap10calcs.parse_rdsap_xml('my_rdsap10_file.xml')
   rdsap_report.report_header.country_code.value = 'Wales'
   rdsap_report.sap_data.sap_property_details.door_count.value = 2
   tree.write('my_rdsap10_file_edited.xml', encoding="utf-8", xml_declaration=True, pretty_print=True)

.. _creating_a_rdsap_xml_input_file_from_scratch:

Creating a RdSAP XML input file from scratch
--------------------------------------------

This code uses the :py:func:`sap10calcs.create_rdsap_report_xml` function to create an empty :py:class:`~sap10calcs.classes_RdSAP_Schema_21_0_0.RdSAP_Report` object, and then uses the object properties and methods to create a complete RdSAP input XML file.

..  code-block:: python

    import sap10calcs
    
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
    sap_heating.add_water_heating_fuel().code = '26'
    sap_heating.add_water_heating_code().value = 901  # From main heating system
    sap_heating.add_immersion_heating_type().value = 'not applicable'
    sap_heating.add_cylinder_size().value = 'No Cylinder'
    sap_heating.add_has_fixed_air_conditioning().value = False
    
    # main_heating_details
    main_heating_details = sap_heating.add_main_heating_details()
    
    # main_heating_1
    main_heating_1 = main_heating_details.add_main_heating()
    main_heating_1.add_main_heating_number().value = 1
    main_heating_1.add_main_heating_category().value = 'boiler with radiators or underfloor heating'
    main_heating_1.add_main_fuel_type().code = '26'
    main_heating_1.add_main_heating_control().value = 2106  # "Programmer, room thermostat and TRVs"
    main_heating_1.add_main_heating_data_source().value = 'SAP Table'
    main_heating_1.add_sap_main_heating_code().value = 104  
        # "Gas boilers (including mains gas, LPG and biogas) 1998 or later: Condensing combi with automatic ignition"
    main_heating_1.add_boiler_ignition_type().value = 'auto-ignition'
    main_heating_1.add_boiler_flue_type().value = 'open'
    main_heating_1.add_fan_flue_present().value = 'Yes'
    main_heating_1.add_heat_emitter_type().value = 'radiators'
    main_heating_1.add_main_heating_fraction().value = 1
    main_heating_1.add_has_fghrs().value = 'No'
    main_heating_1.add_emitter_temperature().value = 'unknown'
    main_heating_1.add_central_heating_pump_age().value = 'unknown'
    
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
    #sap_building_part_1.add_floor_insulation_thickness().value = '50mm'
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
    
    # sap_windows
    sap_windows = sap_property_details.add_sap_windows()
    
    # sap_window_1
    sap_window_1 = sap_windows.add_sap_window()
    sap_window_1.add_window_location().value = 'Main Property'
    sap_window_1.add_window_height().value = 1
    sap_window_1.add_window_width().value = 1
    sap_window_1.add_draught_proofed().value = False
    sap_window_1.add_glazing_type().value = 'single glazing'
    sap_window_1.add_window_type().value = 'window'
    sap_window_1.add_orientation().value = 'South'
    window_transmission_details_1 = sap_window_1.add_window_transmission_details()
    window_transmission_details_1.add_data_source().value = 'manufacturer data'
    window_transmission_details_1.add_u_value().value = 1
    window_transmission_details_1.add_solar_transmittance().value = 0.8
    sap_window_1.add_frame_factor().value = 0.9
    sap_window_1.add_pvc_frame().value = True
    sap_window_1.add_window_wall_type().value = 'External wall type 1'
    sap_window_1.add_permanent_shutters_present().value = 'No'
    sap_window_1.add_permanent_shutters_insulated().value = 'No'
    
    tree.write('my_rdsap10_file.xml', encoding="utf-8", xml_declaration=True, pretty_print=True)

This creates the following XML file (shown below using the :py:func:`display` function):

..  code-block:: XML

    
    <RdSAP-Report xmlns="https://epbr.digital.communities.gov.uk/xsd/rdsap">
      <Schema-Version-Original>RdSAP-Schema-21.0.0</Schema-Version-Original>
      <SAP-Version>10.2 ['SAP version 10.2, dated April 2023']</SAP-Version>
      <Report-Header>
        <Country-Code>ENG ['England']</Country-Code>
      </Report-Header>
      <SAP-Data>
        <SAP-Property-Details>
          <Property-Type>0 ['House']</Property-Type>
          <Built-Form>1 ['Detached']</Built-Form>
          <Extensions-Count>0</Extensions-Count>
          <Habitable-Room-Count>1</Habitable-Room-Count>
          <Heated-Room-Count>1</Heated-Room-Count>
          <Low-Energy-Fixed-Lighting-Bulbs-Count>0</Low-Energy-Fixed-Lighting-Bulbs-Count>
          <Incandescent-Fixed-Lighting-Bulbs-Count>0</Incandescent-Fixed-Lighting-Bulbs-Count>
          <Measurement-Type>1 ['Internal']</Measurement-Type>
          <Solar-Water-Heating>N ['No']</Solar-Water-Heating>
          <Pressure-Test>6 ['yes - measured at 50 Pa']</Pressure-Test>
          <Air-Permeability>0</Air-Permeability>
          <Mechanical-Ventilation>0 ['natural']</Mechanical-Ventilation>
          <Conservatory-Type>1 ['no conservatory']</Conservatory-Type>
          <Door-Count>0</Door-Count>
          <Percent-Draughtproofed>0</Percent-Draughtproofed>
          <SAP-Heating>
            <Water-Heating-Fuel>26 ['mains gas (not community)']</Water-Heating-Fuel>
            <Water-Heating-Code>901</Water-Heating-Code>
            <Immersion-Heating-Type>NA ['not applicable']</Immersion-Heating-Type>
            <Cylinder-Size>1 ['No Cylinder']</Cylinder-Size>
            <Has-Fixed-Air-Conditioning>0 ['False']</Has-Fixed-Air-Conditioning>
            <Main-Heating-Details>
              <Main-Heating>
                <Main-Heating-Number>1</Main-Heating-Number>
                <Main-Heating-Category>2 ['boiler with radiators or underfloor heating']</Main-Heating-Category>
                <Main-Fuel-Type>26 ['mains gas (not community)']</Main-Fuel-Type>
                <Main-Heating-Control>2106</Main-Heating-Control>
                <Main-Heating-Data-Source>2 ['SAP Table']</Main-Heating-Data-Source>
                <SAP-Main-Heating-Code>104</SAP-Main-Heating-Code>
                <Boiler-Ignition-Type>1 ['auto-ignition']</Boiler-Ignition-Type>
                <Boiler-Flue-Type>1 ['open']</Boiler-Flue-Type>
                <Fan-Flue-Present>Y ['Yes']</Fan-Flue-Present>
                <Heat-Emitter-Type>1 ['radiators']</Heat-Emitter-Type>
                <Main-Heating-Fraction>1</Main-Heating-Fraction>
                <Has-FGHRS>N ['No']</Has-FGHRS>
                <Emitter-Temperature>0 ['unknown']</Emitter-Temperature>
                <Central-Heating-Pump-Age>0 ['unknown']</Central-Heating-Pump-Age>
              </Main-Heating>
            </Main-Heating-Details>
          </SAP-Heating>
          <SAP-Energy-Source>
            <Meter-Type>2 ['Single']</Meter-Type>
            <Mains-Gas>Y ['mains gas available in the property']</Mains-Gas>
            <Electricity-Smart-Meter-Present>0 ['False']</Electricity-Smart-Meter-Present>
            <Gas-Smart-Meter-Present>0 ['False']</Gas-Smart-Meter-Present>
            <Is-Dwelling-Export-Capable>0 ['False']</Is-Dwelling-Export-Capable>
            <Wind-Turbines-Count>0</Wind-Turbines-Count>
            <Wind-Turbines-Terrain-Type>4 ['not recorded']</Wind-Turbines-Terrain-Type>
            <PV-Connection>0 ['not applicable (FGHRS or no PV)']</PV-Connection>
            <Photovoltaic-Supply>
              <None-Or-No-Details>
                <Percent-Roof-Area>0</Percent-Roof-Area>
              </None-Or-No-Details>
            </Photovoltaic-Supply>
          </SAP-Energy-Source>
          <SAP-Building-Parts>
            <SAP-Building-Part>
              <Building-Part-Number>1</Building-Part-Number>
              <Construction-Age-Band>H ['England and Wales: 1991-1995; Scotland: 1992-1998; Northern Ireland: 1992-1999']</Construction-Age-Band>
              <Floor-U-Value>1.0</Floor-U-Value>
              <Floor-Heat-Loss>7 ['Ground floor']</Floor-Heat-Loss>
              <Roof-Construction>4 ['Pitched (slates or tiles), access to loft']</Roof-Construction>
              <Roof-U-Value>1.0</Roof-U-Value>
              <Roof-Insulation-Location>2 ['Joists']</Roof-Insulation-Location>
              <Wall-Construction>4 ['cavity']</Wall-Construction>
              <Wall-Dry-Lined>N ['No']</Wall-Dry-Lined>
              <Wall-U-Value>1.0</Wall-U-Value>
              <Wall-Insulation-Type>2 ['filled cavity']</Wall-Insulation-Type>
              <Wall-Thickness-Measured>N ['No']</Wall-Thickness-Measured>
              <Party-Wall-Construction>NA ['not applicable (detached property or no party wall in this building part)']</Party-Wall-Construction>
              <SAP-Floor-Dimensions>
                <SAP-Floor-Dimension>
                  <Heat-Loss-Perimeter>40</Heat-Loss-Perimeter>
                  <Room-Height>3</Room-Height>
                  <Total-Floor-Area>100</Total-Floor-Area>
                  <Floor>0 ['lowest occupied']</Floor>
                  <Floor-Construction>2 ['suspended timber']</Floor-Construction>
                  <Floor-Insulation>1 ['as built']</Floor-Insulation>
                  <Party-Wall-Length>0</Party-Wall-Length>
                </SAP-Floor-Dimension>
              </SAP-Floor-Dimensions>
            </SAP-Building-Part>
          </SAP-Building-Parts>
          <SAP-Windows>
            <SAP-Window>
              <Window-Location>0 ['Main Property']</Window-Location>
              <Window-Height>1</Window-Height>
              <Window-Width>1</Window-Width>
              <Draught-Proofed>0 ['False']</Draught-Proofed>
              <Glazing-Type>5 ['single glazing']</Glazing-Type>
              <Window-Type>1 ['window']</Window-Type>
              <Orientation>5 ['South']</Orientation>
              <Window-Transmission-Details>
                <Data-Source>2 ['manufacturer data']</Data-Source>
                <U-Value>1</U-Value>
                <Solar-Transmittance>0.8</Solar-Transmittance>
              </Window-Transmission-Details>
              <Frame-Factor>0.9</Frame-Factor>
              <PVC-Frame>1 ['True']</PVC-Frame>
              <Window-Wall-Type>1 ['External wall type 1']</Window-Wall-Type>
              <Permanent-Shutters-Present>N ['No']</Permanent-Shutters-Present>
              <Permanent-Shutters-Insulated>N ['No']</Permanent-Shutters-Insulated>
            </SAP-Window>
          </SAP-Windows>
        </SAP-Property-Details>
      </SAP-Data>
    </RdSAP-Report>
    