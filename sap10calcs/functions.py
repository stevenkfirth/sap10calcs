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
        calculation_method = 'Energy rating',
        year = None,
        month = None,
        day = None,    
        verbose = False,
        url = 'https://netzeroapis.com/calc/sap10',
        extra = None,
        auth_token = None
        ):
    ""
    
    url = url + f'?calculation_method={calculation_method}'
    
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
        
    if not year is None:
        url = url + f'&year={year}'
        
    if not month is None:
        url = url + f'&month={month}'
        
    if not day is None:
        url = url + f'&day={day}'
        
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
    ""
    
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
    ""
    
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
    ""
    
    tree = etree.parse(
        input_file,
        parser = RdSAP_Schema_21_0_0_parser
        )
    
    root = tree.getroot() 
    
    return tree, root
    
    
    
def parse_xml(
        input_file
        ):
    ""
    
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
    ""
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
            

    
    
    
    
    
    
