# -*- coding: utf-8 -*-

import requests
from lxml import etree
from io import StringIO, BytesIO
import json

from .instances import SAP_Schema_19_1_0_parser
from .instances import RdSAP_Schema_21_0_0_parser


def calculate(
        input_file = None,
        input_lxml = None,
        calculation_method = 'Energy rating',  # should perhaps be 'calculation_type' ??
        year = None,
        month = None,
        day = None,    
        verbose = False,
        url = 'https://netzeroapis.com/calc/sap10',
        extra = None,
        auth_token = None
        ):
    """Runs a SAP10 calculation.

    This takes the SAP10 XML input file and sends it to the remote API service to run a SAP10 calculation.

    See also: :ref:`running_a_sap10_calculation`.

    :param str input_file: The filepath to the SAP10 input XML file stored on the local computer. This is an XML file based on the XML schema `SAP-Schema-19.1.0 <https://github.com/communitiesuk/epb-register-api/tree/master/api/schemas/xml/SAP-Schema-19.1.0/SAP>`__. Default is `None`. See also: :ref:`an_example_input_file`.
    :param input_lxml: The input XML object. This can be used instead of providing the `input_file` parameter. This is useful if an XML input file is being edited and means a calculation can be run without saving the XML to a local file first. Default is `None`. See also: :ref:`an_example_input_file`.
    :type input_lxml: ~sap10calcs.classes_SAP_Schema_19_1_0.SAP_Compliance_Report or ~sap10calcs.classes_SAP_Schema_19_1_0.SAP_Report
    :param str calculation_method: The type of SAP calculation to be run. The options are: 'New dwelling as designed - dwelling emissions'; 'Energy rating'; 'EPC costs, emissions and primary energy'. Default is `Energy rating`.
    :param int year: If using 'EPC costs, emissions and primary energy', this is the year for the calculation. Default is `None`.
    :param int month: If using 'EPC costs, emissions and primary energy', this is the month for the calculation. Default is `None`.
    :param int day: If using 'EPC costs, emissions and primary energy', this is the day for the calculation. Default is `None`.
    :param bool verbose: Prints additional runtime information to stdout, including the API call. Default is `False`.
    :param str url: The url used for the API call. Default is `https://netzeroapis.com/calc/sap10`.
    :param dict extra: An optional dictionary that can be used to provide extra instructions to the SAP calculation. Default is `None`.
    :param str auth_token: The authorization token for the remote API service. See `here <https://netzeroapis.com/redoc#section/Authorization>`__ for more details. If the authorization token is not valid, then an error message will be returned. Default is `None`.
    :returns: A dictionary with the results of the call to the remote API service. See also: :ref:`an_example_output_dictionary`. 
    :rtype: dict

    The return dictionary includes the following key/value pairs:

    - **api_call_datetime** *(str)*: The time and date when the API was called.
    - **api_call_url** *(str)*: The url used for the API call.
    - **api_call_filename** *(str)*: The name of the SAP XML file used for the API call.
    - **api_call_server_time_seconds** *(float)*: The time taken to run the SAP 10 calculation.
    - **licenses** *(list(str))*: A list of the licenses which apply to the returned calculation results.
    - **api_call_overwrite**: *(dict)*: The overwrite dictionary used in the SAP 10 calculation.
    - **api_call_addition**: *(dict)*: The addition dictionary used in the SAP 10 calculation.
    - **api_call_break_point**: *(dict)*: The break point used in the SAP 10 calculation.
    - **sap_calculation_output_dict** *(dict)*: The outputs of the SAP 10.2 calculation. The keys of this dictionary match with the names of the output variables in the SAP 10.2 calculation worksheet of SAP 10.2 document.
    - **sap_calculation_success** *(bool)*: `True` if the SAP calculation process completes fully, otherwise `False`.
    - **sap_calculation_error_type** *(str or None)*: The error type if an error occurs during the SAP calculation process, otherwise `None`.
    - **sap_calculation_error_message** *(str or None)*: The error message if an error occurs during the SAP calculation process, otherwise `None`.
    - **sap_calculation_error_traceback** *(str or None)*: The error traceback (in Python) if an error occurs during the SAP calculation process, otherwise `None`.

    """
    
    url = url + f'?calculation_type={calculation_method}'
    
    if not year is None:
        url = url + f'&year={year}'
        
    if not month is None:
        url = url + f'&month={month}'
        
    if not day is None:
        url = url + f'&day={day}'
    
    if not input_file is None:
        with open(input_file, 'rb') as f:
            input_string = f.read()
    elif not input_lxml is None:
        input_string = etree.tostring(input_lxml)
    else:
        raise Exception
        
    files = {'file': BytesIO(input_string)}
        
    if not extra is None:
        files['extra'] = json.dumps(extra)
        
    if verbose:
        print('url:', url)
        
    if not auth_token is None:
        headers = {'Authorization': f'Bearer {auth_token}'}
    else:
        headers = {}   
        
    if verbose:
        print('headers:', headers)
    
    r = requests.post(
        url,
        files = files,
        headers = headers
        )
    
    
    if verbose:
        print('status_code:', r.status_code)
    
    if r.status_code == 200:
        
        return r.json()
    
    elif r.status_code in [401, 404]:
        
        raise Exception(str(r.status_code) + ' - ' + str(r.json()['detail']))
    
    elif r.status_code == 500:
        
        raise Exception(str(r.status_code) + ' - ' + str(r.content.decode()))
    
    else:
        
        raise Exception(str(r.status_code) + ' - ' + str(r.content.decode()))
            
        
    
