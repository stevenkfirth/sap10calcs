from sap10calcs import classes_SAP_Schema_19_1_0

def write_class(f, kls):
    ""
    f.write(f'## <a name="{kls._expanded_name}"></a>{kls.element_name}\n\n')
    f.write(f'{kls._expanded_name}\n\n')
    f.write(f'Documentation: {kls.documentation}\n\n')



with open('sap_schema_19_1_0.md', 'w') as f:

    f.write('# SAP Schema 19.1.0. docs\n\n')
    f.write('Return to [homepage](index.md).\n\n')
    
    SAP_Compliance_Report = classes_SAP_Schema_19_1_0.SAP_Compliance_Report
    SAP_Compliance_Report._parent_class = None
    SAP_Compliance_Report._expanded_name = 'SAP_Compliance_Report'

    write_class(f, SAP_Compliance_Report)










