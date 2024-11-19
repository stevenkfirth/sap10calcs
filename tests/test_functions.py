# -*- coding: utf-8 -*-

import unittest
from io import StringIO
from lxml import etree
import os

import sap10calcs

with open('_auth.txt') as f:
    auth_token = f.read()
    
input_fp = os.path.join(
    os.pardir,
    'example_input_files',
    'detached_house.xml'
    )


rdsap_input_fp = os.path.join(
    os.pardir,
    'rdsap_example_input_files',
    'rdsap_detached_house.xml'
    )


class TestCalculate(unittest.TestCase):
    ""
    
    # successful run with file input
    def test_1(self):
        ""
        
        result = sap10calcs.calculate(
            input_file = input_fp,
            auth_token = auth_token  # note does not start with 'Bearer '
            )
        
        self.assertEqual(
            result['sap_calculation_success'], 
            True
            )
        
        self.assertEqual(
            result["sap_calculation_output_dict"]['value_258'], 
            74
            )
        

    # successful run with lxml input
    def test_2(self):
        ""

        tree = etree.parse(input_fp)
        root = tree.getroot()
        
        result = sap10calcs.calculate(
            input_lxml = root,
            auth_token = auth_token
            )
        
        self.assertEqual(
            result['sap_calculation_success'], 
            True
            )
        
        self.assertEqual(
            result["sap_calculation_output_dict"]['value_258'], 
            74
            )
        
        
    # successful run with file input and extras
    def test_3(self):
        ""
        
        result = sap10calcs.calculate(
            input_file = input_fp,
            extra = {'overwrite': {'value_258': 80}},
            auth_token = auth_token  # note does not start with 'Bearer '
            )
        
        self.assertEqual(
            result['sap_calculation_success'], 
            True
            )
        
        self.assertEqual(
            result["sap_calculation_output_dict"]['value_258'], 
            80
            )
        

class TestCreateSapReportXML(unittest.TestCase):
    ""
    
    def test_1(self):
        ""
        
        tree, root = sap10calcs.create_sap_report_xml()

        self.assertEqual(
            ''.join(etree.tostring(tree, pretty_print=True).decode().split())
            ,
            ''.join("""
            <SAP-Report xmlns="https://epbr.digital.communities.gov.uk/xsd/sap">
              <Schema-Version-Original>SAP-Schema-19.1.0</Schema-Version-Original>
              <SAP-Version>10.2</SAP-Version>
            </SAP-Report>
            """.split())
            )


class TestCreateRdSapReportXML(unittest.TestCase):
    ""
    
    def test_1(self):
        ""
        
        tree, root = sap10calcs.create_rdsap_report_xml()
        
        self.assertEqual(
            ''.join(etree.tostring(tree, pretty_print=True).decode().split())
            ,
            ''.join("""
            <RdSAP-Report xmlns="https://epbr.digital.communities.gov.uk/xsd/rdsap">
              <Schema-Version-Original>RdSAP-Schema-21.0.0</Schema-Version-Original>
              <SAP-Version>10.2</SAP-Version>
            </RdSAP-Report>
            """.split())
            )



class TestParseRdSapXML(unittest.TestCase):
    ""
    
    def test_1(self):
        ""
        
        tree, root = sap10calcs.parse_rdsap_xml(
            rdsap_input_fp
            )
        
        # print(root.display())
        
        
class TestParseXML(unittest.TestCase):
    ""
    
    def test_1(self):
        ""
        
        tree, root = sap10calcs.parse_xml(
            input_fp
            )


        
class TestRdSAP(unittest.TestCase):
    ""
    
    # successful run with file input
    def test_1(self):
        ""
        
        result = sap10calcs.rdsap(
            input_file = rdsap_input_fp,
            auth_token = auth_token  # note does not start with 'Bearer '
            )
        
        self.assertEqual(
            result['rdsap_calculation_success'], 
            True
            )
        
        
    
    # successful run with lxml input
    def test_2(self):
        ""

        tree = etree.parse(rdsap_input_fp)
        root = tree.getroot()
        
        result = sap10calcs.rdsap(
            input_lxml = root,
            auth_token = auth_token
            )
        
        self.assertEqual(
            result['rdsap_calculation_success'], 
            True
            )
        
        


if __name__ == '__main__':

    unittest.main()        