def create_sap_report_xml():
    """Creates an new SAP XML document.

    See also: :ref:`creating_a_sap_xml_input_file_from_scratch`.

    :returns: A two-item tuple containing an `lxml ElementTree <https://lxml.de/tutorial.html>`__ and a `SAP-Report <https://stevenkfirth.github.io/sap10calcs/sap_schema_19_1_0.html#sap-report>`__ element with two child elements: `Schema-Version-Original <https://stevenkfirth.github.io/sap10calcs/rdsap_schema_21_0_0.html#RdSAP-Report/Schema-Version-Original>`__ (text value of "SAP-Schema-19.1.0") and `SAP-Version <https://stevenkfirth.github.io/sap10calcs/rdsap_schema_21_0_0.html#RdSAP-Report/SAP-Version>`__ (text value of "10.2"). 
    :rtype: (`lxml.etree.ElementTree <https://lxml.de/tutorial.html#the-elementtree-class>`__, :py:class:`sap10calcs.classes_SAP_Schema_19_1_0.SAP_Report`)

    """
    
    xml = """
    <SAP-Report xmlns="https://epbr.digital.communities.gov.uk/xsd/sap">
        <Schema-Version-Original>SAP-Schema-19.1.0</Schema-Version-Original>
        <SAP-Version>10.2</SAP-Version>
    </SAP-Report>"""

    tree = etree.parse(
        StringIO(xml),
        parser = SAP_Schema_19_1_0_parser
        )
    
    root = tree.getroot() 
    
    return tree, root
    
    
    
def create_rdsap_report_xml():
    """Creates an new RdSAP XML document.

    See also: :ref:`creating_a_rdsap_xml_input_file_from_scratch`.

    :returns: A two-item tuple containing an `lxml ElementTree <https://lxml.de/tutorial.html>`__ and a `RdSAP-Report <https://stevenkfirth.github.io/sap10calcs/rdsap_schema_21_0_0.html#rdsap-report>`__ element with two child elements: `Schema-Version-Original <https://stevenkfirth.github.io/sap10calcs/rdsap_schema_21_0_0.html#RdSAP-Report/Schema-Version-Original>`__ (text value of "RdSAP-Schema-21.0.0") and `SAP-Version <https://stevenkfirth.github.io/sap10calcs/rdsap_schema_21_0_0.html#RdSAP-Report/SAP-Version>`__ (text value of "10.2"). 
    :rtype: (`lxml.etree.ElementTree <https://lxml.de/tutorial.html#the-elementtree-class>`__, :py:class:`sap10calcs.classes_RdSAP_Schema_21_0_0.RdSAP_Report`)

    """
    
    xml = """
    <RdSAP-Report xmlns="https://epbr.digital.communities.gov.uk/xsd/rdsap">
        <Schema-Version-Original>RdSAP-Schema-21.0.0</Schema-Version-Original>
        <SAP-Version>10.2</SAP-Version>
    </RdSAP-Report>"""

    tree = etree.parse(
        StringIO(xml),
        parser = RdSAP_Schema_21_0_0_parser
        )
    
    root = tree.getroot() 
    
    return tree, root
    
    
def parse_rdsap_xml(
        input_file
        ):
    """Reads a RdSAP XML file.

    See also: :ref:`editing_an_existing_rdsap_xml_file`.
    
    :returns: A two-item tuple containing an `lxml ElementTree <https://lxml.de/tutorial.html>`__ and the root node of the XML file (a `RdSAP-Report <https://stevenkfirth.github.io/sap10calcs/rdsap_schema_21_0_0.html#rdsap-report>`__ element).
    :rtype: (`lxml.etree.ElementTree <https://lxml.de/tutorial.html#the-elementtree-class>`__, :py:class:`sap10calcs.classes_RdSAP_Schema_21_0_0.RdSAP_Report`)

    """
    
    tree = etree.parse(
        input_file,
        parser = RdSAP_Schema_21_0_0_parser
        )
    
    root = tree.getroot() 
    
    return tree, root
    
    
    
