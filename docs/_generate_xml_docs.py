from sap10calcs import classes_SAP_Schema_19_1_0

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
    f.write(f'## <a name="{kls._expanded_name}"></a>{kls.element_name}\n\n')
    f.write(f'`{kls._expanded_name}`\n\n')
    f.write(f'- Documentation: *{kls.documentation}*\n')

    if kls._parent_class is None:
        x = None
    else:
        x = f'[`{kls._parent_class.element_name}`](#{kls._parent_class._expanded_name})'
    f.write(f'- Parent element: {x}\n\n')
    



with open('sap_schema_19_1_0.md', 'w') as f:

    f.write('# SAP Schema 19.1.0. docs\n\n')
    f.write('This page contains the documentation for the XML schema [SAP-Schema-19.1.0](https://github.com/communitiesuk/epb-register-api/tree/master/api/schemas/xml/SAP-Schema-19.1.0/SAP).\n\n')
    f.write('This XML schema describes the format of the XML input files for SAP 10.2 calculations.\n\n')
    f.write('The root XML element can be either a [SAP-Compliance-Report](#SAP_Compliance_Report) or a [SAP-Report](#SAP_Compliance_Report__SAP_Report) element.\n\n')
    
    SAP_Compliance_Report = classes_SAP_Schema_19_1_0.SAP_Compliance_Report
    SAP_Compliance_Report._parent_class = None
    SAP_Compliance_Report._expanded_name = SAP_Compliance_Report.element_name

    write_class(f, SAP_Compliance_Report)
    write_subclass(f, SAP_Compliance_Report)










