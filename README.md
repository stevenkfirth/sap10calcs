# sap10calcs
SAP 10.2 energy calculation method in Python

## Introduction

SAP 10 is the Standard Assessment Procedure version 10, the UK Government's energy calculation method for building regulations and Energy Performance Certificates for new and existing dwellings. 

SAP 10 is developed and published by the Building Research Establishment: https://bregroup.com/expertise/energy/sap/sap10.

This Python package implements SAP 10.2, the current version of SAP in use for UK building regulations. The package has two main uses:

- Running SAP10.2 calculations
- Creating and/or editing the input files for SAP10.2 calculations

## Documentation

All documentation for this Python package is contained in the readme file on the [sap10calcs GitHub page](https://github.com/stevenkfirth/sap10calcs/tree/main).

## Contents of this directory

- **example_input_files**: A directory containing a suite of SAP XML files, and the code used to create these files.
- **examples**: A directory containing examples of how to use this Python package.
- **sap10**: A directory containing the source code of this Python package.
- **test**: A directory containing unittests to test this Python package.


## Installation

Available on PyPi here: https://pypi.org/project/sap10calcs/

Download using the command `pip install sap10calcs`. This command should be run in the Command Prompt or, if using the Anaconda distribution, the Anaconda Prompt.

## Issues & requests?

All comments welcome. Please send any issues and requests to Steven Firth at S.K.Firth@lboro.ac.uk.

## Authors

Steven Firth: https://www.lboro.ac.uk/departments/abce/staff/steven-firth/

## Quick example

This example runs a SAP10.2 calculation.

```python
import sap10calcs
result = sap10calcs.calculate(input_file = 'detached_house.xml')
output_dict = result['sap_calculation_output_dict']
print(output_dict['value_258'], output_dict['sap_band'])  # SAP rating, SAP band
# >>> 75, "C"
```

## Blog posts

For more information, please see the blog posts available here: https://www.stevenfirth.com/tag/sap10/

## API - Functions

### sap10calcs.calculate()

Description: This function runs a SAP 10.2 calculation and returns the results.

Note: This is a wrapper for a [remote API service](https://netzeroapis.com/redoc#operation/sap10_calc_sap10_post) which provides SAP calculations. An internet connection is therefore required. An authorization token for the API service may also be required.

Signature:

```python
sap10calcs.calculate(
        input_file = None,
        input_lxml = None,
        calculation_method = 'Energy rating',
        year = None,
        month = None,
        day = None,    
        verbose = False, 
        auth_token = None
        )
```

Arguments: 
- **input_file** *(str)*: The filepath of the SAP XML input file. This is an XML file based on the XML schema [SAP-Schema-19.1.0](https://github.com/communitiesuk/epb-register-api/tree/master/api/schemas/xml/SAP-Schema-19.1.0/SAP).
- **input_lxml** *(sap10calcs.sap_xml.SAP_Compliance_Report, sap10calcs.sap_xml.SAP_Report or lxml.etree.ElementBase*): An alternative to the `input_file` argument. This is a Python instance (i.e. an object) which holds the XML data instead. This is useful if an XML input file is being edited and means a calculation can be run without saving the XML to a local file first.
- **calculation_method** *(str)*: The type of SAP calculation to be run. The options are: *'New dwelling as designed - dwelling emissions'*; *'Energy rating'*; *'EPC costs, emissions and primary energy'*. Default is `Energy rating`.
- **year** *(int)*: If using *'EPC costs, emissions and primary energy'*, this is the year for the calculation.
- **month** *(int)*: If using *'EPC costs, emissions and primary energy'*, this is the month for the calculation.
- **day** *(int)*: If using *'EPC costs, emissions and primary energy'*, this is the day for the calculation.
- **verbose** *(bool)*: Prints additional runtime information to stdout, including the API call. Default is `False`.
- **auth_token** *(str)*: The authorization token for the API call. See [here](https://netzeroapis.com/redoc#section/Authorization) for more details. If the authorization token is not valid, then an error message will be returned.

Returns:
- *(dict)*: A dictionary of the results of the API call. This dictionary includes the following key/value pairs:
    - **api_call_datetime** *(str)*: The time and date when the API was called.
    - **api_call_url** *(str)*: The url used for the API call.
    - **api_call_filename** *(str)*: The name of the SAP XML file used for the API call.
    - **api_call_server_time_seconds** *(float)*: The time taken to run the SAP 10 calculation.
    - **licenses** *(list)*: A list of the licenses which apply to the returned calculation results.
    - **sap_calculation_output_dict** *(dict)*: The outputs of the SAP 10.2 calculation. The keys of this dictionary match with the names of the output variables in the SAP 10.2 calculation worksheet of SAP 10.2 document.
    - **sap_calculation_success** *(bool)*: `True` if the SAP calculation process completes fully, otherwise `False`.
    - **sap_calculation_error_type** *(str or None)*: The error type if an error occurs during the SAP calculation process, otherwise `None`.
    - **sap_calculation_error_message** *(str or None)*: The error message if an error occurs during the SAP calculation process, otherwise `None`.
    - **sap_calculation_error_traceback** *(str or None)*: The error traceback (in Python) if an error occurs during the SAP calculation process, otherwise `None`.

[Example - running a SAP calculation](https://github.com/stevenkfirth/sap10calcs/blob/main/examples/Example%20-%20running%20a%20SAP%20calculation.ipynb):

```python
import sap10calcs
result = sap10calcs.calculate(input_file = 'detached_house.xml')
output_dict = result['sap_calculation_output_dict']
print(output_dict['value_258'], output_dict['sap_band'])  # SAP rating, SAP band
# >>> 75, "C"
```

### sap10calcs.create_sap_report_xml()

Description: This function creates a lxml tree with a SAP_Report element as the root element.

Note: This is used when creating a SAP XML file from scratch. This should be used in conjuntion with the [lxml package](https://lxml.de/), the standard third-party Python package for working with XML files.

Signature:

```python
sap10.create_sap_report_xml()
```

Returns:
- A tuple with two items:
    - `tree`: An lxml.etree with a single root element of a [`SAP_Report`](#sap10sap_xmlsap_compliance_reportsap_report) instance.
    - `root`: A [`SAP_Report`](#sap10sap_xmlsap_compliance_reportsap_report) instance, where SAP_Report is a subclass of an lxml.element. This is an lxml element and can be used to work with the XML using the normal lxml functions and techniques. It also contains additional class properties and methods which are designed to help working with SAP10 XML files.

[Example - creating a new empty SAP XML file](https://github.com/stevenkfirth/sap10calcs/blob/main/examples/Example%20-%20creating%20a%20new%20empty%20SAP%20XML%20file.ipynb):

This example creates an lxml etree with a `SAP_report` root node. The xml tree is then printed using the standard lxml method (`etree.to_string`) and using a custom method provided by the `SAP_report` class (`display`).

```python
import sap10calcs
from lxml import etree
tree, root = sap10calcs.create_sap_report_xml()
print(tree)
print(root)
print(root.display(show_values = True))
```

```xml
<lxml.etree._ElementTree object at 0x0000014DBBCD3E80>
<SAP_Report {https://epbr.digital.communities.gov.uk/xsd/sap}SAP-Report>
<SAP-Report xmlns="https://epbr.digital.communities.gov.uk/xsd/sap">
  <Schema-Version-Original>SAP-Schema-19.1.0</Schema-Version-Original>
  <SAP-Version>10.2 ['SAP version 10.2, dated Oct 2020']</SAP-Version>
</SAP-Report>
```


### sap10calcs.parse_xml()

Description: This function parses an existing SAP XML file.

Note: This is designed to work with SAP XML files based on the XML schema [SAP-Schema-19.1.0](https://github.com/communitiesuk/epb-register-api/tree/master/api/schemas/xml/SAP-Schema-19.1.0/SAP). This should be used in conjuntion with the [lxml package](https://lxml.de/), the standard third-party Python package for working with XML files.

Signature:

```python
sap10calcs.create_sap_report_xml(
    input_file
)
```
Arguments: 
- **input_file** *(str)*: The filepath of the SAP 10 XML input file. This is an XML file based on the XML schema [SAP-Schema-19.1.0](https://github.com/communitiesuk/epb-register-api/tree/master/api/schemas/xml/SAP-Schema-19.1.0/SAP).

Returns:
- A tuple with two items:
    - `tree`: An lxml.etree with a single root element of a [`SAP_Report`](#sap10calcssap_xmlsap_report) instance or a [`SAP_Compliance_Report`](#sap10calcssap_xmlsap_compliance_report) instance.
    - `root`: A [`SAP_Report`](#sap10calcssap_xmlsap_report) instance or a [`SAP_Compliance_Report`](#sap10calcssap_xmlsap_compliance_report) instance. These are an lxml element and can be used to work with the XML using the normal lxml functions and techniques. It also contains additional class properties and methods which are designed to help working with SAP10 XML files.

[Example - parsing an existing SAP XML file](https://github.com/stevenkfirth/sap10calcs/blob/main/examples/Example%20-%20parsing%20an%20existing%20SAP%20XML%20file.ipynb):

The example file below is for a detached house and was created [here](https://github.com/stevenkfirth/sap10calcs/blob/main/examples/Example%20-%20creating%20a%20complete%20SAP%20XML%20file.ipynb).

```python
import sap10calcs
tree, root = sap10calcs.parse_xml('Example - creating a complete SAP XML file.xml')
print(tree)
print(root)
print(root.display(show_values = True))
```

```xml
<lxml.etree._ElementTree object at 0x000002776240B540>
<SAP_Report {https://epbr.digital.communities.gov.uk/xsd/sap}SAP-Report>
<SAP-Report xmlns="https://epbr.digital.communities.gov.uk/xsd/sap">
  <Schema-Version-Original>SAP-Schema-19.1.0</Schema-Version-Original>
  <SAP-Version>10.2 ['SAP version 10.2, dated Oct 2020']</SAP-Version>
  <SAP10-Data>
    <Data-Type>1 ['new dwelling as designed']</Data-Type>
    <SAP-Property-Details>
      <Cold-Water-Source>1 ['mains']</Cold-Water-Source>
      <Living-Area>30</Living-Area>
      <Windows-Overshading>2 ['average or unknown']</Windows-Overshading>
      <SAP-Building-Parts>
        <SAP-Building-Part>
          <Building-Part-Number>1</Building-Part-Number>
          <SAP-Floor-Dimensions>
            <SAP-Floor-Dimension>
              <Floor-Type>2 ['ground floor']</Floor-Type>
              <Storey>0 ['Ground']</Storey>
              <Total-Floor-Area>100</Total-Floor-Area>
              <Storey-Height>3</Storey-Height>
              <Heat-Loss-Area>100</Heat-Loss-Area>
              <U-Value>0.5</U-Value>
            </SAP-Floor-Dimension>
          </SAP-Floor-Dimensions>
          <SAP-Walls>
            <SAP-Wall>
              <Wall-Type>2 ['exposed wall']</Wall-Type>
              <Total-Wall-Area>120</Total-Wall-Area>
              <U-Value>0.5</U-Value>
              <Name>sap_wall_1_1</Name>
            </SAP-Wall>
          </SAP-Walls>
          <SAP-Roofs>
            <SAP-Roof>
              <Total-Roof-Area>100</Total-Roof-Area>
              <U-Value>0.5</U-Value>
              <Roof-Type>2 ['exposed roof']</Roof-Type>
              <Name>sap_roof_1_1</Name>
            </SAP-Roof>
          </SAP-Roofs>
          <SAP-Openings>
            <SAP-Opening>
              <Type>sap_opening_type_1</Type>
              <Height>1.5</Height>
              <Width>5</Width>
              <Location>sap_wall_1_1</Location>
              <Orientation>5 ['South']</Orientation>
            </SAP-Opening>
          </SAP-Openings>
          <SAP-Thermal-Bridges>
            <Thermal-Bridge-Code>1 ['default']</Thermal-Bridge-Code>
          </SAP-Thermal-Bridges>
        </SAP-Building-Part>
      </SAP-Building-Parts>
      <SAP-Opening-Types>
        <SAP-Opening-Type>
          <Name>sap_opening_type_1</Name>
          <Type>4 ['window']</Type>
          <Data-Source>2 ['manufacturer declaration']</Data-Source>
          <U-Value>1.5</U-Value>
          <Glazing-Type>3 ['double']</Glazing-Type>
        </SAP-Opening-Type>
      </SAP-Opening-Types>
      <SAP-Heating>
        <Has-Hot-Water-Cylinder>0 ['False']</Has-Hot-Water-Cylinder>
        <Thermal-Store>1 ['none']</Thermal-Store>
        <Secondary-Heating-Category>1 ['none']</Secondary-Heating-Category>
        <Water-Heating-Code>901</Water-Heating-Code>
        <Main-Heating-Details>
          <Main-Heating>
            <Main-Heating-Number>1</Main-Heating-Number>
            <Main-Fuel-Type>1 ['Gas: mains gas']</Main-Fuel-Type>
            <Main-Heating-Category>2 ['boiler with radiators or underfloor heating']</Main-Heating-Category>
            <Main-Heating-Data-Source>3 ['from SAP table']</Main-Heating-Data-Source>
            <Main-Heating-Code>104</Main-Heating-Code>
            <Is-Central-Heating-Pump-In-Heated-Space>1 ['True']</Is-Central-Heating-Pump-In-Heated-Space>
            <Main-Heating-Fraction>1</Main-Heating-Fraction>
            <Heat-Emitter-Type>1 ['radiators']</Heat-Emitter-Type>
            <Main-Heating-Control>2106</Main-Heating-Control>
            <Has-Separate-Delayed-Start>0 ['False']</Has-Separate-Delayed-Start>
            <Is-Interlocked-System>0 ['False']</Is-Interlocked-System>
          </Main-Heating>
        </Main-Heating-Details>
      </SAP-Heating>
      <SAP-Ventilation>
        <Open-Chimneys-Count>0</Open-Chimneys-Count>
        <Open-Flues-Count>0</Open-Flues-Count>
        <Closed-Flues-Count>0</Closed-Flues-Count>
        <Boilers-Flues-Count>0</Boilers-Flues-Count>
        <Other-Flues-Count>0</Other-Flues-Count>
        <Blocked-Chimneys-Count>0</Blocked-Chimneys-Count>
        <Extract-Fans-Count>0</Extract-Fans-Count>
        <PSV-Count>0</PSV-Count>
        <Flueless-Gas-Fires-Count>0</Flueless-Gas-Fires-Count>
        <Pressure-Test>2 ['yes (new dwelling, design value)']</Pressure-Test>
        <Air-Permeability>3.5</Air-Permeability>
        <Sheltered-Sides-Count>2</Sheltered-Sides-Count>
        <Ventilation-Type>1 ['natural with intermittent extract fans']</Ventilation-Type>
      </SAP-Ventilation>
    </SAP-Property-Details>
  </SAP10-Data>
</SAP-Report>

```






## API - Classes

### sap10calcs.sap_xml.SAP_Compliance_Report.SAP_Report

Description: A custom lxml.element class which contains additional properties and methods for SAP-Report XML elements. 

Note: This can be the root of a SAP XML file. Instances of this class should arise from using [`create_sap_report_xml()`](#sap10calcscreate_sap_report_xml) or [`parse_xml()`](#sap10calcsparse_xml), and should not created by the user directly. The custom methods and properties can be used to access and create other XML elements.

[Example - viewing the properties and methods of a SAP_Report element](https://github.com/stevenkfirth/sap10calcs/blob/main/examples/Example%20-%20viewing%20the%20properties%20and%20methods%20of%20a%20SAP_Report%20element.ipynb)

```python
import sap10calcs
tree, sap_report = sap10calcs.parse_xml('Example - creating a complete SAP XML file.xml')
print(sap_report.sap_xml_properties)  # these are the custom properties provided by this Python package
print(sap_report.sap_version)  # access a child element
```

```
['code',  
 'value',
 'sap_xml_codes',
 'schema_version_original',
 'schema_version_current',
 'sap_version',
 'sap_data_version',
 'pcdf_revision_number',
 'calculation_software_name',
 'calculation_software_version',
 'user_interface_name',
 'user_interface_version',
 'report_header',
 'energy_assessment',
 'sap10_data',
 'pdf',
 'insurance_details',
 'externaldefinitions_revision_number']
 <SAP_Version {https://epbr.digital.communities.gov.uk/xsd/sap}SAP-Version>
```

### sap10calcs.sap_xml.SAP_Compliance_Report

Description: A custom lxml.element class which contains additional properties and methods for SAP-Compliance-Report XML elements.

Note: This can be the root of a SAP XML file. Instances of this class may arise from using [`parse_xml()`](#sap10calcsparse_xml), and should not created by the user directly. The custom methods and properties can be used to access and create other XML elements.

Example - see the [SAP_Report](#sap10calcssap_xmlsap_compliance_reportsap_report) example above.


### sap10calcs.sap_xml.[...many other classes...]

Description: Custom lxml.element classes which contains additional properties and methods for all possible XML elements in the XML schema [SAP-Schema-19.1.0](https://github.com/communitiesuk/epb-register-api/tree/master/api/schemas/xml/SAP-Schema-19.1.0/SAP).

Note: These should not be created directly by the users.

[Example - creating a complete SAP XML file](https://github.com/stevenkfirth/sap10calcs/blob/main/examples/Example%20-%20creating%20a%20complete%20SAP%20XML%20file.ipynb). This provides a use-case for how these custom properties and methods can be used to create a comlete SAP XML file.

The full set of classes can be seen in the source code [here](https://github.com/stevenkfirth/sap10calcs/blob/main/sap10/classes_SAP_Schema_19_1_0.py).

## FAQs

### How do I find out more about the SAP calculation?.

Please see the documentation for the API service: https://netzeroapis.com/redoc#operation/sap10_calc_sap10_post

### How do I created my own SAP XML input files?

This blog post discusses how to do this: 

### Can I use a Reduced-data SAP (RdSAP) input file?

RdSAP is a separate process to the main SAP calculation. RdSAP input files are simpler and have less inputs than the full SAP input files, and are typically used for existing buildings where collecting the data for a full SAP input file would be difficult. To run a full SAP calculation using a RdSAP input file, the RdSAP input file must first be converted to a full SAP input file.

This additional functionality is under development. If this is of interest, please [send a request](#issues--requests).


