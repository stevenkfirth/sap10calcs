# -*- coding: utf-8 -*-

import unittest
from io import StringIO
from lxml import etree

import sap10




class SAP_Schema_19_1_0(unittest.TestCase):
    ""
    
    def test_1(self):
        ""
        
        xml = '<SAP-Report xmlns="https://epbr.digital.communities.gov.uk/xsd/sap" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.epcregister.com/xsd/sap http://www.epcregister.com/xsd/SAP/Templates/SAP-Report.xsd"></SAP-Report>'

        tree = etree.parse(
            StringIO(xml),
            parser = sap10.SAP_Schema_19_1_0_parser
            )
        
        root = tree.getroot() 

        #print(root)
        #print(root.subclass_method_names)
        #print(etree.tostring(tree).decode())


    def test_2(self):
        ""
        
        tree, root = sap10.create_sap_report_xml()
        
        sap_report = root
        
        sap10_data = sap_report.add_sap10_data()
        
        sap_property_details = sap10_data.add_sap_property_details()
        
        sap_energy_source = sap_property_details.add_sap_energy_source()
        
        electricity_tariff = sap_energy_source.add_electricity_tariff()
        
        electricity_tariff.text = '1'  # 'standard tariff'
        
        print(sap_report.display())

        




if __name__ == '__main__':

    unittest.main()        


