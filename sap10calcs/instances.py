# -*- coding: utf-8 -*-

#%% Setup

from lxml import etree
import importlib
import os


#%% SAP_Schema_19_1_0_parser
# - defines the module-level variable `SAP_Schema_19_1_0_parser`
# - This is an instance of lxml.etree.XMLParser

from . import classes_SAP_Schema_19_1_0

SAP_Schema_19_1_0_parser = etree.XMLParser(remove_blank_text=True)

def MyLookup_factory():
    ""
    
    class MyLookup(etree.PythonElementClassLookup):
        ""
        
        def lookup(self, document, element):
            
            # setup
            tag = element.tag
            if '}' in tag:
                name = tag.split('}')[1]
            else:
                return etree.ElementBase
            class_name = name.replace('-','_')
            #print('name', name)
            
            # generate path
            x = element
            path = [class_name]
            
            while True:
                parent = x.getparent()
                if parent is None:
                    break
                if '}' in parent.tag:
                    parent_class_name = parent.tag.split('}')[1].replace('-','_')
                else:
                    return etree.ElementBase
                path.insert(0,parent_class_name)
                x = parent
                
            if path[0] == 'SAP_Report':
                path.insert(0,'SAP_Compliance_Report')
            
            # get class_SAP_Schema_19_1_0
            x = classes_SAP_Schema_19_1_0
            for y in path:
                
                try:
                    x = getattr(x,y)
                except AttributeError:
                    return etree.ElementBase
                
            class_SAP_Schema_19_1_0 = x
            
            if x is None:
                
                return etree.ElementBase
            
            else:
                
                return type(class_name,tuple([class_SAP_Schema_19_1_0]),{})
    
    return MyLookup

SAP_Schema_19_1_0_parser.set_element_class_lookup(MyLookup_factory()())

#%% RdSAP_Schema_21_0_0_parser
# - defines the module-level variable `RdSAP_Schema_21_0_0_parser`
# - This is an instance of lxml.etree.XMLParser

from . import classes_RdSAP_Schema_21_0_0

RdSAP_Schema_21_0_0_parser = etree.XMLParser(remove_blank_text=True)

def MyLookup_factory():
    ""
    
    class MyLookup(etree.PythonElementClassLookup):
        ""
        
        def lookup(self, document, element):
            
            # setup
            tag = element.tag
            if '}' in tag:
                name = tag.split('}')[1]
            else:
                return etree.ElementBase
            class_name = name.replace('-','_')
            #print('name', name)
            
            # generate path
            x = element
            path = [class_name]
            
            while True:
                parent = x.getparent()
                if parent is None:
                    break
                if '}' in parent.tag:
                    parent_class_name = parent.tag.split('}')[1].replace('-','_')
                else:
                    return etree.ElementBase
                path.insert(0,parent_class_name)
                x = parent
                
            #if path[0] == 'SAP_Report':
            #    path.insert(0,'SAP_Compliance_Report')
            
            # get class_SAP_Schema_19_1_0
            x = classes_RdSAP_Schema_21_0_0
            for y in path:
                
                try:
                    x = getattr(x,y)
                except AttributeError:
                    return etree.ElementBase
                
            class_RdSAP_Schema_21_0_0 = x
            
            if x is None:
                
                return etree.ElementBase
            
            else:
                
                return type(class_name,tuple([class_RdSAP_Schema_21_0_0]),{})
    
    return MyLookup

RdSAP_Schema_21_0_0_parser.set_element_class_lookup(MyLookup_factory()())




