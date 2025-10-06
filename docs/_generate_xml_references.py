# this generates the XML schema pages for the Sphinx website.



print('START')

from sap10calcs import classes_SAP_Schema_19_1_0, classes_RdSAP_Schema_21_0_0
import datetime

def write_subclass(f, kls):
    ""

    for subclass_class_name in kls.subclass_class_names:

        subkls = getattr(kls,subclass_class_name)
        subkls._parent_class = kls
        subkls._expanded_name = f'{kls._expanded_name}/{subkls.element_name}'

        write_class(f, subkls)
        write_subclass(f, subkls)




def write_class(f, kls):
    ""
    f.write(f'.. _{kls._expanded_name}:\n\n')

    f.write(f'{kls.element_name}\n')
    f.write(f'{'-'*len(kls.element_name)}\n\n')

    y = ''
    for x in kls._expanded_name.split('/'):
        y = y + ('/' if not y == '' else '') + x
        f.write(f'<:ref:`{y}`>/')
        #f.write(f'[`{x}`](#{y})/')
        
    f.write('\n\n')

    #f.write(f'`{kls._expanded_name}`\n\n')

    if not kls.documentation is None:
        f.write(f'- Documentation: *{kls.documentation}*\n')

    if not kls.type_documentation is None:
        f.write(f'- Documentation2: *{kls.type_documentation}*\n')

    if not kls._parent_class is None:
        f.write(f'- Parent element: <:ref:`{kls._parent_class._expanded_name}`>\n')

    subklses = [getattr(kls,subclass_class_name) for subclass_class_name in kls.subclass_class_names]
    
    if len(subklses) > 0:
        x = ' '.join([f'<:ref:`{kls._expanded_name}/{subkls.element_name}`>' for subkls in subklses] )
        f.write(f'- Child elements: {x}\n')

    f.write(f'- Has text value: *{kls.has_text_node}*\n')

    if kls.map_codes is None:

        if not kls.python_type is None:
            if kls.python_type == datetime.date.fromisoformat:
                f.write(f'- Data type: *Date string (ISO format)*\n')
            else:
                f.write(f'- Data type: *{kls.python_type}*\n')

    else:

        f.write(f'- Codes:\n')
        for k,v in kls.map_codes.items():
            f.write(f'    - **"{k}"** - *{v}*\n')

    f.write(f'- Minimum occurrence: *{kls.min_occurs}*\n')
    f.write(f'- Maximum occurrence: *{kls.max_occurs}*\n')
    
    f.write('\n')



with open('sap_schema_19_1_0.rst', 'w') as f:

    f.write('.. _sap_xml_reference:\n\n')

    f.write('SAP XML reference\n')
    f.write('=================\n\n')

    f.write('This page contains the documentation for the XML schema `SAP-Schema-19.1.0 <https://github.com/communitiesuk/epb-register-api/tree/master/api/schemas/xml/SAP-Schema-19.1.0/SAP>`__.\n\n')
    f.write('This XML schema describes the format of the XML input files for SAP 10.2 calculations.\n\n')
    f.write('The root XML element can be either a :ref:`SAP-Compliance-Report` or a :ref:`SAP-Compliance-Report/SAP-Report` element.\n\n')
    
    SAP_Compliance_Report = classes_SAP_Schema_19_1_0.SAP_Compliance_Report
    SAP_Compliance_Report._parent_class = None
    SAP_Compliance_Report._expanded_name = SAP_Compliance_Report.element_name
    
    write_class(f, SAP_Compliance_Report)
    write_subclass(f, SAP_Compliance_Report)


with open('rdsap_schema_21_0_0.rst', 'w') as f:

    f.write('.. _rdsap_xml_reference:\n\n')

    f.write('RdSAP XML reference\n')
    f.write('===================\n\n')

    f.write('This page contains the documentation for the XML schema `RdSAP-Schema-21.0.0 <https://github.com/communitiesuk/epb-register-api/tree/master/api/schemas/xml/RdSAP-Schema-21.0.0/RdSAP>`__.\n\n')
    f.write('This XML schema describes the format of the XML input files for RdSAP 10 calculations.\n\n')
    f.write('The root XML element is a :ref:`RdSAP-Report` element.\n\n')
    
    RdSAP_Report = classes_RdSAP_Schema_21_0_0.RdSAP_Report
    RdSAP_Report._parent_class = None
    RdSAP_Report._expanded_name = RdSAP_Report.element_name
    RdSAP_Report._ref = f'#{RdSAP_Report.element_name.lower()}'

    write_class(f, RdSAP_Report)
    write_subclass(f, RdSAP_Report)










