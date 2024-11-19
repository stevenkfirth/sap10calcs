# SAP Schema 19.1.0. docs

This page contains the documentation for the XML schema [SAP-Schema-19.1.0](https://github.com/communitiesuk/epb-register-api/tree/master/api/schemas/xml/SAP-Schema-19.1.0/SAP).

This XML schema describes the format of the XML input files for SAP 10.2 calculations.

The root XML element can be either a [SAP-Compliance-Report](#SAP_Compliance_Report) or a [SAP-Report](#SAP_Compliance_Report__SAP_Report) element.

## <a name="SAP_Compliance_Report"></a>SAP-Compliance-Report

`SAP_Compliance_Report`

- Documentation: *None*
- Parent element: None

## <a name="SAP_Compliance_Report__SAP_Report"></a>SAP-Report

`SAP_Compliance_Report__SAP_Report`

- Documentation: *The SAP report corresponding to the compliance report.*
- Parent element: [`SAP-Compliance-Report`](#SAP_Compliance_Report)

## <a name="SAP_Compliance_Report__SAP_Report__Schema_Version_Original"></a>Schema-Version-Original

`SAP_Compliance_Report__SAP_Report__Schema_Version_Original`

- Documentation: *The schema version that the data conformed to when it was lodged.*
- Parent element: [`SAP-Report`](#SAP_Compliance_Report__SAP_Report)

## <a name="SAP_Compliance_Report__SAP_Report__Schema_Version_Current"></a>Schema-Version-Current

`SAP_Compliance_Report__SAP_Report__Schema_Version_Current`

- Documentation: *The schema version to which the data conforms. This node is inserted by the register when a retrieval is requested. It must not be present in a lodgement being sent to the register.*
- Parent element: [`SAP-Report`](#SAP_Compliance_Report__SAP_Report)

## <a name="SAP_Compliance_Report__SAP_Report__SAP_Version"></a>SAP-Version

`SAP_Compliance_Report__SAP_Report__SAP_Version`

- Documentation: *SAP version that was used for the calculation.*
- Parent element: [`SAP-Report`](#SAP_Compliance_Report__SAP_Report)

## <a name="SAP_Compliance_Report__SAP_Report__SAP_Data_Version"></a>SAP-Data-Version

`SAP_Compliance_Report__SAP_Report__SAP_Data_Version`

- Documentation: *Version of SAP that was used to define the input data for the calculation.*
- Parent element: [`SAP-Report`](#SAP_Compliance_Report__SAP_Report)

## <a name="SAP_Compliance_Report__SAP_Report__PCDF_Revision_Number"></a>PCDF-Revision-Number

`SAP_Compliance_Report__SAP_Report__PCDF_Revision_Number`

- Documentation: *Revision Number of the PCDF file used for the calculations.*
- Parent element: [`SAP-Report`](#SAP_Compliance_Report__SAP_Report)

## <a name="SAP_Compliance_Report__SAP_Report__Calculation_Software_Name"></a>Calculation-Software-Name

`SAP_Compliance_Report__SAP_Report__Calculation_Software_Name`

- Documentation: *Name of the software used to perform the SAP calculation.*
- Parent element: [`SAP-Report`](#SAP_Compliance_Report__SAP_Report)

## <a name="SAP_Compliance_Report__SAP_Report__Calculation_Software_Version"></a>Calculation-Software-Version

`SAP_Compliance_Report__SAP_Report__Calculation_Software_Version`

- Documentation: *Version of the software used to perform the SAP calculation.*
- Parent element: [`SAP-Report`](#SAP_Compliance_Report__SAP_Report)

## <a name="SAP_Compliance_Report__SAP_Report__User_Interface_Name"></a>User-Interface-Name

`SAP_Compliance_Report__SAP_Report__User_Interface_Name`

- Documentation: *None*
- Parent element: [`SAP-Report`](#SAP_Compliance_Report__SAP_Report)

## <a name="SAP_Compliance_Report__SAP_Report__User_Interface_Version"></a>User-Interface-Version

`SAP_Compliance_Report__SAP_Report__User_Interface_Version`

- Documentation: *None*
- Parent element: [`SAP-Report`](#SAP_Compliance_Report__SAP_Report)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header"></a>Report-Header

`SAP_Compliance_Report__SAP_Report__Report_Header`

- Documentation: *None*
- Parent element: [`SAP-Report`](#SAP_Compliance_Report__SAP_Report)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__RRN"></a>RRN

`SAP_Compliance_Report__SAP_Report__Report_Header__RRN`

- Documentation: *Report Reference Number is the unique report Identifier that the report will be publicly known by. The RRN is allocated to the Report at the point that it is registered and will be algorithmically derived from the natural key characteristics of the Home Condition Report i.e. The Unique Property Reference Number (UPRN) and Inspection Date.*
- Parent element: [`Report-Header`](#SAP_Compliance_Report__SAP_Report__Report_Header)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Inspection_Date"></a>Inspection-Date

`SAP_Compliance_Report__SAP_Report__Report_Header__Inspection_Date`

- Documentation: *The date that the inspection was actually carried out by the Home Inspector.*
- Parent element: [`Report-Header`](#SAP_Compliance_Report__SAP_Report__Report_Header)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Report_Type"></a>Report-Type

`SAP_Compliance_Report__SAP_Report__Report_Header__Report_Type`

- Documentation: *The type of Home Inspection that was carried out. Initially the only allowed type will be a Home Condition Report inspection but this may be extended in the future to cover Energy Assessment Only inspections.*
- Parent element: [`Report-Header`](#SAP_Compliance_Report__SAP_Report__Report_Header)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Completion_Date"></a>Completion-Date

`SAP_Compliance_Report__SAP_Report__Report_Header__Completion_Date`

- Documentation: *The date that the Home Inspector completed the report. This will be after the Inspection Date but generally before the Registration Date.*
- Parent element: [`Report-Header`](#SAP_Compliance_Report__SAP_Report__Report_Header)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Registration_Date"></a>Registration-Date

`SAP_Compliance_Report__SAP_Report__Report_Header__Registration_Date`

- Documentation: *The date that the report was submitted to the HCR Registration Organisation for lodging in the HCR Register.*
- Parent element: [`Report-Header`](#SAP_Compliance_Report__SAP_Report__Report_Header)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Status"></a>Status

`SAP_Compliance_Report__SAP_Report__Report_Header__Status`

- Documentation: *The Status of the Report. A Home Condition Report can have a number of distinct states depending on whereabouts in its overall lifecycle the HCR is - see Home Condition Report Statechart for more details.*
- Parent element: [`Report-Header`](#SAP_Compliance_Report__SAP_Report__Report_Header)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Language_Code"></a>Language-Code

`SAP_Compliance_Report__SAP_Report__Report_Header__Language_Code`

- Documentation: *The language that the report is written in.*
- Parent element: [`Report-Header`](#SAP_Compliance_Report__SAP_Report__Report_Header)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Tenure"></a>Tenure

`SAP_Compliance_Report__SAP_Report__Report_Header__Tenure`

- Documentation: *None*
- Parent element: [`Report-Header`](#SAP_Compliance_Report__SAP_Report__Report_Header)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Transaction_Type"></a>Transaction-Type

`SAP_Compliance_Report__SAP_Report__Report_Header__Transaction_Type`

- Documentation: *None*
- Parent element: [`Report-Header`](#SAP_Compliance_Report__SAP_Report__Report_Header)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Seller_Commission_Report"></a>Seller-Commission-Report

`SAP_Compliance_Report__SAP_Report__Report_Header__Seller_Commission_Report`

- Documentation: *Indicates that the HCR was commissioned by the Seller of the Property or their Agent. This is required in order to differentiate these reports from Buyer commisioned reports which are not eligible for inclusion in a Home Information Pack*
- Parent element: [`Report-Header`](#SAP_Compliance_Report__SAP_Report__Report_Header)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Property_Type"></a>Property-Type

`SAP_Compliance_Report__SAP_Report__Report_Header__Property_Type`

- Documentation: *Describes the type of Property that is being inspected. This should be the same as the Property-Type recorded in the Property-Details section.*
- Parent element: [`Report-Header`](#SAP_Compliance_Report__SAP_Report__Report_Header)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector"></a>Home-Inspector

`SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector`

- Documentation: *None*
- Parent element: [`Report-Header`](#SAP_Compliance_Report__SAP_Report__Report_Header)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Name"></a>Name

`SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Name`

- Documentation: *The name by which the Home Inspector is registered. This is a structured name containing prefix, first name + surname.*
- Parent element: [`Home-Inspector`](#SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Notify_Lodgement"></a>Notify-Lodgement

`SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Notify_Lodgement`

- Documentation: *Indicates whether the assessor wants to be notified that a the report has been lodged in the register*
- Parent element: [`Home-Inspector`](#SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Contact_Address"></a>Contact-Address

`SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Contact_Address`

- Documentation: *The address that any written correspondence can be sent to. This is not the same as the Registered Address because it may, of course, be a Post Office Box.*
- Parent element: [`Home-Inspector`](#SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Contact_Address__Address_Line_1"></a>Address-Line-1

`SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Contact_Address__Address_Line_1`

- Documentation: *None*
- Parent element: [`Contact-Address`](#SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Contact_Address)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Contact_Address__Address_Line_2"></a>Address-Line-2

`SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Contact_Address__Address_Line_2`

- Documentation: *None*
- Parent element: [`Contact-Address`](#SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Contact_Address)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Contact_Address__Address_Line_3"></a>Address-Line-3

`SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Contact_Address__Address_Line_3`

- Documentation: *None*
- Parent element: [`Contact-Address`](#SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Contact_Address)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Contact_Address__Post_Town"></a>Post-Town

`SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Contact_Address__Post_Town`

- Documentation: *None*
- Parent element: [`Contact-Address`](#SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Contact_Address)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Contact_Address__Postcode"></a>Postcode

`SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Contact_Address__Postcode`

- Documentation: *The Postcode for the Address*
- Parent element: [`Contact-Address`](#SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Contact_Address)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Web_Site"></a>Web-Site

`SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Web_Site`

- Documentation: *None*
- Parent element: [`Home-Inspector`](#SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__E_Mail"></a>E-Mail

`SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__E_Mail`

- Documentation: *the E-Mail address that the Authorised User can be contacted at.*
- Parent element: [`Home-Inspector`](#SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Fax"></a>Fax

`SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Fax`

- Documentation: *None*
- Parent element: [`Home-Inspector`](#SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Telephone"></a>Telephone

`SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Telephone`

- Documentation: *None*
- Parent element: [`Home-Inspector`](#SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Company_Name"></a>Company-Name

`SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Company_Name`

- Documentation: *The Name of the Company that the assessor is employed by.*
- Parent element: [`Home-Inspector`](#SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Scheme_Name"></a>Scheme-Name

`SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Scheme_Name`

- Documentation: *None*
- Parent element: [`Home-Inspector`](#SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Scheme_Web_Site"></a>Scheme-Web-Site

`SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Scheme_Web_Site`

- Documentation: *None*
- Parent element: [`Home-Inspector`](#SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Identification_Number"></a>Identification-Number

`SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Identification_Number`

- Documentation: *None*
- Parent element: [`Home-Inspector`](#SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Identification_Number__Certificate_Number"></a>Certificate-Number

`SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Identification_Number__Certificate_Number`

- Documentation: *The unique identifier assigned to the assessor by the scheme by which they can be identified throughout their membership of the scheme.*
- Parent element: [`Identification-Number`](#SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Identification_Number)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Identification_Number__Membership_Number"></a>Membership-Number

`SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Identification_Number__Membership_Number`

- Documentation: *For Scottish DEAs only*
- Parent element: [`Identification-Number`](#SAP_Compliance_Report__SAP_Report__Report_Header__Home_Inspector__Identification_Number)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Property"></a>Property

`SAP_Compliance_Report__SAP_Report__Report_Header__Property`

- Documentation: *None*
- Parent element: [`Report-Header`](#SAP_Compliance_Report__SAP_Report__Report_Header)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Property__Address"></a>Address

`SAP_Compliance_Report__SAP_Report__Report_Header__Property__Address`

- Documentation: *Address for the property.*
- Parent element: [`Property`](#SAP_Compliance_Report__SAP_Report__Report_Header__Property)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Property__Address__Address_Line_1"></a>Address-Line-1

`SAP_Compliance_Report__SAP_Report__Report_Header__Property__Address__Address_Line_1`

- Documentation: *None*
- Parent element: [`Address`](#SAP_Compliance_Report__SAP_Report__Report_Header__Property__Address)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Property__Address__Address_Line_2"></a>Address-Line-2

`SAP_Compliance_Report__SAP_Report__Report_Header__Property__Address__Address_Line_2`

- Documentation: *None*
- Parent element: [`Address`](#SAP_Compliance_Report__SAP_Report__Report_Header__Property__Address)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Property__Address__Address_Line_3"></a>Address-Line-3

`SAP_Compliance_Report__SAP_Report__Report_Header__Property__Address__Address_Line_3`

- Documentation: *None*
- Parent element: [`Address`](#SAP_Compliance_Report__SAP_Report__Report_Header__Property__Address)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Property__Address__Post_Town"></a>Post-Town

`SAP_Compliance_Report__SAP_Report__Report_Header__Property__Address__Post_Town`

- Documentation: *None*
- Parent element: [`Address`](#SAP_Compliance_Report__SAP_Report__Report_Header__Property__Address)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Property__Address__Postcode"></a>Postcode

`SAP_Compliance_Report__SAP_Report__Report_Header__Property__Address__Postcode`

- Documentation: *The Postcode for the Address*
- Parent element: [`Address`](#SAP_Compliance_Report__SAP_Report__Report_Header__Property__Address)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Property__UPRN"></a>UPRN

`SAP_Compliance_Report__SAP_Report__Report_Header__Property__UPRN`

- Documentation: *Unique Property Reference Number*
- Parent element: [`Property`](#SAP_Compliance_Report__SAP_Report__Report_Header__Property)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Property__Site_Reference"></a>Site-Reference

`SAP_Compliance_Report__SAP_Report__Report_Header__Property__Site_Reference`

- Documentation: *A site reference*
- Parent element: [`Property`](#SAP_Compliance_Report__SAP_Report__Report_Header__Property)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Property__Plot_Reference"></a>Plot-Reference

`SAP_Compliance_Report__SAP_Report__Report_Header__Property__Plot_Reference`

- Documentation: *A plot reference*
- Parent element: [`Property`](#SAP_Compliance_Report__SAP_Report__Report_Header__Property)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Region_Code"></a>Region-Code

`SAP_Compliance_Report__SAP_Report__Report_Header__Region_Code`

- Documentation: *Region within the UK.*
- Parent element: [`Report-Header`](#SAP_Compliance_Report__SAP_Report__Report_Header)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Country_Code"></a>Country-Code

`SAP_Compliance_Report__SAP_Report__Report_Header__Country_Code`

- Documentation: *Country within the UK.*
- Parent element: [`Report-Header`](#SAP_Compliance_Report__SAP_Report__Report_Header)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Related_Party_Disclosure"></a>Related-Party-Disclosure

`SAP_Compliance_Report__SAP_Report__Report_Header__Related_Party_Disclosure`

- Documentation: *None*
- Parent element: [`Report-Header`](#SAP_Compliance_Report__SAP_Report__Report_Header)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Related_Party_Disclosure__Related_Party_Disclosure_Text"></a>Related-Party-Disclosure-Text

`SAP_Compliance_Report__SAP_Report__Report_Header__Related_Party_Disclosure__Related_Party_Disclosure_Text`

- Documentation: *For backward compatibility only.*
- Parent element: [`Related-Party-Disclosure`](#SAP_Compliance_Report__SAP_Report__Report_Header__Related_Party_Disclosure)

## <a name="SAP_Compliance_Report__SAP_Report__Report_Header__Related_Party_Disclosure__Related_Party_Disclosure_Number"></a>Related-Party-Disclosure-Number

`SAP_Compliance_Report__SAP_Report__Report_Header__Related_Party_Disclosure__Related_Party_Disclosure_Number`

- Documentation: *Code indicating any potential conflicts of interest or commercial relationships with other parties.*
- Parent element: [`Related-Party-Disclosure`](#SAP_Compliance_Report__SAP_Report__Report_Header__Related_Party_Disclosure)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment"></a>Energy-Assessment

`SAP_Compliance_Report__SAP_Report__Energy_Assessment`

- Documentation: *None*
- Parent element: [`SAP-Report`](#SAP_Compliance_Report__SAP_Report)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Assessment_Date"></a>Assessment-Date

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Assessment_Date`

- Documentation: *Date of assessment.*
- Parent element: [`Energy-Assessment`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary"></a>Property-Summary

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary`

- Documentation: *None*
- Parent element: [`Energy-Assessment`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Walls"></a>Walls

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Walls`

- Documentation: *None*
- Parent element: [`Property-Summary`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Walls__Description"></a>Description

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Walls__Description`

- Documentation: *Overall description of the property feature*
- Parent element: [`Walls`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Walls)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Walls__Energy_Efficiency_Rating"></a>Energy-Efficiency-Rating

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Walls__Energy_Efficiency_Rating`

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: [`Walls`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Walls)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Walls__Environmental_Efficiency_Rating"></a>Environmental-Efficiency-Rating

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Walls__Environmental_Efficiency_Rating`

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: [`Walls`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Walls)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Roof"></a>Roof

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Roof`

- Documentation: *None*
- Parent element: [`Property-Summary`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Roof__Description"></a>Description

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Roof__Description`

- Documentation: *Overall description of the property feature*
- Parent element: [`Roof`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Roof)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Roof__Energy_Efficiency_Rating"></a>Energy-Efficiency-Rating

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Roof__Energy_Efficiency_Rating`

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: [`Roof`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Roof)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Roof__Environmental_Efficiency_Rating"></a>Environmental-Efficiency-Rating

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Roof__Environmental_Efficiency_Rating`

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: [`Roof`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Roof)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Floor"></a>Floor

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Floor`

- Documentation: *None*
- Parent element: [`Property-Summary`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Floor__Description"></a>Description

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Floor__Description`

- Documentation: *Overall description of the property feature*
- Parent element: [`Floor`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Floor)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Floor__Energy_Efficiency_Rating"></a>Energy-Efficiency-Rating

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Floor__Energy_Efficiency_Rating`

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: [`Floor`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Floor)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Floor__Environmental_Efficiency_Rating"></a>Environmental-Efficiency-Rating

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Floor__Environmental_Efficiency_Rating`

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: [`Floor`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Floor)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Windows"></a>Windows

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Windows`

- Documentation: *None*
- Parent element: [`Property-Summary`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Windows__Description"></a>Description

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Windows__Description`

- Documentation: *Overall description of the property feature*
- Parent element: [`Windows`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Windows)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Windows__Energy_Efficiency_Rating"></a>Energy-Efficiency-Rating

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Windows__Energy_Efficiency_Rating`

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: [`Windows`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Windows)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Windows__Environmental_Efficiency_Rating"></a>Environmental-Efficiency-Rating

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Windows__Environmental_Efficiency_Rating`

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: [`Windows`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Windows)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Main_Heating"></a>Main-Heating

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Main_Heating`

- Documentation: *None*
- Parent element: [`Property-Summary`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Main_Heating__Description"></a>Description

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Main_Heating__Description`

- Documentation: *Overall description of the property feature*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Main_Heating__Energy_Efficiency_Rating"></a>Energy-Efficiency-Rating

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Main_Heating__Energy_Efficiency_Rating`

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Main_Heating__Environmental_Efficiency_Rating"></a>Environmental-Efficiency-Rating

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Main_Heating__Environmental_Efficiency_Rating`

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Main_Heating_Controls"></a>Main-Heating-Controls

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Main_Heating_Controls`

- Documentation: *None*
- Parent element: [`Property-Summary`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Main_Heating_Controls__Description"></a>Description

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Main_Heating_Controls__Description`

- Documentation: *Overall description of the property feature*
- Parent element: [`Main-Heating-Controls`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Main_Heating_Controls)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Main_Heating_Controls__Energy_Efficiency_Rating"></a>Energy-Efficiency-Rating

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Main_Heating_Controls__Energy_Efficiency_Rating`

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: [`Main-Heating-Controls`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Main_Heating_Controls)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Main_Heating_Controls__Environmental_Efficiency_Rating"></a>Environmental-Efficiency-Rating

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Main_Heating_Controls__Environmental_Efficiency_Rating`

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: [`Main-Heating-Controls`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Main_Heating_Controls)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Secondary_Heating"></a>Secondary-Heating

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Secondary_Heating`

- Documentation: *None*
- Parent element: [`Property-Summary`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Secondary_Heating__Description"></a>Description

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Secondary_Heating__Description`

- Documentation: *Overall description of the property feature*
- Parent element: [`Secondary-Heating`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Secondary_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Secondary_Heating__Energy_Efficiency_Rating"></a>Energy-Efficiency-Rating

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Secondary_Heating__Energy_Efficiency_Rating`

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: [`Secondary-Heating`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Secondary_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Secondary_Heating__Environmental_Efficiency_Rating"></a>Environmental-Efficiency-Rating

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Secondary_Heating__Environmental_Efficiency_Rating`

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: [`Secondary-Heating`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Secondary_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Hot_Water"></a>Hot-Water

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Hot_Water`

- Documentation: *None*
- Parent element: [`Property-Summary`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Hot_Water__Description"></a>Description

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Hot_Water__Description`

- Documentation: *Overall description of the property feature*
- Parent element: [`Hot-Water`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Hot_Water)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Hot_Water__Energy_Efficiency_Rating"></a>Energy-Efficiency-Rating

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Hot_Water__Energy_Efficiency_Rating`

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: [`Hot-Water`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Hot_Water)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Hot_Water__Environmental_Efficiency_Rating"></a>Environmental-Efficiency-Rating

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Hot_Water__Environmental_Efficiency_Rating`

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: [`Hot-Water`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Hot_Water)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Lighting"></a>Lighting

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Lighting`

- Documentation: *None*
- Parent element: [`Property-Summary`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Lighting__Description"></a>Description

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Lighting__Description`

- Documentation: *Overall description of the property feature*
- Parent element: [`Lighting`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Lighting)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Lighting__Energy_Efficiency_Rating"></a>Energy-Efficiency-Rating

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Lighting__Energy_Efficiency_Rating`

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: [`Lighting`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Lighting)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Lighting__Environmental_Efficiency_Rating"></a>Environmental-Efficiency-Rating

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Lighting__Environmental_Efficiency_Rating`

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: [`Lighting`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Lighting)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Air_Tightness"></a>Air-Tightness

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Air_Tightness`

- Documentation: *None*
- Parent element: [`Property-Summary`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Air_Tightness__Description"></a>Description

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Air_Tightness__Description`

- Documentation: *Overall description of the property feature*
- Parent element: [`Air-Tightness`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Air_Tightness)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Air_Tightness__Energy_Efficiency_Rating"></a>Energy-Efficiency-Rating

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Air_Tightness__Energy_Efficiency_Rating`

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: [`Air-Tightness`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Air_Tightness)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Air_Tightness__Environmental_Efficiency_Rating"></a>Environmental-Efficiency-Rating

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Air_Tightness__Environmental_Efficiency_Rating`

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: [`Air-Tightness`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Air_Tightness)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Has_Fixed_Air_Conditioning"></a>Has-Fixed-Air-Conditioning

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Has_Fixed_Air_Conditioning`

- Documentation: *Fixed air conditioning?*
- Parent element: [`Property-Summary`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Has_Hot_Water_Cylinder"></a>Has-Hot-Water-Cylinder

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Has_Hot_Water_Cylinder`

- Documentation: *Hot water cylinder?*
- Parent element: [`Property-Summary`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Has_Heated_Separate_Conservatory"></a>Has-Heated-Separate-Conservatory

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Has_Heated_Separate_Conservatory`

- Documentation: *Heated separate conservatory?*
- Parent element: [`Property-Summary`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Dwelling_Type"></a>Dwelling-Type

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Dwelling_Type`

- Documentation: *Is a string such as Detached house or Top-floor flat*
- Parent element: [`Property-Summary`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Total_Floor_Area"></a>Total-Floor-Area

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Total_Floor_Area`

- Documentation: *Is a number such as 125*
- Parent element: [`Property-Summary`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Multiple_Glazed_Percentage"></a>Multiple-Glazed-Percentage

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Multiple_Glazed_Percentage`

- Documentation: *Fraction of windows that are multiply glazed to nearest 1%.*
- Parent element: [`Property-Summary`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Multiple_Glazed_Percentage_NR"></a>Multiple-Glazed-Percentage-NR

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Multiple_Glazed_Percentage_NR`

- Documentation: *For backward compatibility only, do not use.*
- Parent element: [`Property-Summary`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Is_Zero_Carbon_Home"></a>Is-Zero-Carbon-Home

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary__Is_Zero_Carbon_Home`

- Documentation: *Is dwelling a Zero Carbon Home?*
- Parent element: [`Property-Summary`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Property_Summary)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use"></a>Energy-Use

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use`

- Documentation: *Calculated results from the energy assessment.*
- Parent element: [`Energy-Assessment`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__DER"></a>DER

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__DER`

- Documentation: *The DER of the Property*
- Parent element: [`Energy-Use`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__TER"></a>TER

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__TER`

- Documentation: *The TER of the Property*
- Parent element: [`Energy-Use`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__DPER"></a>DPER

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__DPER`

- Documentation: *The DPER of the Property*
- Parent element: [`Energy-Use`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__TPER"></a>TPER

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__TPER`

- Documentation: *The TPER of the Property*
- Parent element: [`Energy-Use`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__DFEE"></a>DFEE

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__DFEE`

- Documentation: *The DFEE of the Property*
- Parent element: [`Energy-Use`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__TFEE"></a>TFEE

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__TFEE`

- Documentation: *The TFEE of the Property*
- Parent element: [`Energy-Use`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__Energy_Rating_Current"></a>Energy-Rating-Current

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__Energy_Rating_Current`

- Documentation: *The Current Energy Rating of the Property*
- Parent element: [`Energy-Use`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__Energy_Rating_Potential"></a>Energy-Rating-Potential

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__Energy_Rating_Potential`

- Documentation: *The overall Energy Rating for the Property being assessed.*
- Parent element: [`Energy-Use`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__Energy_Rating_Average"></a>Energy-Rating-Average

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__Energy_Rating_Average`

- Documentation: *Average SAP rating for the country concerned. 0 if unknown or not applicable*
- Parent element: [`Energy-Use`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__Environmental_Impact_Current"></a>Environmental-Impact-Current

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__Environmental_Impact_Current`

- Documentation: *The estimated current Environmental Impact Rating of the property*
- Parent element: [`Energy-Use`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__Environmental_Impact_Potential"></a>Environmental-Impact-Potential

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__Environmental_Impact_Potential`

- Documentation: *The estimated potential Environmental Impact Rating of the property*
- Parent element: [`Energy-Use`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__Energy_Consumption_Current"></a>Energy-Consumption-Current

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__Energy_Consumption_Current`

- Documentation: *Estimated total energy consumption for the Property in a 12 month period. Value is Kilowatt Hours per Square Metre (kWh/m2)*
- Parent element: [`Energy-Use`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__Energy_Consumption_Potential"></a>Energy-Consumption-Potential

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__Energy_Consumption_Potential`

- Documentation: *Estimated total energy consumption for the Property in a 12 month period. Value is Kilowatt Hours per Square Metre (kWh/m2)*
- Parent element: [`Energy-Use`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__CO2_Emissions_Current"></a>CO2-Emissions-Current

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__CO2_Emissions_Current`

- Documentation: *CO2 emissions per year in tonnes/year.*
- Parent element: [`Energy-Use`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__CO2_Emissions_Current_Per_Floor_Area"></a>CO2-Emissions-Current-Per-Floor-Area

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__CO2_Emissions_Current_Per_Floor_Area`

- Documentation: *CO2 emissions per square metre floor area per year in kg/m2.*
- Parent element: [`Energy-Use`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__CO2_Emissions_Potential"></a>CO2-Emissions-Potential

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__CO2_Emissions_Potential`

- Documentation: *Estimated value in Tonnes per Year of the total CO2 emissions produced by the Property in 12 month period.*
- Parent element: [`Energy-Use`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__Lighting_Cost_Current"></a>Lighting-Cost-Current

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__Lighting_Cost_Current`

- Documentation: *The current estimated cost of Lighting for the property*
- Parent element: [`Energy-Use`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__Lighting_Cost_Potential"></a>Lighting-Cost-Potential

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__Lighting_Cost_Potential`

- Documentation: *The current estimated cost of Lighting for the property*
- Parent element: [`Energy-Use`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__Heating_Cost_Current"></a>Heating-Cost-Current

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__Heating_Cost_Current`

- Documentation: *The current estimated cost of Heating for the property*
- Parent element: [`Energy-Use`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__Heating_Cost_Potential"></a>Heating-Cost-Potential

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__Heating_Cost_Potential`

- Documentation: *The current estimated cost of Heating for the property*
- Parent element: [`Energy-Use`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__Hot_Water_Cost_Current"></a>Hot-Water-Cost-Current

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__Hot_Water_Cost_Current`

- Documentation: *|The current estimated cost of Hot Water for the property*
- Parent element: [`Energy-Use`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__Hot_Water_Cost_Potential"></a>Hot-Water-Cost-Potential

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use__Hot_Water_Cost_Potential`

- Documentation: *|The current estimated cost of Hot Water for the property*
- Parent element: [`Energy-Use`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Energy_Use)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements"></a>Suggested-Improvements

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements`

- Documentation: *Improvement measures listed on the EPC.*
- Parent element: [`Energy-Assessment`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement"></a>Improvement

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement`

- Documentation: *None*
- Parent element: [`Suggested-Improvements`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement__Sequence"></a>Sequence

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement__Sequence`

- Documentation: *Sequence of the Suggested Improvements within the set of Suggested Improvements. This is used to order the Recommendations on the output HCR / EPC so that the cumulative Ratings make sense. The Improved Energy Ratings that result from carrying out a Suggested Improvement are cumulative and assume that the improvements have been installed in the order they appear in the list. Hence they must be sequenced.*
- Parent element: [`Improvement`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement__Improvement_Category"></a>Improvement-Category

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement__Improvement_Category`

- Documentation: *The category of improvement. This identifies where on the report the recommendation is printed.*
- Parent element: [`Improvement`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement__Improvement_Type"></a>Improvement-Type

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement__Improvement_Type`

- Documentation: *Suggested work to be carried out on the Property to improve its energy efficiency. This should be a enumerated list of acceptable improvements but it hasn't yet been defined.*
- Parent element: [`Improvement`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement__Typical_Saving"></a>Typical-Saving

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement__Typical_Saving`

- Documentation: *Typical savings (in British Pounds) per year if the suggested improvement is carried out. 0 if not assessed*
- Parent element: [`Improvement`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement__Energy_Performance_Rating"></a>Energy-Performance-Rating

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement__Energy_Performance_Rating`

- Documentation: *The estimated Energy performance rating of the Property after the Suggested Improvement has been carried out providing any preceding Suggested Improvement has also been carried out. 0 if not assessed*
- Parent element: [`Improvement`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement__Environmental_Impact_Rating"></a>Environmental-Impact-Rating

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement__Environmental_Impact_Rating`

- Documentation: *The estimated Environmental Impact rating of the Property after the Suggested Improvement has been carried out providing any preceding Suggested Improvement has also been carried out. 0 if not assessed*
- Parent element: [`Improvement`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement__Improvement_Details"></a>Improvement-Details

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement__Improvement_Details`

- Documentation: *None*
- Parent element: [`Improvement`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement__Improvement_Details__Improvement_Texts"></a>Improvement-Texts

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement__Improvement_Details__Improvement_Texts`

- Documentation: *For backward compatability only*
- Parent element: [`Improvement-Details`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement__Improvement_Details)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement__Improvement_Details__Improvement_Texts__Improvement_Summary"></a>Improvement-Summary

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement__Improvement_Details__Improvement_Texts__Improvement_Summary`

- Documentation: *A short description of the suggested improvement.*
- Parent element: [`Improvement-Texts`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement__Improvement_Details__Improvement_Texts)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement__Improvement_Details__Improvement_Texts__Improvement_Heading"></a>Improvement-Heading

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement__Improvement_Details__Improvement_Texts__Improvement_Heading`

- Documentation: *Text to precede the improvement description. If this field is not provided the 'Improvement-Summary' is used instead.*
- Parent element: [`Improvement-Texts`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement__Improvement_Details__Improvement_Texts)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement__Improvement_Details__Improvement_Texts__Improvement_Description"></a>Improvement-Description

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement__Improvement_Details__Improvement_Texts__Improvement_Description`

- Documentation: *Detailed description of the suggested improvement.*
- Parent element: [`Improvement-Texts`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement__Improvement_Details__Improvement_Texts)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement__Improvement_Details__Improvement_Number"></a>Improvement-Number

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement__Improvement_Details__Improvement_Number`

- Documentation: *None*
- Parent element: [`Improvement-Details`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement__Improvement_Details)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement__Indicative_Cost"></a>Indicative-Cost

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement__Indicative_Cost`

- Documentation: *None*
- Parent element: [`Improvement`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement__Green_Deal_Category"></a>Green-Deal-Category

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement__Green_Deal_Category`

- Documentation: *None*
- Parent element: [`Improvement`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Suggested_Improvements__Improvement)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__LZC_Energy_Sources"></a>LZC-Energy-Sources

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__LZC_Energy_Sources`

- Documentation: *None*
- Parent element: [`Energy-Assessment`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__LZC_Energy_Sources__LZC_Energy_Source"></a>LZC-Energy-Source

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__LZC_Energy_Sources__LZC_Energy_Source`

- Documentation: *Low and zero carbon energy source(s) for the property.*
- Parent element: [`LZC-Energy-Sources`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__LZC_Energy_Sources)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive"></a>Renewable-Heat-Incentive

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive`

- Documentation: *None*
- Parent element: [`Energy-Assessment`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive__RHI_New_Dwelling"></a>RHI-New-Dwelling

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive__RHI_New_Dwelling`

- Documentation: *None*
- Parent element: [`Renewable-Heat-Incentive`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive__RHI_New_Dwelling__Space_Heating"></a>Space-Heating

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive__RHI_New_Dwelling__Space_Heating`

- Documentation: *Space heating requirement.*
- Parent element: [`RHI-New-Dwelling`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive__RHI_New_Dwelling)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive__RHI_New_Dwelling__Water_Heating"></a>Water-Heating

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive__RHI_New_Dwelling__Water_Heating`

- Documentation: *Water heating requirement.*
- Parent element: [`RHI-New-Dwelling`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive__RHI_New_Dwelling)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive__RHI_Existing_Dwelling"></a>RHI-Existing-Dwelling

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive__RHI_Existing_Dwelling`

- Documentation: *None*
- Parent element: [`Renewable-Heat-Incentive`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive__RHI_Existing_Dwelling__Space_Heating_Existing_Dwelling"></a>Space-Heating-Existing-Dwelling

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive__RHI_Existing_Dwelling__Space_Heating_Existing_Dwelling`

- Documentation: *Space heating requirement for existing dwelling.*
- Parent element: [`RHI-Existing-Dwelling`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive__RHI_Existing_Dwelling)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive__RHI_Existing_Dwelling__Space_Heating_With_Loft_Insulation"></a>Space-Heating-With-Loft-Insulation

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive__RHI_Existing_Dwelling__Space_Heating_With_Loft_Insulation`

- Documentation: *Space heating requirement after implementation of loft insulation recommendation, omit if loft insulation not recommended. For backwards compatibility only, do not use*
- Parent element: [`RHI-Existing-Dwelling`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive__RHI_Existing_Dwelling)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive__RHI_Existing_Dwelling__Space_Heating_With_Cavity_Insulation"></a>Space-Heating-With-Cavity-Insulation

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive__RHI_Existing_Dwelling__Space_Heating_With_Cavity_Insulation`

- Documentation: *Space heating requirement after implementation of cavity insulation recommendation, omit if cavity insulation not recommended. For backwards compatibility only, do not use*
- Parent element: [`RHI-Existing-Dwelling`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive__RHI_Existing_Dwelling)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive__RHI_Existing_Dwelling__Space_Heating_With_Loft_And_Cavity_Insulation"></a>Space-Heating-With-Loft-And-Cavity-Insulation

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive__RHI_Existing_Dwelling__Space_Heating_With_Loft_And_Cavity_Insulation`

- Documentation: *Space heating requirement after implementation of loft and cavity insulation recommendations, same as existing dwelling if neither is recommended. For backwards compatibility only, do not use*
- Parent element: [`RHI-Existing-Dwelling`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive__RHI_Existing_Dwelling)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive__RHI_Existing_Dwelling__Water_Heating"></a>Water-Heating

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive__RHI_Existing_Dwelling__Water_Heating`

- Documentation: *Water heating requirement.*
- Parent element: [`RHI-Existing-Dwelling`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive__RHI_Existing_Dwelling)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive__RHI_Existing_Dwelling__Impact_Of_Loft_Insulation"></a>Impact-Of-Loft-Insulation

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive__RHI_Existing_Dwelling__Impact_Of_Loft_Insulation`

- Documentation: *Reduction in space heating requirement with loft insulation (as negative value). Omit if not applicable*
- Parent element: [`RHI-Existing-Dwelling`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive__RHI_Existing_Dwelling)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive__RHI_Existing_Dwelling__Impact_Of_Cavity_Insulation"></a>Impact-Of-Cavity-Insulation

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive__RHI_Existing_Dwelling__Impact_Of_Cavity_Insulation`

- Documentation: *Reduction in space heating requirement with cavity insulation (as negative value). Omit if not applicable*
- Parent element: [`RHI-Existing-Dwelling`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive__RHI_Existing_Dwelling)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive__RHI_Existing_Dwelling__Impact_Of_Solid_Wall_Insulation"></a>Impact-Of-Solid-Wall-Insulation

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive__RHI_Existing_Dwelling__Impact_Of_Solid_Wall_Insulation`

- Documentation: *Reduction in space heating requirement with solid wall insulation (as negative value). Omit if not applicable*
- Parent element: [`RHI-Existing-Dwelling`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Renewable_Heat_Incentive__RHI_Existing_Dwelling)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Green_Deal_Package"></a>Green-Deal-Package

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Green_Deal_Package`

- Documentation: *Improvements that can form a Green Deal package*
- Parent element: [`Energy-Assessment`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Green_Deal_Package__Green_Deal_Improvement"></a>Green-Deal-Improvement

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Green_Deal_Package__Green_Deal_Improvement`

- Documentation: *Improvements from Suggested-Improvements in the Green Deal package*
- Parent element: [`Green-Deal-Package`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Green_Deal_Package)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Green_Deal_Package__Green_Deal_Improvement__Improvement_Type"></a>Improvement-Type

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Green_Deal_Package__Green_Deal_Improvement__Improvement_Type`

- Documentation: *None*
- Parent element: [`Green-Deal-Improvement`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Green_Deal_Package__Green_Deal_Improvement)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Green_Deal_Package__Green_Deal_Improvement__Improvement_Number"></a>Improvement-Number

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Green_Deal_Package__Green_Deal_Improvement__Improvement_Number`

- Documentation: *None*
- Parent element: [`Green-Deal-Improvement`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Green_Deal_Package__Green_Deal_Improvement)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Green_Deal_Package__Electricity_Saving"></a>Electricity-Saving

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Green_Deal_Package__Electricity_Saving`

- Documentation: *Total electricity saving for the package*
- Parent element: [`Green-Deal-Package`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Green_Deal_Package)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Green_Deal_Package__Gas_Saving"></a>Gas-Saving

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Green_Deal_Package__Gas_Saving`

- Documentation: *Total gas saving for the package*
- Parent element: [`Green-Deal-Package`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Green_Deal_Package)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Green_Deal_Package__Other_Fuel_Saving"></a>Other-Fuel-Saving

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Green_Deal_Package__Other_Fuel_Saving`

- Documentation: *Total other saving for the package*
- Parent element: [`Green-Deal-Package`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Green_Deal_Package)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements"></a>Alternative-Improvements

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements`

- Documentation: *Alternative improvements to some of those given in Suggested-Improvements*
- Parent element: [`Energy-Assessment`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement"></a>Improvement

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement`

- Documentation: *None*
- Parent element: [`Alternative-Improvements`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement__Sequence"></a>Sequence

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement__Sequence`

- Documentation: *Sequence of the Suggested Improvements within the set of Suggested Improvements. This is used to order the Recommendations on the output HCR / EPC so that the cumulative Ratings make sense. The Improved Energy Ratings that result from carrying out a Suggested Improvement are cumulative and assume that the improvements have been installed in the order they appear in the list. Hence they must be sequenced.*
- Parent element: [`Improvement`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement__Improvement_Category"></a>Improvement-Category

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement__Improvement_Category`

- Documentation: *The category of improvement. This identifies where on the report the recommendation is printed.*
- Parent element: [`Improvement`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement__Improvement_Type"></a>Improvement-Type

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement__Improvement_Type`

- Documentation: *Suggested work to be carried out on the Property to improve its energy efficiency. This should be a enumerated list of acceptable improvements but it hasn't yet been defined.*
- Parent element: [`Improvement`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement__Typical_Saving"></a>Typical-Saving

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement__Typical_Saving`

- Documentation: *Typical savings (in British Pounds) per year if the suggested improvement is carried out. 0 if not assessed*
- Parent element: [`Improvement`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement__Energy_Performance_Rating"></a>Energy-Performance-Rating

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement__Energy_Performance_Rating`

- Documentation: *The estimated Energy performance rating of the Property after the Suggested Improvement has been carried out providing any preceding Suggested Improvement has also been carried out. 0 if not assessed*
- Parent element: [`Improvement`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement__Environmental_Impact_Rating"></a>Environmental-Impact-Rating

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement__Environmental_Impact_Rating`

- Documentation: *The estimated Environmental Impact rating of the Property after the Suggested Improvement has been carried out providing any preceding Suggested Improvement has also been carried out. 0 if not assessed*
- Parent element: [`Improvement`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement__Improvement_Details"></a>Improvement-Details

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement__Improvement_Details`

- Documentation: *None*
- Parent element: [`Improvement`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement__Improvement_Details__Improvement_Texts"></a>Improvement-Texts

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement__Improvement_Details__Improvement_Texts`

- Documentation: *For backward compatability only*
- Parent element: [`Improvement-Details`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement__Improvement_Details)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement__Improvement_Details__Improvement_Texts__Improvement_Summary"></a>Improvement-Summary

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement__Improvement_Details__Improvement_Texts__Improvement_Summary`

- Documentation: *A short description of the suggested improvement.*
- Parent element: [`Improvement-Texts`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement__Improvement_Details__Improvement_Texts)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement__Improvement_Details__Improvement_Texts__Improvement_Heading"></a>Improvement-Heading

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement__Improvement_Details__Improvement_Texts__Improvement_Heading`

- Documentation: *Text to precede the improvement description. If this field is not provided the 'Improvement-Summary' is used instead.*
- Parent element: [`Improvement-Texts`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement__Improvement_Details__Improvement_Texts)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement__Improvement_Details__Improvement_Texts__Improvement_Description"></a>Improvement-Description

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement__Improvement_Details__Improvement_Texts__Improvement_Description`

- Documentation: *Detailed description of the suggested improvement.*
- Parent element: [`Improvement-Texts`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement__Improvement_Details__Improvement_Texts)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement__Improvement_Details__Improvement_Number"></a>Improvement-Number

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement__Improvement_Details__Improvement_Number`

- Documentation: *None*
- Parent element: [`Improvement-Details`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement__Improvement_Details)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement__Indicative_Cost"></a>Indicative-Cost

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement__Indicative_Cost`

- Documentation: *None*
- Parent element: [`Improvement`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement__Green_Deal_Category"></a>Green-Deal-Category

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement__Green_Deal_Category`

- Documentation: *None*
- Parent element: [`Improvement`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Alternative_Improvements__Improvement)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Addendum"></a>Addendum

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Addendum`

- Documentation: *None*
- Parent element: [`Energy-Assessment`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Addendum__Cavity_Fill_Recommended"></a>Cavity-Fill-Recommended

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Addendum__Cavity_Fill_Recommended`

- Documentation: *Cavity fill is recommended*
- Parent element: [`Addendum`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Addendum)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Addendum__Stone_Walls"></a>Stone-Walls

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Addendum__Stone_Walls`

- Documentation: *Stone walls present, not insulated*
- Parent element: [`Addendum`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Addendum)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Addendum__System_Build"></a>System-Build

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Addendum__System_Build`

- Documentation: *System build present*
- Parent element: [`Addendum`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Addendum)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Addendum__Access_Issues"></a>Access-Issues

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Addendum__Access_Issues`

- Documentation: *Dwelling has access issues for cavity wall insulation. Include only when at least one of Cavity-Fill-Recommended, Stone-Walls, System-Build is also present*
- Parent element: [`Addendum`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Addendum)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Addendum__High_Exposure"></a>High-Exposure

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Addendum__High_Exposure`

- Documentation: *Dwelling may be exposed to wind-driven rain. Include only when at least one of Cavity-Fill-Recommended, Stone-Walls, System-Build is also present*
- Parent element: [`Addendum`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Addendum)

## <a name="SAP_Compliance_Report__SAP_Report__Energy_Assessment__Addendum__Narrow_Cavities"></a>Narrow-Cavities

`SAP_Compliance_Report__SAP_Report__Energy_Assessment__Addendum__Narrow_Cavities`

- Documentation: *Dwelling may have narrow cavities. Include only when Cavity-Fill-Recommended is also present*
- Parent element: [`Addendum`](#SAP_Compliance_Report__SAP_Report__Energy_Assessment__Addendum)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data"></a>SAP10-Data

`SAP_Compliance_Report__SAP_Report__SAP10_Data`

- Documentation: *None*
- Parent element: [`SAP-Report`](#SAP_Compliance_Report__SAP_Report)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__Data_Type"></a>Data-Type

`SAP_Compliance_Report__SAP_Report__SAP10_Data__Data_Type`

- Documentation: *Type of SAP data that has been collected.*
- Parent element: [`SAP10-Data`](#SAP_Compliance_Report__SAP_Report__SAP10_Data)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details"></a>SAP-Property-Details

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details`

- Documentation: *None*
- Parent element: [`SAP10-Data`](#SAP_Compliance_Report__SAP_Report__SAP10_Data)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Property_Type"></a>Property-Type

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Property_Type`

- Documentation: *The type of Property, such as House, Flat, Mansion, Maisonette etc.*
- Parent element: [`SAP-Property-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Built_Form"></a>Built-Form

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Built_Form`

- Documentation: *The building type of the Property e.g. Detached, Semi-Detached, Terrace etc. Together with the Property Type, the Built Form provides a structured description of the property.*
- Parent element: [`SAP-Property-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Living_Area"></a>Living-Area

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Living_Area`

- Documentation: *The size of the living area in square metres. The living area is the room marked on a plan as the lounge or living room, or the largest public room (irrespective of usage by particular occupants), together with any rooms not separated from the lounge or living room by doors, and including any cupboards directly accessed from the lounge or living room. Living area does not, however, extend over more than one storey, even when stairs enter the living area directly.*
- Parent element: [`SAP-Property-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Lowest_Storey_Area"></a>Lowest-Storey-Area

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Lowest_Storey_Area`

- Documentation: *The Area of the lowest storey in square meters including unheated or communal areas such as garages or corridors.*
- Parent element: [`SAP-Property-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Orientation"></a>Orientation

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Orientation`

- Documentation: *The orientation of the front of the property.*
- Parent element: [`SAP-Property-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Conservatory_Type"></a>Conservatory-Type

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Conservatory_Type`

- Documentation: *Type of conservatory.*
- Parent element: [`SAP-Property-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Terrain_Type"></a>Terrain-Type

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Terrain_Type`

- Documentation: *Terrain type. Needed for wind-turbines and for applying measures.*
- Parent element: [`SAP-Property-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Has_Special_Feature"></a>Has-Special-Feature

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Has_Special_Feature`

- Documentation: *For backwards compatibility only, do not use.*
- Parent element: [`SAP-Property-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Special_Feature_Description"></a>Special-Feature-Description

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Special_Feature_Description`

- Documentation: *For backwards compatibility only, do not use.*
- Parent element: [`SAP-Property-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Energy_Saved_Or_Generated"></a>Energy-Saved-Or-Generated

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Energy_Saved_Or_Generated`

- Documentation: *For backwards compatibility only, do not use.*
- Parent element: [`SAP-Property-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Saved_Or_Generated_Fuel"></a>Saved-Or-Generated-Fuel

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Saved_Or_Generated_Fuel`

- Documentation: *For backwards compatibility only, do not use.*
- Parent element: [`SAP-Property-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Energy_Used"></a>Energy-Used

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Energy_Used`

- Documentation: *For backwards compatibility only, do not use.*
- Parent element: [`SAP-Property-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Energy_Used_Fuel"></a>Energy-Used-Fuel

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Energy_Used_Fuel`

- Documentation: *For backwards compatibility only, do not use.*
- Parent element: [`SAP-Property-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Is_In_Smoke_Control_Area"></a>Is-In-Smoke-Control-Area

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Is_In_Smoke_Control_Area`

- Documentation: *Is property in a smoke control area? Only if a solid fuel appliance is used.*
- Parent element: [`SAP-Property-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Cold_Water_Source"></a>Cold-Water-Source

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Cold_Water_Source`

- Documentation: *What is the cold water source? Either mains or header tank.*
- Parent element: [`SAP-Property-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Windows_Overshading"></a>Windows-Overshading

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Windows_Overshading`

- Documentation: *Average amount of overshading of windows.*
- Parent element: [`SAP-Property-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Thermal_Mass_Parameter"></a>Thermal-Mass-Parameter

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Thermal_Mass_Parameter`

- Documentation: *Average thermal mass parameter for the dwelling in kJ/m2K. If omitted it is calculated using the kappa values of each element.*
- Parent element: [`SAP-Property-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Additional_Allowable_Electricity_Generation"></a>Additional-Allowable-Electricity-Generation

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Additional_Allowable_Electricity_Generation`

- Documentation: *Additional allowable electricity generation applicable to this dwelling in kWh per square metre; only if Zero Carbon Home assessment.*
- Parent element: [`SAP-Property-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Gas_Smart_Meter_Present"></a>Gas-Smart-Meter-Present

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Gas_Smart_Meter_Present`

- Documentation: *None*
- Parent element: [`SAP-Property-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Electricity_Smart_Meter_Present"></a>Electricity-Smart-Meter-Present

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Electricity_Smart_Meter_Present`

- Documentation: *None*
- Parent element: [`SAP-Property-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Is_Dwelling_Export_Capable"></a>Is-Dwelling-Export-Capable

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Is_Dwelling_Export_Capable`

- Documentation: *None*
- Parent element: [`SAP-Property-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__PV_Connection"></a>PV-Connection

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__PV_Connection`

- Documentation: *None*
- Parent element: [`SAP-Property-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__PV_Diverter"></a>PV-Diverter

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__PV_Diverter`

- Documentation: *Diverter present.*
- Parent element: [`SAP-Property-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Battery_Capacity"></a>Battery-Capacity

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Battery_Capacity`

- Documentation: *Battery capacity if diverter present.*
- Parent element: [`SAP-Property-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Is_Wind_Turbine_Connected_To_Dwelling_Meter"></a>Is-Wind-Turbine-Connected-To-Dwelling-Meter

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Is_Wind_Turbine_Connected_To_Dwelling_Meter`

- Documentation: *Whether the wind turbine is connected to the Dwelling's meter.*
- Parent element: [`SAP-Property-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating"></a>SAP-Heating

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating`

- Documentation: *None*
- Parent element: [`SAP-Property-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Water_Heating_Code"></a>Water-Heating-Code

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Water_Heating_Code`

- Documentation: *The type of Water Heating present in the Property.*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Water_Fuel_Type"></a>Water-Fuel-Type

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Water_Fuel_Type`

- Documentation: *The type of fuel used to power the central heating e.g. Gas, Electricity. Not used if water system is main or secondary system.*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Has_Hot_Water_Cylinder"></a>Has-Hot-Water-Cylinder

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Has_Hot_Water_Cylinder`

- Documentation: *Hot water cylinder?*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Secondary_Heating_Category"></a>Secondary-Heating-Category

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Secondary_Heating_Category`

- Documentation: *Category of heating system for the secondary heating system.*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Secondary_Heating_Data_Source"></a>Secondary-Heating-Data-Source

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Secondary_Heating_Data_Source`

- Documentation: *Source of secondary heating system data; only if secondary heating system.*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Secondary_Heating_Efficiency"></a>Secondary-Heating-Efficiency

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Secondary_Heating_Efficiency`

- Documentation: *None*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Secondary_Heating_Commisioning_Certificate"></a>Secondary-Heating-Commisioning-Certificate

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Secondary_Heating_Commisioning_Certificate`

- Documentation: *Secondary heating system commisioning certificate number.*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Secondary_Heating_Installation_Engineer"></a>Secondary-Heating-Installation-Engineer

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Secondary_Heating_Installation_Engineer`

- Documentation: *Secondary heating installation engineer registration reference.*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Secondary_Heating_Code"></a>Secondary-Heating-Code

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Secondary_Heating_Code`

- Documentation: *Type of secondary heating present in the property; only if required and if heating data source is SAP table.*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Secondary_Fuel_Type"></a>Secondary-Fuel-Type

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Secondary_Fuel_Type`

- Documentation: *The type of fuel used to power the secondary heating e.g. Gas, Electricity; only if required.*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Secondary_Heating_PCDF_Fuel_Index"></a>Secondary-Heating-PCDF-Fuel-Index

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Secondary_Heating_PCDF_Fuel_Index`

- Documentation: *PCDF index number of the fuel type, only if Secondary-Fuel-Type is 99 (fuel from database).*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Secondary_Heating_Flue_Type"></a>Secondary-Heating-Flue-Type

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Secondary_Heating_Flue_Type`

- Documentation: *Secondary flue type; only if secondary efficiency is manufacturer declaration and if there is a flue.*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Thermal_Store"></a>Thermal-Store

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Thermal_Store`

- Documentation: *The type of thermal store; not used if main heating system is community heating scheme.*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Has_Fixed_Air_Conditioning"></a>Has-Fixed-Air-Conditioning

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Has_Fixed_Air_Conditioning`

- Documentation: *Fixed air conditioning?*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Immersion_Heating_Type"></a>Immersion-Heating-Type

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Immersion_Heating_Type`

- Documentation: *The type of immersion heating; only if immersion.*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Is_Heat_Pump_Assisted_By_Immersion"></a>Is-Heat-Pump-Assisted-By-Immersion

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Is_Heat_Pump_Assisted_By_Immersion`

- Documentation: *Is heat pump assisted by immersion? Applicable only to hot water only heat pumps*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Is_Heat_Pump_Installed_To_MIS"></a>Is-Heat-Pump-Installed-To-MIS

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Is_Heat_Pump_Installed_To_MIS`

- Documentation: *Is heat pump installed to MIS standard? Only if water heating from hot water only heat pump.*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Is_Immersion_For_Summer_Use"></a>Is-Immersion-For-Summer-Use

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Is_Immersion_For_Summer_Use`

- Documentation: *Immersion for summer use? Only if main heating is solid fuel fire or room heater with boiler.*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Is_Secondary_Heating_HETAS_Approved"></a>Is-Secondary-Heating-HETAS-Approved

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Is_Secondary_Heating_HETAS_Approved`

- Documentation: *Secondary heating appliance is HETAS approved? Only if solid fuel.*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Hot_Water_Store_Manufacturer"></a>Hot-Water-Store-Manufacturer

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Hot_Water_Store_Manufacturer`

- Documentation: *Store Manufacturer name.*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Hot_Water_Store_Model"></a>Hot-Water-Store-Model

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Hot_Water_Store_Model`

- Documentation: *Store Model name.*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Hot_Water_Store_Commissioning_Certificate"></a>Hot-Water-Store-Commissioning-Certificate

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Hot_Water_Store_Commissioning_Certificate`

- Documentation: *Store comissioning certificate number.*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Hot_Water_Store_Installer_Engineer_Registration"></a>Hot-Water-Store-Installer-Engineer-Registration

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Hot_Water_Store_Installer_Engineer_Registration`

- Documentation: *Store installer engineer registration number.*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Hot_Water_Store_Size"></a>Hot-Water-Store-Size

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Hot_Water_Store_Size`

- Documentation: *Hot water store size in litres; if there is a hot water store. Store refers to hot water store type which can be cylinder (if thermal store is "none"), hot-water only thermal store or integrated thermal store. Not applicable if (a) combi boiler whose data source database or (b) instantaneous combi boiler or (c) combi boiler from SAP table or (d) instantaneous water heater.*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Hot_Water_Store_Heat_Transfer_Area"></a>Hot-Water-Store-Heat-Transfer-Area

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Hot_Water_Store_Heat_Transfer_Area`

- Documentation: *Used when a heat pump is associated with a separate and specified hot water vessel.*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Hot_Water_Store_Heat_Loss_Source"></a>Hot-Water-Store-Heat-Loss-Source

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Hot_Water_Store_Heat_Loss_Source`

- Documentation: *The source of the hot water store heat loss information; if there is a hot water store. Not applicable if (a) combi boiler whose data source database or (b) instantaneous combi boiler or (c) combi boiler from SAP table or (d) instantaneous water heater.*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Hot_Water_Store_Heat_Loss"></a>Hot-Water-Store-Heat-Loss

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Hot_Water_Store_Heat_Loss`

- Documentation: *Hot water store declared loss in kWh/day; only if there is a hot water store and if manufacturer declared loss. Not applicable if (a) combi boiler whose data source database or (b) instantaneous combi boiler or (c) combi boiler from SAP table or (d) instantaneous water heater.*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Hot_Water_Store_Insulation_Type"></a>Hot-Water-Store-Insulation-Type

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Hot_Water_Store_Insulation_Type`

- Documentation: *Hot water store insulation; only if there is a hot water store and if loss from SAP table. Not applicable if (a) combi boiler whose data source database or (b) instantaneous combi boiler or (c) combi boiler from SAP table or (d) instantaneous water heater.*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Hot_Water_Store_Insulation_Thickness"></a>Hot-Water-Store-Insulation-Thickness

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Hot_Water_Store_Insulation_Thickness`

- Documentation: *Hot water store insulation thickness in mm; only if there is a hot water store and if loss from SAP table. Not applicable if (a) combi boiler whose data source database or (b) instantaneous combi boiler or (c) combi boiler from SAP table or (d) instantaneous water heater.*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Is_Thermal_Store_Near_Boiler"></a>Is-Thermal-Store-Near-Boiler

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Is_Thermal_Store_Near_Boiler`

- Documentation: *Thermal store connected to boiler by no more than 1.5 m of insulated pipework? Only if thermal store. Not applicable if combi boiler or instantaneous water heater.*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Is_Thermal_Store_Or_CPSU_In_Airing_Cupboard"></a>Is-Thermal-Store-Or-CPSU-In-Airing-Cupboard

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Is_Thermal_Store_Or_CPSU_In_Airing_Cupboard`

- Documentation: *Thermal store or CPSU in airing cupboard? Only if (a) boiler with integrated or hot-water-only thermal store, or (b) main heating is CPSU.*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Has_Cylinder_Thermostat"></a>Has-Cylinder-Thermostat

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Has_Cylinder_Thermostat`

- Documentation: *Hot water cylinder thermostat? Not applicable if combi boiler or instantaneous water heater.*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Is_Cylinder_In_Heated_Space"></a>Is-Cylinder-In-Heated-Space

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Is_Cylinder_In_Heated_Space`

- Documentation: *Hot water cylinder in heated space? Not applicable if combi boiler or instantaneous water heater.*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Is_Hot_Water_Separately_Timed"></a>Is-Hot-Water-Separately-Timed

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Is_Hot_Water_Separately_Timed`

- Documentation: *Hot water separately timed? Not applicable if combi boiler or instantaneous water heater.*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Hot_Water_Controls_Manufacturer"></a>Hot-Water-Controls-Manufacturer

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Hot_Water_Controls_Manufacturer`

- Documentation: *None*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Hot_Water_Controls_Model"></a>Hot-Water-Controls-Model

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Hot_Water_Controls_Model`

- Documentation: *None*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems"></a>SAP-Community-Heating-Systems

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems`

- Documentation: *None*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System"></a>SAP-Community-Heating-System

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System`

- Documentation: *None*
- Parent element: [`SAP-Community-Heating-Systems`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heating_Name"></a>Community-Heating-Name

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heating_Name`

- Documentation: *The name of the community heating system*
- Parent element: [`SAP-Community-Heating-System`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heating_CO2_Emission_Factor"></a>Community-Heating-CO2-Emission-Factor

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heating_CO2_Emission_Factor`

- Documentation: *the community heating CO2 emission factor*
- Parent element: [`SAP-Community-Heating-System`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heating_Primary_Energy_Factor"></a>Community-Heating-Primary-Energy-Factor

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heating_Primary_Energy_Factor`

- Documentation: *The community heating Primary Energy Factor*
- Parent element: [`SAP-Community-Heating-System`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heating_Use"></a>Community-Heating-Use

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heating_Use`

- Documentation: *Specifies what kind of heating the community system is used for.*
- Parent element: [`SAP-Community-Heating-System`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Is_Community_Heating_Cylinder_In_Dwelling"></a>Is-Community-Heating-Cylinder-In-Dwelling

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Is_Community_Heating_Cylinder_In_Dwelling`

- Documentation: *Community heating, cylinder in dwelling?*
- Parent element: [`SAP-Community-Heating-System`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Is_HIU_In_Dwelling"></a>Is-HIU-In-Dwelling

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Is_HIU_In_Dwelling`

- Documentation: *Community heating, HIU in dwelling?*
- Parent element: [`SAP-Community-Heating-System`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__HIU_Index_Number"></a>HIU-Index-Number

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__HIU_Index_Number`

- Documentation: *Heat Interface Unit index number, if present.*
- Parent element: [`SAP-Community-Heating-System`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heating_Distribution_Type"></a>Community-Heating-Distribution-Type

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heating_Distribution_Type`

- Documentation: *Community heating distribution*
- Parent element: [`SAP-Community-Heating-System`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heat_Sources"></a>Community-Heat-Sources

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heat_Sources`

- Documentation: *To be provided when there is no Heat-Network-Index-Number.*
- Parent element: [`SAP-Community-Heating-System`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heat_Sources__Community_Heat_Source"></a>Community-Heat-Source

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heat_Sources__Community_Heat_Source`

- Documentation: *None*
- Parent element: [`Community-Heat-Sources`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heat_Sources)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heat_Sources__Community_Heat_Source__Heat_Source_Type"></a>Heat-Source-Type

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heat_Sources__Community_Heat_Source__Heat_Source_Type`

- Documentation: *None*
- Parent element: [`Community-Heat-Source`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heat_Sources__Community_Heat_Source)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heat_Sources__Community_Heat_Source__Heat_Fraction"></a>Heat-Fraction

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heat_Sources__Community_Heat_Source__Heat_Fraction`

- Documentation: *Fraction of heat for the system provided by this heat source.*
- Parent element: [`Community-Heat-Source`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heat_Sources__Community_Heat_Source)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heat_Sources__Community_Heat_Source__Fuel_Type"></a>Fuel-Type

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heat_Sources__Community_Heat_Source__Fuel_Type`

- Documentation: *None*
- Parent element: [`Community-Heat-Source`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heat_Sources__Community_Heat_Source)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heat_Sources__Community_Heat_Source__PCDF_Fuel_Index"></a>PCDF-Fuel-Index

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heat_Sources__Community_Heat_Source__PCDF_Fuel_Index`

- Documentation: *None*
- Parent element: [`Community-Heat-Source`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heat_Sources__Community_Heat_Source)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heat_Sources__Community_Heat_Source__Heat_Efficiency"></a>Heat-Efficiency

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heat_Sources__Community_Heat_Source__Heat_Efficiency`

- Documentation: *Heat efficiency in %.*
- Parent element: [`Community-Heat-Source`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heat_Sources__Community_Heat_Source)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heat_Sources__Community_Heat_Source__Power_Efficiency"></a>Power-Efficiency

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heat_Sources__Community_Heat_Source__Power_Efficiency`

- Documentation: *Power efficiency in %. Include when heat source is CHP.*
- Parent element: [`Community-Heat-Source`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heat_Sources__Community_Heat_Source)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heat_Sources__Community_Heat_Source__Description"></a>Description

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heat_Sources__Community_Heat_Source__Description`

- Documentation: *None*
- Parent element: [`Community-Heat-Source`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heat_Sources__Community_Heat_Source)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heat_Sources__Community_Heat_Source__CHP_Electricity_Generation"></a>CHP-Electricity-Generation

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heat_Sources__Community_Heat_Source__CHP_Electricity_Generation`

- Documentation: *CHP Electricity generation options from table 12f.*
- Parent element: [`Community-Heat-Source`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heat_Sources__Community_Heat_Source)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heating_Distribution_Loss_Factor"></a>Community-Heating-Distribution-Loss-Factor

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Community_Heating_Distribution_Loss_Factor`

- Documentation: *Used when Community-Heating-Distribution-Type is calculated.*
- Parent element: [`SAP-Community-Heating-System`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Charging_Linked_To_Heat_Use"></a>Charging-Linked-To-Heat-Use

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Charging_Linked_To_Heat_Use`

- Documentation: *Used for hot-water-only systems.*
- Parent element: [`SAP-Community-Heating-System`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Heat_Network_Index_Number"></a>Heat-Network-Index-Number

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Heat_Network_Index_Number`

- Documentation: *Index number of heat network, if applicable.*
- Parent element: [`SAP-Community-Heating-System`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Sub_Network_Name"></a>Sub-Network-Name

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Sub_Network_Name`

- Documentation: *The name by which the sub community heat network is known.*
- Parent element: [`SAP-Community-Heating-System`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Heat_Network_Existing"></a>Heat-Network-Existing

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Heat_Network_Existing`

- Documentation: *Whether the heat network is existing or new.*
- Parent element: [`SAP-Community-Heating-System`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Heat_Network_Assessed_As_New"></a>Heat-Network-Assessed-As-New

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System__Heat_Network_Assessed_As_New`

- Documentation: *Whether the heat network is assessed as a new heat network (post June 2022) for Eng with a standalone gas boiler notional building.*
- Parent element: [`SAP-Community-Heating-System`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Community_Heating_Systems__SAP_Community_Heating_System)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details"></a>Main-Heating-Details

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details`

- Documentation: *None*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating"></a>Main-Heating

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating`

- Documentation: *None*
- Parent element: [`Main-Heating-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Number"></a>Main-Heating-Number

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Number`

- Documentation: *Identifies the main heating as system 1 or system 2. System 1 must always be present, system 2 is included only when there are two systems.*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Category"></a>Main-Heating-Category

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Category`

- Documentation: *Category of heating system for the main heating system.*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Data_Source"></a>Main-Heating-Data-Source

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Data_Source`

- Documentation: *Source of main heating system data.*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Index_Number"></a>Main-Heating-Index-Number

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Index_Number`

- Documentation: *The ID of the heating system from the product database, if system from database.*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Manufacturer"></a>Main-Heating-Manufacturer

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Manufacturer`

- Documentation: *None*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Model"></a>Main-Heating-Model

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Model`

- Documentation: *None*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Commissioning_Certificate"></a>Main-Heating-Commissioning-Certificate

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Commissioning_Certificate`

- Documentation: *None*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Installation_Engineer"></a>Main-Heating-Installation-Engineer

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Installation_Engineer`

- Documentation: *Main heating installation engineer registration reference.*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Is_Condensing_Boiler"></a>Is-Condensing-Boiler

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Is_Condensing_Boiler`

- Documentation: *Is the boiler a condensing boiler? If boiler efficiency is manufacturer declaration.*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Condensing_Boiler_Heat_Distribution"></a>Condensing-Boiler-Heat-Distribution

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Condensing_Boiler_Heat_Distribution`

- Documentation: *The temperature distribution of the condensing boiler.*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Heat_Pump_Heat_Distribution"></a>Heat-Pump-Heat-Distribution

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Heat_Pump_Heat_Distribution`

- Documentation: *The temperature distribution of the heat pump, for wet systems only.*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Gas_Or_Oil_Boiler_Type"></a>Gas-Or-Oil-Boiler-Type

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Gas_Or_Oil_Boiler_Type`

- Documentation: *Boiler type; if boiler efficiency is manufacturer declaration and fuel is gas or oil.*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Combi_Boiler_Type"></a>Combi-Boiler-Type

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Combi_Boiler_Type`

- Documentation: *Combi boiler type; if it is a combi boiler and boiler efficiency is manufacturer declaration.*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Case_Heat_Emission"></a>Case-Heat-Emission

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Case_Heat_Emission`

- Documentation: *Case heat emission at full load in kW; if it is a range cooker boiler and boiler efficiency is manufacturer declaration.*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Heat_Transfer_To_Water"></a>Heat-Transfer-To-Water

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Heat_Transfer_To_Water`

- Documentation: *Heat transfer to water at full load in kW; if it is a range cooker boiler and boiler efficiency is manufacturer declaration.*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Solid_Fuel_Boiler_Type"></a>Solid-Fuel-Boiler-Type

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Solid_Fuel_Boiler_Type`

- Documentation: *Boiler type; if boiler efficiency is manufacturer declaration and fuel is solid.*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Code"></a>Main-Heating-Code

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Code`

- Documentation: *Main heating code; when heating data source is SAP table.*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Fuel_Type"></a>Main-Fuel-Type

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Fuel_Type`

- Documentation: *The type of fuel used to power the central heating e.g. Gas, Electricity; not used if main heating system is community heating scheme.*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__PCDF_Fuel_Index"></a>PCDF-Fuel-Index

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__PCDF_Fuel_Index`

- Documentation: *PCDF index number of the fuel type, only if Main-Fuel-Type is 99 (fuel from database).*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Control"></a>Main-Heating-Control

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Control`

- Documentation: *Type of Main Control for the Heating System.*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Heat_Emitter_Type"></a>Heat-Emitter-Type

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Heat_Emitter_Type`

- Documentation: *Identifies the means by which the central heating system (if present) emits heat; only when wet system (radiators or underfloor).*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Underfloor_Heat_Emitter_Type"></a>Underfloor-Heat-Emitter-Type

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Underfloor_Heat_Emitter_Type`

- Documentation: *Means by which an underfloor heating system (if present) emits heat; only when wet system (underfloor).*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Flue_Type"></a>Main-Heating-Flue-Type

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Flue_Type`

- Documentation: *The type of main heating flue; only if flued appliance.*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Is_Flue_Fan_Present"></a>Is-Flue-Fan-Present

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Is_Flue_Fan_Present`

- Documentation: *Indicates whether the heating system contains a fan flue; only if boiler.*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Is_Central_Heating_Pump_In_Heated_Space"></a>Is-Central-Heating-Pump-In-Heated-Space

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Is_Central_Heating_Pump_In_Heated_Space`

- Documentation: *Central heating pump in heated space? Only when wet system (radiators or underfloor).*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Is_Oil_Pump_In_Heated_Space"></a>Is-Oil-Pump-In-Heated-Space

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Is_Oil_Pump_In_Heated_Space`

- Documentation: *Oil pump in heated space? Only if oil boiler.*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Is_Interlocked_System"></a>Is-Interlocked-System

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Is_Interlocked_System`

- Documentation: *Interlocked system? Only when wet system (radiators or underfloor).*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Has_Separate_Delayed_Start"></a>Has-Separate-Delayed-Start

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Has_Separate_Delayed_Start`

- Documentation: *True if there is a delayed start control separate from a controller in the database.*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Boiler_Fuel_Feed"></a>Boiler-Fuel-Feed

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Boiler_Fuel_Feed`

- Documentation: *The type of boiler fuel feed; only if solid fuel boiler with manufacturer declaration.*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Is_Main_Heating_HETAS_Approved"></a>Is-Main-Heating-HETAS-Approved

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Is_Main_Heating_HETAS_Approved`

- Documentation: *Main heating appliance is HETAS approved? Only if solid fuel.*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Electric_CPSU_Operating_Temperature"></a>Electric-CPSU-Operating-Temperature

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Electric_CPSU_Operating_Temperature`

- Documentation: *Electric CPSU operating temperature in Celcius; only if main heating is electric CPSU.*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Fraction"></a>Main-Heating-Fraction

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Fraction`

- Documentation: *Fraction of main heating provided by this system, is 1 if only one main system.*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Burner_Control"></a>Burner-Control

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Burner_Control`

- Documentation: *None*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Efficiency_Type"></a>Efficiency-Type

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Efficiency_Type`

- Documentation: *None*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Efficiency_Winter"></a>Main-Heating-Efficiency-Winter

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Efficiency_Winter`

- Documentation: *To be used if main heating data is manufacturer declaration and Efficiency-Type is winter and summer.*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Efficiency_Summer"></a>Main-Heating-Efficiency-Summer

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Efficiency_Summer`

- Documentation: *To be used if main heating data is manufacturer declaration and Efficiency-Type is winter and summer.*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Efficiency"></a>Main-Heating-Efficiency

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Efficiency`

- Documentation: *If main heating is any system other than heat network.*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_System_Type"></a>Main-Heating-System-Type

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_System_Type`

- Documentation: *Main heating system type or technology, for e.g., combi boiler, air source heat pump, etc.*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Has_FGHRS"></a>Has-FGHRS

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Has_FGHRS`

- Documentation: *Flue Gas Heat Recovery System.*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Index_Number"></a>FGHRS-Index-Number

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Index_Number`

- Documentation: *FGHRS index number; only if FGHRS.*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source"></a>FGHRS-Energy-Source

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source`

- Documentation: *None*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__PV_Arrays"></a>PV-Arrays

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__PV_Arrays`

- Documentation: *None*
- Parent element: [`FGHRS-Energy-Source`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__PV_Arrays__PV_Array"></a>PV-Array

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__PV_Arrays__PV_Array`

- Documentation: *None*
- Parent element: [`PV-Arrays`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__PV_Arrays)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__PV_Arrays__PV_Array__Peak_Power"></a>Peak-Power

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__PV_Arrays__PV_Array__Peak_Power`

- Documentation: *Peak kW of photovoltaics (PVs) (kWp); 0.0 if none.*
- Parent element: [`PV-Array`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__PV_Arrays__PV_Array)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__PV_Arrays__PV_Array__Orientation"></a>Orientation

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__PV_Arrays__PV_Array__Orientation`

- Documentation: *PV orientation; only if peak kWp > 0.*
- Parent element: [`PV-Array`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__PV_Arrays__PV_Array)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__PV_Arrays__PV_Array__Pitch"></a>Pitch

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__PV_Arrays__PV_Array__Pitch`

- Documentation: *PV pitch; only if peak kWp > 0.*
- Parent element: [`PV-Array`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__PV_Arrays__PV_Array)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__PV_Arrays__PV_Array__Overshading"></a>Overshading

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__PV_Arrays__PV_Array__Overshading`

- Documentation: *PV overshading; only if peak kWp > 0 and no MCS certificate.*
- Parent element: [`PV-Array`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__PV_Arrays__PV_Array)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__PV_Arrays__PV_Array__MCS_Certificate"></a>MCS-Certificate

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__PV_Arrays__PV_Array__MCS_Certificate`

- Documentation: *Does the installation have a MCS certificate.*
- Parent element: [`PV-Array`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__PV_Arrays__PV_Array)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__PV_Arrays__PV_Array__MCS_Certificate_Reference"></a>MCS-Certificate-Reference

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__PV_Arrays__PV_Array__MCS_Certificate_Reference`

- Documentation: *MCS certificate reference number*
- Parent element: [`PV-Array`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__PV_Arrays__PV_Array)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__PV_Arrays__PV_Array__PV_Panel_Manufacturer_Name"></a>PV-Panel-Manufacturer-Name

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__PV_Arrays__PV_Array__PV_Panel_Manufacturer_Name`

- Documentation: *Manufacturer of PV panels*
- Parent element: [`PV-Array`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__PV_Arrays__PV_Array)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__PV_Arrays__PV_Array__Overshading_MCS"></a>Overshading-MCS

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__PV_Arrays__PV_Array__Overshading_MCS`

- Documentation: *Overshading factor calculated according to MCS.*
- Parent element: [`PV-Array`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__PV_Arrays__PV_Array)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__Wind_Turbines"></a>Wind-Turbines

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__Wind_Turbines`

- Documentation: *None*
- Parent element: [`FGHRS-Energy-Source`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__Wind_Turbines__Wind_Turbine"></a>Wind-Turbine

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__Wind_Turbines__Wind_Turbine`

- Documentation: *None*
- Parent element: [`Wind-Turbines`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__Wind_Turbines)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__Wind_Turbines__Wind_Turbine__Wind_Turbine_Manufacturer_Name"></a>Wind-Turbine-Manufacturer-Name

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__Wind_Turbines__Wind_Turbine__Wind_Turbine_Manufacturer_Name`

- Documentation: *Wind turbine manufacturer name.*
- Parent element: [`Wind-Turbine`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__Wind_Turbines__Wind_Turbine)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__Wind_Turbines__Wind_Turbine__Wind_Turbine_Certificate"></a>Wind-Turbine-Certificate

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__Wind_Turbines__Wind_Turbine__Wind_Turbine_Certificate`

- Documentation: *Wind turbine certificate.*
- Parent element: [`Wind-Turbine`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__Wind_Turbines__Wind_Turbine)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__Wind_Turbines__Wind_Turbine__Wind_Turbine_Rotor_Diameter"></a>Wind-Turbine-Rotor-Diameter

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__Wind_Turbines__Wind_Turbine__Wind_Turbine_Rotor_Diameter`

- Documentation: *Wind turbine rotor diameter in metres; only if wind turbine.*
- Parent element: [`Wind-Turbine`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__Wind_Turbines__Wind_Turbine)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__Wind_Turbines__Wind_Turbine__Wind_Turbine_Hub_Height"></a>Wind-Turbine-Hub-Height

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__Wind_Turbines__Wind_Turbine__Wind_Turbine_Hub_Height`

- Documentation: *Wind turbine hub height above building in metres; only if wind turbine.*
- Parent element: [`Wind-Turbine`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__Wind_Turbines__Wind_Turbine)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__Electricity_Tariff"></a>Electricity-Tariff

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__Electricity_Tariff`

- Documentation: *Type of electricity tariff.*
- Parent element: [`FGHRS-Energy-Source`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__Hydro_Electric_Generation"></a>Hydro-Electric-Generation

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__Hydro_Electric_Generation`

- Documentation: *Electricity generated by hydro-electric generator, in kWh/year. To be provided if Hydro-Electric-Generation-Month is not provided.*
- Parent element: [`FGHRS-Energy-Source`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__Hydro_Electric_Certificate"></a>Hydro-Electric-Certificate

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__Hydro_Electric_Certificate`

- Documentation: *Reference to certification of hydro electric output.*
- Parent element: [`FGHRS-Energy-Source`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__Hydro_Electric_Generation_Months"></a>Hydro-Electric-Generation-Months

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__Hydro_Electric_Generation_Months`

- Documentation: *Electricity generated by hydro-electric generator, in kWh/month. To be provided if Hydro-Electric-Generation is not provided.*
- Parent element: [`FGHRS-Energy-Source`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__Hydro_Electric_Generation_Months__Hydro_Electric_Generation_Month"></a>Hydro-Electric-Generation-Month

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__Hydro_Electric_Generation_Months__Hydro_Electric_Generation_Month`

- Documentation: *None*
- Parent element: [`Hydro-Electric-Generation-Months`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__Hydro_Electric_Generation_Months)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__Hydro_Electric_Generation_Months__Hydro_Electric_Generation_Month__Hydro_Month"></a>Hydro-Month

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__Hydro_Electric_Generation_Months__Hydro_Electric_Generation_Month__Hydro_Month`

- Documentation: *None*
- Parent element: [`Hydro-Electric-Generation-Month`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__Hydro_Electric_Generation_Months__Hydro_Electric_Generation_Month)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__Hydro_Electric_Generation_Months__Hydro_Electric_Generation_Month__Hydro_Value"></a>Hydro-Value

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__Hydro_Electric_Generation_Months__Hydro_Electric_Generation_Month__Hydro_Value`

- Documentation: *Hydro electricity in kWh in month.*
- Parent element: [`Hydro-Electric-Generation-Month`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__Hydro_Electric_Generation_Months__Hydro_Electric_Generation_Month)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__Is_Hydro_Output_Connected_To_Dwelling_Meter"></a>Is-Hydro-Output-Connected-To-Dwelling-Meter

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source__Is_Hydro_Output_Connected_To_Dwelling_Meter`

- Documentation: *Whether the hydro-electric station is connected to dwelling's electricity meter*
- Parent element: [`FGHRS-Energy-Source`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__FGHRS_Energy_Source)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Declared_Values"></a>Main-Heating-Declared-Values

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Declared_Values`

- Documentation: *None*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Declared_Values__Efficiency"></a>Efficiency

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Declared_Values__Efficiency`

- Documentation: *None*
- Parent element: [`Main-Heating-Declared-Values`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Declared_Values)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Declared_Values__Make_Model"></a>Make-Model

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Declared_Values__Make_Model`

- Documentation: *None*
- Parent element: [`Main-Heating-Declared-Values`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Declared_Values)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Declared_Values__Test_Method"></a>Test-Method

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Declared_Values__Test_Method`

- Documentation: *None*
- Parent element: [`Main-Heating-Declared-Values`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Main_Heating_Declared_Values)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Storage_Heaters"></a>Storage-Heaters

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Storage_Heaters`

- Documentation: *None*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Storage_Heaters__Storage_Heater"></a>Storage-Heater

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Storage_Heaters__Storage_Heater`

- Documentation: *None*
- Parent element: [`Storage-Heaters`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Storage_Heaters)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Storage_Heaters__Storage_Heater__Number_Of_Heaters"></a>Number-Of-Heaters

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Storage_Heaters__Storage_Heater__Number_Of_Heaters`

- Documentation: *The number of storage heaters with this index number.*
- Parent element: [`Storage-Heater`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Storage_Heaters__Storage_Heater)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Storage_Heaters__Storage_Heater__Index_Number"></a>Index-Number

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Storage_Heaters__Storage_Heater__Index_Number`

- Documentation: *The index number of the heater from the product database.*
- Parent element: [`Storage-Heater`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Storage_Heaters__Storage_Heater)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Storage_Heaters__Storage_Heater__High_Heat_Retention"></a>High-Heat-Retention

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Storage_Heaters__Storage_Heater__High_Heat_Retention`

- Documentation: *Whether heater is high heat retention type.*
- Parent element: [`Storage-Heater`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Storage_Heaters__Storage_Heater)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Emitter_Temperature"></a>Emitter-Temperature

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Emitter_Temperature`

- Documentation: *Gas and oil boilers and heat pump from database: 0, 1, 3 or 4 Other heat pump 0, 2 or 4. Other systems NA.*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__MCS_Installed_Heat_Pump"></a>MCS-Installed-Heat-Pump

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__MCS_Installed_Heat_Pump`

- Documentation: *Whether heat pump was installed under the Microgeneration Certification Scheme.*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Central_Heating_Pump_Age"></a>Central-Heating-Pump-Age

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Central_Heating_Pump_Age`

- Documentation: *Included for systems with a central heating pump, i.e. wet system.*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Control_Index_Number"></a>Control-Index-Number

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Control_Index_Number`

- Documentation: *The ID of the controller from the product database.*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Heating_Controller_Function"></a>Heating-Controller-Function

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Heating_Controller_Function`

- Documentation: *None*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Heating_Controller_Ecodesign_Class"></a>Heating-Controller-Ecodesign-Class

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Heating_Controller_Ecodesign_Class`

- Documentation: *None*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Heating_Controller_Manufacturer"></a>Heating-Controller-Manufacturer

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Heating_Controller_Manufacturer`

- Documentation: *None*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Heating_Controller_Model"></a>Heating-Controller-Model

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating__Heating_Controller_Model`

- Documentation: *None*
- Parent element: [`Main-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Details__Main_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Heating_Design_Water_Use"></a>SAP-Heating-Design-Water-Use

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__SAP_Heating_Design_Water_Use`

- Documentation: *None*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Systems_Interaction"></a>Main-Heating-Systems-Interaction

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Main_Heating_Systems_Interaction`

- Documentation: *None*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Secondary_Heating_Declared_Values"></a>Secondary-Heating-Declared-Values

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Secondary_Heating_Declared_Values`

- Documentation: *Use when manufacturer's declared values.*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Secondary_Heating_Declared_Values__Efficiency"></a>Efficiency

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Secondary_Heating_Declared_Values__Efficiency`

- Documentation: *None*
- Parent element: [`Secondary-Heating-Declared-Values`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Secondary_Heating_Declared_Values)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Secondary_Heating_Declared_Values__Make_Model"></a>Make-Model

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Secondary_Heating_Declared_Values__Make_Model`

- Documentation: *None*
- Parent element: [`Secondary-Heating-Declared-Values`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Secondary_Heating_Declared_Values)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Secondary_Heating_Declared_Values__Test_Method"></a>Test-Method

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Secondary_Heating_Declared_Values__Test_Method`

- Documentation: *None*
- Parent element: [`Secondary-Heating-Declared-Values`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Secondary_Heating_Declared_Values)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Primary_Pipework_Insulation"></a>Primary-Pipework-Insulation

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Primary_Pipework_Insulation`

- Documentation: *Not applicable to combi boiler or instantaneous water heater.*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details"></a>Solar-Heating-Details

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details`

- Documentation: *None*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Solar_Heating_Collector_Manufacturer"></a>Solar-Heating-Collector-Manufacturer

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Solar_Heating_Collector_Manufacturer`

- Documentation: *Panel manufacturer*
- Parent element: [`Solar-Heating-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Solar_Heating_Certificate"></a>Solar-Heating-Certificate

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Solar_Heating_Certificate`

- Documentation: *Solar heating certificate*
- Parent element: [`Solar-Heating-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Solar_Panel_Aperture_Area"></a>Solar-Panel-Aperture-Area

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Solar_Panel_Aperture_Area`

- Documentation: *Panel aperture area in square metres.*
- Parent element: [`Solar-Heating-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Solar_Panel_Collector_Type"></a>Solar-Panel-Collector-Type

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Solar_Panel_Collector_Type`

- Documentation: *Type of solar panel collector.*
- Parent element: [`Solar-Heating-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Solar_Panel_Collector_Data_Source"></a>Solar-Panel-Collector-Data-Source

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Solar_Panel_Collector_Data_Source`

- Documentation: *Source of solar panel collector data.*
- Parent element: [`Solar-Heating-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Solar_Panel_Collector_Zero_Loss_Efficiency"></a>Solar-Panel-Collector-Zero-Loss-Efficiency

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Solar_Panel_Collector_Zero_Loss_Efficiency`

- Documentation: *Collector zero-loss efficiency; only if declared values.*
- Parent element: [`Solar-Heating-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Solar_Panel_Collector_Heat_Loss_Rate"></a>Solar-Panel-Collector-Heat-Loss-Rate

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Solar_Panel_Collector_Heat_Loss_Rate`

- Documentation: *Collector heat loss rate; for backward compatibility only, do not use.*
- Parent element: [`Solar-Heating-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Solar_Panel_Collector_Linear_Heat_Loss_Coefficient"></a>Solar-Panel-Collector-Linear-Heat-Loss-Coefficient

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Solar_Panel_Collector_Linear_Heat_Loss_Coefficient`

- Documentation: *Collector linear heat loss coefficient; only if declared values.*
- Parent element: [`Solar-Heating-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Solar_Panel_Collector_Second_Order_Heat_Loss_Coefficient"></a>Solar-Panel-Collector-Second-Order-Heat-Loss-Coefficient

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Solar_Panel_Collector_Second_Order_Heat_Loss_Coefficient`

- Documentation: *Collector 2nd order heat loss coefficient; only if declared values.*
- Parent element: [`Solar-Heating-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Solar_Panel_Collector_Orientation"></a>Solar-Panel-Collector-Orientation

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Solar_Panel_Collector_Orientation`

- Documentation: *Collector orientation.*
- Parent element: [`Solar-Heating-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Solar_Panel_Collector_Pitch"></a>Solar-Panel-Collector-Pitch

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Solar_Panel_Collector_Pitch`

- Documentation: *None*
- Parent element: [`Solar-Heating-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Solar_Panel_Collector_Overshading"></a>Solar-Panel-Collector-Overshading

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Solar_Panel_Collector_Overshading`

- Documentation: *None*
- Parent element: [`Solar-Heating-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Has_Solar_Powered_Pump"></a>Has-Solar-Powered-Pump

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Has_Solar_Powered_Pump`

- Documentation: *None*
- Parent element: [`Solar-Heating-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Is_Solar_Store_Combined_Cylinder"></a>Is-Solar-Store-Combined-Cylinder

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Is_Solar_Store_Combined_Cylinder`

- Documentation: *None*
- Parent element: [`Solar-Heating-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Solar_Store_Volume"></a>Solar-Store-Volume

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Solar_Store_Volume`

- Documentation: *Dedicated solar store volume in litres.*
- Parent element: [`Solar-Heating-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Collector_Loop_Efficiency"></a>Collector-Loop-Efficiency

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Collector_Loop_Efficiency`

- Documentation: *Collector loop efficiency; only if declared values.*
- Parent element: [`Solar-Heating-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Incidence_Angle_Modifier"></a>Incidence-Angle-Modifier

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Incidence_Angle_Modifier`

- Documentation: *Incidence angle modifier; only if declared values.*
- Parent element: [`Solar-Heating-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Is_Community_Solar"></a>Is-Community-Solar

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Is_Community_Solar`

- Documentation: *None*
- Parent element: [`Solar-Heating-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Service_Provision"></a>Service-Provision

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Service_Provision`

- Documentation: *None*
- Parent element: [`Solar-Heating-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Overall_Heat_Loss"></a>Overall-Heat-Loss

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details__Overall_Heat_Loss`

- Documentation: *Overall heat loss coefficient of system; only if declared values.*
- Parent element: [`Solar-Heating-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Solar_Heating_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Instantaneous_WWHRS"></a>Instantaneous-WWHRS

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Instantaneous_WWHRS`

- Documentation: *Waste Water Heat Recovery System.*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Instantaneous_WWHRS__WWHRS_Index_Number1"></a>WWHRS-Index-Number1

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Instantaneous_WWHRS__WWHRS_Index_Number1`

- Documentation: *None*
- Parent element: [`Instantaneous-WWHRS`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Instantaneous_WWHRS)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Instantaneous_WWHRS__WWHRS_Index_Number2"></a>WWHRS-Index-Number2

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Instantaneous_WWHRS__WWHRS_Index_Number2`

- Documentation: *Omit if no second system.*
- Parent element: [`Instantaneous-WWHRS`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Instantaneous_WWHRS)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Instantaneous_WWHRS__WWHRS_Efficiency1"></a>WWHRS-Efficiency1

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Instantaneous_WWHRS__WWHRS_Efficiency1`

- Documentation: *None*
- Parent element: [`Instantaneous-WWHRS`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Instantaneous_WWHRS)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Instantaneous_WWHRS__WWHRS_Manufacturer1"></a>WWHRS-Manufacturer1

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Instantaneous_WWHRS__WWHRS_Manufacturer1`

- Documentation: *None*
- Parent element: [`Instantaneous-WWHRS`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Instantaneous_WWHRS)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Instantaneous_WWHRS__WWHRS_Model1"></a>WWHRS-Model1

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Instantaneous_WWHRS__WWHRS_Model1`

- Documentation: *None*
- Parent element: [`Instantaneous-WWHRS`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Instantaneous_WWHRS)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Instantaneous_WWHRS__WWHRS_Efficiency2"></a>WWHRS-Efficiency2

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Instantaneous_WWHRS__WWHRS_Efficiency2`

- Documentation: *None*
- Parent element: [`Instantaneous-WWHRS`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Instantaneous_WWHRS)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Instantaneous_WWHRS__WWHRS_Manufacturer2"></a>WWHRS-Manufacturer2

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Instantaneous_WWHRS__WWHRS_Manufacturer2`

- Documentation: *None*
- Parent element: [`Instantaneous-WWHRS`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Instantaneous_WWHRS)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Instantaneous_WWHRS__WWHRS_Model2"></a>WWHRS-Model2

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Instantaneous_WWHRS__WWHRS_Model2`

- Documentation: *None*
- Parent element: [`Instantaneous-WWHRS`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Instantaneous_WWHRS)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Storage_WWHRS"></a>Storage-WWHRS

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Storage_WWHRS`

- Documentation: *None*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Storage_WWHRS__WWHRS_Index_Number"></a>WWHRS-Index-Number

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Storage_WWHRS__WWHRS_Index_Number`

- Documentation: *None*
- Parent element: [`Storage-WWHRS`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Storage_WWHRS)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Storage_WWHRS__WWHRS_Store_Volume"></a>WWHRS-Store-Volume

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Storage_WWHRS__WWHRS_Store_Volume`

- Documentation: *Dedicated store volume in litres.*
- Parent element: [`Storage-WWHRS`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Storage_WWHRS)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Storage_WWHRS__Storage_WWHRS_Efficiency"></a>Storage-WWHRS-Efficiency

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Storage_WWHRS__Storage_WWHRS_Efficiency`

- Documentation: *None*
- Parent element: [`Storage-WWHRS`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Storage_WWHRS)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Storage_WWHRS__Storage_WWHRS_Manufacturer"></a>Storage-WWHRS-Manufacturer

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Storage_WWHRS__Storage_WWHRS_Manufacturer`

- Documentation: *None*
- Parent element: [`Storage-WWHRS`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Storage_WWHRS)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Storage_WWHRS__Storage_WWHRS_Model"></a>Storage-WWHRS-Model

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Storage_WWHRS__Storage_WWHRS_Model`

- Documentation: *None*
- Parent element: [`Storage-WWHRS`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Storage_WWHRS)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Shower_Outlets"></a>Shower-Outlets

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Shower_Outlets`

- Documentation: *None*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Shower_Outlets__Shower_Outlet"></a>Shower-Outlet

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Shower_Outlets__Shower_Outlet`

- Documentation: *None*
- Parent element: [`Shower-Outlets`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Shower_Outlets)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Shower_Outlets__Shower_Outlet__Shower_Outlet_Type"></a>Shower-Outlet-Type

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Shower_Outlets__Shower_Outlet__Shower_Outlet_Type`

- Documentation: *Hot water type for this shower outlet.*
- Parent element: [`Shower-Outlet`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Shower_Outlets__Shower_Outlet)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Shower_Outlets__Shower_Outlet__Shower_Flow_Rate"></a>Shower-Flow-Rate

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Shower_Outlets__Shower_Outlet__Shower_Flow_Rate`

- Documentation: *The flow rate. Only when a shower is not instantaneous electric. Leave blank if NO flow limiter fitted.*
- Parent element: [`Shower-Outlet`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Shower_Outlets__Shower_Outlet)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Shower_Outlets__Shower_Outlet__Shower_Power"></a>Shower-Power

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Shower_Outlets__Shower_Outlet__Shower_Power`

- Documentation: *The shower power, only if shower outlet type is instantaneous electric.*
- Parent element: [`Shower-Outlet`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Shower_Outlets__Shower_Outlet)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Shower_Outlets__Shower_Outlet__Shower_WWHRS"></a>Shower-WWHRS

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Shower_Outlets__Shower_Outlet__Shower_WWHRS`

- Documentation: *The WWHRS with which the shower is connected. If shower outlet type is instantaneous electric shower then only a storage WWHRS can be selected or none.*
- Parent element: [`Shower-Outlet`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Shower_Outlets__Shower_Outlet)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Number_Baths"></a>Number-Baths

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Number_Baths`

- Documentation: *None*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Number_Baths_WWHRS"></a>Number-Baths-WWHRS

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating__Number_Baths_WWHRS`

- Documentation: *None*
- Parent element: [`SAP-Heating`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Heating)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source"></a>SAP-Energy-Source

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source`

- Documentation: *None*
- Parent element: [`SAP-Property-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__PV_Arrays"></a>PV-Arrays

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__PV_Arrays`

- Documentation: *None*
- Parent element: [`SAP-Energy-Source`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__PV_Arrays__PV_Array"></a>PV-Array

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__PV_Arrays__PV_Array`

- Documentation: *None*
- Parent element: [`PV-Arrays`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__PV_Arrays)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__PV_Arrays__PV_Array__Peak_Power"></a>Peak-Power

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__PV_Arrays__PV_Array__Peak_Power`

- Documentation: *Peak kW of photovoltaics (PVs) (kWp); 0.0 if none.*
- Parent element: [`PV-Array`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__PV_Arrays__PV_Array)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__PV_Arrays__PV_Array__Orientation"></a>Orientation

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__PV_Arrays__PV_Array__Orientation`

- Documentation: *PV orientation; only if peak kWp > 0.*
- Parent element: [`PV-Array`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__PV_Arrays__PV_Array)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__PV_Arrays__PV_Array__Pitch"></a>Pitch

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__PV_Arrays__PV_Array__Pitch`

- Documentation: *PV pitch; only if peak kWp > 0.*
- Parent element: [`PV-Array`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__PV_Arrays__PV_Array)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__PV_Arrays__PV_Array__Overshading"></a>Overshading

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__PV_Arrays__PV_Array__Overshading`

- Documentation: *PV overshading; only if peak kWp > 0 and no MCS certificate.*
- Parent element: [`PV-Array`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__PV_Arrays__PV_Array)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__PV_Arrays__PV_Array__MCS_Certificate"></a>MCS-Certificate

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__PV_Arrays__PV_Array__MCS_Certificate`

- Documentation: *Does the installation have a MCS certificate.*
- Parent element: [`PV-Array`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__PV_Arrays__PV_Array)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__PV_Arrays__PV_Array__MCS_Certificate_Reference"></a>MCS-Certificate-Reference

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__PV_Arrays__PV_Array__MCS_Certificate_Reference`

- Documentation: *MCS certificate reference number*
- Parent element: [`PV-Array`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__PV_Arrays__PV_Array)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__PV_Arrays__PV_Array__PV_Panel_Manufacturer_Name"></a>PV-Panel-Manufacturer-Name

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__PV_Arrays__PV_Array__PV_Panel_Manufacturer_Name`

- Documentation: *Manufacturer of PV panels*
- Parent element: [`PV-Array`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__PV_Arrays__PV_Array)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__PV_Arrays__PV_Array__Overshading_MCS"></a>Overshading-MCS

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__PV_Arrays__PV_Array__Overshading_MCS`

- Documentation: *Overshading factor calculated according to MCS.*
- Parent element: [`PV-Array`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__PV_Arrays__PV_Array)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__Wind_Turbines"></a>Wind-Turbines

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__Wind_Turbines`

- Documentation: *None*
- Parent element: [`SAP-Energy-Source`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__Wind_Turbines__Wind_Turbine"></a>Wind-Turbine

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__Wind_Turbines__Wind_Turbine`

- Documentation: *None*
- Parent element: [`Wind-Turbines`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__Wind_Turbines)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__Wind_Turbines__Wind_Turbine__Wind_Turbine_Manufacturer_Name"></a>Wind-Turbine-Manufacturer-Name

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__Wind_Turbines__Wind_Turbine__Wind_Turbine_Manufacturer_Name`

- Documentation: *Wind turbine manufacturer name.*
- Parent element: [`Wind-Turbine`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__Wind_Turbines__Wind_Turbine)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__Wind_Turbines__Wind_Turbine__Wind_Turbine_Certificate"></a>Wind-Turbine-Certificate

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__Wind_Turbines__Wind_Turbine__Wind_Turbine_Certificate`

- Documentation: *Wind turbine certificate.*
- Parent element: [`Wind-Turbine`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__Wind_Turbines__Wind_Turbine)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__Wind_Turbines__Wind_Turbine__Wind_Turbine_Rotor_Diameter"></a>Wind-Turbine-Rotor-Diameter

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__Wind_Turbines__Wind_Turbine__Wind_Turbine_Rotor_Diameter`

- Documentation: *Wind turbine rotor diameter in metres; only if wind turbine.*
- Parent element: [`Wind-Turbine`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__Wind_Turbines__Wind_Turbine)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__Wind_Turbines__Wind_Turbine__Wind_Turbine_Hub_Height"></a>Wind-Turbine-Hub-Height

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__Wind_Turbines__Wind_Turbine__Wind_Turbine_Hub_Height`

- Documentation: *Wind turbine hub height above building in metres; only if wind turbine.*
- Parent element: [`Wind-Turbine`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__Wind_Turbines__Wind_Turbine)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__Electricity_Tariff"></a>Electricity-Tariff

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__Electricity_Tariff`

- Documentation: *Type of electricity tariff.*
- Parent element: [`SAP-Energy-Source`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__Hydro_Electric_Generation"></a>Hydro-Electric-Generation

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__Hydro_Electric_Generation`

- Documentation: *Electricity generated by hydro-electric generator, in kWh/year. To be provided if Hydro-Electric-Generation-Month is not provided.*
- Parent element: [`SAP-Energy-Source`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__Hydro_Electric_Certificate"></a>Hydro-Electric-Certificate

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__Hydro_Electric_Certificate`

- Documentation: *Reference to certification of hydro electric output.*
- Parent element: [`SAP-Energy-Source`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__Hydro_Electric_Generation_Months"></a>Hydro-Electric-Generation-Months

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__Hydro_Electric_Generation_Months`

- Documentation: *Electricity generated by hydro-electric generator, in kWh/month. To be provided if Hydro-Electric-Generation is not provided.*
- Parent element: [`SAP-Energy-Source`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__Hydro_Electric_Generation_Months__Hydro_Electric_Generation_Month"></a>Hydro-Electric-Generation-Month

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__Hydro_Electric_Generation_Months__Hydro_Electric_Generation_Month`

- Documentation: *None*
- Parent element: [`Hydro-Electric-Generation-Months`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__Hydro_Electric_Generation_Months)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__Hydro_Electric_Generation_Months__Hydro_Electric_Generation_Month__Hydro_Month"></a>Hydro-Month

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__Hydro_Electric_Generation_Months__Hydro_Electric_Generation_Month__Hydro_Month`

- Documentation: *None*
- Parent element: [`Hydro-Electric-Generation-Month`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__Hydro_Electric_Generation_Months__Hydro_Electric_Generation_Month)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__Hydro_Electric_Generation_Months__Hydro_Electric_Generation_Month__Hydro_Value"></a>Hydro-Value

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__Hydro_Electric_Generation_Months__Hydro_Electric_Generation_Month__Hydro_Value`

- Documentation: *Hydro electricity in kWh in month.*
- Parent element: [`Hydro-Electric-Generation-Month`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__Hydro_Electric_Generation_Months__Hydro_Electric_Generation_Month)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__Is_Hydro_Output_Connected_To_Dwelling_Meter"></a>Is-Hydro-Output-Connected-To-Dwelling-Meter

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source__Is_Hydro_Output_Connected_To_Dwelling_Meter`

- Documentation: *Whether the hydro-electric station is connected to dwelling's electricity meter*
- Parent element: [`SAP-Energy-Source`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Energy_Source)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts"></a>SAP-Building-Parts

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts`

- Documentation: *None*
- Parent element: [`SAP-Property-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part"></a>SAP-Building-Part

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part`

- Documentation: *None*
- Parent element: [`SAP-Building-Parts`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__Building_Part_Number"></a>Building-Part-Number

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__Building_Part_Number`

- Documentation: *An integer value which uniquely identifies the building part in the property. The value "1" must be assigned to the main dwelling.*
- Parent element: [`SAP-Building-Part`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__Identifier"></a>Identifier

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__Identifier`

- Documentation: *Identifier for the Building part - generally only required if there are more that one Building Parts of the same type e.g. "West Wing" and "East Wing" Extensions*
- Parent element: [`SAP-Building-Part`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__Construction_Year"></a>Construction-Year

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__Construction_Year`

- Documentation: *The year when this building part was constructed. Not used if 'Construction-Age-Band' is used.*
- Parent element: [`SAP-Building-Part`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__Construction_Age_Band"></a>Construction-Age-Band

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__Construction_Age_Band`

- Documentation: *The age band when this building part was constructed. Not used if 'Construction-Year' is used.*
- Parent element: [`SAP-Building-Part`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Openings"></a>SAP-Openings

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Openings`

- Documentation: *None*
- Parent element: [`SAP-Building-Part`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Openings__SAP_Opening"></a>SAP-Opening

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Openings__SAP_Opening`

- Documentation: *None*
- Parent element: [`SAP-Openings`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Openings)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Openings__SAP_Opening__Name"></a>Name

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Openings__SAP_Opening__Name`

- Documentation: *Unique name which identifies this opening. Can be just a number, e.g. "1". However, an opening cannot have the same name as a wall.*
- Parent element: [`SAP-Opening`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Openings__SAP_Opening)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Openings__SAP_Opening__Type"></a>Type

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Openings__SAP_Opening__Type`

- Documentation: *The name of the SAP-Opening-Type for this opening.*
- Parent element: [`SAP-Opening`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Openings__SAP_Opening)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Openings__SAP_Opening__Location"></a>Location

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Openings__SAP_Opening__Location`

- Documentation: *Name of the wall or roof which contains the opening.*
- Parent element: [`SAP-Opening`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Openings__SAP_Opening)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Openings__SAP_Opening__Orientation"></a>Orientation

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Openings__SAP_Opening__Orientation`

- Documentation: *Compass direction in which the opening faces.*
- Parent element: [`SAP-Opening`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Openings__SAP_Opening)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Openings__SAP_Opening__Width"></a>Width

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Openings__SAP_Opening__Width`

- Documentation: *The width of the opening in metres. If the Width field is used to record the opening area, set the Height to 1.*
- Parent element: [`SAP-Opening`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Openings__SAP_Opening)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Openings__SAP_Opening__Height"></a>Height

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Openings__SAP_Opening__Height`

- Documentation: *The height of the opening in metres. If the Height field is used to record the opening area, set the Width to 1.*
- Parent element: [`SAP-Opening`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Openings__SAP_Opening)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Openings__SAP_Opening__Pitch"></a>Pitch

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Openings__SAP_Opening__Pitch`

- Documentation: *Pitch of roof containing roof window.*
- Parent element: [`SAP-Opening`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Openings__SAP_Opening)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Roofs"></a>SAP-Roofs

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Roofs`

- Documentation: *None*
- Parent element: [`SAP-Building-Part`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Roofs__SAP_Roof"></a>SAP-Roof

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Roofs__SAP_Roof`

- Documentation: *None*
- Parent element: [`SAP-Roofs`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Roofs)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Roofs__SAP_Roof__Name"></a>Name

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Roofs__SAP_Roof__Name`

- Documentation: *Unique name which identifies this roof. Can be just a number, e.g. "1". However, a roof cannot have the same name as a wall.*
- Parent element: [`SAP-Roof`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Roofs__SAP_Roof)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Roofs__SAP_Roof__Description"></a>Description

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Roofs__SAP_Roof__Description`

- Documentation: *Descriptive notes about the roof.*
- Parent element: [`SAP-Roof`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Roofs__SAP_Roof)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Roofs__SAP_Roof__Roof_Type"></a>Roof-Type

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Roofs__SAP_Roof__Roof_Type`

- Documentation: *None*
- Parent element: [`SAP-Roof`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Roofs__SAP_Roof)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Roofs__SAP_Roof__Total_Roof_Area"></a>Total-Roof-Area

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Roofs__SAP_Roof__Total_Roof_Area`

- Documentation: *Total roof area in square metres, inclusive of any openings.*
- Parent element: [`SAP-Roof`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Roofs__SAP_Roof)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Roofs__SAP_Roof__U_Value"></a>U-Value

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Roofs__SAP_Roof__U_Value`

- Documentation: *Exposed roof U-value.*
- Parent element: [`SAP-Roof`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Roofs__SAP_Roof)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Roofs__SAP_Roof__Kappa_Value"></a>Kappa-Value

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Roofs__SAP_Roof__Kappa_Value`

- Documentation: *Heat capacity per unit area in kJ/m2K.*
- Parent element: [`SAP-Roof`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Roofs__SAP_Roof)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Floor_Dimensions"></a>SAP-Floor-Dimensions

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Floor_Dimensions`

- Documentation: *None*
- Parent element: [`SAP-Building-Part`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Floor_Dimensions__SAP_Floor_Dimension"></a>SAP-Floor-Dimension

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Floor_Dimensions__SAP_Floor_Dimension`

- Documentation: *None*
- Parent element: [`SAP-Floor-Dimensions`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Floor_Dimensions)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Floor_Dimensions__SAP_Floor_Dimension__Name"></a>Name

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Floor_Dimensions__SAP_Floor_Dimension__Name`

- Documentation: *A name describing the floor dimensioned.*
- Parent element: [`SAP-Floor-Dimension`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Floor_Dimensions__SAP_Floor_Dimension)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Floor_Dimensions__SAP_Floor_Dimension__Storey"></a>Storey

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Floor_Dimensions__SAP_Floor_Dimension__Storey`

- Documentation: *Building storey on which the floor is located.*
- Parent element: [`SAP-Floor-Dimension`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Floor_Dimensions__SAP_Floor_Dimension)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Floor_Dimensions__SAP_Floor_Dimension__Description"></a>Description

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Floor_Dimensions__SAP_Floor_Dimension__Description`

- Documentation: *Descriptive notes about the floor.*
- Parent element: [`SAP-Floor-Dimension`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Floor_Dimensions__SAP_Floor_Dimension)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Floor_Dimensions__SAP_Floor_Dimension__Floor_Type"></a>Floor-Type

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Floor_Dimensions__SAP_Floor_Dimension__Floor_Type`

- Documentation: *Type of floor (exposure).*
- Parent element: [`SAP-Floor-Dimension`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Floor_Dimensions__SAP_Floor_Dimension)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Floor_Dimensions__SAP_Floor_Dimension__Total_Floor_Area"></a>Total-Floor-Area

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Floor_Dimensions__SAP_Floor_Dimension__Total_Floor_Area`

- Documentation: *The total floor area of the storey in square metres.*
- Parent element: [`SAP-Floor-Dimension`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Floor_Dimensions__SAP_Floor_Dimension)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Floor_Dimensions__SAP_Floor_Dimension__Storey_Height"></a>Storey-Height

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Floor_Dimensions__SAP_Floor_Dimension__Storey_Height`

- Documentation: *Average height of the storey in metres.*
- Parent element: [`SAP-Floor-Dimension`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Floor_Dimensions__SAP_Floor_Dimension)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Floor_Dimensions__SAP_Floor_Dimension__Heat_Loss_Area"></a>Heat-Loss-Area

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Floor_Dimensions__SAP_Floor_Dimension__Heat_Loss_Area`

- Documentation: *The estimated total heat loss area for the floor in square metres.*
- Parent element: [`SAP-Floor-Dimension`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Floor_Dimensions__SAP_Floor_Dimension)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Floor_Dimensions__SAP_Floor_Dimension__U_Value"></a>U-Value

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Floor_Dimensions__SAP_Floor_Dimension__U_Value`

- Documentation: *Heat loss floor U-value.*
- Parent element: [`SAP-Floor-Dimension`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Floor_Dimensions__SAP_Floor_Dimension)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Floor_Dimensions__SAP_Floor_Dimension__Kappa_Value"></a>Kappa-Value

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Floor_Dimensions__SAP_Floor_Dimension__Kappa_Value`

- Documentation: *Heat capacity of floor per unit area in kJ/m2K.*
- Parent element: [`SAP-Floor-Dimension`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Floor_Dimensions__SAP_Floor_Dimension)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Floor_Dimensions__SAP_Floor_Dimension__Kappa_Value_From_Below"></a>Kappa-Value-From-Below

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Floor_Dimensions__SAP_Floor_Dimension__Kappa_Value_From_Below`

- Documentation: *Heat capacity of ceiling below. Applies to the non-heat-loss area of an upper floor.*
- Parent element: [`SAP-Floor-Dimension`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Floor_Dimensions__SAP_Floor_Dimension)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Thermal_Bridges"></a>SAP-Thermal-Bridges

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Thermal_Bridges`

- Documentation: *None*
- Parent element: [`SAP-Building-Part`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Thermal_Bridges__Thermal_Bridge_Code"></a>Thermal-Bridge-Code

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Thermal_Bridges__Thermal_Bridge_Code`

- Documentation: *Code which indicates how the thermal bridge data has been recorded.*
- Parent element: [`SAP-Thermal-Bridges`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Thermal_Bridges)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Thermal_Bridges__User_Defined_Y_Value"></a>User-Defined-Y-Value

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Thermal_Bridges__User_Defined_Y_Value`

- Documentation: *Global y-value for all thermal bridges in watts per square metre per kelvin; only if thermal bridge code is: user defined (global y-value)*
- Parent element: [`SAP-Thermal-Bridges`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Thermal_Bridges)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Thermal_Bridges__Calculation_Reference"></a>Calculation-Reference

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Thermal_Bridges__Calculation_Reference`

- Documentation: *Reference to the details of the calculation of the global y-value; only if thermal bridging is user defined global y-value.*
- Parent element: [`SAP-Thermal-Bridges`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Thermal_Bridges)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Thermal_Bridges__SAP_Thermal_Bridge"></a>SAP-Thermal-Bridge

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Thermal_Bridges__SAP_Thermal_Bridge`

- Documentation: *None*
- Parent element: [`SAP-Thermal-Bridges`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Thermal_Bridges)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Thermal_Bridges__SAP_Thermal_Bridge__Thermal_Bridge_Type"></a>Thermal-Bridge-Type

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Thermal_Bridges__SAP_Thermal_Bridge__Thermal_Bridge_Type`

- Documentation: *Code to indicate a particular type of thermal bridge; only if thermal bridge code is: user defined (individual values).*
- Parent element: [`SAP-Thermal-Bridge`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Thermal_Bridges__SAP_Thermal_Bridge)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Thermal_Bridges__SAP_Thermal_Bridge__Length"></a>Length

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Thermal_Bridges__SAP_Thermal_Bridge__Length`

- Documentation: *Length of the thermal bridge in metres; only if thermal bridge code is: user defined (individual values).*
- Parent element: [`SAP-Thermal-Bridge`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Thermal_Bridges__SAP_Thermal_Bridge)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Thermal_Bridges__SAP_Thermal_Bridge__Psi_Value"></a>Psi-Value

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Thermal_Bridges__SAP_Thermal_Bridge__Psi_Value`

- Documentation: *Linear thermal transmittance (psi-value); only if thermal bridging is user defined individual values.*
- Parent element: [`SAP-Thermal-Bridge`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Thermal_Bridges__SAP_Thermal_Bridge)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Thermal_Bridges__SAP_Thermal_Bridge__Psi_Value_Source"></a>Psi-Value-Source

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Thermal_Bridges__SAP_Thermal_Bridge__Psi_Value_Source`

- Documentation: *None*
- Parent element: [`SAP-Thermal-Bridge`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Thermal_Bridges__SAP_Thermal_Bridge)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Thermal_Bridges__SAP_Thermal_Bridge__Psi_Value_Calculation_Reference"></a>Psi-Value-Calculation-Reference

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Thermal_Bridges__SAP_Thermal_Bridge__Psi_Value_Calculation_Reference`

- Documentation: *Reference to the details of the calculation of the psi-value.*
- Parent element: [`SAP-Thermal-Bridge`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Thermal_Bridges__SAP_Thermal_Bridge)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Walls"></a>SAP-Walls

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Walls`

- Documentation: *None*
- Parent element: [`SAP-Building-Part`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Walls__SAP_Wall"></a>SAP-Wall

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Walls__SAP_Wall`

- Documentation: *None*
- Parent element: [`SAP-Walls`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Walls)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Walls__SAP_Wall__Name"></a>Name

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Walls__SAP_Wall__Name`

- Documentation: *Unique name which identifies this wall within its storey. Can be just a number, e.g. "1". However, a wall cannot have the same name as an opening or a roof.*
- Parent element: [`SAP-Wall`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Walls__SAP_Wall)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Walls__SAP_Wall__Description"></a>Description

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Walls__SAP_Wall__Description`

- Documentation: *Descriptive notes about the wall.*
- Parent element: [`SAP-Wall`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Walls__SAP_Wall)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Walls__SAP_Wall__Wall_Type"></a>Wall-Type

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Walls__SAP_Wall__Wall_Type`

- Documentation: *Type of wall (exposure).*
- Parent element: [`SAP-Wall`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Walls__SAP_Wall)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Walls__SAP_Wall__Total_Wall_Area"></a>Total-Wall-Area

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Walls__SAP_Wall__Total_Wall_Area`

- Documentation: *Total wall area in square metres, inclusive of any openings.*
- Parent element: [`SAP-Wall`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Walls__SAP_Wall)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Walls__SAP_Wall__U_Value"></a>U-Value

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Walls__SAP_Wall__U_Value`

- Documentation: *Exposed wall U-value.*
- Parent element: [`SAP-Wall`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Walls__SAP_Wall)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Walls__SAP_Wall__Is_Curtain_Walling"></a>Is-Curtain-Walling

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Walls__SAP_Wall__Is_Curtain_Walling`

- Documentation: *Whether the wall is curtain walling, i.e. a facade construction consisting of a frame of aluminium vertical and horizontal members, infilled with glazing units and opaque panels.*
- Parent element: [`SAP-Wall`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Walls__SAP_Wall)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Walls__SAP_Wall__Kappa_Value"></a>Kappa-Value

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Walls__SAP_Wall__Kappa_Value`

- Documentation: *Heat capacity per unit area in kJ/m2K.*
- Parent element: [`SAP-Wall`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Building_Parts__SAP_Building_Part__SAP_Walls__SAP_Wall)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types"></a>SAP-Opening-Types

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types`

- Documentation: *None*
- Parent element: [`SAP-Property-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type"></a>SAP-Opening-Type

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type`

- Documentation: *None*
- Parent element: [`SAP-Opening-Types`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type__Name"></a>Name

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type__Name`

- Documentation: *Unique name which identifies this opening type. Can be just a number, e.g. "1".*
- Parent element: [`SAP-Opening-Type`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type__Description"></a>Description

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type__Description`

- Documentation: *Descriptive notes about the opening type.*
- Parent element: [`SAP-Opening-Type`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type__Data_Source"></a>Data-Source

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type__Data_Source`

- Documentation: *The source of the data for this type of opening.*
- Parent element: [`SAP-Opening-Type`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type__Type"></a>Type

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type__Type`

- Documentation: *The (physical) type of opening that this opening type represents.*
- Parent element: [`SAP-Opening-Type`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type__Glazing_Type"></a>Glazing-Type

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type__Glazing_Type`

- Documentation: *The type of glazing; if U-value is from BFRC or manufacturer declaration, give as one of - single - double - triple.*
- Parent element: [`SAP-Opening-Type`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type__Glazing_Gap"></a>Glazing-Gap

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type__Glazing_Gap`

- Documentation: *Gap between glass panes; only if SAP table and double, triple glazed or secondary glazing.*
- Parent element: [`SAP-Opening-Type`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type__IsArgonFilled"></a>IsArgonFilled

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type__IsArgonFilled`

- Documentation: *Is the opening argon-filled? Only if SAP table.*
- Parent element: [`SAP-Opening-Type`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type__IsKryptonFilled"></a>IsKryptonFilled

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type__IsKryptonFilled`

- Documentation: *Is the opening krypton-filled? Only if SAP table.*
- Parent element: [`SAP-Opening-Type`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type__Frame_Type"></a>Frame-Type

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type__Frame_Type`

- Documentation: *The type of frame, only if data source is SAP table and it is a window, roof window or half-glazed door.*
- Parent element: [`SAP-Opening-Type`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type__Solar_Transmittance"></a>Solar-Transmittance

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type__Solar_Transmittance`

- Documentation: *The solar transmittance; not if a door.*
- Parent element: [`SAP-Opening-Type`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type__Frame_Factor"></a>Frame-Factor

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type__Frame_Factor`

- Documentation: *The frame factor; not if a door.*
- Parent element: [`SAP-Opening-Type`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type__U_Value"></a>U-Value

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type__U_Value`

- Documentation: *The U-value. For rooflights, the U-value should be in the horizontal plane.*
- Parent element: [`SAP-Opening-Type`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Opening_Types__SAP_Opening_Type)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation"></a>SAP-Ventilation

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation`

- Documentation: *None*
- Parent element: [`SAP-Property-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Closed_Flues_Count"></a>Closed-Flues-Count

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Closed_Flues_Count`

- Documentation: *The number of Closed Flues or chimneys in the Property.*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Open_Flues_Count"></a>Open-Flues-Count

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Open_Flues_Count`

- Documentation: *The number of Open Flues in the Property.*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Boilers_Flues_Count"></a>Boilers-Flues-Count

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Boilers_Flues_Count`

- Documentation: *The number of Boiler Flues or chimneys in the Property.*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Other_Flues_Count"></a>Other-Flues-Count

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Other_Flues_Count`

- Documentation: *The number of Other Flues or chimneys in the Property.*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Open_Chimneys_Count"></a>Open-Chimneys-Count

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Open_Chimneys_Count`

- Documentation: *The number of Open Chimneys in the Property.*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Blocked_Chimneys_Count"></a>Blocked-Chimneys-Count

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Blocked_Chimneys_Count`

- Documentation: *The number of Blocked Chimneys in the Property.*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Fans_Vents_Count"></a>Fans-Vents-Count

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Fans_Vents_Count`

- Documentation: *For backward compatibility only, do not use.*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Flueless_Gas_Fires_Count"></a>Flueless-Gas-Fires-Count

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Flueless_Gas_Fires_Count`

- Documentation: *The number of flueless gas fires in the Property.*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Pressure_Test"></a>Pressure-Test

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Pressure_Test`

- Documentation: *Whether there has been a pressure test, or whether an assumed value is used for the air permeability.*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Pressure_Test_Certificate_Number"></a>Pressure-Test-Certificate-Number

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Pressure_Test_Certificate_Number`

- Documentation: *The pressure test certificate number or test engineer reference.*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Air_Permeability"></a>Air-Permeability

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Air_Permeability`

- Documentation: *Air permeability; only if pressure test (yes or assumed).*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Ground_Floor_Type"></a>Ground-Floor-Type

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Ground_Floor_Type`

- Documentation: *The type of ground floor; nly if no pressure test.*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Wall_Type"></a>Wall-Type

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Wall_Type`

- Documentation: *The construction of the walls; only if no pressure test.*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Has_Draught_Lobby"></a>Has-Draught-Lobby

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Has_Draught_Lobby`

- Documentation: *Is there a draft lobby? Only if no pressure test.*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__DraughtStripping"></a>DraughtStripping

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__DraughtStripping`

- Documentation: *Draughtstripping percentage; only if no pressure test.*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Sheltered_Sides_Count"></a>Sheltered-Sides-Count

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Sheltered_Sides_Count`

- Documentation: *The number of sheltered sides in the Property.*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Ventilation_Type"></a>Ventilation-Type

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Ventilation_Type`

- Documentation: *The type of ventilation.*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Mechanical_Ventilation_Data_Source"></a>Mechanical-Ventilation-Data-Source

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Mechanical_Ventilation_Data_Source`

- Documentation: *Source of mechanical ventilation data; only if mechanical ventilation.*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Mechanical_Vent_System_Index_Number"></a>Mechanical-Vent-System-Index-Number

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Mechanical_Vent_System_Index_Number`

- Documentation: *Mechanical vent system index number; if mechanical vent data from database (MEV c, MEV dc, MV, MVHR).*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Mechanical_Vent_Commissioning_Certificate_Number"></a>Mechanical-Vent-Commissioning-Certificate-Number

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Mechanical_Vent_Commissioning_Certificate_Number`

- Documentation: *Mechanical ventilation Commissioning certificate number .*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Mechanical_Vent_Installation_Engineer"></a>Mechanical-Vent-Installation-Engineer

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Mechanical_Vent_Installation_Engineer`

- Documentation: *Mechanical ventilation installation engineer registration reference.*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Mechanical_Vent_System_Make_Model"></a>Mechanical-Vent-System-Make-Model

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Mechanical_Vent_System_Make_Model`

- Documentation: *Mechanical ventilation system make and model.*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Wet_Rooms_Count"></a>Wet-Rooms-Count

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Wet_Rooms_Count`

- Documentation: *Number of wet rooms, including the kitchen; if mech vent data from manufacturer declaration or database (MEV c, MV, MVHR).*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Mechanical_Vent_Specific_Fan_Power"></a>Mechanical-Vent-Specific-Fan-Power

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Mechanical_Vent_Specific_Fan_Power`

- Documentation: *Mechanical vent specific fan power in watts per (litres per second); if mechanical vent data (PIV from outside, MEV c or dc, MV, MVHR).*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Mechanical_Vent_Heat_Recovery_Efficiency"></a>Mechanical-Vent-Heat-Recovery-Efficiency

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Mechanical_Vent_Heat_Recovery_Efficiency`

- Documentation: *Mechanical vent heat recovery efficiency percentage; if mechanical vent (MVHR).*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Mechanical_Vent_Duct_Type"></a>Mechanical-Vent-Duct-Type

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Mechanical_Vent_Duct_Type`

- Documentation: *Mechanical vent duct type; if MEV c, MV or MVHR.*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Mechanical_Vent_Duct_Insulation"></a>Mechanical-Vent-Duct-Insulation

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Mechanical_Vent_Duct_Insulation`

- Documentation: *Mechanical vent duct insulation; if MVHR.*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Mechanical_Vent_Duct_Insulation_Level"></a>Mechanical-Vent-Duct-Insulation-Level

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Mechanical_Vent_Duct_Insulation_Level`

- Documentation: *Mechanical vent duct insulation; if MVHR.*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Mechanical_Vent_Duct_Placement"></a>Mechanical-Vent-Duct-Placement

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Mechanical_Vent_Duct_Placement`

- Documentation: *Mechanical ventilation duct insulation; if MVHR.*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Mechanical_Vent_Measured_Installation"></a>Mechanical-Vent-Measured-Installation

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Mechanical_Vent_Measured_Installation`

- Documentation: *Mechanical ventilation SPF measured in situ; if MVHR or balanced.*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Kitchen_Room_Fans_Count"></a>Kitchen-Room-Fans-Count

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Kitchen_Room_Fans_Count`

- Documentation: *MEV dc, number of fans in room, kitchen; if mechanical vent data from database or manufacturer declaration (MEV dc).*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Kitchen_Room_Fans_Specific_Power"></a>Kitchen-Room-Fans-Specific-Power

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Kitchen_Room_Fans_Specific_Power`

- Documentation: *MEV dc, specific fan power of fans in room, kitchen, in watts per (litres per second); if mechanical vent data from manufacturer declaration (MEV dc).*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Non_Kitchen_Room_Fans_Count"></a>Non-Kitchen-Room-Fans-Count

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Non_Kitchen_Room_Fans_Count`

- Documentation: *MEV dc, number of fans in room, rooms other than kitchen; if mechanical vent data from database or manufacturer declaration (MEV dc).*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Non_Kitchen_Room_Fans_Specific_Power"></a>Non-Kitchen-Room-Fans-Specific-Power

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Non_Kitchen_Room_Fans_Specific_Power`

- Documentation: *MEV dc, specific fan power of fans in room, rooms other than kitchen, in watts per (litres per second); if mechanical vent data from manufacturer declaration (MEV dc).*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Kitchen_Duct_Fans_Count"></a>Kitchen-Duct-Fans-Count

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Kitchen_Duct_Fans_Count`

- Documentation: *MEV dc, number of fans via duct, kitchen; if mechanical vent data from database or manufacturer declaration (MEV dc).*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Kitchen_Duct_Fans_Specific_Power"></a>Kitchen-Duct-Fans-Specific-Power

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Kitchen_Duct_Fans_Specific_Power`

- Documentation: *MEV dc, specific fan power of fans via duct, kitchen, in watts per (litres per second); if mechanical vent data from manufacturer declaration (MEV dc).*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Non_Kitchen_Duct_Fans_Count"></a>Non-Kitchen-Duct-Fans-Count

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Non_Kitchen_Duct_Fans_Count`

- Documentation: *MEV dc, number of fans via duct, rooms other than kitchen; if mechanical vent data from database or manufacturer declaration (MEV dc).*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Non_Kitchen_Duct_Fans_Specific_Power"></a>Non-Kitchen-Duct-Fans-Specific-Power

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Non_Kitchen_Duct_Fans_Specific_Power`

- Documentation: *MEV dc, specific fan power of fans via duct, rooms other than kitchen, in watts per (litres per second); if mechanical vent data from manufacturer declaration (MEV dc).*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Kitchen_Wall_Fans_Count"></a>Kitchen-Wall-Fans-Count

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Kitchen_Wall_Fans_Count`

- Documentation: *MEV dc, number of fans through wall, kitchen; if mechanical vent data from database or manufacturer declaration (MEV dc).*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Kitchen_Wall_Fans_Specific_Power"></a>Kitchen-Wall-Fans-Specific-Power

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Kitchen_Wall_Fans_Specific_Power`

- Documentation: *MEV dc, specific fan power of fans through wall, kitchen, in watts per (litres per second); if mechanical vent data from manufacturer declaration (MEV dc).*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Non_Kitchen_Wall_Fans_Count"></a>Non-Kitchen-Wall-Fans-Count

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Non_Kitchen_Wall_Fans_Count`

- Documentation: *MEV dc, number of fans through wall, rooms other than kitchen; if mechanical vent data from database or manufacturer declaration (MEV dc).*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Non_Kitchen_Wall_Fans_Specific_Power"></a>Non-Kitchen-Wall-Fans-Specific-Power

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Non_Kitchen_Wall_Fans_Specific_Power`

- Documentation: *MEV dc, specific fan power of fans through wall, rooms other than kitchen, in watts per (litres per second); if mechanical vent data from manufacturer declaration (MEV dc).*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Extract_Fans_Count"></a>Extract-Fans-Count

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Extract_Fans_Count`

- Documentation: *None*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__PSV_Count"></a>PSV-Count

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__PSV_Count`

- Documentation: *None*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Is_Mechanical_Vent_Approved_Installer_Scheme"></a>Is-Mechanical-Vent-Approved-Installer-Scheme

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Is_Mechanical_Vent_Approved_Installer_Scheme`

- Documentation: *None*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Mechanical_Vent_Ducts_Index_Number"></a>Mechanical-Vent-Ducts-Index-Number

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation__Mechanical_Vent_Ducts_Index_Number`

- Documentation: *Mechanical vent ducts index number; if applicable.*
- Parent element: [`SAP-Ventilation`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Ventilation)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Lighting"></a>SAP-Lighting

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Lighting`

- Documentation: *None*
- Parent element: [`SAP-Property-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Lighting__Fixed_Lights"></a>Fixed-Lights

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Lighting__Fixed_Lights`

- Documentation: *The record of a lighting type within the building.*
- Parent element: [`SAP-Lighting`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Lighting)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Lighting__Fixed_Lights__Fixed_Light"></a>Fixed-Light

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Lighting__Fixed_Lights__Fixed_Light`

- Documentation: *None*
- Parent element: [`Fixed-Lights`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Lighting__Fixed_Lights)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Lighting__Fixed_Lights__Fixed_Light__Lighting_Efficacy"></a>Lighting-Efficacy

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Lighting__Fixed_Lights__Fixed_Light__Lighting_Efficacy`

- Documentation: *The efficacy of the lighting type in lumens/Watt.*
- Parent element: [`Fixed-Light`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Lighting__Fixed_Lights__Fixed_Light)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Lighting__Fixed_Lights__Fixed_Light__Lighting_Power"></a>Lighting-Power

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Lighting__Fixed_Lights__Fixed_Light__Lighting_Power`

- Documentation: *The power of the selected lighting type in Watts.*
- Parent element: [`Fixed-Light`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Lighting__Fixed_Lights__Fixed_Light)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Lighting__Fixed_Lights__Fixed_Light__Lighting_Outlets"></a>Lighting-Outlets

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Lighting__Fixed_Lights__Fixed_Light__Lighting_Outlets`

- Documentation: *The number of light fitting outlets of that type.*
- Parent element: [`Fixed-Light`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Lighting__Fixed_Lights__Fixed_Light)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Deselected_Improvements"></a>SAP-Deselected-Improvements

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Deselected_Improvements`

- Documentation: *None*
- Parent element: [`SAP-Property-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Deselected_Improvements__Deselected_Improvement_Measure"></a>Deselected-Improvement-Measure

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Deselected_Improvements__Deselected_Improvement_Measure`

- Documentation: *None*
- Parent element: [`SAP-Deselected-Improvements`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Deselected_Improvements)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Flat_Details"></a>SAP-Flat-Details

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Flat_Details`

- Documentation: *None*
- Parent element: [`SAP-Property-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Flat_Details__Level"></a>Level

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Flat_Details__Level`

- Documentation: *Indication of where a flat is located in a building.*
- Parent element: [`SAP-Flat-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Flat_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Flat_Details__Storeys"></a>Storeys

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Flat_Details__Storeys`

- Documentation: *Count of number of storeys present in the block of flats.*
- Parent element: [`SAP-Flat-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Flat_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features"></a>SAP-Special-Features

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features`

- Documentation: *None*
- Parent element: [`SAP-Property-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature"></a>SAP-Special-Feature

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature`

- Documentation: *None*
- Parent element: [`SAP-Special-Features`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature__Description"></a>Description

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature__Description`

- Documentation: *None*
- Parent element: [`SAP-Special-Feature`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature__Energy_Feature"></a>Energy-Feature

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature__Energy_Feature`

- Documentation: *None*
- Parent element: [`SAP-Special-Feature`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature__Energy_Feature__Energy_Saved_Or_Generated"></a>Energy-Saved-Or-Generated

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature__Energy_Feature__Energy_Saved_Or_Generated`

- Documentation: *Energy saved or generated in kWh/year.*
- Parent element: [`Energy-Feature`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature__Energy_Feature)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature__Energy_Feature__Saved_Or_Generated_Fuel"></a>Saved-Or-Generated-Fuel

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature__Energy_Feature__Saved_Or_Generated_Fuel`

- Documentation: *None*
- Parent element: [`Energy-Feature`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature__Energy_Feature)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature__Energy_Feature__Energy_Used"></a>Energy-Used

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature__Energy_Feature__Energy_Used`

- Documentation: *Energy used in kWh/year.*
- Parent element: [`Energy-Feature`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature__Energy_Feature)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature__Energy_Feature__Energy_Used_Fuel"></a>Energy-Used-Fuel

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature__Energy_Feature__Energy_Used_Fuel`

- Documentation: *None*
- Parent element: [`Energy-Feature`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature__Energy_Feature)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature__Energy_Feature__Air_Change_Rates"></a>Air-Change-Rates

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature__Energy_Feature__Air_Change_Rates`

- Documentation: *For Appendix Q procedure that provides air change rates. Only one Special Feature can have data on air change rates.*
- Parent element: [`Energy-Feature`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature__Energy_Feature)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature__Energy_Feature__Air_Change_Rates__Air_Change_Rate"></a>Air-Change-Rate

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature__Energy_Feature__Air_Change_Rates__Air_Change_Rate`

- Documentation: *None*
- Parent element: [`Air-Change-Rates`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature__Energy_Feature__Air_Change_Rates)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature__Energy_Feature__Air_Change_Rates__Air_Change_Rate__Air_Change_Rate_Month"></a>Air-Change-Rate-Month

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature__Energy_Feature__Air_Change_Rates__Air_Change_Rate__Air_Change_Rate_Month`

- Documentation: *None*
- Parent element: [`Air-Change-Rate`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature__Energy_Feature__Air_Change_Rates__Air_Change_Rate)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature__Energy_Feature__Air_Change_Rates__Air_Change_Rate__Air_Change_Rate_Value"></a>Air-Change-Rate-Value

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature__Energy_Feature__Air_Change_Rates__Air_Change_Rate__Air_Change_Rate_Value`

- Documentation: *Air change rate in month.*
- Parent element: [`Air-Change-Rate`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature__Energy_Feature__Air_Change_Rates__Air_Change_Rate)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature__Emissions_Feature"></a>Emissions-Feature

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature__Emissions_Feature`

- Documentation: *None*
- Parent element: [`SAP-Special-Feature`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature__Emissions_Feature__Emissions_Saved"></a>Emissions-Saved

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature__Emissions_Feature__Emissions_Saved`

- Documentation: *Emissions saved in kg/year.*
- Parent element: [`Emissions-Feature`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature__Emissions_Feature)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature__Emissions_Feature__Emissions_Created"></a>Emissions-Created

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature__Emissions_Feature__Emissions_Created`

- Documentation: *Additional emissions in kg/year.*
- Parent element: [`Emissions-Feature`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Special_Features__SAP_Special_Feature__Emissions_Feature)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Design_Water_Use"></a>Design-Water-Use

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__Design_Water_Use`

- Documentation: *Design limit for total water use.*
- Parent element: [`SAP-Property-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Cooling"></a>SAP-Cooling

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Cooling`

- Documentation: *None*
- Parent element: [`SAP-Property-Details`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Cooling__Cooled_Area"></a>Cooled-Area

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Cooling__Cooled_Area`

- Documentation: *None*
- Parent element: [`SAP-Cooling`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Cooling)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Cooling__Cooling_System_Data_Source"></a>Cooling-System-Data-Source

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Cooling__Cooling_System_Data_Source`

- Documentation: *None*
- Parent element: [`SAP-Cooling`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Cooling)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Cooling__Cooling_System_Class"></a>Cooling-System-Class

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Cooling__Cooling_System_Class`

- Documentation: *Data set includes either class or SEER, not both.*
- Parent element: [`SAP-Cooling`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Cooling)

## <a name="SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Cooling__System_Energy_Efficiency_Ratio"></a>System-Energy-Efficiency-Ratio

`SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Cooling__System_Energy_Efficiency_Ratio`

- Documentation: *SEER.*
- Parent element: [`SAP-Cooling`](#SAP_Compliance_Report__SAP_Report__SAP10_Data__SAP_Property_Details__SAP_Cooling)

## <a name="SAP_Compliance_Report__SAP_Report__PDF"></a>PDF

`SAP_Compliance_Report__SAP_Report__PDF`

- Documentation: *DEPRECATED - DO NOT USE This element is allowed for backwards-compatibility but any data sent here will not be read, processed or stored by the register.*
- Parent element: [`SAP-Report`](#SAP_Compliance_Report__SAP_Report)

## <a name="SAP_Compliance_Report__SAP_Report__Insurance_Details"></a>Insurance-Details

`SAP_Compliance_Report__SAP_Report__Insurance_Details`

- Documentation: *None*
- Parent element: [`SAP-Report`](#SAP_Compliance_Report__SAP_Report)

## <a name="SAP_Compliance_Report__SAP_Report__Insurance_Details__Insurer"></a>Insurer

`SAP_Compliance_Report__SAP_Report__Insurance_Details__Insurer`

- Documentation: *The name of the insurance company that underwrites / issued the insurance policy*
- Parent element: [`Insurance-Details`](#SAP_Compliance_Report__SAP_Report__Insurance_Details)

## <a name="SAP_Compliance_Report__SAP_Report__Insurance_Details__Policy_No"></a>Policy-No

`SAP_Compliance_Report__SAP_Report__Insurance_Details__Policy_No`

- Documentation: *The policy number of the insurance policy*
- Parent element: [`Insurance-Details`](#SAP_Compliance_Report__SAP_Report__Insurance_Details)

## <a name="SAP_Compliance_Report__SAP_Report__Insurance_Details__Effective_Date"></a>Effective-Date

`SAP_Compliance_Report__SAP_Report__Insurance_Details__Effective_Date`

- Documentation: *The date that the insurance policy becomes effective (commences cover)*
- Parent element: [`Insurance-Details`](#SAP_Compliance_Report__SAP_Report__Insurance_Details)

## <a name="SAP_Compliance_Report__SAP_Report__Insurance_Details__Expiry_Date"></a>Expiry-Date

`SAP_Compliance_Report__SAP_Report__Insurance_Details__Expiry_Date`

- Documentation: *The date that the insurance policy is supposed to expire.*
- Parent element: [`Insurance-Details`](#SAP_Compliance_Report__SAP_Report__Insurance_Details)

## <a name="SAP_Compliance_Report__SAP_Report__Insurance_Details__PI_Limit"></a>PI-Limit

`SAP_Compliance_Report__SAP_Report__Insurance_Details__PI_Limit`

- Documentation: *The upper limit of the Professional Indemnity cover provided by the insurance policy.*
- Parent element: [`Insurance-Details`](#SAP_Compliance_Report__SAP_Report__Insurance_Details)

## <a name="SAP_Compliance_Report__SAP_Report__ExternalDefinitions_Revision_Number"></a>ExternalDefinitions-Revision-Number

`SAP_Compliance_Report__SAP_Report__ExternalDefinitions_Revision_Number`

- Documentation: *A number indicating the version of related ExternalDefinitions.xsd*
- Parent element: [`SAP-Report`](#SAP_Compliance_Report__SAP_Report)

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

## <a name="SAP_Compliance_Report__Client_Address__Address_Line_1"></a>Address-Line-1

`SAP_Compliance_Report__Client_Address__Address_Line_1`

- Documentation: *None*
- Parent element: [`Client-Address`](#SAP_Compliance_Report__Client_Address)

## <a name="SAP_Compliance_Report__Client_Address__Address_Line_2"></a>Address-Line-2

`SAP_Compliance_Report__Client_Address__Address_Line_2`

- Documentation: *None*
- Parent element: [`Client-Address`](#SAP_Compliance_Report__Client_Address)

## <a name="SAP_Compliance_Report__Client_Address__Address_Line_3"></a>Address-Line-3

`SAP_Compliance_Report__Client_Address__Address_Line_3`

- Documentation: *None*
- Parent element: [`Client-Address`](#SAP_Compliance_Report__Client_Address)

## <a name="SAP_Compliance_Report__Client_Address__Post_Town"></a>Post-Town

`SAP_Compliance_Report__Client_Address__Post_Town`

- Documentation: *None*
- Parent element: [`Client-Address`](#SAP_Compliance_Report__Client_Address)

## <a name="SAP_Compliance_Report__Client_Address__Postcode"></a>Postcode

`SAP_Compliance_Report__Client_Address__Postcode`

- Documentation: *The Postcode for the Address*
- Parent element: [`Client-Address`](#SAP_Compliance_Report__Client_Address)

## <a name="SAP_Compliance_Report__Is_Multiple_Compliance"></a>Is-Multiple-Compliance

`SAP_Compliance_Report__Is_Multiple_Compliance`

- Documentation: *Is the compliance report part of a multiple compliance calculation.*
- Parent element: [`SAP-Compliance-Report`](#SAP_Compliance_Report)