def parse_xml(
        input_file
        ):
    """Reads a SAP XML file.

    See also: :ref:`editing_an_existing_sap_xml_file`.
    
    :returns: A two-item tuple containing an `lxml ElementTree <https://lxml.de/tutorial.html>`__ and the root node of the XML file (a a `SAP-Report <https://stevenkfirth.github.io/sap10calcs/sap_schema_19_1_0.html#sap-report>`__ element or a `SAP-Compliance-Report <https://stevenkfirth.github.io/sap10calcs/sap_schema_19_1_0.html#sap-compliance-report>`__ element).
    :rtype: (`lxml.etree.ElementTree <https://lxml.de/tutorial.html#the-elementtree-class>`__, :py:class:`sap10calcs.classes_RdSAP_Schema_21_0_0.RdSAP_Report` or :py:class:`sap10calcs.classes_SAP_Schema_19_1_0.SAP_Compliance_Report`)

    """
    
    tree = etree.parse(
        input_file,
        parser = SAP_Schema_19_1_0_parser
        )
    
    root = tree.getroot() 
    
    return tree, root
    

def rdsap(
    input_file = None,
    input_lxml = None,
    verbose = False,
    url = 'https://netzeroapis.com/calc/rdsap10',
    auth_token = None
    ):
    """Runs a RdSAP10 calculation.

    This takes the RdSAP10 XML input file and sends it to the remote API service to run a RdSAP10 calculation.

    See also: :ref:`running_a_rdsap10_calculation`.

    :param str input_file: The filepath to the RdSAP10 input XML file stored on the local computer. This is an XML file based on the XML schema `RdSAP-Schema-21.0.0 <https://github.com/communitiesuk/epb-register-api/tree/master/api/schemas/xml/RdSAP-Schema-21.0.0/RdSAP>`__. Default is `None`. 
    :param input_lxml: The input XML object. This can be used instead of providing the `input_file` parameter. This is useful if an XML input file is being edited and means a calculation can be run without saving the XML to a local file first. Default is `None`. 
    :type input_lxml: ~sap10calcs.classes_RdSAP_Schema_21_0_0.RdSAP_Report 
    :param bool verbose: Prints additional runtime information to stdout, including the API call. Default is `False`.
    :param str url: The url used for the API call. Default is `https://netzeroapis.com/calc/rdsap10`.
    :param str auth_token: The authorization token for the remote API service. See `here <https://netzeroapis.com/redoc#section/Authorization>`__ for more details. If the authorization token is not valid, then an error message will be returned. Default is `None`.
    :returns: A dictionary with the results of the call to the remote API service.  
    :rtype: dict

    The return dictionary includes the following key/value pairs:

    - **api_call_datetime** *(str)*: The time and date when the API was called.
    - **api_call_url** *(str)*: The url used for the API call.
    - **api_call_filename** *(str)*: The name of the SAP XML file used for the API call.
    - **api_call_server_time_seconds** *(float)*: The time taken to run the SAP 10 calculation.
    - **licenses** *(list(str))*: A list of the licenses which apply to the returned calculation results.
    - **api_call_overwrite**: *(dict)*: The overwrite dictionary used in the SAP 10 calculation.
    - **rdsap_calculation_output_dict** *(dict)*: The outputs of the RdSAP 10.2 calculation. 
    - **rdsap_calculation_success** *(bool)*: `True` if the RdSAP calculation process completes fully, otherwise `False`.
    - **rdsap_calculation_error_type** *(str or None)*: The error type if an error occurs during the SAP calculation process, otherwise `None`.
    - **rdsap_calculation_error_message** *(str or None)*: The error message if an error occurs during the SAP calculation process, otherwise `None`.
    - **rdsap_calculation_error_traceback** *(str or None)*: The error traceback (in Python) if an error occurs during the SAP calculation process, otherwise `None`.
    - **sap_xml** *(str)*: A string containing the full SAP10 XML which is the main output of the RdSAP10 calculation process.

    """
    
    if verbose:
        print('url:', url)

    if not input_file is None:
        with open(input_file, 'rb') as f:
            input_string = f.read()
    elif not input_lxml is None:
        input_string = etree.tostring(input_lxml)
    else:
        raise Exception
        
    files = {'file': BytesIO(input_string)}

    if not auth_token is None:
        headers = {'Authorization': f'Bearer {auth_token}'}
    else:
        headers = {}   
    if verbose:
        print('headers:', headers)
    
    r = requests.post(
        url,
        files = files,
        headers = headers
        )
    
    if verbose:
        print('status_code:', r.status_code)
    
    if r.status_code == 200:

        return r.json()

    elif r.status_code in [401, 404]:
        raise Exception(str(r.status_code) + ' - ' + str(r.json()['detail']))
    elif r.status_code == 500:
        raise Exception(str(r.status_code) + ' - ' + str(r.content.decode()))
    else:
        raise Exception(str(r.status_code) + ' - ' + str(r.content.decode()))
            

    
    
    
    
    
    
