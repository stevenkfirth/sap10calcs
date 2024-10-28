# -*- coding: utf-8 -*-

import unittest
from io import StringIO
from lxml import etree
import os

import sap10calcs


class calculate(unittest.TestCase):
    ""
    
    def _test_1(self):
        ""
        
        
        result = sap10calcs.calculate(
            input_file = os.path.join(
                os.pardir,
                'example_input_files',
                'detached_house.xml'
                ),
            verbose = True,
            url = 'http://127.0.0.1:8000/calc/sap10',
            #year = 2024,
            #auth_token = 'my_token'
            )
        
        output_dict = result.pop('sap_calculation_output_dict')
        result
        
        print(result)
        
        
        
        # #print(result['api_call_url'])
        # print(result['sap_calculation_success'])
        # print(result['sap_calculation_error_type'])
        # print(result['sap_calculation_error_message'])
        # print(result['sap_calculation_error_traceback'])
        
        # output_dict = result['sap_calculation_output_dict']
        
        if result['sap_calculation_success']:
        
            print(output_dict['sap_band'])
            
        else:
            
            print(output_dict)


    def _test2(self):
        ""

        tree, root = sap10calcs.create_sap_report_xml()

        result = sap10.calculate(
            input_lxml = root,
            verbose = True
            )
        
        print(result['sap_calculation_success'])
        print(result['sap_calculation_error_type'])
        print(result['sap_calculation_error_message'])
        print(result['sap_calculation_error_traceback'])
        
        

class create_sap_report_xml(unittest.TestCase):
    ""
    
    def _test_1(self):
        ""
        
        tree, root = sap10calcs.create_sap_report_xml()

        print(etree.tostring(tree, pretty_print=True).decode())
        print('---')
        print(root.display())


class create_rdsap_report_xml(unittest.TestCase):
    ""
    
    def test_1(self):
        ""
        
        tree, root = sap10calcs.create_rdsap_report_xml()

        #print(etree.tostring(tree, pretty_print=True).decode())
        #print('---')
        print(root.display())
        
        print(root.sap_xml_properties)


if __name__ == '__main__':

    unittest.main()        


