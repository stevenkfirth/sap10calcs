# SAP Schema 19.1.0. docs

This page contains the documentation for the XML schema [SAP-Schema-19.1.0](https://github.com/communitiesuk/epb-register-api/tree/master/api/schemas/xml/SAP-Schema-19.1.0/SAP).

This XML schema describes the format of the XML input files for SAP 10.2 calculations.

The root XMl element can be either a [SAP-Compliance-Report](#SAP_Compliance_Report) or a [SAP-Report](#SAP_Compliance_Report__SAP_Report) element.

## <a name="SAP_Compliance_Report"></a>SAP-Compliance-Report

`SAP_Compliance_Report`

- Documentation: *None*
- Parent element: None

## <a name="SAP_Compliance_Report__SAP_Report"></a>SAP-Report

`SAP_Compliance_Report__SAP_Report`

- Documentation: *The SAP report corresponding to the compliance report.*
- Parent element: [`SAP-Compliance-Report`](#SAP_Compliance_Report)

## <a name="SAP_Compliance_Report__Client_Name"></a>Client-Name

`SAP_Compliance_Report__Client_Name`

- Documentation: *Name of the client. External to the EPC schema for GDPR purposes.*
- Parent element: [`SAP-Compliance-Report`](#SAP_Compliance_Report)

## <a name="SAP_Compliance_Report__Client_Company"></a>Client-Company

`SAP_Compliance_Report__Client_Company`

- Documentation: *Company name of the client. External to the EPC schema for GDPR purposes.*
- Parent element: [`SAP-Compliance-Report`](#SAP_Compliance_Report)

## <a name="SAP_Compliance_Report__Client_Address"></a>Client-Address

`SAP_Compliance_Report__Client_Address`

- Documentation: *Address of the client. External to the EPC schema for GDPR purposes.*
- Parent element: [`SAP-Compliance-Report`](#SAP_Compliance_Report)

## <a name="SAP_Compliance_Report__Is_Multiple_Compliance"></a>Is-Multiple-Compliance

`SAP_Compliance_Report__Is_Multiple_Compliance`

- Documentation: *Is the compliance report part of a multiple compliance calculation.*
- Parent element: [`SAP-Compliance-Report`](#SAP_Compliance_Report)

