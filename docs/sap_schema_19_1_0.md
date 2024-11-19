# SAP Schema 19.1.0. docs

This page contains the documentation for the XML schema [SAP-Schema-19.1.0](https://github.com/communitiesuk/epb-register-api/tree/master/api/schemas/xml/SAP-Schema-19.1.0/SAP).

This XML schema describes the format of the XML input files for SAP 10.2 calculations.

The root XML element can be either a [SAP-Compliance-Report](#SAP_Compliance_Report) or a [SAP-Report](#SAP_Compliance_Report__SAP_Report) element.

## <a name="SAP-Compliance-Report"></a>SAP-Compliance-Report

`SAP-Compliance-Report`

- Documentation: *None*
- Parent element: None

## <a name="SAP-Compliance-Report/SAP-Report"></a>SAP-Report

`SAP-Compliance-Report/SAP-Report`

- Documentation: *The SAP report corresponding to the compliance report.*
- Parent element: [`SAP-Compliance-Report`](#SAP-Compliance-Report)

## <a name="SAP-Compliance-Report/SAP-Report/Schema-Version-Original"></a>Schema-Version-Original

`SAP-Compliance-Report/SAP-Report/Schema-Version-Original`

- Documentation: *The schema version that the data conformed to when it was lodged.*
- Parent element: [`SAP-Report`](#SAP-Compliance-Report/SAP-Report)

## <a name="SAP-Compliance-Report/SAP-Report/Schema-Version-Current"></a>Schema-Version-Current

`SAP-Compliance-Report/SAP-Report/Schema-Version-Current`

- Documentation: *The schema version to which the data conforms. This node is inserted by the register when a retrieval is requested. It must not be present in a lodgement being sent to the register.*
- Parent element: [`SAP-Report`](#SAP-Compliance-Report/SAP-Report)

## <a name="SAP-Compliance-Report/SAP-Report/SAP-Version"></a>SAP-Version

`SAP-Compliance-Report/SAP-Report/SAP-Version`

- Documentation: *SAP version that was used for the calculation.*
- Parent element: [`SAP-Report`](#SAP-Compliance-Report/SAP-Report)

## <a name="SAP-Compliance-Report/SAP-Report/SAP-Data-Version"></a>SAP-Data-Version

`SAP-Compliance-Report/SAP-Report/SAP-Data-Version`

- Documentation: *Version of SAP that was used to define the input data for the calculation.*
- Parent element: [`SAP-Report`](#SAP-Compliance-Report/SAP-Report)

## <a name="SAP-Compliance-Report/SAP-Report/PCDF-Revision-Number"></a>PCDF-Revision-Number

`SAP-Compliance-Report/SAP-Report/PCDF-Revision-Number`

- Documentation: *Revision Number of the PCDF file used for the calculations.*
- Parent element: [`SAP-Report`](#SAP-Compliance-Report/SAP-Report)

## <a name="SAP-Compliance-Report/SAP-Report/Calculation-Software-Name"></a>Calculation-Software-Name

`SAP-Compliance-Report/SAP-Report/Calculation-Software-Name`

- Documentation: *Name of the software used to perform the SAP calculation.*
- Parent element: [`SAP-Report`](#SAP-Compliance-Report/SAP-Report)

## <a name="SAP-Compliance-Report/SAP-Report/Calculation-Software-Version"></a>Calculation-Software-Version

`SAP-Compliance-Report/SAP-Report/Calculation-Software-Version`

- Documentation: *Version of the software used to perform the SAP calculation.*
- Parent element: [`SAP-Report`](#SAP-Compliance-Report/SAP-Report)

## <a name="SAP-Compliance-Report/SAP-Report/User-Interface-Name"></a>User-Interface-Name

`SAP-Compliance-Report/SAP-Report/User-Interface-Name`

- Documentation: *None*
- Parent element: [`SAP-Report`](#SAP-Compliance-Report/SAP-Report)

## <a name="SAP-Compliance-Report/SAP-Report/User-Interface-Version"></a>User-Interface-Version

`SAP-Compliance-Report/SAP-Report/User-Interface-Version`

- Documentation: *None*
- Parent element: [`SAP-Report`](#SAP-Compliance-Report/SAP-Report)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header"></a>Report-Header

`SAP-Compliance-Report/SAP-Report/Report-Header`

- Documentation: *None*
- Parent element: [`SAP-Report`](#SAP-Compliance-Report/SAP-Report)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/RRN"></a>RRN

`SAP-Compliance-Report/SAP-Report/Report-Header/RRN`

- Documentation: *Report Reference Number is the unique report Identifier that the report will be publicly known by. The RRN is allocated to the Report at the point that it is registered and will be algorithmically derived from the natural key characteristics of the Home Condition Report i.e. The Unique Property Reference Number (UPRN) and Inspection Date.*
- Parent element: [`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Inspection-Date"></a>Inspection-Date

`SAP-Compliance-Report/SAP-Report/Report-Header/Inspection-Date`

- Documentation: *The date that the inspection was actually carried out by the Home Inspector.*
- Parent element: [`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Report-Type"></a>Report-Type

`SAP-Compliance-Report/SAP-Report/Report-Header/Report-Type`

- Documentation: *The type of Home Inspection that was carried out. Initially the only allowed type will be a Home Condition Report inspection but this may be extended in the future to cover Energy Assessment Only inspections.*
- Parent element: [`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Completion-Date"></a>Completion-Date

`SAP-Compliance-Report/SAP-Report/Report-Header/Completion-Date`

- Documentation: *The date that the Home Inspector completed the report. This will be after the Inspection Date but generally before the Registration Date.*
- Parent element: [`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Registration-Date"></a>Registration-Date

`SAP-Compliance-Report/SAP-Report/Report-Header/Registration-Date`

- Documentation: *The date that the report was submitted to the HCR Registration Organisation for lodging in the HCR Register.*
- Parent element: [`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Status"></a>Status

`SAP-Compliance-Report/SAP-Report/Report-Header/Status`

- Documentation: *The Status of the Report. A Home Condition Report can have a number of distinct states depending on whereabouts in its overall lifecycle the HCR is - see Home Condition Report Statechart for more details.*
- Parent element: [`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Language-Code"></a>Language-Code

`SAP-Compliance-Report/SAP-Report/Report-Header/Language-Code`

- Documentation: *The language that the report is written in.*
- Parent element: [`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Tenure"></a>Tenure

`SAP-Compliance-Report/SAP-Report/Report-Header/Tenure`

- Documentation: *None*
- Parent element: [`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Transaction-Type"></a>Transaction-Type

`SAP-Compliance-Report/SAP-Report/Report-Header/Transaction-Type`

- Documentation: *None*
- Parent element: [`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Seller-Commission-Report"></a>Seller-Commission-Report

`SAP-Compliance-Report/SAP-Report/Report-Header/Seller-Commission-Report`

- Documentation: *Indicates that the HCR was commissioned by the Seller of the Property or their Agent. This is required in order to differentiate these reports from Buyer commisioned reports which are not eligible for inclusion in a Home Information Pack*
- Parent element: [`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Property-Type"></a>Property-Type

`SAP-Compliance-Report/SAP-Report/Report-Header/Property-Type`

- Documentation: *Describes the type of Property that is being inspected. This should be the same as the Property-Type recorded in the Property-Details section.*
- Parent element: [`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector"></a>Home-Inspector

`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector`

- Documentation: *None*
- Parent element: [`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Name"></a>Name

`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Name`

- Documentation: *The name by which the Home Inspector is registered. This is a structured name containing prefix, first name + surname.*
- Parent element: [`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Notify-Lodgement"></a>Notify-Lodgement

`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Notify-Lodgement`

- Documentation: *Indicates whether the assessor wants to be notified that a the report has been lodged in the register*
- Parent element: [`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address"></a>Contact-Address

`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address`

- Documentation: *The address that any written correspondence can be sent to. This is not the same as the Registered Address because it may, of course, be a Post Office Box.*
- Parent element: [`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Address-Line-1"></a>Address-Line-1

`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Address-Line-1`

- Documentation: *None*
- Parent element: [`Contact-Address`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Address-Line-2"></a>Address-Line-2

`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Address-Line-2`

- Documentation: *None*
- Parent element: [`Contact-Address`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Address-Line-3"></a>Address-Line-3

`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Address-Line-3`

- Documentation: *None*
- Parent element: [`Contact-Address`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Post-Town"></a>Post-Town

`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Post-Town`

- Documentation: *None*
- Parent element: [`Contact-Address`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Postcode"></a>Postcode

`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Postcode`

- Documentation: *The Postcode for the Address*
- Parent element: [`Contact-Address`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Web-Site"></a>Web-Site

`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Web-Site`

- Documentation: *None*
- Parent element: [`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/E-Mail"></a>E-Mail

`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/E-Mail`

- Documentation: *the E-Mail address that the Authorised User can be contacted at.*
- Parent element: [`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Fax"></a>Fax

`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Fax`

- Documentation: *None*
- Parent element: [`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Telephone"></a>Telephone

`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Telephone`

- Documentation: *None*
- Parent element: [`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Company-Name"></a>Company-Name

`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Company-Name`

- Documentation: *The Name of the Company that the assessor is employed by.*
- Parent element: [`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Scheme-Name"></a>Scheme-Name

`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Scheme-Name`

- Documentation: *None*
- Parent element: [`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Scheme-Web-Site"></a>Scheme-Web-Site

`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Scheme-Web-Site`

- Documentation: *None*
- Parent element: [`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Identification-Number"></a>Identification-Number

`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Identification-Number`

- Documentation: *None*
- Parent element: [`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Identification-Number/Certificate-Number"></a>Certificate-Number

`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Identification-Number/Certificate-Number`

- Documentation: *The unique identifier assigned to the assessor by the scheme by which they can be identified throughout their membership of the scheme.*
- Parent element: [`Identification-Number`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Identification-Number)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Identification-Number/Membership-Number"></a>Membership-Number

`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Identification-Number/Membership-Number`

- Documentation: *For Scottish DEAs only*
- Parent element: [`Identification-Number`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Identification-Number)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Property"></a>Property

`SAP-Compliance-Report/SAP-Report/Report-Header/Property`

- Documentation: *None*
- Parent element: [`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address"></a>Address

`SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address`

- Documentation: *Address for the property.*
- Parent element: [`Property`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Address-Line-1"></a>Address-Line-1

`SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Address-Line-1`

- Documentation: *None*
- Parent element: [`Address`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Address-Line-2"></a>Address-Line-2

`SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Address-Line-2`

- Documentation: *None*
- Parent element: [`Address`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Address-Line-3"></a>Address-Line-3

`SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Address-Line-3`

- Documentation: *None*
- Parent element: [`Address`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Post-Town"></a>Post-Town

`SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Post-Town`

- Documentation: *None*
- Parent element: [`Address`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Postcode"></a>Postcode

`SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Postcode`

- Documentation: *The Postcode for the Address*
- Parent element: [`Address`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Property/UPRN"></a>UPRN

`SAP-Compliance-Report/SAP-Report/Report-Header/Property/UPRN`

- Documentation: *Unique Property Reference Number*
- Parent element: [`Property`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Property/Site-Reference"></a>Site-Reference

`SAP-Compliance-Report/SAP-Report/Report-Header/Property/Site-Reference`

- Documentation: *A site reference*
- Parent element: [`Property`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Property/Plot-Reference"></a>Plot-Reference

`SAP-Compliance-Report/SAP-Report/Report-Header/Property/Plot-Reference`

- Documentation: *A plot reference*
- Parent element: [`Property`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Region-Code"></a>Region-Code

`SAP-Compliance-Report/SAP-Report/Report-Header/Region-Code`

- Documentation: *Region within the UK.*
- Parent element: [`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Country-Code"></a>Country-Code

`SAP-Compliance-Report/SAP-Report/Report-Header/Country-Code`

- Documentation: *Country within the UK.*
- Parent element: [`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Related-Party-Disclosure"></a>Related-Party-Disclosure

`SAP-Compliance-Report/SAP-Report/Report-Header/Related-Party-Disclosure`

- Documentation: *None*
- Parent element: [`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Related-Party-Disclosure/Related-Party-Disclosure-Text"></a>Related-Party-Disclosure-Text

`SAP-Compliance-Report/SAP-Report/Report-Header/Related-Party-Disclosure/Related-Party-Disclosure-Text`

- Documentation: *For backward compatibility only.*
- Parent element: [`Related-Party-Disclosure`](#SAP-Compliance-Report/SAP-Report/Report-Header/Related-Party-Disclosure)

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Related-Party-Disclosure/Related-Party-Disclosure-Number"></a>Related-Party-Disclosure-Number

`SAP-Compliance-Report/SAP-Report/Report-Header/Related-Party-Disclosure/Related-Party-Disclosure-Number`

- Documentation: *Code indicating any potential conflicts of interest or commercial relationships with other parties.*
- Parent element: [`Related-Party-Disclosure`](#SAP-Compliance-Report/SAP-Report/Report-Header/Related-Party-Disclosure)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment"></a>Energy-Assessment

`SAP-Compliance-Report/SAP-Report/Energy-Assessment`

- Documentation: *None*
- Parent element: [`SAP-Report`](#SAP-Compliance-Report/SAP-Report)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Assessment-Date"></a>Assessment-Date

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Assessment-Date`

- Documentation: *Date of assessment.*
- Parent element: [`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary"></a>Property-Summary

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`

- Documentation: *None*
- Parent element: [`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls"></a>Walls

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls`

- Documentation: *None*
- Parent element: [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls/Description"></a>Description

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls/Description`

- Documentation: *Overall description of the property feature*
- Parent element: [`Walls`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls/Energy-Efficiency-Rating"></a>Energy-Efficiency-Rating

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls/Energy-Efficiency-Rating`

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: [`Walls`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls/Environmental-Efficiency-Rating"></a>Environmental-Efficiency-Rating

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls/Environmental-Efficiency-Rating`

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: [`Walls`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof"></a>Roof

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof`

- Documentation: *None*
- Parent element: [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof/Description"></a>Description

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof/Description`

- Documentation: *Overall description of the property feature*
- Parent element: [`Roof`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof/Energy-Efficiency-Rating"></a>Energy-Efficiency-Rating

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof/Energy-Efficiency-Rating`

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: [`Roof`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof/Environmental-Efficiency-Rating"></a>Environmental-Efficiency-Rating

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof/Environmental-Efficiency-Rating`

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: [`Roof`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor"></a>Floor

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor`

- Documentation: *None*
- Parent element: [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor/Description"></a>Description

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor/Description`

- Documentation: *Overall description of the property feature*
- Parent element: [`Floor`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor/Energy-Efficiency-Rating"></a>Energy-Efficiency-Rating

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor/Energy-Efficiency-Rating`

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: [`Floor`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor/Environmental-Efficiency-Rating"></a>Environmental-Efficiency-Rating

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor/Environmental-Efficiency-Rating`

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: [`Floor`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows"></a>Windows

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows`

- Documentation: *None*
- Parent element: [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows/Description"></a>Description

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows/Description`

- Documentation: *Overall description of the property feature*
- Parent element: [`Windows`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows/Energy-Efficiency-Rating"></a>Energy-Efficiency-Rating

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows/Energy-Efficiency-Rating`

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: [`Windows`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows/Environmental-Efficiency-Rating"></a>Environmental-Efficiency-Rating

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows/Environmental-Efficiency-Rating`

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: [`Windows`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating"></a>Main-Heating

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating`

- Documentation: *None*
- Parent element: [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating/Description"></a>Description

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating/Description`

- Documentation: *Overall description of the property feature*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating/Energy-Efficiency-Rating"></a>Energy-Efficiency-Rating

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating/Energy-Efficiency-Rating`

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating/Environmental-Efficiency-Rating"></a>Environmental-Efficiency-Rating

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating/Environmental-Efficiency-Rating`

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls"></a>Main-Heating-Controls

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls`

- Documentation: *None*
- Parent element: [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls/Description"></a>Description

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls/Description`

- Documentation: *Overall description of the property feature*
- Parent element: [`Main-Heating-Controls`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls/Energy-Efficiency-Rating"></a>Energy-Efficiency-Rating

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls/Energy-Efficiency-Rating`

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: [`Main-Heating-Controls`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls/Environmental-Efficiency-Rating"></a>Environmental-Efficiency-Rating

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls/Environmental-Efficiency-Rating`

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: [`Main-Heating-Controls`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating"></a>Secondary-Heating

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating`

- Documentation: *None*
- Parent element: [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating/Description"></a>Description

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating/Description`

- Documentation: *Overall description of the property feature*
- Parent element: [`Secondary-Heating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating/Energy-Efficiency-Rating"></a>Energy-Efficiency-Rating

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating/Energy-Efficiency-Rating`

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: [`Secondary-Heating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating/Environmental-Efficiency-Rating"></a>Environmental-Efficiency-Rating

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating/Environmental-Efficiency-Rating`

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: [`Secondary-Heating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water"></a>Hot-Water

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water`

- Documentation: *None*
- Parent element: [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water/Description"></a>Description

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water/Description`

- Documentation: *Overall description of the property feature*
- Parent element: [`Hot-Water`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water/Energy-Efficiency-Rating"></a>Energy-Efficiency-Rating

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water/Energy-Efficiency-Rating`

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: [`Hot-Water`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water/Environmental-Efficiency-Rating"></a>Environmental-Efficiency-Rating

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water/Environmental-Efficiency-Rating`

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: [`Hot-Water`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting"></a>Lighting

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting`

- Documentation: *None*
- Parent element: [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting/Description"></a>Description

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting/Description`

- Documentation: *Overall description of the property feature*
- Parent element: [`Lighting`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting/Energy-Efficiency-Rating"></a>Energy-Efficiency-Rating

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting/Energy-Efficiency-Rating`

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: [`Lighting`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting/Environmental-Efficiency-Rating"></a>Environmental-Efficiency-Rating

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting/Environmental-Efficiency-Rating`

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: [`Lighting`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness"></a>Air-Tightness

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness`

- Documentation: *None*
- Parent element: [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness/Description"></a>Description

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness/Description`

- Documentation: *Overall description of the property feature*
- Parent element: [`Air-Tightness`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness/Energy-Efficiency-Rating"></a>Energy-Efficiency-Rating

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness/Energy-Efficiency-Rating`

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: [`Air-Tightness`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness/Environmental-Efficiency-Rating"></a>Environmental-Efficiency-Rating

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness/Environmental-Efficiency-Rating`

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: [`Air-Tightness`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Has-Fixed-Air-Conditioning"></a>Has-Fixed-Air-Conditioning

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Has-Fixed-Air-Conditioning`

- Documentation: *Fixed air conditioning?*
- Parent element: [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Has-Hot-Water-Cylinder"></a>Has-Hot-Water-Cylinder

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Has-Hot-Water-Cylinder`

- Documentation: *Hot water cylinder?*
- Parent element: [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Has-Heated-Separate-Conservatory"></a>Has-Heated-Separate-Conservatory

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Has-Heated-Separate-Conservatory`

- Documentation: *Heated separate conservatory?*
- Parent element: [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Dwelling-Type"></a>Dwelling-Type

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Dwelling-Type`

- Documentation: *Is a string such as Detached house or Top-floor flat*
- Parent element: [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Total-Floor-Area"></a>Total-Floor-Area

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Total-Floor-Area`

- Documentation: *Is a number such as 125*
- Parent element: [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Multiple-Glazed-Percentage"></a>Multiple-Glazed-Percentage

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Multiple-Glazed-Percentage`

- Documentation: *Fraction of windows that are multiply glazed to nearest 1%.*
- Parent element: [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Multiple-Glazed-Percentage-NR"></a>Multiple-Glazed-Percentage-NR

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Multiple-Glazed-Percentage-NR`

- Documentation: *For backward compatibility only, do not use.*
- Parent element: [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Is-Zero-Carbon-Home"></a>Is-Zero-Carbon-Home

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Is-Zero-Carbon-Home`

- Documentation: *Is dwelling a Zero Carbon Home?*
- Parent element: [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use"></a>Energy-Use

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`

- Documentation: *Calculated results from the energy assessment.*
- Parent element: [`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/DER"></a>DER

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/DER`

- Documentation: *The DER of the Property*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/TER"></a>TER

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/TER`

- Documentation: *The TER of the Property*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/DPER"></a>DPER

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/DPER`

- Documentation: *The DPER of the Property*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/TPER"></a>TPER

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/TPER`

- Documentation: *The TPER of the Property*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/DFEE"></a>DFEE

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/DFEE`

- Documentation: *The DFEE of the Property*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/TFEE"></a>TFEE

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/TFEE`

- Documentation: *The TFEE of the Property*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Rating-Current"></a>Energy-Rating-Current

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Rating-Current`

- Documentation: *The Current Energy Rating of the Property*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Rating-Potential"></a>Energy-Rating-Potential

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Rating-Potential`

- Documentation: *The overall Energy Rating for the Property being assessed.*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Rating-Average"></a>Energy-Rating-Average

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Rating-Average`

- Documentation: *Average SAP rating for the country concerned. 0 if unknown or not applicable*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Environmental-Impact-Current"></a>Environmental-Impact-Current

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Environmental-Impact-Current`

- Documentation: *The estimated current Environmental Impact Rating of the property*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Environmental-Impact-Potential"></a>Environmental-Impact-Potential

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Environmental-Impact-Potential`

- Documentation: *The estimated potential Environmental Impact Rating of the property*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Consumption-Current"></a>Energy-Consumption-Current

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Consumption-Current`

- Documentation: *Estimated total energy consumption for the Property in a 12 month period. Value is Kilowatt Hours per Square Metre (kWh/m2)*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Consumption-Potential"></a>Energy-Consumption-Potential

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Consumption-Potential`

- Documentation: *Estimated total energy consumption for the Property in a 12 month period. Value is Kilowatt Hours per Square Metre (kWh/m2)*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/CO2-Emissions-Current"></a>CO2-Emissions-Current

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/CO2-Emissions-Current`

- Documentation: *CO2 emissions per year in tonnes/year.*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/CO2-Emissions-Current-Per-Floor-Area"></a>CO2-Emissions-Current-Per-Floor-Area

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/CO2-Emissions-Current-Per-Floor-Area`

- Documentation: *CO2 emissions per square metre floor area per year in kg/m2.*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/CO2-Emissions-Potential"></a>CO2-Emissions-Potential

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/CO2-Emissions-Potential`

- Documentation: *Estimated value in Tonnes per Year of the total CO2 emissions produced by the Property in 12 month period.*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Lighting-Cost-Current"></a>Lighting-Cost-Current

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Lighting-Cost-Current`

- Documentation: *The current estimated cost of Lighting for the property*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Lighting-Cost-Potential"></a>Lighting-Cost-Potential

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Lighting-Cost-Potential`

- Documentation: *The current estimated cost of Lighting for the property*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Heating-Cost-Current"></a>Heating-Cost-Current

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Heating-Cost-Current`

- Documentation: *The current estimated cost of Heating for the property*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Heating-Cost-Potential"></a>Heating-Cost-Potential

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Heating-Cost-Potential`

- Documentation: *The current estimated cost of Heating for the property*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Hot-Water-Cost-Current"></a>Hot-Water-Cost-Current

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Hot-Water-Cost-Current`

- Documentation: *|The current estimated cost of Hot Water for the property*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Hot-Water-Cost-Potential"></a>Hot-Water-Cost-Potential

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Hot-Water-Cost-Potential`

- Documentation: *|The current estimated cost of Hot Water for the property*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements"></a>Suggested-Improvements

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements`

- Documentation: *Improvement measures listed on the EPC.*
- Parent element: [`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement"></a>Improvement

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`

- Documentation: *None*
- Parent element: [`Suggested-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Sequence"></a>Sequence

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Sequence`

- Documentation: *Sequence of the Suggested Improvements within the set of Suggested Improvements. This is used to order the Recommendations on the output HCR / EPC so that the cumulative Ratings make sense. The Improved Energy Ratings that result from carrying out a Suggested Improvement are cumulative and assume that the improvements have been installed in the order they appear in the list. Hence they must be sequenced.*
- Parent element: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Category"></a>Improvement-Category

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Category`

- Documentation: *The category of improvement. This identifies where on the report the recommendation is printed.*
- Parent element: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Type"></a>Improvement-Type

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Type`

- Documentation: *Suggested work to be carried out on the Property to improve its energy efficiency. This should be a enumerated list of acceptable improvements but it hasn't yet been defined.*
- Parent element: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Typical-Saving"></a>Typical-Saving

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Typical-Saving`

- Documentation: *Typical savings (in British Pounds) per year if the suggested improvement is carried out. 0 if not assessed*
- Parent element: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Energy-Performance-Rating"></a>Energy-Performance-Rating

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Energy-Performance-Rating`

- Documentation: *The estimated Energy performance rating of the Property after the Suggested Improvement has been carried out providing any preceding Suggested Improvement has also been carried out. 0 if not assessed*
- Parent element: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Environmental-Impact-Rating"></a>Environmental-Impact-Rating

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Environmental-Impact-Rating`

- Documentation: *The estimated Environmental Impact rating of the Property after the Suggested Improvement has been carried out providing any preceding Suggested Improvement has also been carried out. 0 if not assessed*
- Parent element: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details"></a>Improvement-Details

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details`

- Documentation: *None*
- Parent element: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts"></a>Improvement-Texts

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts`

- Documentation: *For backward compatability only*
- Parent element: [`Improvement-Details`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Summary"></a>Improvement-Summary

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Summary`

- Documentation: *A short description of the suggested improvement.*
- Parent element: [`Improvement-Texts`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Heading"></a>Improvement-Heading

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Heading`

- Documentation: *Text to precede the improvement description. If this field is not provided the 'Improvement-Summary' is used instead.*
- Parent element: [`Improvement-Texts`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Description"></a>Improvement-Description

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Description`

- Documentation: *Detailed description of the suggested improvement.*
- Parent element: [`Improvement-Texts`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Number"></a>Improvement-Number

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Number`

- Documentation: *None*
- Parent element: [`Improvement-Details`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Indicative-Cost"></a>Indicative-Cost

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Indicative-Cost`

- Documentation: *None*
- Parent element: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Green-Deal-Category"></a>Green-Deal-Category

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Green-Deal-Category`

- Documentation: *None*
- Parent element: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/LZC-Energy-Sources"></a>LZC-Energy-Sources

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/LZC-Energy-Sources`

- Documentation: *None*
- Parent element: [`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/LZC-Energy-Sources/LZC-Energy-Source"></a>LZC-Energy-Source

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/LZC-Energy-Sources/LZC-Energy-Source`

- Documentation: *Low and zero carbon energy source(s) for the property.*
- Parent element: [`LZC-Energy-Sources`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/LZC-Energy-Sources)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive"></a>Renewable-Heat-Incentive

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive`

- Documentation: *None*
- Parent element: [`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-New-Dwelling"></a>RHI-New-Dwelling

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-New-Dwelling`

- Documentation: *None*
- Parent element: [`Renewable-Heat-Incentive`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-New-Dwelling/Space-Heating"></a>Space-Heating

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-New-Dwelling/Space-Heating`

- Documentation: *Space heating requirement.*
- Parent element: [`RHI-New-Dwelling`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-New-Dwelling)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-New-Dwelling/Water-Heating"></a>Water-Heating

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-New-Dwelling/Water-Heating`

- Documentation: *Water heating requirement.*
- Parent element: [`RHI-New-Dwelling`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-New-Dwelling)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling"></a>RHI-Existing-Dwelling

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling`

- Documentation: *None*
- Parent element: [`Renewable-Heat-Incentive`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Space-Heating-Existing-Dwelling"></a>Space-Heating-Existing-Dwelling

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Space-Heating-Existing-Dwelling`

- Documentation: *Space heating requirement for existing dwelling.*
- Parent element: [`RHI-Existing-Dwelling`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Space-Heating-With-Loft-Insulation"></a>Space-Heating-With-Loft-Insulation

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Space-Heating-With-Loft-Insulation`

- Documentation: *Space heating requirement after implementation of loft insulation recommendation, omit if loft insulation not recommended. For backwards compatibility only, do not use*
- Parent element: [`RHI-Existing-Dwelling`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Space-Heating-With-Cavity-Insulation"></a>Space-Heating-With-Cavity-Insulation

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Space-Heating-With-Cavity-Insulation`

- Documentation: *Space heating requirement after implementation of cavity insulation recommendation, omit if cavity insulation not recommended. For backwards compatibility only, do not use*
- Parent element: [`RHI-Existing-Dwelling`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Space-Heating-With-Loft-And-Cavity-Insulation"></a>Space-Heating-With-Loft-And-Cavity-Insulation

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Space-Heating-With-Loft-And-Cavity-Insulation`

- Documentation: *Space heating requirement after implementation of loft and cavity insulation recommendations, same as existing dwelling if neither is recommended. For backwards compatibility only, do not use*
- Parent element: [`RHI-Existing-Dwelling`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Water-Heating"></a>Water-Heating

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Water-Heating`

- Documentation: *Water heating requirement.*
- Parent element: [`RHI-Existing-Dwelling`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Impact-Of-Loft-Insulation"></a>Impact-Of-Loft-Insulation

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Impact-Of-Loft-Insulation`

- Documentation: *Reduction in space heating requirement with loft insulation (as negative value). Omit if not applicable*
- Parent element: [`RHI-Existing-Dwelling`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Impact-Of-Cavity-Insulation"></a>Impact-Of-Cavity-Insulation

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Impact-Of-Cavity-Insulation`

- Documentation: *Reduction in space heating requirement with cavity insulation (as negative value). Omit if not applicable*
- Parent element: [`RHI-Existing-Dwelling`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Impact-Of-Solid-Wall-Insulation"></a>Impact-Of-Solid-Wall-Insulation

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Impact-Of-Solid-Wall-Insulation`

- Documentation: *Reduction in space heating requirement with solid wall insulation (as negative value). Omit if not applicable*
- Parent element: [`RHI-Existing-Dwelling`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package"></a>Green-Deal-Package

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package`

- Documentation: *Improvements that can form a Green Deal package*
- Parent element: [`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement"></a>Green-Deal-Improvement

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement`

- Documentation: *Improvements from Suggested-Improvements in the Green Deal package*
- Parent element: [`Green-Deal-Package`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement/Improvement-Type"></a>Improvement-Type

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement/Improvement-Type`

- Documentation: *None*
- Parent element: [`Green-Deal-Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement/Improvement-Number"></a>Improvement-Number

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement/Improvement-Number`

- Documentation: *None*
- Parent element: [`Green-Deal-Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Electricity-Saving"></a>Electricity-Saving

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Electricity-Saving`

- Documentation: *Total electricity saving for the package*
- Parent element: [`Green-Deal-Package`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Gas-Saving"></a>Gas-Saving

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Gas-Saving`

- Documentation: *Total gas saving for the package*
- Parent element: [`Green-Deal-Package`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Other-Fuel-Saving"></a>Other-Fuel-Saving

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Other-Fuel-Saving`

- Documentation: *Total other saving for the package*
- Parent element: [`Green-Deal-Package`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements"></a>Alternative-Improvements

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements`

- Documentation: *Alternative improvements to some of those given in Suggested-Improvements*
- Parent element: [`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement"></a>Improvement

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`

- Documentation: *None*
- Parent element: [`Alternative-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Sequence"></a>Sequence

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Sequence`

- Documentation: *Sequence of the Suggested Improvements within the set of Suggested Improvements. This is used to order the Recommendations on the output HCR / EPC so that the cumulative Ratings make sense. The Improved Energy Ratings that result from carrying out a Suggested Improvement are cumulative and assume that the improvements have been installed in the order they appear in the list. Hence they must be sequenced.*
- Parent element: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Category"></a>Improvement-Category

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Category`

- Documentation: *The category of improvement. This identifies where on the report the recommendation is printed.*
- Parent element: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Type"></a>Improvement-Type

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Type`

- Documentation: *Suggested work to be carried out on the Property to improve its energy efficiency. This should be a enumerated list of acceptable improvements but it hasn't yet been defined.*
- Parent element: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Typical-Saving"></a>Typical-Saving

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Typical-Saving`

- Documentation: *Typical savings (in British Pounds) per year if the suggested improvement is carried out. 0 if not assessed*
- Parent element: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Energy-Performance-Rating"></a>Energy-Performance-Rating

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Energy-Performance-Rating`

- Documentation: *The estimated Energy performance rating of the Property after the Suggested Improvement has been carried out providing any preceding Suggested Improvement has also been carried out. 0 if not assessed*
- Parent element: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Environmental-Impact-Rating"></a>Environmental-Impact-Rating

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Environmental-Impact-Rating`

- Documentation: *The estimated Environmental Impact rating of the Property after the Suggested Improvement has been carried out providing any preceding Suggested Improvement has also been carried out. 0 if not assessed*
- Parent element: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details"></a>Improvement-Details

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details`

- Documentation: *None*
- Parent element: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts"></a>Improvement-Texts

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts`

- Documentation: *For backward compatability only*
- Parent element: [`Improvement-Details`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Summary"></a>Improvement-Summary

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Summary`

- Documentation: *A short description of the suggested improvement.*
- Parent element: [`Improvement-Texts`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Heading"></a>Improvement-Heading

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Heading`

- Documentation: *Text to precede the improvement description. If this field is not provided the 'Improvement-Summary' is used instead.*
- Parent element: [`Improvement-Texts`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Description"></a>Improvement-Description

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Description`

- Documentation: *Detailed description of the suggested improvement.*
- Parent element: [`Improvement-Texts`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Number"></a>Improvement-Number

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Number`

- Documentation: *None*
- Parent element: [`Improvement-Details`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Indicative-Cost"></a>Indicative-Cost

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Indicative-Cost`

- Documentation: *None*
- Parent element: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Green-Deal-Category"></a>Green-Deal-Category

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Green-Deal-Category`

- Documentation: *None*
- Parent element: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum"></a>Addendum

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum`

- Documentation: *None*
- Parent element: [`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/Cavity-Fill-Recommended"></a>Cavity-Fill-Recommended

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/Cavity-Fill-Recommended`

- Documentation: *Cavity fill is recommended*
- Parent element: [`Addendum`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/Stone-Walls"></a>Stone-Walls

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/Stone-Walls`

- Documentation: *Stone walls present, not insulated*
- Parent element: [`Addendum`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/System-Build"></a>System-Build

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/System-Build`

- Documentation: *System build present*
- Parent element: [`Addendum`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/Access-Issues"></a>Access-Issues

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/Access-Issues`

- Documentation: *Dwelling has access issues for cavity wall insulation. Include only when at least one of Cavity-Fill-Recommended, Stone-Walls, System-Build is also present*
- Parent element: [`Addendum`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/High-Exposure"></a>High-Exposure

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/High-Exposure`

- Documentation: *Dwelling may be exposed to wind-driven rain. Include only when at least one of Cavity-Fill-Recommended, Stone-Walls, System-Build is also present*
- Parent element: [`Addendum`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum)

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/Narrow-Cavities"></a>Narrow-Cavities

`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/Narrow-Cavities`

- Documentation: *Dwelling may have narrow cavities. Include only when Cavity-Fill-Recommended is also present*
- Parent element: [`Addendum`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data"></a>SAP10-Data

`SAP-Compliance-Report/SAP-Report/SAP10-Data`

- Documentation: *None*
- Parent element: [`SAP-Report`](#SAP-Compliance-Report/SAP-Report)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/Data-Type"></a>Data-Type

`SAP-Compliance-Report/SAP-Report/SAP10-Data/Data-Type`

- Documentation: *Type of SAP data that has been collected.*
- Parent element: [`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details"></a>SAP-Property-Details

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`

- Documentation: *None*
- Parent element: [`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Property-Type"></a>Property-Type

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Property-Type`

- Documentation: *The type of Property, such as House, Flat, Mansion, Maisonette etc.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Built-Form"></a>Built-Form

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Built-Form`

- Documentation: *The building type of the Property e.g. Detached, Semi-Detached, Terrace etc. Together with the Property Type, the Built Form provides a structured description of the property.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Living-Area"></a>Living-Area

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Living-Area`

- Documentation: *The size of the living area in square metres. The living area is the room marked on a plan as the lounge or living room, or the largest public room (irrespective of usage by particular occupants), together with any rooms not separated from the lounge or living room by doors, and including any cupboards directly accessed from the lounge or living room. Living area does not, however, extend over more than one storey, even when stairs enter the living area directly.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Lowest-Storey-Area"></a>Lowest-Storey-Area

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Lowest-Storey-Area`

- Documentation: *The Area of the lowest storey in square meters including unheated or communal areas such as garages or corridors.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Orientation"></a>Orientation

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Orientation`

- Documentation: *The orientation of the front of the property.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Conservatory-Type"></a>Conservatory-Type

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Conservatory-Type`

- Documentation: *Type of conservatory.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Terrain-Type"></a>Terrain-Type

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Terrain-Type`

- Documentation: *Terrain type. Needed for wind-turbines and for applying measures.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Has-Special-Feature"></a>Has-Special-Feature

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Has-Special-Feature`

- Documentation: *For backwards compatibility only, do not use.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Special-Feature-Description"></a>Special-Feature-Description

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Special-Feature-Description`

- Documentation: *For backwards compatibility only, do not use.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Energy-Saved-Or-Generated"></a>Energy-Saved-Or-Generated

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Energy-Saved-Or-Generated`

- Documentation: *For backwards compatibility only, do not use.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Saved-Or-Generated-Fuel"></a>Saved-Or-Generated-Fuel

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Saved-Or-Generated-Fuel`

- Documentation: *For backwards compatibility only, do not use.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Energy-Used"></a>Energy-Used

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Energy-Used`

- Documentation: *For backwards compatibility only, do not use.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Energy-Used-Fuel"></a>Energy-Used-Fuel

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Energy-Used-Fuel`

- Documentation: *For backwards compatibility only, do not use.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Is-In-Smoke-Control-Area"></a>Is-In-Smoke-Control-Area

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Is-In-Smoke-Control-Area`

- Documentation: *Is property in a smoke control area? Only if a solid fuel appliance is used.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Cold-Water-Source"></a>Cold-Water-Source

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Cold-Water-Source`

- Documentation: *What is the cold water source? Either mains or header tank.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Windows-Overshading"></a>Windows-Overshading

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Windows-Overshading`

- Documentation: *Average amount of overshading of windows.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Thermal-Mass-Parameter"></a>Thermal-Mass-Parameter

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Thermal-Mass-Parameter`

- Documentation: *Average thermal mass parameter for the dwelling in kJ/m2K. If omitted it is calculated using the kappa values of each element.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Additional-Allowable-Electricity-Generation"></a>Additional-Allowable-Electricity-Generation

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Additional-Allowable-Electricity-Generation`

- Documentation: *Additional allowable electricity generation applicable to this dwelling in kWh per square metre; only if Zero Carbon Home assessment.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Gas-Smart-Meter-Present"></a>Gas-Smart-Meter-Present

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Gas-Smart-Meter-Present`

- Documentation: *None*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Electricity-Smart-Meter-Present"></a>Electricity-Smart-Meter-Present

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Electricity-Smart-Meter-Present`

- Documentation: *None*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Is-Dwelling-Export-Capable"></a>Is-Dwelling-Export-Capable

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Is-Dwelling-Export-Capable`

- Documentation: *None*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/PV-Connection"></a>PV-Connection

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/PV-Connection`

- Documentation: *None*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/PV-Diverter"></a>PV-Diverter

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/PV-Diverter`

- Documentation: *Diverter present.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Battery-Capacity"></a>Battery-Capacity

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Battery-Capacity`

- Documentation: *Battery capacity if diverter present.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Is-Wind-Turbine-Connected-To-Dwelling-Meter"></a>Is-Wind-Turbine-Connected-To-Dwelling-Meter

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Is-Wind-Turbine-Connected-To-Dwelling-Meter`

- Documentation: *Whether the wind turbine is connected to the Dwelling's meter.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating"></a>SAP-Heating

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`

- Documentation: *None*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Water-Heating-Code"></a>Water-Heating-Code

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Water-Heating-Code`

- Documentation: *The type of Water Heating present in the Property.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Water-Fuel-Type"></a>Water-Fuel-Type

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Water-Fuel-Type`

- Documentation: *The type of fuel used to power the central heating e.g. Gas, Electricity. Not used if water system is main or secondary system.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Has-Hot-Water-Cylinder"></a>Has-Hot-Water-Cylinder

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Has-Hot-Water-Cylinder`

- Documentation: *Hot water cylinder?*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Category"></a>Secondary-Heating-Category

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Category`

- Documentation: *Category of heating system for the secondary heating system.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Data-Source"></a>Secondary-Heating-Data-Source

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Data-Source`

- Documentation: *Source of secondary heating system data; only if secondary heating system.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Efficiency"></a>Secondary-Heating-Efficiency

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Efficiency`

- Documentation: *None*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Commisioning-Certificate"></a>Secondary-Heating-Commisioning-Certificate

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Commisioning-Certificate`

- Documentation: *Secondary heating system commisioning certificate number.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Installation-Engineer"></a>Secondary-Heating-Installation-Engineer

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Installation-Engineer`

- Documentation: *Secondary heating installation engineer registration reference.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Code"></a>Secondary-Heating-Code

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Code`

- Documentation: *Type of secondary heating present in the property; only if required and if heating data source is SAP table.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Fuel-Type"></a>Secondary-Fuel-Type

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Fuel-Type`

- Documentation: *The type of fuel used to power the secondary heating e.g. Gas, Electricity; only if required.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-PCDF-Fuel-Index"></a>Secondary-Heating-PCDF-Fuel-Index

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-PCDF-Fuel-Index`

- Documentation: *PCDF index number of the fuel type, only if Secondary-Fuel-Type is 99 (fuel from database).*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Flue-Type"></a>Secondary-Heating-Flue-Type

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Flue-Type`

- Documentation: *Secondary flue type; only if secondary efficiency is manufacturer declaration and if there is a flue.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Thermal-Store"></a>Thermal-Store

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Thermal-Store`

- Documentation: *The type of thermal store; not used if main heating system is community heating scheme.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Has-Fixed-Air-Conditioning"></a>Has-Fixed-Air-Conditioning

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Has-Fixed-Air-Conditioning`

- Documentation: *Fixed air conditioning?*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Immersion-Heating-Type"></a>Immersion-Heating-Type

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Immersion-Heating-Type`

- Documentation: *The type of immersion heating; only if immersion.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Heat-Pump-Assisted-By-Immersion"></a>Is-Heat-Pump-Assisted-By-Immersion

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Heat-Pump-Assisted-By-Immersion`

- Documentation: *Is heat pump assisted by immersion? Applicable only to hot water only heat pumps*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Heat-Pump-Installed-To-MIS"></a>Is-Heat-Pump-Installed-To-MIS

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Heat-Pump-Installed-To-MIS`

- Documentation: *Is heat pump installed to MIS standard? Only if water heating from hot water only heat pump.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Immersion-For-Summer-Use"></a>Is-Immersion-For-Summer-Use

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Immersion-For-Summer-Use`

- Documentation: *Immersion for summer use? Only if main heating is solid fuel fire or room heater with boiler.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Secondary-Heating-HETAS-Approved"></a>Is-Secondary-Heating-HETAS-Approved

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Secondary-Heating-HETAS-Approved`

- Documentation: *Secondary heating appliance is HETAS approved? Only if solid fuel.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Manufacturer"></a>Hot-Water-Store-Manufacturer

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Manufacturer`

- Documentation: *Store Manufacturer name.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Model"></a>Hot-Water-Store-Model

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Model`

- Documentation: *Store Model name.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Commissioning-Certificate"></a>Hot-Water-Store-Commissioning-Certificate

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Commissioning-Certificate`

- Documentation: *Store comissioning certificate number.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Installer-Engineer-Registration"></a>Hot-Water-Store-Installer-Engineer-Registration

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Installer-Engineer-Registration`

- Documentation: *Store installer engineer registration number.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Size"></a>Hot-Water-Store-Size

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Size`

- Documentation: *Hot water store size in litres; if there is a hot water store. Store refers to hot water store type which can be cylinder (if thermal store is "none"), hot-water only thermal store or integrated thermal store. Not applicable if (a) combi boiler whose data source database or (b) instantaneous combi boiler or (c) combi boiler from SAP table or (d) instantaneous water heater.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Heat-Transfer-Area"></a>Hot-Water-Store-Heat-Transfer-Area

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Heat-Transfer-Area`

- Documentation: *Used when a heat pump is associated with a separate and specified hot water vessel.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Heat-Loss-Source"></a>Hot-Water-Store-Heat-Loss-Source

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Heat-Loss-Source`

- Documentation: *The source of the hot water store heat loss information; if there is a hot water store. Not applicable if (a) combi boiler whose data source database or (b) instantaneous combi boiler or (c) combi boiler from SAP table or (d) instantaneous water heater.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Heat-Loss"></a>Hot-Water-Store-Heat-Loss

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Heat-Loss`

- Documentation: *Hot water store declared loss in kWh/day; only if there is a hot water store and if manufacturer declared loss. Not applicable if (a) combi boiler whose data source database or (b) instantaneous combi boiler or (c) combi boiler from SAP table or (d) instantaneous water heater.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Insulation-Type"></a>Hot-Water-Store-Insulation-Type

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Insulation-Type`

- Documentation: *Hot water store insulation; only if there is a hot water store and if loss from SAP table. Not applicable if (a) combi boiler whose data source database or (b) instantaneous combi boiler or (c) combi boiler from SAP table or (d) instantaneous water heater.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Insulation-Thickness"></a>Hot-Water-Store-Insulation-Thickness

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Insulation-Thickness`

- Documentation: *Hot water store insulation thickness in mm; only if there is a hot water store and if loss from SAP table. Not applicable if (a) combi boiler whose data source database or (b) instantaneous combi boiler or (c) combi boiler from SAP table or (d) instantaneous water heater.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Thermal-Store-Near-Boiler"></a>Is-Thermal-Store-Near-Boiler

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Thermal-Store-Near-Boiler`

- Documentation: *Thermal store connected to boiler by no more than 1.5 m of insulated pipework? Only if thermal store. Not applicable if combi boiler or instantaneous water heater.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Thermal-Store-Or-CPSU-In-Airing-Cupboard"></a>Is-Thermal-Store-Or-CPSU-In-Airing-Cupboard

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Thermal-Store-Or-CPSU-In-Airing-Cupboard`

- Documentation: *Thermal store or CPSU in airing cupboard? Only if (a) boiler with integrated or hot-water-only thermal store, or (b) main heating is CPSU.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Has-Cylinder-Thermostat"></a>Has-Cylinder-Thermostat

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Has-Cylinder-Thermostat`

- Documentation: *Hot water cylinder thermostat? Not applicable if combi boiler or instantaneous water heater.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Cylinder-In-Heated-Space"></a>Is-Cylinder-In-Heated-Space

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Cylinder-In-Heated-Space`

- Documentation: *Hot water cylinder in heated space? Not applicable if combi boiler or instantaneous water heater.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Hot-Water-Separately-Timed"></a>Is-Hot-Water-Separately-Timed

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Hot-Water-Separately-Timed`

- Documentation: *Hot water separately timed? Not applicable if combi boiler or instantaneous water heater.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Controls-Manufacturer"></a>Hot-Water-Controls-Manufacturer

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Controls-Manufacturer`

- Documentation: *None*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Controls-Model"></a>Hot-Water-Controls-Model

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Controls-Model`

- Documentation: *None*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems"></a>SAP-Community-Heating-Systems

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems`

- Documentation: *None*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System"></a>SAP-Community-Heating-System

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`

- Documentation: *None*
- Parent element: [`SAP-Community-Heating-Systems`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Name"></a>Community-Heating-Name

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Name`

- Documentation: *The name of the community heating system*
- Parent element: [`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-CO2-Emission-Factor"></a>Community-Heating-CO2-Emission-Factor

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-CO2-Emission-Factor`

- Documentation: *the community heating CO2 emission factor*
- Parent element: [`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Primary-Energy-Factor"></a>Community-Heating-Primary-Energy-Factor

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Primary-Energy-Factor`

- Documentation: *The community heating Primary Energy Factor*
- Parent element: [`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Use"></a>Community-Heating-Use

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Use`

- Documentation: *Specifies what kind of heating the community system is used for.*
- Parent element: [`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Is-Community-Heating-Cylinder-In-Dwelling"></a>Is-Community-Heating-Cylinder-In-Dwelling

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Is-Community-Heating-Cylinder-In-Dwelling`

- Documentation: *Community heating, cylinder in dwelling?*
- Parent element: [`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Is-HIU-In-Dwelling"></a>Is-HIU-In-Dwelling

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Is-HIU-In-Dwelling`

- Documentation: *Community heating, HIU in dwelling?*
- Parent element: [`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/HIU-Index-Number"></a>HIU-Index-Number

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/HIU-Index-Number`

- Documentation: *Heat Interface Unit index number, if present.*
- Parent element: [`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Distribution-Type"></a>Community-Heating-Distribution-Type

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Distribution-Type`

- Documentation: *Community heating distribution*
- Parent element: [`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources"></a>Community-Heat-Sources

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources`

- Documentation: *To be provided when there is no Heat-Network-Index-Number.*
- Parent element: [`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source"></a>Community-Heat-Source

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source`

- Documentation: *None*
- Parent element: [`Community-Heat-Sources`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Heat-Source-Type"></a>Heat-Source-Type

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Heat-Source-Type`

- Documentation: *None*
- Parent element: [`Community-Heat-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Heat-Fraction"></a>Heat-Fraction

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Heat-Fraction`

- Documentation: *Fraction of heat for the system provided by this heat source.*
- Parent element: [`Community-Heat-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Fuel-Type"></a>Fuel-Type

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Fuel-Type`

- Documentation: *None*
- Parent element: [`Community-Heat-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/PCDF-Fuel-Index"></a>PCDF-Fuel-Index

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/PCDF-Fuel-Index`

- Documentation: *None*
- Parent element: [`Community-Heat-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Heat-Efficiency"></a>Heat-Efficiency

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Heat-Efficiency`

- Documentation: *Heat efficiency in %.*
- Parent element: [`Community-Heat-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Power-Efficiency"></a>Power-Efficiency

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Power-Efficiency`

- Documentation: *Power efficiency in %. Include when heat source is CHP.*
- Parent element: [`Community-Heat-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Description"></a>Description

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Description`

- Documentation: *None*
- Parent element: [`Community-Heat-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/CHP-Electricity-Generation"></a>CHP-Electricity-Generation

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/CHP-Electricity-Generation`

- Documentation: *CHP Electricity generation options from table 12f.*
- Parent element: [`Community-Heat-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Distribution-Loss-Factor"></a>Community-Heating-Distribution-Loss-Factor

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Distribution-Loss-Factor`

- Documentation: *Used when Community-Heating-Distribution-Type is calculated.*
- Parent element: [`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Charging-Linked-To-Heat-Use"></a>Charging-Linked-To-Heat-Use

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Charging-Linked-To-Heat-Use`

- Documentation: *Used for hot-water-only systems.*
- Parent element: [`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Heat-Network-Index-Number"></a>Heat-Network-Index-Number

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Heat-Network-Index-Number`

- Documentation: *Index number of heat network, if applicable.*
- Parent element: [`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Sub-Network-Name"></a>Sub-Network-Name

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Sub-Network-Name`

- Documentation: *The name by which the sub community heat network is known.*
- Parent element: [`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Heat-Network-Existing"></a>Heat-Network-Existing

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Heat-Network-Existing`

- Documentation: *Whether the heat network is existing or new.*
- Parent element: [`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Heat-Network-Assessed-As-New"></a>Heat-Network-Assessed-As-New

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Heat-Network-Assessed-As-New`

- Documentation: *Whether the heat network is assessed as a new heat network (post June 2022) for Eng with a standalone gas boiler notional building.*
- Parent element: [`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details"></a>Main-Heating-Details

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`

- Documentation: *None*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating"></a>Main-Heating

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`

- Documentation: *None*
- Parent element: [`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Number"></a>Main-Heating-Number

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Number`

- Documentation: *Identifies the main heating as system 1 or system 2. System 1 must always be present, system 2 is included only when there are two systems.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Category"></a>Main-Heating-Category

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Category`

- Documentation: *Category of heating system for the main heating system.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Data-Source"></a>Main-Heating-Data-Source

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Data-Source`

- Documentation: *Source of main heating system data.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Index-Number"></a>Main-Heating-Index-Number

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Index-Number`

- Documentation: *The ID of the heating system from the product database, if system from database.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Manufacturer"></a>Main-Heating-Manufacturer

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Manufacturer`

- Documentation: *None*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Model"></a>Main-Heating-Model

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Model`

- Documentation: *None*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Commissioning-Certificate"></a>Main-Heating-Commissioning-Certificate

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Commissioning-Certificate`

- Documentation: *None*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Installation-Engineer"></a>Main-Heating-Installation-Engineer

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Installation-Engineer`

- Documentation: *Main heating installation engineer registration reference.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Condensing-Boiler"></a>Is-Condensing-Boiler

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Condensing-Boiler`

- Documentation: *Is the boiler a condensing boiler? If boiler efficiency is manufacturer declaration.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Condensing-Boiler-Heat-Distribution"></a>Condensing-Boiler-Heat-Distribution

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Condensing-Boiler-Heat-Distribution`

- Documentation: *The temperature distribution of the condensing boiler.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heat-Pump-Heat-Distribution"></a>Heat-Pump-Heat-Distribution

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heat-Pump-Heat-Distribution`

- Documentation: *The temperature distribution of the heat pump, for wet systems only.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Gas-Or-Oil-Boiler-Type"></a>Gas-Or-Oil-Boiler-Type

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Gas-Or-Oil-Boiler-Type`

- Documentation: *Boiler type; if boiler efficiency is manufacturer declaration and fuel is gas or oil.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Combi-Boiler-Type"></a>Combi-Boiler-Type

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Combi-Boiler-Type`

- Documentation: *Combi boiler type; if it is a combi boiler and boiler efficiency is manufacturer declaration.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Case-Heat-Emission"></a>Case-Heat-Emission

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Case-Heat-Emission`

- Documentation: *Case heat emission at full load in kW; if it is a range cooker boiler and boiler efficiency is manufacturer declaration.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heat-Transfer-To-Water"></a>Heat-Transfer-To-Water

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heat-Transfer-To-Water`

- Documentation: *Heat transfer to water at full load in kW; if it is a range cooker boiler and boiler efficiency is manufacturer declaration.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Solid-Fuel-Boiler-Type"></a>Solid-Fuel-Boiler-Type

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Solid-Fuel-Boiler-Type`

- Documentation: *Boiler type; if boiler efficiency is manufacturer declaration and fuel is solid.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Code"></a>Main-Heating-Code

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Code`

- Documentation: *Main heating code; when heating data source is SAP table.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Fuel-Type"></a>Main-Fuel-Type

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Fuel-Type`

- Documentation: *The type of fuel used to power the central heating e.g. Gas, Electricity; not used if main heating system is community heating scheme.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/PCDF-Fuel-Index"></a>PCDF-Fuel-Index

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/PCDF-Fuel-Index`

- Documentation: *PCDF index number of the fuel type, only if Main-Fuel-Type is 99 (fuel from database).*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Control"></a>Main-Heating-Control

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Control`

- Documentation: *Type of Main Control for the Heating System.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heat-Emitter-Type"></a>Heat-Emitter-Type

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heat-Emitter-Type`

- Documentation: *Identifies the means by which the central heating system (if present) emits heat; only when wet system (radiators or underfloor).*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Underfloor-Heat-Emitter-Type"></a>Underfloor-Heat-Emitter-Type

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Underfloor-Heat-Emitter-Type`

- Documentation: *Means by which an underfloor heating system (if present) emits heat; only when wet system (underfloor).*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Flue-Type"></a>Main-Heating-Flue-Type

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Flue-Type`

- Documentation: *The type of main heating flue; only if flued appliance.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Flue-Fan-Present"></a>Is-Flue-Fan-Present

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Flue-Fan-Present`

- Documentation: *Indicates whether the heating system contains a fan flue; only if boiler.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Central-Heating-Pump-In-Heated-Space"></a>Is-Central-Heating-Pump-In-Heated-Space

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Central-Heating-Pump-In-Heated-Space`

- Documentation: *Central heating pump in heated space? Only when wet system (radiators or underfloor).*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Oil-Pump-In-Heated-Space"></a>Is-Oil-Pump-In-Heated-Space

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Oil-Pump-In-Heated-Space`

- Documentation: *Oil pump in heated space? Only if oil boiler.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Interlocked-System"></a>Is-Interlocked-System

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Interlocked-System`

- Documentation: *Interlocked system? Only when wet system (radiators or underfloor).*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Has-Separate-Delayed-Start"></a>Has-Separate-Delayed-Start

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Has-Separate-Delayed-Start`

- Documentation: *True if there is a delayed start control separate from a controller in the database.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Boiler-Fuel-Feed"></a>Boiler-Fuel-Feed

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Boiler-Fuel-Feed`

- Documentation: *The type of boiler fuel feed; only if solid fuel boiler with manufacturer declaration.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Main-Heating-HETAS-Approved"></a>Is-Main-Heating-HETAS-Approved

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Main-Heating-HETAS-Approved`

- Documentation: *Main heating appliance is HETAS approved? Only if solid fuel.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Electric-CPSU-Operating-Temperature"></a>Electric-CPSU-Operating-Temperature

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Electric-CPSU-Operating-Temperature`

- Documentation: *Electric CPSU operating temperature in Celcius; only if main heating is electric CPSU.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Fraction"></a>Main-Heating-Fraction

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Fraction`

- Documentation: *Fraction of main heating provided by this system, is 1 if only one main system.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Burner-Control"></a>Burner-Control

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Burner-Control`

- Documentation: *None*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Efficiency-Type"></a>Efficiency-Type

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Efficiency-Type`

- Documentation: *None*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Efficiency-Winter"></a>Main-Heating-Efficiency-Winter

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Efficiency-Winter`

- Documentation: *To be used if main heating data is manufacturer declaration and Efficiency-Type is winter and summer.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Efficiency-Summer"></a>Main-Heating-Efficiency-Summer

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Efficiency-Summer`

- Documentation: *To be used if main heating data is manufacturer declaration and Efficiency-Type is winter and summer.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Efficiency"></a>Main-Heating-Efficiency

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Efficiency`

- Documentation: *If main heating is any system other than heat network.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-System-Type"></a>Main-Heating-System-Type

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-System-Type`

- Documentation: *Main heating system type or technology, for e.g., combi boiler, air source heat pump, etc.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Has-FGHRS"></a>Has-FGHRS

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Has-FGHRS`

- Documentation: *Flue Gas Heat Recovery System.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Index-Number"></a>FGHRS-Index-Number

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Index-Number`

- Documentation: *FGHRS index number; only if FGHRS.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source"></a>FGHRS-Energy-Source

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source`

- Documentation: *None*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays"></a>PV-Arrays

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays`

- Documentation: *None*
- Parent element: [`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array"></a>PV-Array

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array`

- Documentation: *None*
- Parent element: [`PV-Arrays`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Peak-Power"></a>Peak-Power

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Peak-Power`

- Documentation: *Peak kW of photovoltaics (PVs) (kWp); 0.0 if none.*
- Parent element: [`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Orientation"></a>Orientation

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Orientation`

- Documentation: *PV orientation; only if peak kWp > 0.*
- Parent element: [`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Pitch"></a>Pitch

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Pitch`

- Documentation: *PV pitch; only if peak kWp > 0.*
- Parent element: [`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Overshading"></a>Overshading

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Overshading`

- Documentation: *PV overshading; only if peak kWp > 0 and no MCS certificate.*
- Parent element: [`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/MCS-Certificate"></a>MCS-Certificate

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/MCS-Certificate`

- Documentation: *Does the installation have a MCS certificate.*
- Parent element: [`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/MCS-Certificate-Reference"></a>MCS-Certificate-Reference

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/MCS-Certificate-Reference`

- Documentation: *MCS certificate reference number*
- Parent element: [`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/PV-Panel-Manufacturer-Name"></a>PV-Panel-Manufacturer-Name

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/PV-Panel-Manufacturer-Name`

- Documentation: *Manufacturer of PV panels*
- Parent element: [`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Overshading-MCS"></a>Overshading-MCS

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Overshading-MCS`

- Documentation: *Overshading factor calculated according to MCS.*
- Parent element: [`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines"></a>Wind-Turbines

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines`

- Documentation: *None*
- Parent element: [`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine"></a>Wind-Turbine

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine`

- Documentation: *None*
- Parent element: [`Wind-Turbines`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Manufacturer-Name"></a>Wind-Turbine-Manufacturer-Name

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Manufacturer-Name`

- Documentation: *Wind turbine manufacturer name.*
- Parent element: [`Wind-Turbine`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Certificate"></a>Wind-Turbine-Certificate

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Certificate`

- Documentation: *Wind turbine certificate.*
- Parent element: [`Wind-Turbine`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Rotor-Diameter"></a>Wind-Turbine-Rotor-Diameter

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Rotor-Diameter`

- Documentation: *Wind turbine rotor diameter in metres; only if wind turbine.*
- Parent element: [`Wind-Turbine`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Hub-Height"></a>Wind-Turbine-Hub-Height

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Hub-Height`

- Documentation: *Wind turbine hub height above building in metres; only if wind turbine.*
- Parent element: [`Wind-Turbine`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Electricity-Tariff"></a>Electricity-Tariff

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Electricity-Tariff`

- Documentation: *Type of electricity tariff.*
- Parent element: [`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation"></a>Hydro-Electric-Generation

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation`

- Documentation: *Electricity generated by hydro-electric generator, in kWh/year. To be provided if Hydro-Electric-Generation-Month is not provided.*
- Parent element: [`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Certificate"></a>Hydro-Electric-Certificate

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Certificate`

- Documentation: *Reference to certification of hydro electric output.*
- Parent element: [`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months"></a>Hydro-Electric-Generation-Months

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months`

- Documentation: *Electricity generated by hydro-electric generator, in kWh/month. To be provided if Hydro-Electric-Generation is not provided.*
- Parent element: [`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month"></a>Hydro-Electric-Generation-Month

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month`

- Documentation: *None*
- Parent element: [`Hydro-Electric-Generation-Months`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month/Hydro-Month"></a>Hydro-Month

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month/Hydro-Month`

- Documentation: *None*
- Parent element: [`Hydro-Electric-Generation-Month`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month/Hydro-Value"></a>Hydro-Value

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month/Hydro-Value`

- Documentation: *Hydro electricity in kWh in month.*
- Parent element: [`Hydro-Electric-Generation-Month`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Is-Hydro-Output-Connected-To-Dwelling-Meter"></a>Is-Hydro-Output-Connected-To-Dwelling-Meter

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Is-Hydro-Output-Connected-To-Dwelling-Meter`

- Documentation: *Whether the hydro-electric station is connected to dwelling's electricity meter*
- Parent element: [`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values"></a>Main-Heating-Declared-Values

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values`

- Documentation: *None*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values/Efficiency"></a>Efficiency

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values/Efficiency`

- Documentation: *None*
- Parent element: [`Main-Heating-Declared-Values`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values/Make-Model"></a>Make-Model

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values/Make-Model`

- Documentation: *None*
- Parent element: [`Main-Heating-Declared-Values`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values/Test-Method"></a>Test-Method

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values/Test-Method`

- Documentation: *None*
- Parent element: [`Main-Heating-Declared-Values`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters"></a>Storage-Heaters

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters`

- Documentation: *None*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater"></a>Storage-Heater

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater`

- Documentation: *None*
- Parent element: [`Storage-Heaters`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater/Number-Of-Heaters"></a>Number-Of-Heaters

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater/Number-Of-Heaters`

- Documentation: *The number of storage heaters with this index number.*
- Parent element: [`Storage-Heater`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater/Index-Number"></a>Index-Number

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater/Index-Number`

- Documentation: *The index number of the heater from the product database.*
- Parent element: [`Storage-Heater`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater/High-Heat-Retention"></a>High-Heat-Retention

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater/High-Heat-Retention`

- Documentation: *Whether heater is high heat retention type.*
- Parent element: [`Storage-Heater`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Emitter-Temperature"></a>Emitter-Temperature

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Emitter-Temperature`

- Documentation: *Gas and oil boilers and heat pump from database: 0, 1, 3 or 4 Other heat pump 0, 2 or 4. Other systems NA.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/MCS-Installed-Heat-Pump"></a>MCS-Installed-Heat-Pump

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/MCS-Installed-Heat-Pump`

- Documentation: *Whether heat pump was installed under the Microgeneration Certification Scheme.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Central-Heating-Pump-Age"></a>Central-Heating-Pump-Age

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Central-Heating-Pump-Age`

- Documentation: *Included for systems with a central heating pump, i.e. wet system.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Control-Index-Number"></a>Control-Index-Number

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Control-Index-Number`

- Documentation: *The ID of the controller from the product database.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heating-Controller-Function"></a>Heating-Controller-Function

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heating-Controller-Function`

- Documentation: *None*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heating-Controller-Ecodesign-Class"></a>Heating-Controller-Ecodesign-Class

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heating-Controller-Ecodesign-Class`

- Documentation: *None*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heating-Controller-Manufacturer"></a>Heating-Controller-Manufacturer

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heating-Controller-Manufacturer`

- Documentation: *None*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heating-Controller-Model"></a>Heating-Controller-Model

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heating-Controller-Model`

- Documentation: *None*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Heating-Design-Water-Use"></a>SAP-Heating-Design-Water-Use

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Heating-Design-Water-Use`

- Documentation: *None*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Systems-Interaction"></a>Main-Heating-Systems-Interaction

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Systems-Interaction`

- Documentation: *None*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values"></a>Secondary-Heating-Declared-Values

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values`

- Documentation: *Use when manufacturer's declared values.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values/Efficiency"></a>Efficiency

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values/Efficiency`

- Documentation: *None*
- Parent element: [`Secondary-Heating-Declared-Values`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values/Make-Model"></a>Make-Model

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values/Make-Model`

- Documentation: *None*
- Parent element: [`Secondary-Heating-Declared-Values`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values/Test-Method"></a>Test-Method

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values/Test-Method`

- Documentation: *None*
- Parent element: [`Secondary-Heating-Declared-Values`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Primary-Pipework-Insulation"></a>Primary-Pipework-Insulation

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Primary-Pipework-Insulation`

- Documentation: *Not applicable to combi boiler or instantaneous water heater.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details"></a>Solar-Heating-Details

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`

- Documentation: *None*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Heating-Collector-Manufacturer"></a>Solar-Heating-Collector-Manufacturer

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Heating-Collector-Manufacturer`

- Documentation: *Panel manufacturer*
- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Heating-Certificate"></a>Solar-Heating-Certificate

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Heating-Certificate`

- Documentation: *Solar heating certificate*
- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Aperture-Area"></a>Solar-Panel-Aperture-Area

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Aperture-Area`

- Documentation: *Panel aperture area in square metres.*
- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Type"></a>Solar-Panel-Collector-Type

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Type`

- Documentation: *Type of solar panel collector.*
- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Data-Source"></a>Solar-Panel-Collector-Data-Source

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Data-Source`

- Documentation: *Source of solar panel collector data.*
- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Zero-Loss-Efficiency"></a>Solar-Panel-Collector-Zero-Loss-Efficiency

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Zero-Loss-Efficiency`

- Documentation: *Collector zero-loss efficiency; only if declared values.*
- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Heat-Loss-Rate"></a>Solar-Panel-Collector-Heat-Loss-Rate

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Heat-Loss-Rate`

- Documentation: *Collector heat loss rate; for backward compatibility only, do not use.*
- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Linear-Heat-Loss-Coefficient"></a>Solar-Panel-Collector-Linear-Heat-Loss-Coefficient

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Linear-Heat-Loss-Coefficient`

- Documentation: *Collector linear heat loss coefficient; only if declared values.*
- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Second-Order-Heat-Loss-Coefficient"></a>Solar-Panel-Collector-Second-Order-Heat-Loss-Coefficient

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Second-Order-Heat-Loss-Coefficient`

- Documentation: *Collector 2nd order heat loss coefficient; only if declared values.*
- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Orientation"></a>Solar-Panel-Collector-Orientation

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Orientation`

- Documentation: *Collector orientation.*
- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Pitch"></a>Solar-Panel-Collector-Pitch

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Pitch`

- Documentation: *None*
- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Overshading"></a>Solar-Panel-Collector-Overshading

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Overshading`

- Documentation: *None*
- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Has-Solar-Powered-Pump"></a>Has-Solar-Powered-Pump

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Has-Solar-Powered-Pump`

- Documentation: *None*
- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Is-Solar-Store-Combined-Cylinder"></a>Is-Solar-Store-Combined-Cylinder

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Is-Solar-Store-Combined-Cylinder`

- Documentation: *None*
- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Store-Volume"></a>Solar-Store-Volume

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Store-Volume`

- Documentation: *Dedicated solar store volume in litres.*
- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Collector-Loop-Efficiency"></a>Collector-Loop-Efficiency

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Collector-Loop-Efficiency`

- Documentation: *Collector loop efficiency; only if declared values.*
- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Incidence-Angle-Modifier"></a>Incidence-Angle-Modifier

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Incidence-Angle-Modifier`

- Documentation: *Incidence angle modifier; only if declared values.*
- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Is-Community-Solar"></a>Is-Community-Solar

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Is-Community-Solar`

- Documentation: *None*
- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Service-Provision"></a>Service-Provision

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Service-Provision`

- Documentation: *None*
- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Overall-Heat-Loss"></a>Overall-Heat-Loss

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Overall-Heat-Loss`

- Documentation: *Overall heat loss coefficient of system; only if declared values.*
- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS"></a>Instantaneous-WWHRS

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS`

- Documentation: *Waste Water Heat Recovery System.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Index-Number1"></a>WWHRS-Index-Number1

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Index-Number1`

- Documentation: *None*
- Parent element: [`Instantaneous-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Index-Number2"></a>WWHRS-Index-Number2

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Index-Number2`

- Documentation: *Omit if no second system.*
- Parent element: [`Instantaneous-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Efficiency1"></a>WWHRS-Efficiency1

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Efficiency1`

- Documentation: *None*
- Parent element: [`Instantaneous-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Manufacturer1"></a>WWHRS-Manufacturer1

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Manufacturer1`

- Documentation: *None*
- Parent element: [`Instantaneous-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Model1"></a>WWHRS-Model1

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Model1`

- Documentation: *None*
- Parent element: [`Instantaneous-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Efficiency2"></a>WWHRS-Efficiency2

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Efficiency2`

- Documentation: *None*
- Parent element: [`Instantaneous-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Manufacturer2"></a>WWHRS-Manufacturer2

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Manufacturer2`

- Documentation: *None*
- Parent element: [`Instantaneous-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Model2"></a>WWHRS-Model2

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Model2`

- Documentation: *None*
- Parent element: [`Instantaneous-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS"></a>Storage-WWHRS

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS`

- Documentation: *None*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/WWHRS-Index-Number"></a>WWHRS-Index-Number

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/WWHRS-Index-Number`

- Documentation: *None*
- Parent element: [`Storage-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/WWHRS-Store-Volume"></a>WWHRS-Store-Volume

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/WWHRS-Store-Volume`

- Documentation: *Dedicated store volume in litres.*
- Parent element: [`Storage-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/Storage-WWHRS-Efficiency"></a>Storage-WWHRS-Efficiency

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/Storage-WWHRS-Efficiency`

- Documentation: *None*
- Parent element: [`Storage-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/Storage-WWHRS-Manufacturer"></a>Storage-WWHRS-Manufacturer

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/Storage-WWHRS-Manufacturer`

- Documentation: *None*
- Parent element: [`Storage-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/Storage-WWHRS-Model"></a>Storage-WWHRS-Model

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/Storage-WWHRS-Model`

- Documentation: *None*
- Parent element: [`Storage-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets"></a>Shower-Outlets

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets`

- Documentation: *None*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet"></a>Shower-Outlet

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet`

- Documentation: *None*
- Parent element: [`Shower-Outlets`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-Outlet-Type"></a>Shower-Outlet-Type

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-Outlet-Type`

- Documentation: *Hot water type for this shower outlet.*
- Parent element: [`Shower-Outlet`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-Flow-Rate"></a>Shower-Flow-Rate

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-Flow-Rate`

- Documentation: *The flow rate. Only when a shower is not instantaneous electric. Leave blank if NO flow limiter fitted.*
- Parent element: [`Shower-Outlet`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-Power"></a>Shower-Power

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-Power`

- Documentation: *The shower power, only if shower outlet type is instantaneous electric.*
- Parent element: [`Shower-Outlet`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-WWHRS"></a>Shower-WWHRS

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-WWHRS`

- Documentation: *The WWHRS with which the shower is connected. If shower outlet type is instantaneous electric shower then only a storage WWHRS can be selected or none.*
- Parent element: [`Shower-Outlet`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Number-Baths"></a>Number-Baths

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Number-Baths`

- Documentation: *None*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Number-Baths-WWHRS"></a>Number-Baths-WWHRS

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Number-Baths-WWHRS`

- Documentation: *None*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source"></a>SAP-Energy-Source

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source`

- Documentation: *None*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays"></a>PV-Arrays

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays`

- Documentation: *None*
- Parent element: [`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array"></a>PV-Array

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array`

- Documentation: *None*
- Parent element: [`PV-Arrays`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Peak-Power"></a>Peak-Power

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Peak-Power`

- Documentation: *Peak kW of photovoltaics (PVs) (kWp); 0.0 if none.*
- Parent element: [`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Orientation"></a>Orientation

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Orientation`

- Documentation: *PV orientation; only if peak kWp > 0.*
- Parent element: [`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Pitch"></a>Pitch

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Pitch`

- Documentation: *PV pitch; only if peak kWp > 0.*
- Parent element: [`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Overshading"></a>Overshading

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Overshading`

- Documentation: *PV overshading; only if peak kWp > 0 and no MCS certificate.*
- Parent element: [`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/MCS-Certificate"></a>MCS-Certificate

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/MCS-Certificate`

- Documentation: *Does the installation have a MCS certificate.*
- Parent element: [`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/MCS-Certificate-Reference"></a>MCS-Certificate-Reference

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/MCS-Certificate-Reference`

- Documentation: *MCS certificate reference number*
- Parent element: [`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/PV-Panel-Manufacturer-Name"></a>PV-Panel-Manufacturer-Name

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/PV-Panel-Manufacturer-Name`

- Documentation: *Manufacturer of PV panels*
- Parent element: [`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Overshading-MCS"></a>Overshading-MCS

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Overshading-MCS`

- Documentation: *Overshading factor calculated according to MCS.*
- Parent element: [`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines"></a>Wind-Turbines

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines`

- Documentation: *None*
- Parent element: [`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine"></a>Wind-Turbine

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine`

- Documentation: *None*
- Parent element: [`Wind-Turbines`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Manufacturer-Name"></a>Wind-Turbine-Manufacturer-Name

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Manufacturer-Name`

- Documentation: *Wind turbine manufacturer name.*
- Parent element: [`Wind-Turbine`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Certificate"></a>Wind-Turbine-Certificate

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Certificate`

- Documentation: *Wind turbine certificate.*
- Parent element: [`Wind-Turbine`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Rotor-Diameter"></a>Wind-Turbine-Rotor-Diameter

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Rotor-Diameter`

- Documentation: *Wind turbine rotor diameter in metres; only if wind turbine.*
- Parent element: [`Wind-Turbine`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Hub-Height"></a>Wind-Turbine-Hub-Height

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Hub-Height`

- Documentation: *Wind turbine hub height above building in metres; only if wind turbine.*
- Parent element: [`Wind-Turbine`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Electricity-Tariff"></a>Electricity-Tariff

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Electricity-Tariff`

- Documentation: *Type of electricity tariff.*
- Parent element: [`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation"></a>Hydro-Electric-Generation

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation`

- Documentation: *Electricity generated by hydro-electric generator, in kWh/year. To be provided if Hydro-Electric-Generation-Month is not provided.*
- Parent element: [`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Certificate"></a>Hydro-Electric-Certificate

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Certificate`

- Documentation: *Reference to certification of hydro electric output.*
- Parent element: [`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months"></a>Hydro-Electric-Generation-Months

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months`

- Documentation: *Electricity generated by hydro-electric generator, in kWh/month. To be provided if Hydro-Electric-Generation is not provided.*
- Parent element: [`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month"></a>Hydro-Electric-Generation-Month

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month`

- Documentation: *None*
- Parent element: [`Hydro-Electric-Generation-Months`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month/Hydro-Month"></a>Hydro-Month

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month/Hydro-Month`

- Documentation: *None*
- Parent element: [`Hydro-Electric-Generation-Month`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month/Hydro-Value"></a>Hydro-Value

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month/Hydro-Value`

- Documentation: *Hydro electricity in kWh in month.*
- Parent element: [`Hydro-Electric-Generation-Month`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Is-Hydro-Output-Connected-To-Dwelling-Meter"></a>Is-Hydro-Output-Connected-To-Dwelling-Meter

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Is-Hydro-Output-Connected-To-Dwelling-Meter`

- Documentation: *Whether the hydro-electric station is connected to dwelling's electricity meter*
- Parent element: [`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts"></a>SAP-Building-Parts

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`

- Documentation: *None*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part"></a>SAP-Building-Part

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`

- Documentation: *None*
- Parent element: [`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Building-Part-Number"></a>Building-Part-Number

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Building-Part-Number`

- Documentation: *An integer value which uniquely identifies the building part in the property. The value "1" must be assigned to the main dwelling.*
- Parent element: [`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Identifier"></a>Identifier

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Identifier`

- Documentation: *Identifier for the Building part - generally only required if there are more that one Building Parts of the same type e.g. "West Wing" and "East Wing" Extensions*
- Parent element: [`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Construction-Year"></a>Construction-Year

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Construction-Year`

- Documentation: *The year when this building part was constructed. Not used if 'Construction-Age-Band' is used.*
- Parent element: [`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Construction-Age-Band"></a>Construction-Age-Band

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Construction-Age-Band`

- Documentation: *The age band when this building part was constructed. Not used if 'Construction-Year' is used.*
- Parent element: [`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings"></a>SAP-Openings

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings`

- Documentation: *None*
- Parent element: [`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening"></a>SAP-Opening

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening`

- Documentation: *None*
- Parent element: [`SAP-Openings`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Name"></a>Name

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Name`

- Documentation: *Unique name which identifies this opening. Can be just a number, e.g. "1". However, an opening cannot have the same name as a wall.*
- Parent element: [`SAP-Opening`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Type"></a>Type

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Type`

- Documentation: *The name of the SAP-Opening-Type for this opening.*
- Parent element: [`SAP-Opening`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Location"></a>Location

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Location`

- Documentation: *Name of the wall or roof which contains the opening.*
- Parent element: [`SAP-Opening`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Orientation"></a>Orientation

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Orientation`

- Documentation: *Compass direction in which the opening faces.*
- Parent element: [`SAP-Opening`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Width"></a>Width

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Width`

- Documentation: *The width of the opening in metres. If the Width field is used to record the opening area, set the Height to 1.*
- Parent element: [`SAP-Opening`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Height"></a>Height

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Height`

- Documentation: *The height of the opening in metres. If the Height field is used to record the opening area, set the Width to 1.*
- Parent element: [`SAP-Opening`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Pitch"></a>Pitch

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Pitch`

- Documentation: *Pitch of roof containing roof window.*
- Parent element: [`SAP-Opening`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs"></a>SAP-Roofs

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs`

- Documentation: *None*
- Parent element: [`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof"></a>SAP-Roof

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof`

- Documentation: *None*
- Parent element: [`SAP-Roofs`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Name"></a>Name

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Name`

- Documentation: *Unique name which identifies this roof. Can be just a number, e.g. "1". However, a roof cannot have the same name as a wall.*
- Parent element: [`SAP-Roof`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Description"></a>Description

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Description`

- Documentation: *Descriptive notes about the roof.*
- Parent element: [`SAP-Roof`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Roof-Type"></a>Roof-Type

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Roof-Type`

- Documentation: *None*
- Parent element: [`SAP-Roof`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Total-Roof-Area"></a>Total-Roof-Area

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Total-Roof-Area`

- Documentation: *Total roof area in square metres, inclusive of any openings.*
- Parent element: [`SAP-Roof`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/U-Value"></a>U-Value

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/U-Value`

- Documentation: *Exposed roof U-value.*
- Parent element: [`SAP-Roof`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Kappa-Value"></a>Kappa-Value

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Kappa-Value`

- Documentation: *Heat capacity per unit area in kJ/m2K.*
- Parent element: [`SAP-Roof`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions"></a>SAP-Floor-Dimensions

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions`

- Documentation: *None*
- Parent element: [`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension"></a>SAP-Floor-Dimension

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`

- Documentation: *None*
- Parent element: [`SAP-Floor-Dimensions`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Name"></a>Name

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Name`

- Documentation: *A name describing the floor dimensioned.*
- Parent element: [`SAP-Floor-Dimension`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Storey"></a>Storey

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Storey`

- Documentation: *Building storey on which the floor is located.*
- Parent element: [`SAP-Floor-Dimension`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Description"></a>Description

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Description`

- Documentation: *Descriptive notes about the floor.*
- Parent element: [`SAP-Floor-Dimension`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Floor-Type"></a>Floor-Type

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Floor-Type`

- Documentation: *Type of floor (exposure).*
- Parent element: [`SAP-Floor-Dimension`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Total-Floor-Area"></a>Total-Floor-Area

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Total-Floor-Area`

- Documentation: *The total floor area of the storey in square metres.*
- Parent element: [`SAP-Floor-Dimension`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Storey-Height"></a>Storey-Height

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Storey-Height`

- Documentation: *Average height of the storey in metres.*
- Parent element: [`SAP-Floor-Dimension`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Heat-Loss-Area"></a>Heat-Loss-Area

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Heat-Loss-Area`

- Documentation: *The estimated total heat loss area for the floor in square metres.*
- Parent element: [`SAP-Floor-Dimension`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/U-Value"></a>U-Value

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/U-Value`

- Documentation: *Heat loss floor U-value.*
- Parent element: [`SAP-Floor-Dimension`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Kappa-Value"></a>Kappa-Value

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Kappa-Value`

- Documentation: *Heat capacity of floor per unit area in kJ/m2K.*
- Parent element: [`SAP-Floor-Dimension`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Kappa-Value-From-Below"></a>Kappa-Value-From-Below

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Kappa-Value-From-Below`

- Documentation: *Heat capacity of ceiling below. Applies to the non-heat-loss area of an upper floor.*
- Parent element: [`SAP-Floor-Dimension`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges"></a>SAP-Thermal-Bridges

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges`

- Documentation: *None*
- Parent element: [`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/Thermal-Bridge-Code"></a>Thermal-Bridge-Code

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/Thermal-Bridge-Code`

- Documentation: *Code which indicates how the thermal bridge data has been recorded.*
- Parent element: [`SAP-Thermal-Bridges`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/User-Defined-Y-Value"></a>User-Defined-Y-Value

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/User-Defined-Y-Value`

- Documentation: *Global y-value for all thermal bridges in watts per square metre per kelvin; only if thermal bridge code is: user defined (global y-value)*
- Parent element: [`SAP-Thermal-Bridges`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/Calculation-Reference"></a>Calculation-Reference

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/Calculation-Reference`

- Documentation: *Reference to the details of the calculation of the global y-value; only if thermal bridging is user defined global y-value.*
- Parent element: [`SAP-Thermal-Bridges`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge"></a>SAP-Thermal-Bridge

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge`

- Documentation: *None*
- Parent element: [`SAP-Thermal-Bridges`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Thermal-Bridge-Type"></a>Thermal-Bridge-Type

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Thermal-Bridge-Type`

- Documentation: *Code to indicate a particular type of thermal bridge; only if thermal bridge code is: user defined (individual values).*
- Parent element: [`SAP-Thermal-Bridge`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Length"></a>Length

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Length`

- Documentation: *Length of the thermal bridge in metres; only if thermal bridge code is: user defined (individual values).*
- Parent element: [`SAP-Thermal-Bridge`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Psi-Value"></a>Psi-Value

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Psi-Value`

- Documentation: *Linear thermal transmittance (psi-value); only if thermal bridging is user defined individual values.*
- Parent element: [`SAP-Thermal-Bridge`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Psi-Value-Source"></a>Psi-Value-Source

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Psi-Value-Source`

- Documentation: *None*
- Parent element: [`SAP-Thermal-Bridge`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Psi-Value-Calculation-Reference"></a>Psi-Value-Calculation-Reference

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Psi-Value-Calculation-Reference`

- Documentation: *Reference to the details of the calculation of the psi-value.*
- Parent element: [`SAP-Thermal-Bridge`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls"></a>SAP-Walls

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls`

- Documentation: *None*
- Parent element: [`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall"></a>SAP-Wall

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall`

- Documentation: *None*
- Parent element: [`SAP-Walls`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Name"></a>Name

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Name`

- Documentation: *Unique name which identifies this wall within its storey. Can be just a number, e.g. "1". However, a wall cannot have the same name as an opening or a roof.*
- Parent element: [`SAP-Wall`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Description"></a>Description

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Description`

- Documentation: *Descriptive notes about the wall.*
- Parent element: [`SAP-Wall`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Wall-Type"></a>Wall-Type

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Wall-Type`

- Documentation: *Type of wall (exposure).*
- Parent element: [`SAP-Wall`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Total-Wall-Area"></a>Total-Wall-Area

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Total-Wall-Area`

- Documentation: *Total wall area in square metres, inclusive of any openings.*
- Parent element: [`SAP-Wall`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/U-Value"></a>U-Value

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/U-Value`

- Documentation: *Exposed wall U-value.*
- Parent element: [`SAP-Wall`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Is-Curtain-Walling"></a>Is-Curtain-Walling

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Is-Curtain-Walling`

- Documentation: *Whether the wall is curtain walling, i.e. a facade construction consisting of a frame of aluminium vertical and horizontal members, infilled with glazing units and opaque panels.*
- Parent element: [`SAP-Wall`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Kappa-Value"></a>Kappa-Value

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Kappa-Value`

- Documentation: *Heat capacity per unit area in kJ/m2K.*
- Parent element: [`SAP-Wall`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types"></a>SAP-Opening-Types

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types`

- Documentation: *None*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type"></a>SAP-Opening-Type

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type`

- Documentation: *None*
- Parent element: [`SAP-Opening-Types`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Name"></a>Name

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Name`

- Documentation: *Unique name which identifies this opening type. Can be just a number, e.g. "1".*
- Parent element: [`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Description"></a>Description

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Description`

- Documentation: *Descriptive notes about the opening type.*
- Parent element: [`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Data-Source"></a>Data-Source

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Data-Source`

- Documentation: *The source of the data for this type of opening.*
- Parent element: [`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Type"></a>Type

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Type`

- Documentation: *The (physical) type of opening that this opening type represents.*
- Parent element: [`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Glazing-Type"></a>Glazing-Type

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Glazing-Type`

- Documentation: *The type of glazing; if U-value is from BFRC or manufacturer declaration, give as one of - single - double - triple.*
- Parent element: [`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Glazing-Gap"></a>Glazing-Gap

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Glazing-Gap`

- Documentation: *Gap between glass panes; only if SAP table and double, triple glazed or secondary glazing.*
- Parent element: [`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/IsArgonFilled"></a>IsArgonFilled

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/IsArgonFilled`

- Documentation: *Is the opening argon-filled? Only if SAP table.*
- Parent element: [`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/IsKryptonFilled"></a>IsKryptonFilled

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/IsKryptonFilled`

- Documentation: *Is the opening krypton-filled? Only if SAP table.*
- Parent element: [`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Frame-Type"></a>Frame-Type

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Frame-Type`

- Documentation: *The type of frame, only if data source is SAP table and it is a window, roof window or half-glazed door.*
- Parent element: [`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Solar-Transmittance"></a>Solar-Transmittance

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Solar-Transmittance`

- Documentation: *The solar transmittance; not if a door.*
- Parent element: [`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Frame-Factor"></a>Frame-Factor

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Frame-Factor`

- Documentation: *The frame factor; not if a door.*
- Parent element: [`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/U-Value"></a>U-Value

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/U-Value`

- Documentation: *The U-value. For rooflights, the U-value should be in the horizontal plane.*
- Parent element: [`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation"></a>SAP-Ventilation

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`

- Documentation: *None*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Closed-Flues-Count"></a>Closed-Flues-Count

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Closed-Flues-Count`

- Documentation: *The number of Closed Flues or chimneys in the Property.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Open-Flues-Count"></a>Open-Flues-Count

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Open-Flues-Count`

- Documentation: *The number of Open Flues in the Property.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Boilers-Flues-Count"></a>Boilers-Flues-Count

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Boilers-Flues-Count`

- Documentation: *The number of Boiler Flues or chimneys in the Property.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Other-Flues-Count"></a>Other-Flues-Count

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Other-Flues-Count`

- Documentation: *The number of Other Flues or chimneys in the Property.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Open-Chimneys-Count"></a>Open-Chimneys-Count

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Open-Chimneys-Count`

- Documentation: *The number of Open Chimneys in the Property.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Blocked-Chimneys-Count"></a>Blocked-Chimneys-Count

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Blocked-Chimneys-Count`

- Documentation: *The number of Blocked Chimneys in the Property.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Fans-Vents-Count"></a>Fans-Vents-Count

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Fans-Vents-Count`

- Documentation: *For backward compatibility only, do not use.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Flueless-Gas-Fires-Count"></a>Flueless-Gas-Fires-Count

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Flueless-Gas-Fires-Count`

- Documentation: *The number of flueless gas fires in the Property.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Pressure-Test"></a>Pressure-Test

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Pressure-Test`

- Documentation: *Whether there has been a pressure test, or whether an assumed value is used for the air permeability.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Pressure-Test-Certificate-Number"></a>Pressure-Test-Certificate-Number

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Pressure-Test-Certificate-Number`

- Documentation: *The pressure test certificate number or test engineer reference.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Air-Permeability"></a>Air-Permeability

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Air-Permeability`

- Documentation: *Air permeability; only if pressure test (yes or assumed).*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Ground-Floor-Type"></a>Ground-Floor-Type

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Ground-Floor-Type`

- Documentation: *The type of ground floor; nly if no pressure test.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Wall-Type"></a>Wall-Type

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Wall-Type`

- Documentation: *The construction of the walls; only if no pressure test.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Has-Draught-Lobby"></a>Has-Draught-Lobby

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Has-Draught-Lobby`

- Documentation: *Is there a draft lobby? Only if no pressure test.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/DraughtStripping"></a>DraughtStripping

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/DraughtStripping`

- Documentation: *Draughtstripping percentage; only if no pressure test.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Sheltered-Sides-Count"></a>Sheltered-Sides-Count

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Sheltered-Sides-Count`

- Documentation: *The number of sheltered sides in the Property.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Ventilation-Type"></a>Ventilation-Type

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Ventilation-Type`

- Documentation: *The type of ventilation.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Ventilation-Data-Source"></a>Mechanical-Ventilation-Data-Source

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Ventilation-Data-Source`

- Documentation: *Source of mechanical ventilation data; only if mechanical ventilation.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-System-Index-Number"></a>Mechanical-Vent-System-Index-Number

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-System-Index-Number`

- Documentation: *Mechanical vent system index number; if mechanical vent data from database (MEV c, MEV dc, MV, MVHR).*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Commissioning-Certificate-Number"></a>Mechanical-Vent-Commissioning-Certificate-Number

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Commissioning-Certificate-Number`

- Documentation: *Mechanical ventilation Commissioning certificate number .*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Installation-Engineer"></a>Mechanical-Vent-Installation-Engineer

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Installation-Engineer`

- Documentation: *Mechanical ventilation installation engineer registration reference.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-System-Make-Model"></a>Mechanical-Vent-System-Make-Model

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-System-Make-Model`

- Documentation: *Mechanical ventilation system make and model.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Wet-Rooms-Count"></a>Wet-Rooms-Count

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Wet-Rooms-Count`

- Documentation: *Number of wet rooms, including the kitchen; if mech vent data from manufacturer declaration or database (MEV c, MV, MVHR).*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Specific-Fan-Power"></a>Mechanical-Vent-Specific-Fan-Power

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Specific-Fan-Power`

- Documentation: *Mechanical vent specific fan power in watts per (litres per second); if mechanical vent data (PIV from outside, MEV c or dc, MV, MVHR).*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Heat-Recovery-Efficiency"></a>Mechanical-Vent-Heat-Recovery-Efficiency

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Heat-Recovery-Efficiency`

- Documentation: *Mechanical vent heat recovery efficiency percentage; if mechanical vent (MVHR).*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Duct-Type"></a>Mechanical-Vent-Duct-Type

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Duct-Type`

- Documentation: *Mechanical vent duct type; if MEV c, MV or MVHR.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Duct-Insulation"></a>Mechanical-Vent-Duct-Insulation

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Duct-Insulation`

- Documentation: *Mechanical vent duct insulation; if MVHR.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Duct-Insulation-Level"></a>Mechanical-Vent-Duct-Insulation-Level

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Duct-Insulation-Level`

- Documentation: *Mechanical vent duct insulation; if MVHR.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Duct-Placement"></a>Mechanical-Vent-Duct-Placement

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Duct-Placement`

- Documentation: *Mechanical ventilation duct insulation; if MVHR.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Measured-Installation"></a>Mechanical-Vent-Measured-Installation

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Measured-Installation`

- Documentation: *Mechanical ventilation SPF measured in situ; if MVHR or balanced.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Room-Fans-Count"></a>Kitchen-Room-Fans-Count

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Room-Fans-Count`

- Documentation: *MEV dc, number of fans in room, kitchen; if mechanical vent data from database or manufacturer declaration (MEV dc).*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Room-Fans-Specific-Power"></a>Kitchen-Room-Fans-Specific-Power

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Room-Fans-Specific-Power`

- Documentation: *MEV dc, specific fan power of fans in room, kitchen, in watts per (litres per second); if mechanical vent data from manufacturer declaration (MEV dc).*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Room-Fans-Count"></a>Non-Kitchen-Room-Fans-Count

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Room-Fans-Count`

- Documentation: *MEV dc, number of fans in room, rooms other than kitchen; if mechanical vent data from database or manufacturer declaration (MEV dc).*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Room-Fans-Specific-Power"></a>Non-Kitchen-Room-Fans-Specific-Power

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Room-Fans-Specific-Power`

- Documentation: *MEV dc, specific fan power of fans in room, rooms other than kitchen, in watts per (litres per second); if mechanical vent data from manufacturer declaration (MEV dc).*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Duct-Fans-Count"></a>Kitchen-Duct-Fans-Count

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Duct-Fans-Count`

- Documentation: *MEV dc, number of fans via duct, kitchen; if mechanical vent data from database or manufacturer declaration (MEV dc).*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Duct-Fans-Specific-Power"></a>Kitchen-Duct-Fans-Specific-Power

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Duct-Fans-Specific-Power`

- Documentation: *MEV dc, specific fan power of fans via duct, kitchen, in watts per (litres per second); if mechanical vent data from manufacturer declaration (MEV dc).*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Duct-Fans-Count"></a>Non-Kitchen-Duct-Fans-Count

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Duct-Fans-Count`

- Documentation: *MEV dc, number of fans via duct, rooms other than kitchen; if mechanical vent data from database or manufacturer declaration (MEV dc).*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Duct-Fans-Specific-Power"></a>Non-Kitchen-Duct-Fans-Specific-Power

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Duct-Fans-Specific-Power`

- Documentation: *MEV dc, specific fan power of fans via duct, rooms other than kitchen, in watts per (litres per second); if mechanical vent data from manufacturer declaration (MEV dc).*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Wall-Fans-Count"></a>Kitchen-Wall-Fans-Count

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Wall-Fans-Count`

- Documentation: *MEV dc, number of fans through wall, kitchen; if mechanical vent data from database or manufacturer declaration (MEV dc).*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Wall-Fans-Specific-Power"></a>Kitchen-Wall-Fans-Specific-Power

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Wall-Fans-Specific-Power`

- Documentation: *MEV dc, specific fan power of fans through wall, kitchen, in watts per (litres per second); if mechanical vent data from manufacturer declaration (MEV dc).*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Wall-Fans-Count"></a>Non-Kitchen-Wall-Fans-Count

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Wall-Fans-Count`

- Documentation: *MEV dc, number of fans through wall, rooms other than kitchen; if mechanical vent data from database or manufacturer declaration (MEV dc).*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Wall-Fans-Specific-Power"></a>Non-Kitchen-Wall-Fans-Specific-Power

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Wall-Fans-Specific-Power`

- Documentation: *MEV dc, specific fan power of fans through wall, rooms other than kitchen, in watts per (litres per second); if mechanical vent data from manufacturer declaration (MEV dc).*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Extract-Fans-Count"></a>Extract-Fans-Count

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Extract-Fans-Count`

- Documentation: *None*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/PSV-Count"></a>PSV-Count

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/PSV-Count`

- Documentation: *None*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Is-Mechanical-Vent-Approved-Installer-Scheme"></a>Is-Mechanical-Vent-Approved-Installer-Scheme

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Is-Mechanical-Vent-Approved-Installer-Scheme`

- Documentation: *None*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Ducts-Index-Number"></a>Mechanical-Vent-Ducts-Index-Number

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Ducts-Index-Number`

- Documentation: *Mechanical vent ducts index number; if applicable.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting"></a>SAP-Lighting

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting`

- Documentation: *None*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights"></a>Fixed-Lights

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights`

- Documentation: *The record of a lighting type within the building.*
- Parent element: [`SAP-Lighting`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light"></a>Fixed-Light

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light`

- Documentation: *None*
- Parent element: [`Fixed-Lights`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light/Lighting-Efficacy"></a>Lighting-Efficacy

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light/Lighting-Efficacy`

- Documentation: *The efficacy of the lighting type in lumens/Watt.*
- Parent element: [`Fixed-Light`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light/Lighting-Power"></a>Lighting-Power

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light/Lighting-Power`

- Documentation: *The power of the selected lighting type in Watts.*
- Parent element: [`Fixed-Light`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light/Lighting-Outlets"></a>Lighting-Outlets

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light/Lighting-Outlets`

- Documentation: *The number of light fitting outlets of that type.*
- Parent element: [`Fixed-Light`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Deselected-Improvements"></a>SAP-Deselected-Improvements

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Deselected-Improvements`

- Documentation: *None*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Deselected-Improvements/Deselected-Improvement-Measure"></a>Deselected-Improvement-Measure

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Deselected-Improvements/Deselected-Improvement-Measure`

- Documentation: *None*
- Parent element: [`SAP-Deselected-Improvements`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Deselected-Improvements)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Flat-Details"></a>SAP-Flat-Details

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Flat-Details`

- Documentation: *None*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Flat-Details/Level"></a>Level

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Flat-Details/Level`

- Documentation: *Indication of where a flat is located in a building.*
- Parent element: [`SAP-Flat-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Flat-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Flat-Details/Storeys"></a>Storeys

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Flat-Details/Storeys`

- Documentation: *Count of number of storeys present in the block of flats.*
- Parent element: [`SAP-Flat-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Flat-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features"></a>SAP-Special-Features

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features`

- Documentation: *None*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature"></a>SAP-Special-Feature

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`

- Documentation: *None*
- Parent element: [`SAP-Special-Features`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Description"></a>Description

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Description`

- Documentation: *None*
- Parent element: [`SAP-Special-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature"></a>Energy-Feature

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature`

- Documentation: *None*
- Parent element: [`SAP-Special-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Energy-Saved-Or-Generated"></a>Energy-Saved-Or-Generated

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Energy-Saved-Or-Generated`

- Documentation: *Energy saved or generated in kWh/year.*
- Parent element: [`Energy-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Saved-Or-Generated-Fuel"></a>Saved-Or-Generated-Fuel

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Saved-Or-Generated-Fuel`

- Documentation: *None*
- Parent element: [`Energy-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Energy-Used"></a>Energy-Used

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Energy-Used`

- Documentation: *Energy used in kWh/year.*
- Parent element: [`Energy-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Energy-Used-Fuel"></a>Energy-Used-Fuel

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Energy-Used-Fuel`

- Documentation: *None*
- Parent element: [`Energy-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates"></a>Air-Change-Rates

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates`

- Documentation: *For Appendix Q procedure that provides air change rates. Only one Special Feature can have data on air change rates.*
- Parent element: [`Energy-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate"></a>Air-Change-Rate

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate`

- Documentation: *None*
- Parent element: [`Air-Change-Rates`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate/Air-Change-Rate-Month"></a>Air-Change-Rate-Month

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate/Air-Change-Rate-Month`

- Documentation: *None*
- Parent element: [`Air-Change-Rate`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate/Air-Change-Rate-Value"></a>Air-Change-Rate-Value

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate/Air-Change-Rate-Value`

- Documentation: *Air change rate in month.*
- Parent element: [`Air-Change-Rate`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature"></a>Emissions-Feature

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature`

- Documentation: *None*
- Parent element: [`SAP-Special-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature/Emissions-Saved"></a>Emissions-Saved

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature/Emissions-Saved`

- Documentation: *Emissions saved in kg/year.*
- Parent element: [`Emissions-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature/Emissions-Created"></a>Emissions-Created

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature/Emissions-Created`

- Documentation: *Additional emissions in kg/year.*
- Parent element: [`Emissions-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Design-Water-Use"></a>Design-Water-Use

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Design-Water-Use`

- Documentation: *Design limit for total water use.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling"></a>SAP-Cooling

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling`

- Documentation: *None*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling/Cooled-Area"></a>Cooled-Area

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling/Cooled-Area`

- Documentation: *None*
- Parent element: [`SAP-Cooling`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling/Cooling-System-Data-Source"></a>Cooling-System-Data-Source

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling/Cooling-System-Data-Source`

- Documentation: *None*
- Parent element: [`SAP-Cooling`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling/Cooling-System-Class"></a>Cooling-System-Class

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling/Cooling-System-Class`

- Documentation: *Data set includes either class or SEER, not both.*
- Parent element: [`SAP-Cooling`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling)

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling/System-Energy-Efficiency-Ratio"></a>System-Energy-Efficiency-Ratio

`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling/System-Energy-Efficiency-Ratio`

- Documentation: *SEER.*
- Parent element: [`SAP-Cooling`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling)

## <a name="SAP-Compliance-Report/SAP-Report/PDF"></a>PDF

`SAP-Compliance-Report/SAP-Report/PDF`

- Documentation: *DEPRECATED - DO NOT USE This element is allowed for backwards-compatibility but any data sent here will not be read, processed or stored by the register.*
- Parent element: [`SAP-Report`](#SAP-Compliance-Report/SAP-Report)

## <a name="SAP-Compliance-Report/SAP-Report/Insurance-Details"></a>Insurance-Details

`SAP-Compliance-Report/SAP-Report/Insurance-Details`

- Documentation: *None*
- Parent element: [`SAP-Report`](#SAP-Compliance-Report/SAP-Report)

## <a name="SAP-Compliance-Report/SAP-Report/Insurance-Details/Insurer"></a>Insurer

`SAP-Compliance-Report/SAP-Report/Insurance-Details/Insurer`

- Documentation: *The name of the insurance company that underwrites / issued the insurance policy*
- Parent element: [`Insurance-Details`](#SAP-Compliance-Report/SAP-Report/Insurance-Details)

## <a name="SAP-Compliance-Report/SAP-Report/Insurance-Details/Policy-No"></a>Policy-No

`SAP-Compliance-Report/SAP-Report/Insurance-Details/Policy-No`

- Documentation: *The policy number of the insurance policy*
- Parent element: [`Insurance-Details`](#SAP-Compliance-Report/SAP-Report/Insurance-Details)

## <a name="SAP-Compliance-Report/SAP-Report/Insurance-Details/Effective-Date"></a>Effective-Date

`SAP-Compliance-Report/SAP-Report/Insurance-Details/Effective-Date`

- Documentation: *The date that the insurance policy becomes effective (commences cover)*
- Parent element: [`Insurance-Details`](#SAP-Compliance-Report/SAP-Report/Insurance-Details)

## <a name="SAP-Compliance-Report/SAP-Report/Insurance-Details/Expiry-Date"></a>Expiry-Date

`SAP-Compliance-Report/SAP-Report/Insurance-Details/Expiry-Date`

- Documentation: *The date that the insurance policy is supposed to expire.*
- Parent element: [`Insurance-Details`](#SAP-Compliance-Report/SAP-Report/Insurance-Details)

## <a name="SAP-Compliance-Report/SAP-Report/Insurance-Details/PI-Limit"></a>PI-Limit

`SAP-Compliance-Report/SAP-Report/Insurance-Details/PI-Limit`

- Documentation: *The upper limit of the Professional Indemnity cover provided by the insurance policy.*
- Parent element: [`Insurance-Details`](#SAP-Compliance-Report/SAP-Report/Insurance-Details)

## <a name="SAP-Compliance-Report/SAP-Report/ExternalDefinitions-Revision-Number"></a>ExternalDefinitions-Revision-Number

`SAP-Compliance-Report/SAP-Report/ExternalDefinitions-Revision-Number`

- Documentation: *A number indicating the version of related ExternalDefinitions.xsd*
- Parent element: [`SAP-Report`](#SAP-Compliance-Report/SAP-Report)

## <a name="SAP-Compliance-Report/Client-Name"></a>Client-Name

`SAP-Compliance-Report/Client-Name`

- Documentation: *Name of the client. External to the EPC schema for GDPR purposes.*
- Parent element: [`SAP-Compliance-Report`](#SAP-Compliance-Report)

## <a name="SAP-Compliance-Report/Client-Company"></a>Client-Company

`SAP-Compliance-Report/Client-Company`

- Documentation: *Company name of the client. External to the EPC schema for GDPR purposes.*
- Parent element: [`SAP-Compliance-Report`](#SAP-Compliance-Report)

## <a name="SAP-Compliance-Report/Client-Address"></a>Client-Address

`SAP-Compliance-Report/Client-Address`

- Documentation: *Address of the client. External to the EPC schema for GDPR purposes.*
- Parent element: [`SAP-Compliance-Report`](#SAP-Compliance-Report)

## <a name="SAP-Compliance-Report/Client-Address/Address-Line-1"></a>Address-Line-1

`SAP-Compliance-Report/Client-Address/Address-Line-1`

- Documentation: *None*
- Parent element: [`Client-Address`](#SAP-Compliance-Report/Client-Address)

## <a name="SAP-Compliance-Report/Client-Address/Address-Line-2"></a>Address-Line-2

`SAP-Compliance-Report/Client-Address/Address-Line-2`

- Documentation: *None*
- Parent element: [`Client-Address`](#SAP-Compliance-Report/Client-Address)

## <a name="SAP-Compliance-Report/Client-Address/Address-Line-3"></a>Address-Line-3

`SAP-Compliance-Report/Client-Address/Address-Line-3`

- Documentation: *None*
- Parent element: [`Client-Address`](#SAP-Compliance-Report/Client-Address)

## <a name="SAP-Compliance-Report/Client-Address/Post-Town"></a>Post-Town

`SAP-Compliance-Report/Client-Address/Post-Town`

- Documentation: *None*
- Parent element: [`Client-Address`](#SAP-Compliance-Report/Client-Address)

## <a name="SAP-Compliance-Report/Client-Address/Postcode"></a>Postcode

`SAP-Compliance-Report/Client-Address/Postcode`

- Documentation: *The Postcode for the Address*
- Parent element: [`Client-Address`](#SAP-Compliance-Report/Client-Address)

## <a name="SAP-Compliance-Report/Is-Multiple-Compliance"></a>Is-Multiple-Compliance

`SAP-Compliance-Report/Is-Multiple-Compliance`

- Documentation: *Is the compliance report part of a multiple compliance calculation.*
- Parent element: [`SAP-Compliance-Report`](#SAP-Compliance-Report)

