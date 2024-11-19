# SAP Schema 19.1.0. docs

This page contains the documentation for the XML schema [SAP-Schema-19.1.0](https://github.com/communitiesuk/epb-register-api/tree/master/api/schemas/xml/SAP-Schema-19.1.0/SAP).

This XML schema describes the format of the XML input files for SAP 10.2 calculations.

The root XML element can be either a [SAP-Compliance-Report](#SAP_Compliance_Report) or a [SAP-Report](#SAP_Compliance_Report__SAP_Report) element.

## <a name="SAP-Compliance-Report"></a>SAP-Compliance-Report

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/

- Child elements: [`SAP-Report`](#SAP-Compliance-Report/SAP-Report) [`Client-Name`](#SAP-Compliance-Report/Client-Name) [`Client-Company`](#SAP-Compliance-Report/Client-Company) [`Client-Address`](#SAP-Compliance-Report/Client-Address) [`Is-Multiple-Compliance`](#SAP-Compliance-Report/Is-Multiple-Compliance)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report"></a>SAP-Report

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/

- Documentation: *The SAP report corresponding to the compliance report.*
- Parent element: [`SAP-Compliance-Report`](#SAP-Compliance-Report)
- Child elements: [`Schema-Version-Original`](#SAP-Compliance-Report/SAP-Report/Schema-Version-Original) [`Schema-Version-Current`](#SAP-Compliance-Report/SAP-Report/Schema-Version-Current) [`SAP-Version`](#SAP-Compliance-Report/SAP-Report/SAP-Version) [`SAP-Data-Version`](#SAP-Compliance-Report/SAP-Report/SAP-Data-Version) [`PCDF-Revision-Number`](#SAP-Compliance-Report/SAP-Report/PCDF-Revision-Number) [`Calculation-Software-Name`](#SAP-Compliance-Report/SAP-Report/Calculation-Software-Name) [`Calculation-Software-Version`](#SAP-Compliance-Report/SAP-Report/Calculation-Software-Version) [`User-Interface-Name`](#SAP-Compliance-Report/SAP-Report/User-Interface-Name) [`User-Interface-Version`](#SAP-Compliance-Report/SAP-Report/User-Interface-Version) [`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header) [`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment) [`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data) [`PDF`](#SAP-Compliance-Report/SAP-Report/PDF) [`Insurance-Details`](#SAP-Compliance-Report/SAP-Report/Insurance-Details) [`ExternalDefinitions-Revision-Number`](#SAP-Compliance-Report/SAP-Report/ExternalDefinitions-Revision-Number)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Schema-Version-Original"></a>Schema-Version-Original

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Schema-Version-Original`](#SAP-Compliance-Report/SAP-Report/Schema-Version-Original)/

- Documentation: *The schema version that the data conformed to when it was lodged.*
- Parent element: [`SAP-Report`](#SAP-Compliance-Report/SAP-Report)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Schema-Version-Current"></a>Schema-Version-Current

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Schema-Version-Current`](#SAP-Compliance-Report/SAP-Report/Schema-Version-Current)/

- Documentation: *The schema version to which the data conforms. This node is inserted by the register when a retrieval is requested. It must not be present in a lodgement being sent to the register.*
- Parent element: [`SAP-Report`](#SAP-Compliance-Report/SAP-Report)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP-Version"></a>SAP-Version

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP-Version`](#SAP-Compliance-Report/SAP-Report/SAP-Version)/

- Documentation: *SAP version that was used for the calculation.*
- Parent element: [`SAP-Report`](#SAP-Compliance-Report/SAP-Report)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"9.80"** - *SAP 2005 version 9.80, dated October 2005*
    - **"9.81"** - *SAP version 9.81, dated January 2008*
    - **"9.82"** - *SAP version 9.82, dated Jun 2008*
    - **"9.83"** - *SAP version 9.83, dated Jun 2009*
    - **"9.90"** - *SAP version 9.90, dated Mar 2010*
    - **"9.91"** - *SAP version 9.91, dated Jan 2012*
    - **"9.92"** - *SAP version 9.92, dated Oct 2013*
    - **"10.2"** - *SAP version 10.2, dated Oct 2020*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP-Data-Version"></a>SAP-Data-Version

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP-Data-Version`](#SAP-Compliance-Report/SAP-Report/SAP-Data-Version)/

- Documentation: *Version of SAP that was used to define the input data for the calculation.*
- Parent element: [`SAP-Report`](#SAP-Compliance-Report/SAP-Report)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"9.80"** - *SAP 2005 version 9.80, dated October 2005*
    - **"9.81"** - *SAP version 9.81, dated January 2008*
    - **"9.82"** - *SAP version 9.82, dated Jun 2008*
    - **"9.83"** - *SAP version 9.83, dated Jun 2009*
    - **"9.90"** - *SAP version 9.90, dated Mar 2010*
    - **"9.91"** - *SAP version 9.91, dated Jan 2012*
    - **"9.92"** - *SAP version 9.92, dated Oct 2013*
    - **"10.2"** - *SAP version 10.2, dated Oct 2020*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/PCDF-Revision-Number"></a>PCDF-Revision-Number

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`PCDF-Revision-Number`](#SAP-Compliance-Report/SAP-Report/PCDF-Revision-Number)/

- Documentation: *Revision Number of the PCDF file used for the calculations.*
- Parent element: [`SAP-Report`](#SAP-Compliance-Report/SAP-Report)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Calculation-Software-Name"></a>Calculation-Software-Name

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Calculation-Software-Name`](#SAP-Compliance-Report/SAP-Report/Calculation-Software-Name)/

- Documentation: *Name of the software used to perform the SAP calculation.*
- Parent element: [`SAP-Report`](#SAP-Compliance-Report/SAP-Report)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Calculation-Software-Version"></a>Calculation-Software-Version

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Calculation-Software-Version`](#SAP-Compliance-Report/SAP-Report/Calculation-Software-Version)/

- Documentation: *Version of the software used to perform the SAP calculation.*
- Parent element: [`SAP-Report`](#SAP-Compliance-Report/SAP-Report)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/User-Interface-Name"></a>User-Interface-Name

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`User-Interface-Name`](#SAP-Compliance-Report/SAP-Report/User-Interface-Name)/

- Parent element: [`SAP-Report`](#SAP-Compliance-Report/SAP-Report)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/User-Interface-Version"></a>User-Interface-Version

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`User-Interface-Version`](#SAP-Compliance-Report/SAP-Report/User-Interface-Version)/

- Parent element: [`SAP-Report`](#SAP-Compliance-Report/SAP-Report)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header"></a>Report-Header

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/

- Documentation2: *Report Header contains all the identification and searchable details for the Report.*
- Parent element: [`SAP-Report`](#SAP-Compliance-Report/SAP-Report)
- Child elements: [`RRN`](#SAP-Compliance-Report/SAP-Report/Report-Header/RRN) [`Inspection-Date`](#SAP-Compliance-Report/SAP-Report/Report-Header/Inspection-Date) [`Report-Type`](#SAP-Compliance-Report/SAP-Report/Report-Header/Report-Type) [`Completion-Date`](#SAP-Compliance-Report/SAP-Report/Report-Header/Completion-Date) [`Registration-Date`](#SAP-Compliance-Report/SAP-Report/Report-Header/Registration-Date) [`Status`](#SAP-Compliance-Report/SAP-Report/Report-Header/Status) [`Language-Code`](#SAP-Compliance-Report/SAP-Report/Report-Header/Language-Code) [`Tenure`](#SAP-Compliance-Report/SAP-Report/Report-Header/Tenure) [`Transaction-Type`](#SAP-Compliance-Report/SAP-Report/Report-Header/Transaction-Type) [`Seller-Commission-Report`](#SAP-Compliance-Report/SAP-Report/Report-Header/Seller-Commission-Report) [`Property-Type`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property-Type) [`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector) [`Property`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property) [`Region-Code`](#SAP-Compliance-Report/SAP-Report/Report-Header/Region-Code) [`Country-Code`](#SAP-Compliance-Report/SAP-Report/Report-Header/Country-Code) [`Related-Party-Disclosure`](#SAP-Compliance-Report/SAP-Report/Report-Header/Related-Party-Disclosure)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/RRN"></a>RRN

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`RRN`](#SAP-Compliance-Report/SAP-Report/Report-Header/RRN)/

- Documentation: *Report Reference Number is the unique report Identifier that the report will be publicly known by. The RRN is allocated to the Report at the point that it is registered and will be algorithmically derived from the natural key characteristics of the Home Condition Report i.e. The Unique Property Reference Number (UPRN) and Inspection Date.*
- Parent element: [`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Inspection-Date"></a>Inspection-Date

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Inspection-Date`](#SAP-Compliance-Report/SAP-Report/Report-Header/Inspection-Date)/

- Documentation: *The date that the inspection was actually carried out by the Home Inspector.*
- Parent element: [`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)
- Has text value: *True*
- Data type: *<built-in method fromisoformat of type object at 0x00007FFB580DD990>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Report-Type"></a>Report-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Report-Type`](#SAP-Compliance-Report/SAP-Report/Report-Header/Report-Type)/

- Documentation: *The type of Home Inspection that was carried out. Initially the only allowed type will be a Home Condition Report inspection but this may be extended in the future to cover Energy Assessment Only inspections.*
- Parent element: [`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *Home Condition Report*
    - **"2"** - *RdSAP Energy Performance Certificate*
    - **"3"** - *SAP Energy Performance Certificate*
    - **"4"** - *Interim RdSAP Energy Performance Certificate (to be superseded by SAP EPC)*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Completion-Date"></a>Completion-Date

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Completion-Date`](#SAP-Compliance-Report/SAP-Report/Report-Header/Completion-Date)/

- Documentation: *The date that the Home Inspector completed the report. This will be after the Inspection Date but generally before the Registration Date.*
- Parent element: [`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)
- Has text value: *True*
- Data type: *<built-in method fromisoformat of type object at 0x00007FFB580DD990>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Registration-Date"></a>Registration-Date

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Registration-Date`](#SAP-Compliance-Report/SAP-Report/Report-Header/Registration-Date)/

- Documentation: *The date that the report was submitted to the HCR Registration Organisation for lodging in the HCR Register.*
- Parent element: [`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)
- Has text value: *True*
- Data type: *<built-in method fromisoformat of type object at 0x00007FFB580DD990>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Status"></a>Status

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Status`](#SAP-Compliance-Report/SAP-Report/Report-Header/Status)/

- Documentation: *The Status of the Report. A Home Condition Report can have a number of distinct states depending on whereabouts in its overall lifecycle the HCR is - see Home Condition Report Statechart for more details.*
- Parent element: [`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"cancelled"** - *Cancelled*
    - **"entered"** - *entered on the register*
    - **"appeal"** - *under appeal*
    - **"removed"** - *removed*
    - **"rejected"** - *rejected*
    - **"under investigation"** - *under investigation*
    - **"not for issue"** - *not for issue*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Language-Code"></a>Language-Code

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Language-Code`](#SAP-Compliance-Report/SAP-Report/Report-Header/Language-Code)/

- Documentation: *The language that the report is written in.*
- Parent element: [`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *English*
    - **"2"** - *Welsh*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Tenure"></a>Tenure

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Tenure`](#SAP-Compliance-Report/SAP-Report/Report-Header/Tenure)/

- Parent element: [`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *owner-occupied*
    - **"2"** - *rented (social)*
    - **"3"** - *rented (private)*
    - **"ND"** - *unknown*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Transaction-Type"></a>Transaction-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Transaction-Type`](#SAP-Compliance-Report/SAP-Report/Report-Header/Transaction-Type)/

- Parent element: [`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *marketed sale*
    - **"2"** - *non marketed sale*
    - **"3"** - *rental (social) - this is for backwards compatibility only and should not be used*
    - **"4"** - *rental (private) - this is for backwards compatibility only and should not be used*
    - **"5"** - *none of the above*
    - **"6"** - *new dwelling*
    - **"7"** - *not recorded - this is for backwards compatibility only and should not be used*
    - **"8"** - *rental*
    - **"9"** - *assessment for green deal*
    - **"10"** - *following green deal*
    - **"11"** - *FiT application*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Seller-Commission-Report"></a>Seller-Commission-Report

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Seller-Commission-Report`](#SAP-Compliance-Report/SAP-Report/Report-Header/Seller-Commission-Report)/

- Documentation: *Indicates that the HCR was commissioned by the Seller of the Property or their Agent. This is required in order to differentiate these reports from Buyer commisioned reports which are not eligible for inclusion in a Home Information Pack*
- Parent element: [`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"Y"** - *Yes*
    - **"N"** - *No*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Property-Type"></a>Property-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Property-Type`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property-Type)/

- Documentation: *Describes the type of Property that is being inspected. This should be the same as the Property-Type recorded in the Property-Details section.*
- Parent element: [`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"0"** - *House*
    - **"1"** - *Bungalow*
    - **"2"** - *Flat*
    - **"3"** - *Maisonette*
    - **"4"** - *Park home*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector"></a>Home-Inspector

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)/

- Documentation2: *A Certified Home Inspector is a person certified by a Certification Scheme - that is they exist on the Home Inspector Register - as being qualified to carry out a Home Inspection and produce a Home Condition Report. The exact criteria for fit + proper are laid down in regulations and the Business Standards and it is the responsibility of the Certification Scheme to carry out sufficient checks to ensure those criteria are adhered to. Although covered by a different regulatory regime a Home Inspector and Energy Assessor serve synonymous roles in the product of a Home Condition Report or Energy Performance Certificate respectively.*
- Parent element: [`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)
- Child elements: [`Name`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Name) [`Notify-Lodgement`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Notify-Lodgement) [`Contact-Address`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address) [`Web-Site`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Web-Site) [`E-Mail`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/E-Mail) [`Fax`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Fax) [`Telephone`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Telephone) [`Company-Name`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Company-Name) [`Scheme-Name`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Scheme-Name) [`Scheme-Web-Site`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Scheme-Web-Site) [`Identification-Number`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Identification-Number)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Name"></a>Name

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)/[`Name`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Name)/

- Documentation: *The name by which the Home Inspector is registered. This is a structured name containing prefix, first name + surname.*
- Parent element: [`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Notify-Lodgement"></a>Notify-Lodgement

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)/[`Notify-Lodgement`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Notify-Lodgement)/

- Documentation: *Indicates whether the assessor wants to be notified that a the report has been lodged in the register*
- Parent element: [`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"Y"** - *Yes*
    - **"N"** - *No*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address"></a>Contact-Address

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)/[`Contact-Address`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address)/

- Documentation: *The address that any written correspondence can be sent to. This is not the same as the Registered Address because it may, of course, be a Post Office Box.*
- Documentation2: *An address is composed of a number of structured elements such as Postcode, Post-Town, Street etc.*
- Parent element: [`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)
- Child elements: [`Address-Line-1`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Address-Line-1) [`Address-Line-2`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Address-Line-2) [`Address-Line-3`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Address-Line-3) [`Post-Town`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Post-Town) [`Postcode`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Postcode)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Address-Line-1"></a>Address-Line-1

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)/[`Contact-Address`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address)/[`Address-Line-1`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Address-Line-1)/

- Parent element: [`Contact-Address`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Address-Line-2"></a>Address-Line-2

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)/[`Contact-Address`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address)/[`Address-Line-2`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Address-Line-2)/

- Parent element: [`Contact-Address`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Address-Line-3"></a>Address-Line-3

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)/[`Contact-Address`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address)/[`Address-Line-3`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Address-Line-3)/

- Parent element: [`Contact-Address`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Post-Town"></a>Post-Town

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)/[`Contact-Address`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address)/[`Post-Town`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Post-Town)/

- Parent element: [`Contact-Address`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Postcode"></a>Postcode

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)/[`Contact-Address`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address)/[`Postcode`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Postcode)/

- Documentation: *The Postcode for the Address*
- Parent element: [`Contact-Address`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Web-Site"></a>Web-Site

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)/[`Web-Site`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Web-Site)/

- Parent element: [`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/E-Mail"></a>E-Mail

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)/[`E-Mail`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/E-Mail)/

- Documentation: *the E-Mail address that the Authorised User can be contacted at.*
- Parent element: [`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Fax"></a>Fax

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)/[`Fax`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Fax)/

- Parent element: [`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Telephone"></a>Telephone

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)/[`Telephone`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Telephone)/

- Parent element: [`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Company-Name"></a>Company-Name

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)/[`Company-Name`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Company-Name)/

- Documentation: *The Name of the Company that the assessor is employed by.*
- Parent element: [`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Scheme-Name"></a>Scheme-Name

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)/[`Scheme-Name`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Scheme-Name)/

- Parent element: [`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Scheme-Web-Site"></a>Scheme-Web-Site

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)/[`Scheme-Web-Site`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Scheme-Web-Site)/

- Parent element: [`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Identification-Number"></a>Identification-Number

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)/[`Identification-Number`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Identification-Number)/

- Parent element: [`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)
- Child elements: [`Certificate-Number`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Identification-Number/Certificate-Number) [`Membership-Number`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Identification-Number/Membership-Number)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Identification-Number/Certificate-Number"></a>Certificate-Number

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)/[`Identification-Number`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Identification-Number)/[`Certificate-Number`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Identification-Number/Certificate-Number)/

- Documentation: *The unique identifier assigned to the assessor by the scheme by which they can be identified throughout their membership of the scheme.*
- Parent element: [`Identification-Number`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Identification-Number)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Identification-Number/Membership-Number"></a>Membership-Number

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Home-Inspector`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector)/[`Identification-Number`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Identification-Number)/[`Membership-Number`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Identification-Number/Membership-Number)/

- Documentation: *For Scottish DEAs only*
- Parent element: [`Identification-Number`](#SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Identification-Number)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Property"></a>Property

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Property`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property)/

- Documentation2: *A discrete identifiable possession, such as a piece of real-estate, to which its owner has legal title. For the Home Information Pack legislation the types of property are restricted to residential properties. It should be observed that "a property is a property is a property" and all real-estate properties, whether residential or commercial or whether being sold for the first or the nth time will have a very similar conceptual structure and similar rules and constraints. As such the broad description of a Property can be regarded as a framework, containing a set of extension points, that can be expanded as necessary to cover additional detail.*
- Parent element: [`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)
- Child elements: [`Address`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address) [`UPRN`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property/UPRN) [`Site-Reference`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property/Site-Reference) [`Plot-Reference`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property/Plot-Reference)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address"></a>Address

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Property`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property)/[`Address`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address)/

- Documentation: *Address for the property.*
- Documentation2: *An address is composed of a number of structured elements such as Postcode, Post-Town, Street etc.*
- Parent element: [`Property`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property)
- Child elements: [`Address-Line-1`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Address-Line-1) [`Address-Line-2`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Address-Line-2) [`Address-Line-3`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Address-Line-3) [`Post-Town`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Post-Town) [`Postcode`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Postcode)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Address-Line-1"></a>Address-Line-1

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Property`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property)/[`Address`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address)/[`Address-Line-1`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Address-Line-1)/

- Parent element: [`Address`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Address-Line-2"></a>Address-Line-2

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Property`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property)/[`Address`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address)/[`Address-Line-2`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Address-Line-2)/

- Parent element: [`Address`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Address-Line-3"></a>Address-Line-3

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Property`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property)/[`Address`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address)/[`Address-Line-3`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Address-Line-3)/

- Parent element: [`Address`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Post-Town"></a>Post-Town

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Property`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property)/[`Address`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address)/[`Post-Town`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Post-Town)/

- Parent element: [`Address`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Postcode"></a>Postcode

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Property`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property)/[`Address`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address)/[`Postcode`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Postcode)/

- Documentation: *The Postcode for the Address*
- Parent element: [`Address`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Property/UPRN"></a>UPRN

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Property`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property)/[`UPRN`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property/UPRN)/

- Documentation: *Unique Property Reference Number*
- Parent element: [`Property`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Property/Site-Reference"></a>Site-Reference

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Property`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property)/[`Site-Reference`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property/Site-Reference)/

- Documentation: *A site reference*
- Parent element: [`Property`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Property/Plot-Reference"></a>Plot-Reference

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Property`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property)/[`Plot-Reference`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property/Plot-Reference)/

- Documentation: *A plot reference*
- Parent element: [`Property`](#SAP-Compliance-Report/SAP-Report/Report-Header/Property)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Region-Code"></a>Region-Code

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Region-Code`](#SAP-Compliance-Report/SAP-Report/Report-Header/Region-Code)/

- Documentation: *Region within the UK.*
- Parent element: [`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *Borders*
    - **"2"** - *East Anglia*
    - **"3"** - *East Pennines*
    - **"4"** - *East Scotland*
    - **"5"** - *Highland*
    - **"6"** - *Midlands*
    - **"7"** - *North East England*
    - **"8"** - *North East Scotland*
    - **"9"** - *North West England / South West Scotland*
    - **"10"** - *Northern Ireland*
    - **"11"** - *Orkney*
    - **"12"** - *Severn Valley*
    - **"13"** - *Shetland*
    - **"14"** - *South East England*
    - **"15"** - *South West England*
    - **"16"** - *Southern England*
    - **"17"** - *Thames Valley*
    - **"18"** - *Wales*
    - **"19"** - *West Pennines*
    - **"20"** - *West Scotland*
    - **"21"** - *Western Isles*
    - **"22"** - *Jersey*
    - **"23"** - *Guernsey*
    - **"24"** - *Isle of Man*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Country-Code"></a>Country-Code

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Country-Code`](#SAP-Compliance-Report/SAP-Report/Report-Header/Country-Code)/

- Documentation: *Country within the UK.*
- Parent element: [`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"EAW"** - *England and Wales, for backwards compatibility only.*
    - **"ENG"** - *England*
    - **"WLS"** - *Wales*
    - **"SCT"** - *Scotland*
    - **"NIR"** - *Northern Ireland*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Related-Party-Disclosure"></a>Related-Party-Disclosure

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Related-Party-Disclosure`](#SAP-Compliance-Report/SAP-Report/Report-Header/Related-Party-Disclosure)/

- Parent element: [`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)
- Child elements: [`Related-Party-Disclosure-Text`](#SAP-Compliance-Report/SAP-Report/Report-Header/Related-Party-Disclosure/Related-Party-Disclosure-Text) [`Related-Party-Disclosure-Number`](#SAP-Compliance-Report/SAP-Report/Report-Header/Related-Party-Disclosure/Related-Party-Disclosure-Number)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Related-Party-Disclosure/Related-Party-Disclosure-Text"></a>Related-Party-Disclosure-Text

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Related-Party-Disclosure`](#SAP-Compliance-Report/SAP-Report/Report-Header/Related-Party-Disclosure)/[`Related-Party-Disclosure-Text`](#SAP-Compliance-Report/SAP-Report/Report-Header/Related-Party-Disclosure/Related-Party-Disclosure-Text)/

- Documentation: *For backward compatibility only.*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: [`Related-Party-Disclosure`](#SAP-Compliance-Report/SAP-Report/Report-Header/Related-Party-Disclosure)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Report-Header/Related-Party-Disclosure/Related-Party-Disclosure-Number"></a>Related-Party-Disclosure-Number

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Report-Header`](#SAP-Compliance-Report/SAP-Report/Report-Header)/[`Related-Party-Disclosure`](#SAP-Compliance-Report/SAP-Report/Report-Header/Related-Party-Disclosure)/[`Related-Party-Disclosure-Number`](#SAP-Compliance-Report/SAP-Report/Report-Header/Related-Party-Disclosure/Related-Party-Disclosure-Number)/

- Documentation: *Code indicating any potential conflicts of interest or commercial relationships with other parties.*
- Parent element: [`Related-Party-Disclosure`](#SAP-Compliance-Report/SAP-Report/Report-Header/Related-Party-Disclosure)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *No related party*
    - **"2"** - *Relative of homeowner or of occupier of the property*
    - **"3"** - *Residing at the property*
    - **"4"** - *Financial interest in the property*
    - **"5"** - *Owner or Director of the organisation dealing with the property transaction*
    - **"6"** - *Employed by the professional dealing with the property transaction*
    - **"7"** - *Relative of the professional dealing with the property transaction*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment"></a>Energy-Assessment

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/

- Documentation2: *Energy Efficiency Assessment Report is an inspection report whose purpose is to assess the energy efficiency of the inspected property and provide energy ratings for the significant heat-loss features of the property. The report also identifies a number of potential improvements that may be made to the property in order to increase the energy efficiency.*
- Parent element: [`SAP-Report`](#SAP-Compliance-Report/SAP-Report)
- Child elements: [`Assessment-Date`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Assessment-Date) [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary) [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use) [`Suggested-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements) [`LZC-Energy-Sources`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/LZC-Energy-Sources) [`Renewable-Heat-Incentive`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive) [`Green-Deal-Package`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package) [`Alternative-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements) [`Addendum`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Assessment-Date"></a>Assessment-Date

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Assessment-Date`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Assessment-Date)/

- Documentation: *Date of assessment.*
- Parent element: [`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)
- Has text value: *True*
- Data type: *<built-in method fromisoformat of type object at 0x00007FFB580DD990>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary"></a>Property-Summary

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/

- Parent element: [`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)
- Child elements: [`Walls`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls) [`Roof`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof) [`Floor`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor) [`Windows`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows) [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating) [`Main-Heating-Controls`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls) [`Secondary-Heating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating) [`Hot-Water`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water) [`Lighting`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting) [`Air-Tightness`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness) [`Has-Fixed-Air-Conditioning`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Has-Fixed-Air-Conditioning) [`Has-Hot-Water-Cylinder`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Has-Hot-Water-Cylinder) [`Has-Heated-Separate-Conservatory`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Has-Heated-Separate-Conservatory) [`Dwelling-Type`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Dwelling-Type) [`Total-Floor-Area`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Total-Floor-Area) [`Multiple-Glazed-Percentage`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Multiple-Glazed-Percentage) [`Multiple-Glazed-Percentage-NR`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Multiple-Glazed-Percentage-NR) [`Is-Zero-Carbon-Home`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Is-Zero-Carbon-Home)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls"></a>Walls

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Walls`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls)/

- Parent element: [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)
- Child elements: [`Description`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls/Description) [`Energy-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls/Energy-Efficiency-Rating) [`Environmental-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls/Environmental-Efficiency-Rating)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **unbounded**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls/Description"></a>Description

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Walls`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls)/[`Description`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls/Description)/

- Documentation: *Overall description of the property feature*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: [`Walls`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls/Energy-Efficiency-Rating"></a>Energy-Efficiency-Rating

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Walls`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls)/[`Energy-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls/Energy-Efficiency-Rating)/

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: [`Walls`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls/Environmental-Efficiency-Rating"></a>Environmental-Efficiency-Rating

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Walls`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls)/[`Environmental-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls/Environmental-Efficiency-Rating)/

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: [`Walls`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof"></a>Roof

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Roof`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof)/

- Parent element: [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)
- Child elements: [`Description`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof/Description) [`Energy-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof/Energy-Efficiency-Rating) [`Environmental-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof/Environmental-Efficiency-Rating)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **unbounded**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof/Description"></a>Description

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Roof`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof)/[`Description`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof/Description)/

- Documentation: *Overall description of the property feature*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: [`Roof`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof/Energy-Efficiency-Rating"></a>Energy-Efficiency-Rating

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Roof`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof)/[`Energy-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof/Energy-Efficiency-Rating)/

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: [`Roof`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof/Environmental-Efficiency-Rating"></a>Environmental-Efficiency-Rating

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Roof`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof)/[`Environmental-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof/Environmental-Efficiency-Rating)/

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: [`Roof`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor"></a>Floor

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Floor`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor)/

- Parent element: [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)
- Child elements: [`Description`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor/Description) [`Energy-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor/Energy-Efficiency-Rating) [`Environmental-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor/Environmental-Efficiency-Rating)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **unbounded**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor/Description"></a>Description

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Floor`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor)/[`Description`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor/Description)/

- Documentation: *Overall description of the property feature*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: [`Floor`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor/Energy-Efficiency-Rating"></a>Energy-Efficiency-Rating

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Floor`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor)/[`Energy-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor/Energy-Efficiency-Rating)/

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: [`Floor`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor/Environmental-Efficiency-Rating"></a>Environmental-Efficiency-Rating

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Floor`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor)/[`Environmental-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor/Environmental-Efficiency-Rating)/

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: [`Floor`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows"></a>Windows

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Windows`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows)/

- Parent element: [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)
- Child elements: [`Description`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows/Description) [`Energy-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows/Energy-Efficiency-Rating) [`Environmental-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows/Environmental-Efficiency-Rating)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows/Description"></a>Description

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Windows`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows)/[`Description`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows/Description)/

- Documentation: *Overall description of the property feature*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: [`Windows`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows/Energy-Efficiency-Rating"></a>Energy-Efficiency-Rating

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Windows`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows)/[`Energy-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows/Energy-Efficiency-Rating)/

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: [`Windows`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows/Environmental-Efficiency-Rating"></a>Environmental-Efficiency-Rating

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Windows`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows)/[`Environmental-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows/Environmental-Efficiency-Rating)/

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: [`Windows`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating"></a>Main-Heating

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating)/

- Parent element: [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)
- Child elements: [`Description`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating/Description) [`Energy-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating/Energy-Efficiency-Rating) [`Environmental-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating/Environmental-Efficiency-Rating)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **2**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating/Description"></a>Description

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating)/[`Description`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating/Description)/

- Documentation: *Overall description of the property feature*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating/Energy-Efficiency-Rating"></a>Energy-Efficiency-Rating

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating)/[`Energy-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating/Energy-Efficiency-Rating)/

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating/Environmental-Efficiency-Rating"></a>Environmental-Efficiency-Rating

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating)/[`Environmental-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating/Environmental-Efficiency-Rating)/

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls"></a>Main-Heating-Controls

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Main-Heating-Controls`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls)/

- Parent element: [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)
- Child elements: [`Description`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls/Description) [`Energy-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls/Energy-Efficiency-Rating) [`Environmental-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls/Environmental-Efficiency-Rating)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **2**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls/Description"></a>Description

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Main-Heating-Controls`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls)/[`Description`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls/Description)/

- Documentation: *Overall description of the property feature*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: [`Main-Heating-Controls`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls/Energy-Efficiency-Rating"></a>Energy-Efficiency-Rating

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Main-Heating-Controls`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls)/[`Energy-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls/Energy-Efficiency-Rating)/

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: [`Main-Heating-Controls`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls/Environmental-Efficiency-Rating"></a>Environmental-Efficiency-Rating

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Main-Heating-Controls`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls)/[`Environmental-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls/Environmental-Efficiency-Rating)/

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: [`Main-Heating-Controls`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating"></a>Secondary-Heating

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Secondary-Heating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating)/

- Parent element: [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)
- Child elements: [`Description`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating/Description) [`Energy-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating/Energy-Efficiency-Rating) [`Environmental-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating/Environmental-Efficiency-Rating)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating/Description"></a>Description

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Secondary-Heating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating)/[`Description`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating/Description)/

- Documentation: *Overall description of the property feature*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: [`Secondary-Heating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating/Energy-Efficiency-Rating"></a>Energy-Efficiency-Rating

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Secondary-Heating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating)/[`Energy-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating/Energy-Efficiency-Rating)/

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: [`Secondary-Heating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating/Environmental-Efficiency-Rating"></a>Environmental-Efficiency-Rating

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Secondary-Heating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating)/[`Environmental-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating/Environmental-Efficiency-Rating)/

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: [`Secondary-Heating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water"></a>Hot-Water

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Hot-Water`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water)/

- Parent element: [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)
- Child elements: [`Description`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water/Description) [`Energy-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water/Energy-Efficiency-Rating) [`Environmental-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water/Environmental-Efficiency-Rating)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water/Description"></a>Description

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Hot-Water`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water)/[`Description`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water/Description)/

- Documentation: *Overall description of the property feature*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: [`Hot-Water`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water/Energy-Efficiency-Rating"></a>Energy-Efficiency-Rating

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Hot-Water`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water)/[`Energy-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water/Energy-Efficiency-Rating)/

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: [`Hot-Water`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water/Environmental-Efficiency-Rating"></a>Environmental-Efficiency-Rating

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Hot-Water`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water)/[`Environmental-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water/Environmental-Efficiency-Rating)/

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: [`Hot-Water`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting"></a>Lighting

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Lighting`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting)/

- Parent element: [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)
- Child elements: [`Description`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting/Description) [`Energy-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting/Energy-Efficiency-Rating) [`Environmental-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting/Environmental-Efficiency-Rating)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting/Description"></a>Description

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Lighting`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting)/[`Description`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting/Description)/

- Documentation: *Overall description of the property feature*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: [`Lighting`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting/Energy-Efficiency-Rating"></a>Energy-Efficiency-Rating

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Lighting`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting)/[`Energy-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting/Energy-Efficiency-Rating)/

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: [`Lighting`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting/Environmental-Efficiency-Rating"></a>Environmental-Efficiency-Rating

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Lighting`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting)/[`Environmental-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting/Environmental-Efficiency-Rating)/

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: [`Lighting`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness"></a>Air-Tightness

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Air-Tightness`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness)/

- Parent element: [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)
- Child elements: [`Description`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness/Description) [`Energy-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness/Energy-Efficiency-Rating) [`Environmental-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness/Environmental-Efficiency-Rating)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness/Description"></a>Description

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Air-Tightness`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness)/[`Description`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness/Description)/

- Documentation: *Overall description of the property feature*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: [`Air-Tightness`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness/Energy-Efficiency-Rating"></a>Energy-Efficiency-Rating

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Air-Tightness`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness)/[`Energy-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness/Energy-Efficiency-Rating)/

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: [`Air-Tightness`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness/Environmental-Efficiency-Rating"></a>Environmental-Efficiency-Rating

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Air-Tightness`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness)/[`Environmental-Efficiency-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness/Environmental-Efficiency-Rating)/

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: [`Air-Tightness`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Has-Fixed-Air-Conditioning"></a>Has-Fixed-Air-Conditioning

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Has-Fixed-Air-Conditioning`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Has-Fixed-Air-Conditioning)/

- Documentation: *Fixed air conditioning?*
- Parent element: [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Has-Hot-Water-Cylinder"></a>Has-Hot-Water-Cylinder

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Has-Hot-Water-Cylinder`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Has-Hot-Water-Cylinder)/

- Documentation: *Hot water cylinder?*
- Parent element: [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Has-Heated-Separate-Conservatory"></a>Has-Heated-Separate-Conservatory

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Has-Heated-Separate-Conservatory`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Has-Heated-Separate-Conservatory)/

- Documentation: *Heated separate conservatory?*
- Parent element: [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Dwelling-Type"></a>Dwelling-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Dwelling-Type`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Dwelling-Type)/

- Documentation: *Is a string such as Detached house or Top-floor flat*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Total-Floor-Area"></a>Total-Floor-Area

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Total-Floor-Area`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Total-Floor-Area)/

- Documentation: *Is a number such as 125*
- Parent element: [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Multiple-Glazed-Percentage"></a>Multiple-Glazed-Percentage

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Multiple-Glazed-Percentage`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Multiple-Glazed-Percentage)/

- Documentation: *Fraction of windows that are multiply glazed to nearest 1%.*
- Parent element: [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Multiple-Glazed-Percentage-NR"></a>Multiple-Glazed-Percentage-NR

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Multiple-Glazed-Percentage-NR`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Multiple-Glazed-Percentage-NR)/

- Documentation: *For backward compatibility only, do not use.*
- Parent element: [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Is-Zero-Carbon-Home"></a>Is-Zero-Carbon-Home

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)/[`Is-Zero-Carbon-Home`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Is-Zero-Carbon-Home)/

- Documentation: *Is dwelling a Zero Carbon Home?*
- Parent element: [`Property-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use"></a>Energy-Use

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)/

- Documentation: *Calculated results from the energy assessment.*
- Documentation2: *Part of an Energy Report summarising the results of the various energy calculations made by the Home Inspector.*
- Parent element: [`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)
- Child elements: [`DER`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/DER) [`TER`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/TER) [`DPER`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/DPER) [`TPER`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/TPER) [`DFEE`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/DFEE) [`TFEE`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/TFEE) [`Energy-Rating-Current`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Rating-Current) [`Energy-Rating-Potential`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Rating-Potential) [`Energy-Rating-Average`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Rating-Average) [`Environmental-Impact-Current`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Environmental-Impact-Current) [`Environmental-Impact-Potential`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Environmental-Impact-Potential) [`Energy-Consumption-Current`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Consumption-Current) [`Energy-Consumption-Potential`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Consumption-Potential) [`CO2-Emissions-Current`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/CO2-Emissions-Current) [`CO2-Emissions-Current-Per-Floor-Area`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/CO2-Emissions-Current-Per-Floor-Area) [`CO2-Emissions-Potential`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/CO2-Emissions-Potential) [`Lighting-Cost-Current`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Lighting-Cost-Current) [`Lighting-Cost-Potential`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Lighting-Cost-Potential) [`Heating-Cost-Current`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Heating-Cost-Current) [`Heating-Cost-Potential`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Heating-Cost-Potential) [`Hot-Water-Cost-Current`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Hot-Water-Cost-Current) [`Hot-Water-Cost-Potential`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Hot-Water-Cost-Potential)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/DER"></a>DER

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)/[`DER`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/DER)/

- Documentation: *The DER of the Property*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/TER"></a>TER

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)/[`TER`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/TER)/

- Documentation: *The TER of the Property*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/DPER"></a>DPER

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)/[`DPER`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/DPER)/

- Documentation: *The DPER of the Property*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/TPER"></a>TPER

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)/[`TPER`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/TPER)/

- Documentation: *The TPER of the Property*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/DFEE"></a>DFEE

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)/[`DFEE`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/DFEE)/

- Documentation: *The DFEE of the Property*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/TFEE"></a>TFEE

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)/[`TFEE`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/TFEE)/

- Documentation: *The TFEE of the Property*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Rating-Current"></a>Energy-Rating-Current

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)/[`Energy-Rating-Current`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Rating-Current)/

- Documentation: *The Current Energy Rating of the Property*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Rating-Potential"></a>Energy-Rating-Potential

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)/[`Energy-Rating-Potential`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Rating-Potential)/

- Documentation: *The overall Energy Rating for the Property being assessed.*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Rating-Average"></a>Energy-Rating-Average

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)/[`Energy-Rating-Average`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Rating-Average)/

- Documentation: *Average SAP rating for the country concerned. 0 if unknown or not applicable*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Environmental-Impact-Current"></a>Environmental-Impact-Current

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)/[`Environmental-Impact-Current`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Environmental-Impact-Current)/

- Documentation: *The estimated current Environmental Impact Rating of the property*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Environmental-Impact-Potential"></a>Environmental-Impact-Potential

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)/[`Environmental-Impact-Potential`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Environmental-Impact-Potential)/

- Documentation: *The estimated potential Environmental Impact Rating of the property*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Consumption-Current"></a>Energy-Consumption-Current

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)/[`Energy-Consumption-Current`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Consumption-Current)/

- Documentation: *Estimated total energy consumption for the Property in a 12 month period. Value is Kilowatt Hours per Square Metre (kWh/m2)*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Consumption-Potential"></a>Energy-Consumption-Potential

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)/[`Energy-Consumption-Potential`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Consumption-Potential)/

- Documentation: *Estimated total energy consumption for the Property in a 12 month period. Value is Kilowatt Hours per Square Metre (kWh/m2)*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/CO2-Emissions-Current"></a>CO2-Emissions-Current

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)/[`CO2-Emissions-Current`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/CO2-Emissions-Current)/

- Documentation: *CO2 emissions per year in tonnes/year.*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/CO2-Emissions-Current-Per-Floor-Area"></a>CO2-Emissions-Current-Per-Floor-Area

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)/[`CO2-Emissions-Current-Per-Floor-Area`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/CO2-Emissions-Current-Per-Floor-Area)/

- Documentation: *CO2 emissions per square metre floor area per year in kg/m2.*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/CO2-Emissions-Potential"></a>CO2-Emissions-Potential

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)/[`CO2-Emissions-Potential`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/CO2-Emissions-Potential)/

- Documentation: *Estimated value in Tonnes per Year of the total CO2 emissions produced by the Property in 12 month period.*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Lighting-Cost-Current"></a>Lighting-Cost-Current

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)/[`Lighting-Cost-Current`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Lighting-Cost-Current)/

- Documentation: *The current estimated cost of Lighting for the property*
- Documentation2: *Extension of a Decimal value for use with monetary values where a currency code needs to be specified. The currency code is actually metadata about the value so, in line with good XML practice, the Currency Code is declared as an XML-Attribute of the Money datatype rather than as a separate XML-Element. The currency attribute should then include a list of valid currencies codes that are supported.*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Lighting-Cost-Potential"></a>Lighting-Cost-Potential

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)/[`Lighting-Cost-Potential`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Lighting-Cost-Potential)/

- Documentation: *The current estimated cost of Lighting for the property*
- Documentation2: *Extension of a Decimal value for use with monetary values where a currency code needs to be specified. The currency code is actually metadata about the value so, in line with good XML practice, the Currency Code is declared as an XML-Attribute of the Money datatype rather than as a separate XML-Element. The currency attribute should then include a list of valid currencies codes that are supported.*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Heating-Cost-Current"></a>Heating-Cost-Current

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)/[`Heating-Cost-Current`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Heating-Cost-Current)/

- Documentation: *The current estimated cost of Heating for the property*
- Documentation2: *Extension of a Decimal value for use with monetary values where a currency code needs to be specified. The currency code is actually metadata about the value so, in line with good XML practice, the Currency Code is declared as an XML-Attribute of the Money datatype rather than as a separate XML-Element. The currency attribute should then include a list of valid currencies codes that are supported.*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Heating-Cost-Potential"></a>Heating-Cost-Potential

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)/[`Heating-Cost-Potential`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Heating-Cost-Potential)/

- Documentation: *The current estimated cost of Heating for the property*
- Documentation2: *Extension of a Decimal value for use with monetary values where a currency code needs to be specified. The currency code is actually metadata about the value so, in line with good XML practice, the Currency Code is declared as an XML-Attribute of the Money datatype rather than as a separate XML-Element. The currency attribute should then include a list of valid currencies codes that are supported.*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Hot-Water-Cost-Current"></a>Hot-Water-Cost-Current

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)/[`Hot-Water-Cost-Current`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Hot-Water-Cost-Current)/

- Documentation: *|The current estimated cost of Hot Water for the property*
- Documentation2: *Extension of a Decimal value for use with monetary values where a currency code needs to be specified. The currency code is actually metadata about the value so, in line with good XML practice, the Currency Code is declared as an XML-Attribute of the Money datatype rather than as a separate XML-Element. The currency attribute should then include a list of valid currencies codes that are supported.*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Hot-Water-Cost-Potential"></a>Hot-Water-Cost-Potential

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)/[`Hot-Water-Cost-Potential`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Hot-Water-Cost-Potential)/

- Documentation: *|The current estimated cost of Hot Water for the property*
- Documentation2: *Extension of a Decimal value for use with monetary values where a currency code needs to be specified. The currency code is actually metadata about the value so, in line with good XML practice, the Currency Code is declared as an XML-Attribute of the Money datatype rather than as a separate XML-Element. The currency attribute should then include a list of valid currencies codes that are supported.*
- Parent element: [`Energy-Use`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements"></a>Suggested-Improvements

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Suggested-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements)/

- Documentation: *Improvement measures listed on the EPC.*
- Documentation2: *Part of an Energy Report that describes the a set of improvements that the Home Inspector considers would contribute to the overall energy rating of the property.*
- Parent element: [`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)
- Child elements: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement"></a>Improvement

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Suggested-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements)/[`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement)/

- Parent element: [`Suggested-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements)
- Child elements: [`Sequence`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Sequence) [`Improvement-Category`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Category) [`Improvement-Type`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Type) [`Typical-Saving`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Typical-Saving) [`Energy-Performance-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Energy-Performance-Rating) [`Environmental-Impact-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Environmental-Impact-Rating) [`Improvement-Details`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details) [`Indicative-Cost`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Indicative-Cost) [`Green-Deal-Category`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Green-Deal-Category)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **unbounded**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Sequence"></a>Sequence

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Suggested-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements)/[`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement)/[`Sequence`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Sequence)/

- Documentation: *Sequence of the Suggested Improvements within the set of Suggested Improvements. This is used to order the Recommendations on the output HCR / EPC so that the cumulative Ratings make sense. The Improved Energy Ratings that result from carrying out a Suggested Improvement are cumulative and assume that the improvements have been installed in the order they appear in the list. Hence they must be sequenced.*
- Parent element: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Category"></a>Improvement-Category

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Suggested-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements)/[`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement)/[`Improvement-Category`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Category)/

- Documentation: *The category of improvement. This identifies where on the report the recommendation is printed.*
- Parent element: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *Lower cost - this is for backwards compatibility only and should not be used*
    - **"2"** - *Higher cost - this is for backwards compatibility only and should not be used*
    - **"3"** - *Further measure - this is for backwards compatibility only and should not be used*
    - **"4"** - *Deselected. This is for backwards compatibility only and should not be used.*
    - **"5"** - *Normal measure*
    - **"6"** - *Alternative measure*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Type"></a>Improvement-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Suggested-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements)/[`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement)/[`Improvement-Type`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Type)/

- Documentation: *Suggested work to be carried out on the Property to improve its energy efficiency. This should be a enumerated list of acceptable improvements but it hasn't yet been defined.*
- Parent element: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"A"** - *Loft insulation*
    - **"A2"** - *Flat roof insulation*
    - **"A3"** - *Room-in-roof insulation*
    - **"B"** - *Cavity wall insulation*
    - **"C"** - *Hot water cylinder insulation*
    - **"D"** - *Draughtproofing*
    - **"E"** - *Low energy lights*
    - **"F"** - *Cylinder thermostat*
    - **"G"** - *Heating controls for wet central heating system*
    - **"H"** - *Heating controls for warm air system*
    - **"I"** - *Upgrade boiler, same fuel*
    - **"J"** - *Biomass boiler*
    - **"J2"** - *Biomass boiler as alternative improvement*
    - **"K"** - *Biomass room heater with boiler*
    - **"L"** - *New or replacement fan-assisted storage heaters*
    - **"L2"** - *New or replacement high heat retention storage heaters*
    - **"M"** - *Replacement warm-air unit*
    - **"N"** - *Solar water heating*
    - **"O"** - *Replacement double glazed windows*
    - **"O3"** - *Replacement double glazing units*
    - **"P"** - *Secondary glazing*
    - **"Q"** - *Solid wall insulation*
    - **"Q2"** - *External insulation with cavity wall insulation*
    - **"R"** - *Condensing oil boiler*
    - **"S"** - *Change heating to Band A gas condensing boiler (no fuel switch)*
    - **"T"** - *Change heating to Band A gas condensing boiler (fuel switch)*
    - **"T2"** - *Flue gas heat recovery*
    - **"U"** - *Photovoltaics*
    - **"V"** - *Wind turbine (roof mounted)*
    - **"V2"** - *Wind turbine (on mast)*
    - **"W"** - *Floor insulation*
    - **"X"** - *Insulated doors*
    - **"Y"** - *Instantaneous waste water heat recovery*
    - **"Y2"** - *Storage waste water heat recovery*
    - **"Z1"** - *Air or ground source heat pump*
    - **"Z2"** - *Air or ground source heat pump with underfloor heating*
    - **"Z3"** - *Micro-CHP*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Typical-Saving"></a>Typical-Saving

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Suggested-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements)/[`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement)/[`Typical-Saving`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Typical-Saving)/

- Documentation: *Typical savings (in British Pounds) per year if the suggested improvement is carried out. 0 if not assessed*
- Documentation2: *Extension of a Decimal value for use with monetary values where a currency code needs to be specified. The currency code is actually metadata about the value so, in line with good XML practice, the Currency Code is declared as an XML-Attribute of the Money datatype rather than as a separate XML-Element. The currency attribute should then include a list of valid currencies codes that are supported.*
- Parent element: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Energy-Performance-Rating"></a>Energy-Performance-Rating

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Suggested-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements)/[`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement)/[`Energy-Performance-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Energy-Performance-Rating)/

- Documentation: *The estimated Energy performance rating of the Property after the Suggested Improvement has been carried out providing any preceding Suggested Improvement has also been carried out. 0 if not assessed*
- Parent element: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Environmental-Impact-Rating"></a>Environmental-Impact-Rating

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Suggested-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements)/[`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement)/[`Environmental-Impact-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Environmental-Impact-Rating)/

- Documentation: *The estimated Environmental Impact rating of the Property after the Suggested Improvement has been carried out providing any preceding Suggested Improvement has also been carried out. 0 if not assessed*
- Parent element: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details"></a>Improvement-Details

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Suggested-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements)/[`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement)/[`Improvement-Details`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details)/

- Parent element: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement)
- Child elements: [`Improvement-Texts`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts) [`Improvement-Number`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Number)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts"></a>Improvement-Texts

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Suggested-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements)/[`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement)/[`Improvement-Details`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details)/[`Improvement-Texts`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts)/

- Documentation: *For backward compatability only*
- Parent element: [`Improvement-Details`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details)
- Child elements: [`Improvement-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Summary) [`Improvement-Heading`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Heading) [`Improvement-Description`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Description)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Summary"></a>Improvement-Summary

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Suggested-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements)/[`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement)/[`Improvement-Details`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details)/[`Improvement-Texts`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts)/[`Improvement-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Summary)/

- Documentation: *A short description of the suggested improvement.*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: [`Improvement-Texts`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Heading"></a>Improvement-Heading

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Suggested-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements)/[`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement)/[`Improvement-Details`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details)/[`Improvement-Texts`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts)/[`Improvement-Heading`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Heading)/

- Documentation: *Text to precede the improvement description. If this field is not provided the 'Improvement-Summary' is used instead.*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: [`Improvement-Texts`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Description"></a>Improvement-Description

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Suggested-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements)/[`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement)/[`Improvement-Details`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details)/[`Improvement-Texts`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts)/[`Improvement-Description`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Description)/

- Documentation: *Detailed description of the suggested improvement.*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: [`Improvement-Texts`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Number"></a>Improvement-Number

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Suggested-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements)/[`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement)/[`Improvement-Details`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details)/[`Improvement-Number`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Number)/

- Parent element: [`Improvement-Details`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *Insulate hot water cylinder with 80 mm jacket*
    - **"2"** - *Increase hot water cylinder insulation*
    - **"3"** - *Add additional 80 mm jacket to hot water cylinder*
    - **"4"** - *Hot water cylinder thermostat*
    - **"5"** - *Increase loft insulation to 270 mm*
    - **"6"** - *Cavity wall insulation*
    - **"7"** - *Internal or external wall insulation*
    - **"8"** - *Replace single glazed windows with low-E double glazing*
    - **"9"** - *Secondary glazing to single glazed windows*
    - **"10"** - *Draught proofing*
    - **"11"** - *Heating controls (programmer, room thermostat and TRVs)*
    - **"12"** - *Heating controls (room thermostat and TRVs)*
    - **"13"** - *Heating controls (thermostatic radiator valves)*
    - **"14"** - *Heating controls (room thermostat)*
    - **"15"** - *Heating controls (programmer and TRVs)*
    - **"16"** - *Heating controls (time and temperature zone control)*
    - **"17"** - *Heating controls (programmer and room thermostat)*
    - **"18"** - *Heating controls (room thermostat)*
    - **"19"** - *Solar water heating*
    - **"20"** - *Replace boiler with new condensing boiler*
    - **"21"** - *Replace boiler with new condensing boiler*
    - **"22"** - *Replace boiler with biomass boiler*
    - **"23"** - *Wood pellet stove with boiler and radiators*
    - **"24"** - *Fan assisted storage heaters and dual immersion cylinder*
    - **"25"** - *Fan assisted storage heaters*
    - **"26"** - *Replacement warm air unit*
    - **"27"** - *Change heating to gas condensing boiler*
    - **"28"** - *Condensing oil boiler with radiators*
    - **"29"** - *Change heating to gas condensing boiler*
    - **"30"** - *Fan assisted storage heaters and dual immersion cylinder*
    - **"31"** - *Fan-assisted storage heaters*
    - **"32"** - *Change heating to gas condensing boiler*
    - **"34"** - *Solar photovoltaic panels, 2.5 kWp*
    - **"35"** - *Low energy lighting for all fixed outlets*
    - **"36"** - *Replace heating unit with condensing unit*
    - **"37"** - *Condensing boiler (separate from the range cooker)*
    - **"38"** - *Condensing boiler (separate from the range cooker)*
    - **"39"** - *Wood pellet stove with boiler and radiators*
    - **"40"** - *Change room heaters to condensing boiler*
    - **"41"** - *Change room heaters to condensing boiler*
    - **"42"** - *Replace heating unit with mains gas condensing unit*
    - **"43"** - *Condensing oil boiler with radiators*
    - **"44"** - *Wind turbine*
    - **"45"** - *Flat roof insulation*
    - **"46"** - *Room-in-roof insulation*
    - **"47"** - *Floor insulation*
    - **"48"** - *High performance external doors*
    - **"49"** - *Heat recovery system for mixer showers*
    - **"50"** - *Flue gas heat recovery device in conjunction with boiler*
    - **"51"** - *Air or ground source heat pump*
    - **"52"** - *Air or ground source heat pump with underfloor heating*
    - **"53"** - *Micro CHP*
    - **"54"** - *Biomass boiler (Exempted Appliance if in Smoke Control Area)*
    - **"55"** - *External insulation with cavity wall insulation*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Indicative-Cost"></a>Indicative-Cost

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Suggested-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements)/[`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement)/[`Indicative-Cost`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Indicative-Cost)/

- Parent element: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Green-Deal-Category"></a>Green-Deal-Category

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Suggested-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements)/[`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement)/[`Green-Deal-Category`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Green-Deal-Category)/

- Parent element: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *1. Not eligible for Green Deal*
    - **"2"** - *2. Eligible with additional finance*
    - **"3"** - *3. Eligible without additional finance*
    - **"NI"** - *Not assessed. Use for alternative measures and for new dwelling EPCs*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/LZC-Energy-Sources"></a>LZC-Energy-Sources

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`LZC-Energy-Sources`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/LZC-Energy-Sources)/

- Documentation2: *Details of low and zero carbon energy source(s) for the property, if any.*
- Parent element: [`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)
- Child elements: [`LZC-Energy-Source`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/LZC-Energy-Sources/LZC-Energy-Source)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/LZC-Energy-Sources/LZC-Energy-Source"></a>LZC-Energy-Source

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`LZC-Energy-Sources`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/LZC-Energy-Sources)/[`LZC-Energy-Source`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/LZC-Energy-Sources/LZC-Energy-Source)/

- Documentation: *Low and zero carbon energy source(s) for the property.*
- Parent element: [`LZC-Energy-Sources`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/LZC-Energy-Sources)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *Biofuel main heating*
    - **"2"** - *Biofuel community heating*
    - **"3"** - *Biofuel community heating for some of heat generation*
    - **"4"** - *Biofuel secondary heating*
    - **"5"** - *Geothermal heat source*
    - **"6"** - *Community combined heat and power*
    - **"7"** - *Ground source heat pump*
    - **"8"** - *Water source heat pump*
    - **"9"** - *Air source heat pump*
    - **"10"** - *Solar water heating*
    - **"11"** - *Solar photovoltaics*
    - **"12"** - *Wind turbine*
    - **"13"** - *Community heat pump*
    - **"14"** - *Hydro-electric generation*
    - **"15"** - *Micro-CHP*
    - **"16"** - *Exhaust air heat pump*
    - **"17"** - *Solar-assisted heat pump*
- Minimum occurrence: **1**
- Maximum occurrence: **unbounded**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive"></a>Renewable-Heat-Incentive

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Renewable-Heat-Incentive`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive)/

- Parent element: [`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)
- Child elements: [`RHI-New-Dwelling`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-New-Dwelling) [`RHI-Existing-Dwelling`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-New-Dwelling"></a>RHI-New-Dwelling

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Renewable-Heat-Incentive`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive)/[`RHI-New-Dwelling`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-New-Dwelling)/

- Parent element: [`Renewable-Heat-Incentive`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive)
- Child elements: [`Space-Heating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-New-Dwelling/Space-Heating) [`Water-Heating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-New-Dwelling/Water-Heating)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-New-Dwelling/Space-Heating"></a>Space-Heating

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Renewable-Heat-Incentive`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive)/[`RHI-New-Dwelling`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-New-Dwelling)/[`Space-Heating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-New-Dwelling/Space-Heating)/

- Documentation: *Space heating requirement.*
- Parent element: [`RHI-New-Dwelling`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-New-Dwelling)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-New-Dwelling/Water-Heating"></a>Water-Heating

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Renewable-Heat-Incentive`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive)/[`RHI-New-Dwelling`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-New-Dwelling)/[`Water-Heating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-New-Dwelling/Water-Heating)/

- Documentation: *Water heating requirement.*
- Parent element: [`RHI-New-Dwelling`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-New-Dwelling)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling"></a>RHI-Existing-Dwelling

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Renewable-Heat-Incentive`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive)/[`RHI-Existing-Dwelling`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling)/

- Parent element: [`Renewable-Heat-Incentive`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive)
- Child elements: [`Space-Heating-Existing-Dwelling`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Space-Heating-Existing-Dwelling) [`Space-Heating-With-Loft-Insulation`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Space-Heating-With-Loft-Insulation) [`Space-Heating-With-Cavity-Insulation`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Space-Heating-With-Cavity-Insulation) [`Space-Heating-With-Loft-And-Cavity-Insulation`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Space-Heating-With-Loft-And-Cavity-Insulation) [`Water-Heating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Water-Heating) [`Impact-Of-Loft-Insulation`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Impact-Of-Loft-Insulation) [`Impact-Of-Cavity-Insulation`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Impact-Of-Cavity-Insulation) [`Impact-Of-Solid-Wall-Insulation`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Impact-Of-Solid-Wall-Insulation)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Space-Heating-Existing-Dwelling"></a>Space-Heating-Existing-Dwelling

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Renewable-Heat-Incentive`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive)/[`RHI-Existing-Dwelling`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling)/[`Space-Heating-Existing-Dwelling`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Space-Heating-Existing-Dwelling)/

- Documentation: *Space heating requirement for existing dwelling.*
- Parent element: [`RHI-Existing-Dwelling`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Space-Heating-With-Loft-Insulation"></a>Space-Heating-With-Loft-Insulation

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Renewable-Heat-Incentive`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive)/[`RHI-Existing-Dwelling`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling)/[`Space-Heating-With-Loft-Insulation`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Space-Heating-With-Loft-Insulation)/

- Documentation: *Space heating requirement after implementation of loft insulation recommendation, omit if loft insulation not recommended. For backwards compatibility only, do not use*
- Parent element: [`RHI-Existing-Dwelling`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Space-Heating-With-Cavity-Insulation"></a>Space-Heating-With-Cavity-Insulation

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Renewable-Heat-Incentive`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive)/[`RHI-Existing-Dwelling`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling)/[`Space-Heating-With-Cavity-Insulation`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Space-Heating-With-Cavity-Insulation)/

- Documentation: *Space heating requirement after implementation of cavity insulation recommendation, omit if cavity insulation not recommended. For backwards compatibility only, do not use*
- Parent element: [`RHI-Existing-Dwelling`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Space-Heating-With-Loft-And-Cavity-Insulation"></a>Space-Heating-With-Loft-And-Cavity-Insulation

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Renewable-Heat-Incentive`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive)/[`RHI-Existing-Dwelling`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling)/[`Space-Heating-With-Loft-And-Cavity-Insulation`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Space-Heating-With-Loft-And-Cavity-Insulation)/

- Documentation: *Space heating requirement after implementation of loft and cavity insulation recommendations, same as existing dwelling if neither is recommended. For backwards compatibility only, do not use*
- Parent element: [`RHI-Existing-Dwelling`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Water-Heating"></a>Water-Heating

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Renewable-Heat-Incentive`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive)/[`RHI-Existing-Dwelling`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling)/[`Water-Heating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Water-Heating)/

- Documentation: *Water heating requirement.*
- Parent element: [`RHI-Existing-Dwelling`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Impact-Of-Loft-Insulation"></a>Impact-Of-Loft-Insulation

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Renewable-Heat-Incentive`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive)/[`RHI-Existing-Dwelling`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling)/[`Impact-Of-Loft-Insulation`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Impact-Of-Loft-Insulation)/

- Documentation: *Reduction in space heating requirement with loft insulation (as negative value). Omit if not applicable*
- Parent element: [`RHI-Existing-Dwelling`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Impact-Of-Cavity-Insulation"></a>Impact-Of-Cavity-Insulation

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Renewable-Heat-Incentive`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive)/[`RHI-Existing-Dwelling`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling)/[`Impact-Of-Cavity-Insulation`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Impact-Of-Cavity-Insulation)/

- Documentation: *Reduction in space heating requirement with cavity insulation (as negative value). Omit if not applicable*
- Parent element: [`RHI-Existing-Dwelling`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Impact-Of-Solid-Wall-Insulation"></a>Impact-Of-Solid-Wall-Insulation

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Renewable-Heat-Incentive`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive)/[`RHI-Existing-Dwelling`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling)/[`Impact-Of-Solid-Wall-Insulation`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Impact-Of-Solid-Wall-Insulation)/

- Documentation: *Reduction in space heating requirement with solid wall insulation (as negative value). Omit if not applicable*
- Parent element: [`RHI-Existing-Dwelling`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package"></a>Green-Deal-Package

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Green-Deal-Package`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package)/

- Documentation: *Improvements that can form a Green Deal package*
- Parent element: [`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)
- Child elements: [`Green-Deal-Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement) [`Electricity-Saving`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Electricity-Saving) [`Gas-Saving`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Gas-Saving) [`Other-Fuel-Saving`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Other-Fuel-Saving)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement"></a>Green-Deal-Improvement

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Green-Deal-Package`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package)/[`Green-Deal-Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement)/

- Documentation: *Improvements from Suggested-Improvements in the Green Deal package*
- Parent element: [`Green-Deal-Package`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package)
- Child elements: [`Improvement-Type`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement/Improvement-Type) [`Improvement-Number`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement/Improvement-Number)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **unbounded**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement/Improvement-Type"></a>Improvement-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Green-Deal-Package`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package)/[`Green-Deal-Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement)/[`Improvement-Type`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement/Improvement-Type)/

- Parent element: [`Green-Deal-Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"A"** - *Loft insulation*
    - **"A2"** - *Flat roof insulation*
    - **"A3"** - *Room-in-roof insulation*
    - **"B"** - *Cavity wall insulation*
    - **"C"** - *Hot water cylinder insulation*
    - **"D"** - *Draughtproofing*
    - **"E"** - *Low energy lights*
    - **"F"** - *Cylinder thermostat*
    - **"G"** - *Heating controls for wet central heating system*
    - **"H"** - *Heating controls for warm air system*
    - **"I"** - *Upgrade boiler, same fuel*
    - **"J"** - *Biomass boiler*
    - **"J2"** - *Biomass boiler as alternative improvement*
    - **"K"** - *Biomass room heater with boiler*
    - **"L"** - *New or replacement fan-assisted storage heaters*
    - **"L2"** - *New or replacement high heat retention storage heaters*
    - **"M"** - *Replacement warm-air unit*
    - **"N"** - *Solar water heating*
    - **"O"** - *Replacement double glazed windows*
    - **"O3"** - *Replacement double glazing units*
    - **"P"** - *Secondary glazing*
    - **"Q"** - *Solid wall insulation*
    - **"Q2"** - *External insulation with cavity wall insulation*
    - **"R"** - *Condensing oil boiler*
    - **"S"** - *Change heating to Band A gas condensing boiler (no fuel switch)*
    - **"T"** - *Change heating to Band A gas condensing boiler (fuel switch)*
    - **"T2"** - *Flue gas heat recovery*
    - **"U"** - *Photovoltaics*
    - **"V"** - *Wind turbine (roof mounted)*
    - **"V2"** - *Wind turbine (on mast)*
    - **"W"** - *Floor insulation*
    - **"X"** - *Insulated doors*
    - **"Y"** - *Instantaneous waste water heat recovery*
    - **"Y2"** - *Storage waste water heat recovery*
    - **"Z1"** - *Air or ground source heat pump*
    - **"Z2"** - *Air or ground source heat pump with underfloor heating*
    - **"Z3"** - *Micro-CHP*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement/Improvement-Number"></a>Improvement-Number

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Green-Deal-Package`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package)/[`Green-Deal-Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement)/[`Improvement-Number`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement/Improvement-Number)/

- Parent element: [`Green-Deal-Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *Insulate hot water cylinder with 80 mm jacket*
    - **"2"** - *Increase hot water cylinder insulation*
    - **"3"** - *Add additional 80 mm jacket to hot water cylinder*
    - **"4"** - *Hot water cylinder thermostat*
    - **"5"** - *Increase loft insulation to 270 mm*
    - **"6"** - *Cavity wall insulation*
    - **"7"** - *Internal or external wall insulation*
    - **"8"** - *Replace single glazed windows with low-E double glazing*
    - **"9"** - *Secondary glazing to single glazed windows*
    - **"10"** - *Draught proofing*
    - **"11"** - *Heating controls (programmer, room thermostat and TRVs)*
    - **"12"** - *Heating controls (room thermostat and TRVs)*
    - **"13"** - *Heating controls (thermostatic radiator valves)*
    - **"14"** - *Heating controls (room thermostat)*
    - **"15"** - *Heating controls (programmer and TRVs)*
    - **"16"** - *Heating controls (time and temperature zone control)*
    - **"17"** - *Heating controls (programmer and room thermostat)*
    - **"18"** - *Heating controls (room thermostat)*
    - **"19"** - *Solar water heating*
    - **"20"** - *Replace boiler with new condensing boiler*
    - **"21"** - *Replace boiler with new condensing boiler*
    - **"22"** - *Replace boiler with biomass boiler*
    - **"23"** - *Wood pellet stove with boiler and radiators*
    - **"24"** - *Fan assisted storage heaters and dual immersion cylinder*
    - **"25"** - *Fan assisted storage heaters*
    - **"26"** - *Replacement warm air unit*
    - **"27"** - *Change heating to gas condensing boiler*
    - **"28"** - *Condensing oil boiler with radiators*
    - **"29"** - *Change heating to gas condensing boiler*
    - **"30"** - *Fan assisted storage heaters and dual immersion cylinder*
    - **"31"** - *Fan-assisted storage heaters*
    - **"32"** - *Change heating to gas condensing boiler*
    - **"34"** - *Solar photovoltaic panels, 2.5 kWp*
    - **"35"** - *Low energy lighting for all fixed outlets*
    - **"36"** - *Replace heating unit with condensing unit*
    - **"37"** - *Condensing boiler (separate from the range cooker)*
    - **"38"** - *Condensing boiler (separate from the range cooker)*
    - **"39"** - *Wood pellet stove with boiler and radiators*
    - **"40"** - *Change room heaters to condensing boiler*
    - **"41"** - *Change room heaters to condensing boiler*
    - **"42"** - *Replace heating unit with mains gas condensing unit*
    - **"43"** - *Condensing oil boiler with radiators*
    - **"44"** - *Wind turbine*
    - **"45"** - *Flat roof insulation*
    - **"46"** - *Room-in-roof insulation*
    - **"47"** - *Floor insulation*
    - **"48"** - *High performance external doors*
    - **"49"** - *Heat recovery system for mixer showers*
    - **"50"** - *Flue gas heat recovery device in conjunction with boiler*
    - **"51"** - *Air or ground source heat pump*
    - **"52"** - *Air or ground source heat pump with underfloor heating*
    - **"53"** - *Micro CHP*
    - **"54"** - *Biomass boiler (Exempted Appliance if in Smoke Control Area)*
    - **"55"** - *External insulation with cavity wall insulation*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Electricity-Saving"></a>Electricity-Saving

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Green-Deal-Package`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package)/[`Electricity-Saving`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Electricity-Saving)/

- Documentation: *Total electricity saving for the package*
- Documentation2: *Extension of a Decimal value for use with monetary values where a currency code needs to be specified. The currency code is actually metadata about the value so, in line with good XML practice, the Currency Code is declared as an XML-Attribute of the Money datatype rather than as a separate XML-Element. The currency attribute should then include a list of valid currencies codes that are supported.*
- Parent element: [`Green-Deal-Package`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Gas-Saving"></a>Gas-Saving

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Green-Deal-Package`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package)/[`Gas-Saving`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Gas-Saving)/

- Documentation: *Total gas saving for the package*
- Documentation2: *Extension of a Decimal value for use with monetary values where a currency code needs to be specified. The currency code is actually metadata about the value so, in line with good XML practice, the Currency Code is declared as an XML-Attribute of the Money datatype rather than as a separate XML-Element. The currency attribute should then include a list of valid currencies codes that are supported.*
- Parent element: [`Green-Deal-Package`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Other-Fuel-Saving"></a>Other-Fuel-Saving

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Green-Deal-Package`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package)/[`Other-Fuel-Saving`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Other-Fuel-Saving)/

- Documentation: *Total other saving for the package*
- Documentation2: *Extension of a Decimal value for use with monetary values where a currency code needs to be specified. The currency code is actually metadata about the value so, in line with good XML practice, the Currency Code is declared as an XML-Attribute of the Money datatype rather than as a separate XML-Element. The currency attribute should then include a list of valid currencies codes that are supported.*
- Parent element: [`Green-Deal-Package`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements"></a>Alternative-Improvements

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Alternative-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements)/

- Documentation: *Alternative improvements to some of those given in Suggested-Improvements*
- Documentation2: *Part of an Energy Report that describes the a set of improvements that the Home Inspector considers would contribute to the overall energy rating of the property.*
- Parent element: [`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)
- Child elements: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement"></a>Improvement

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Alternative-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements)/[`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement)/

- Parent element: [`Alternative-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements)
- Child elements: [`Sequence`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Sequence) [`Improvement-Category`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Category) [`Improvement-Type`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Type) [`Typical-Saving`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Typical-Saving) [`Energy-Performance-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Energy-Performance-Rating) [`Environmental-Impact-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Environmental-Impact-Rating) [`Improvement-Details`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details) [`Indicative-Cost`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Indicative-Cost) [`Green-Deal-Category`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Green-Deal-Category)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **unbounded**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Sequence"></a>Sequence

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Alternative-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements)/[`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement)/[`Sequence`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Sequence)/

- Documentation: *Sequence of the Suggested Improvements within the set of Suggested Improvements. This is used to order the Recommendations on the output HCR / EPC so that the cumulative Ratings make sense. The Improved Energy Ratings that result from carrying out a Suggested Improvement are cumulative and assume that the improvements have been installed in the order they appear in the list. Hence they must be sequenced.*
- Parent element: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Category"></a>Improvement-Category

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Alternative-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements)/[`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement)/[`Improvement-Category`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Category)/

- Documentation: *The category of improvement. This identifies where on the report the recommendation is printed.*
- Parent element: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *Lower cost - this is for backwards compatibility only and should not be used*
    - **"2"** - *Higher cost - this is for backwards compatibility only and should not be used*
    - **"3"** - *Further measure - this is for backwards compatibility only and should not be used*
    - **"4"** - *Deselected. This is for backwards compatibility only and should not be used.*
    - **"5"** - *Normal measure*
    - **"6"** - *Alternative measure*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Type"></a>Improvement-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Alternative-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements)/[`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement)/[`Improvement-Type`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Type)/

- Documentation: *Suggested work to be carried out on the Property to improve its energy efficiency. This should be a enumerated list of acceptable improvements but it hasn't yet been defined.*
- Parent element: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"A"** - *Loft insulation*
    - **"A2"** - *Flat roof insulation*
    - **"A3"** - *Room-in-roof insulation*
    - **"B"** - *Cavity wall insulation*
    - **"C"** - *Hot water cylinder insulation*
    - **"D"** - *Draughtproofing*
    - **"E"** - *Low energy lights*
    - **"F"** - *Cylinder thermostat*
    - **"G"** - *Heating controls for wet central heating system*
    - **"H"** - *Heating controls for warm air system*
    - **"I"** - *Upgrade boiler, same fuel*
    - **"J"** - *Biomass boiler*
    - **"J2"** - *Biomass boiler as alternative improvement*
    - **"K"** - *Biomass room heater with boiler*
    - **"L"** - *New or replacement fan-assisted storage heaters*
    - **"L2"** - *New or replacement high heat retention storage heaters*
    - **"M"** - *Replacement warm-air unit*
    - **"N"** - *Solar water heating*
    - **"O"** - *Replacement double glazed windows*
    - **"O3"** - *Replacement double glazing units*
    - **"P"** - *Secondary glazing*
    - **"Q"** - *Solid wall insulation*
    - **"Q2"** - *External insulation with cavity wall insulation*
    - **"R"** - *Condensing oil boiler*
    - **"S"** - *Change heating to Band A gas condensing boiler (no fuel switch)*
    - **"T"** - *Change heating to Band A gas condensing boiler (fuel switch)*
    - **"T2"** - *Flue gas heat recovery*
    - **"U"** - *Photovoltaics*
    - **"V"** - *Wind turbine (roof mounted)*
    - **"V2"** - *Wind turbine (on mast)*
    - **"W"** - *Floor insulation*
    - **"X"** - *Insulated doors*
    - **"Y"** - *Instantaneous waste water heat recovery*
    - **"Y2"** - *Storage waste water heat recovery*
    - **"Z1"** - *Air or ground source heat pump*
    - **"Z2"** - *Air or ground source heat pump with underfloor heating*
    - **"Z3"** - *Micro-CHP*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Typical-Saving"></a>Typical-Saving

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Alternative-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements)/[`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement)/[`Typical-Saving`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Typical-Saving)/

- Documentation: *Typical savings (in British Pounds) per year if the suggested improvement is carried out. 0 if not assessed*
- Documentation2: *Extension of a Decimal value for use with monetary values where a currency code needs to be specified. The currency code is actually metadata about the value so, in line with good XML practice, the Currency Code is declared as an XML-Attribute of the Money datatype rather than as a separate XML-Element. The currency attribute should then include a list of valid currencies codes that are supported.*
- Parent element: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Energy-Performance-Rating"></a>Energy-Performance-Rating

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Alternative-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements)/[`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement)/[`Energy-Performance-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Energy-Performance-Rating)/

- Documentation: *The estimated Energy performance rating of the Property after the Suggested Improvement has been carried out providing any preceding Suggested Improvement has also been carried out. 0 if not assessed*
- Parent element: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Environmental-Impact-Rating"></a>Environmental-Impact-Rating

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Alternative-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements)/[`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement)/[`Environmental-Impact-Rating`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Environmental-Impact-Rating)/

- Documentation: *The estimated Environmental Impact rating of the Property after the Suggested Improvement has been carried out providing any preceding Suggested Improvement has also been carried out. 0 if not assessed*
- Parent element: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details"></a>Improvement-Details

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Alternative-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements)/[`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement)/[`Improvement-Details`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details)/

- Parent element: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement)
- Child elements: [`Improvement-Texts`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts) [`Improvement-Number`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Number)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts"></a>Improvement-Texts

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Alternative-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements)/[`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement)/[`Improvement-Details`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details)/[`Improvement-Texts`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts)/

- Documentation: *For backward compatability only*
- Parent element: [`Improvement-Details`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details)
- Child elements: [`Improvement-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Summary) [`Improvement-Heading`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Heading) [`Improvement-Description`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Description)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Summary"></a>Improvement-Summary

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Alternative-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements)/[`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement)/[`Improvement-Details`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details)/[`Improvement-Texts`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts)/[`Improvement-Summary`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Summary)/

- Documentation: *A short description of the suggested improvement.*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: [`Improvement-Texts`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Heading"></a>Improvement-Heading

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Alternative-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements)/[`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement)/[`Improvement-Details`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details)/[`Improvement-Texts`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts)/[`Improvement-Heading`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Heading)/

- Documentation: *Text to precede the improvement description. If this field is not provided the 'Improvement-Summary' is used instead.*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: [`Improvement-Texts`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Description"></a>Improvement-Description

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Alternative-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements)/[`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement)/[`Improvement-Details`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details)/[`Improvement-Texts`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts)/[`Improvement-Description`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Description)/

- Documentation: *Detailed description of the suggested improvement.*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: [`Improvement-Texts`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Number"></a>Improvement-Number

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Alternative-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements)/[`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement)/[`Improvement-Details`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details)/[`Improvement-Number`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Number)/

- Parent element: [`Improvement-Details`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *Insulate hot water cylinder with 80 mm jacket*
    - **"2"** - *Increase hot water cylinder insulation*
    - **"3"** - *Add additional 80 mm jacket to hot water cylinder*
    - **"4"** - *Hot water cylinder thermostat*
    - **"5"** - *Increase loft insulation to 270 mm*
    - **"6"** - *Cavity wall insulation*
    - **"7"** - *Internal or external wall insulation*
    - **"8"** - *Replace single glazed windows with low-E double glazing*
    - **"9"** - *Secondary glazing to single glazed windows*
    - **"10"** - *Draught proofing*
    - **"11"** - *Heating controls (programmer, room thermostat and TRVs)*
    - **"12"** - *Heating controls (room thermostat and TRVs)*
    - **"13"** - *Heating controls (thermostatic radiator valves)*
    - **"14"** - *Heating controls (room thermostat)*
    - **"15"** - *Heating controls (programmer and TRVs)*
    - **"16"** - *Heating controls (time and temperature zone control)*
    - **"17"** - *Heating controls (programmer and room thermostat)*
    - **"18"** - *Heating controls (room thermostat)*
    - **"19"** - *Solar water heating*
    - **"20"** - *Replace boiler with new condensing boiler*
    - **"21"** - *Replace boiler with new condensing boiler*
    - **"22"** - *Replace boiler with biomass boiler*
    - **"23"** - *Wood pellet stove with boiler and radiators*
    - **"24"** - *Fan assisted storage heaters and dual immersion cylinder*
    - **"25"** - *Fan assisted storage heaters*
    - **"26"** - *Replacement warm air unit*
    - **"27"** - *Change heating to gas condensing boiler*
    - **"28"** - *Condensing oil boiler with radiators*
    - **"29"** - *Change heating to gas condensing boiler*
    - **"30"** - *Fan assisted storage heaters and dual immersion cylinder*
    - **"31"** - *Fan-assisted storage heaters*
    - **"32"** - *Change heating to gas condensing boiler*
    - **"34"** - *Solar photovoltaic panels, 2.5 kWp*
    - **"35"** - *Low energy lighting for all fixed outlets*
    - **"36"** - *Replace heating unit with condensing unit*
    - **"37"** - *Condensing boiler (separate from the range cooker)*
    - **"38"** - *Condensing boiler (separate from the range cooker)*
    - **"39"** - *Wood pellet stove with boiler and radiators*
    - **"40"** - *Change room heaters to condensing boiler*
    - **"41"** - *Change room heaters to condensing boiler*
    - **"42"** - *Replace heating unit with mains gas condensing unit*
    - **"43"** - *Condensing oil boiler with radiators*
    - **"44"** - *Wind turbine*
    - **"45"** - *Flat roof insulation*
    - **"46"** - *Room-in-roof insulation*
    - **"47"** - *Floor insulation*
    - **"48"** - *High performance external doors*
    - **"49"** - *Heat recovery system for mixer showers*
    - **"50"** - *Flue gas heat recovery device in conjunction with boiler*
    - **"51"** - *Air or ground source heat pump*
    - **"52"** - *Air or ground source heat pump with underfloor heating*
    - **"53"** - *Micro CHP*
    - **"54"** - *Biomass boiler (Exempted Appliance if in Smoke Control Area)*
    - **"55"** - *External insulation with cavity wall insulation*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Indicative-Cost"></a>Indicative-Cost

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Alternative-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements)/[`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement)/[`Indicative-Cost`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Indicative-Cost)/

- Parent element: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Green-Deal-Category"></a>Green-Deal-Category

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Alternative-Improvements`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements)/[`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement)/[`Green-Deal-Category`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Green-Deal-Category)/

- Parent element: [`Improvement`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *1. Not eligible for Green Deal*
    - **"2"** - *2. Eligible with additional finance*
    - **"3"** - *3. Eligible without additional finance*
    - **"NI"** - *Not assessed. Use for alternative measures and for new dwelling EPCs*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum"></a>Addendum

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Addendum`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum)/

- Parent element: [`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)
- Child elements: [`Cavity-Fill-Recommended`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/Cavity-Fill-Recommended) [`Stone-Walls`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/Stone-Walls) [`System-Build`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/System-Build) [`Access-Issues`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/Access-Issues) [`High-Exposure`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/High-Exposure) [`Narrow-Cavities`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/Narrow-Cavities)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/Cavity-Fill-Recommended"></a>Cavity-Fill-Recommended

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Addendum`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum)/[`Cavity-Fill-Recommended`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/Cavity-Fill-Recommended)/

- Documentation: *Cavity fill is recommended*
- Parent element: [`Addendum`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/Stone-Walls"></a>Stone-Walls

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Addendum`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum)/[`Stone-Walls`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/Stone-Walls)/

- Documentation: *Stone walls present, not insulated*
- Parent element: [`Addendum`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/System-Build"></a>System-Build

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Addendum`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum)/[`System-Build`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/System-Build)/

- Documentation: *System build present*
- Parent element: [`Addendum`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/Access-Issues"></a>Access-Issues

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Addendum`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum)/[`Access-Issues`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/Access-Issues)/

- Documentation: *Dwelling has access issues for cavity wall insulation. Include only when at least one of Cavity-Fill-Recommended, Stone-Walls, System-Build is also present*
- Parent element: [`Addendum`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/High-Exposure"></a>High-Exposure

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Addendum`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum)/[`High-Exposure`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/High-Exposure)/

- Documentation: *Dwelling may be exposed to wind-driven rain. Include only when at least one of Cavity-Fill-Recommended, Stone-Walls, System-Build is also present*
- Parent element: [`Addendum`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/Narrow-Cavities"></a>Narrow-Cavities

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Energy-Assessment`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment)/[`Addendum`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum)/[`Narrow-Cavities`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/Narrow-Cavities)/

- Documentation: *Dwelling may have narrow cavities. Include only when Cavity-Fill-Recommended is also present*
- Parent element: [`Addendum`](#SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data"></a>SAP10-Data

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/

- Documentation2: *These are the specific data-items collected by the HI / EA needed to perform the SAP calculation.*
- Parent element: [`SAP-Report`](#SAP-Compliance-Report/SAP-Report)
- Child elements: [`Data-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/Data-Type) [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/Data-Type"></a>Data-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`Data-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/Data-Type)/

- Documentation: *Type of SAP data that has been collected.*
- Parent element: [`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *new dwelling as designed*
    - **"2"** - *new dwelling as built*
    - **"3"** - *new extension to existing dwelling*
    - **"4"** - *new dwelling created by change of use*
    - **"5"** - *existing dwelling*
    - **"6"** - *other*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details"></a>SAP-Property-Details

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/

- Documentation2: *Various measurements a particular Property.*
- Parent element: [`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)
- Child elements: [`Property-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Property-Type) [`Built-Form`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Built-Form) [`Living-Area`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Living-Area) [`Lowest-Storey-Area`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Lowest-Storey-Area) [`Orientation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Orientation) [`Conservatory-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Conservatory-Type) [`Terrain-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Terrain-Type) [`Has-Special-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Has-Special-Feature) [`Special-Feature-Description`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Special-Feature-Description) [`Energy-Saved-Or-Generated`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Energy-Saved-Or-Generated) [`Saved-Or-Generated-Fuel`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Saved-Or-Generated-Fuel) [`Energy-Used`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Energy-Used) [`Energy-Used-Fuel`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Energy-Used-Fuel) [`Is-In-Smoke-Control-Area`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Is-In-Smoke-Control-Area) [`Cold-Water-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Cold-Water-Source) [`Windows-Overshading`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Windows-Overshading) [`Thermal-Mass-Parameter`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Thermal-Mass-Parameter) [`Additional-Allowable-Electricity-Generation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Additional-Allowable-Electricity-Generation) [`Gas-Smart-Meter-Present`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Gas-Smart-Meter-Present) [`Electricity-Smart-Meter-Present`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Electricity-Smart-Meter-Present) [`Is-Dwelling-Export-Capable`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Is-Dwelling-Export-Capable) [`PV-Connection`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/PV-Connection) [`PV-Diverter`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/PV-Diverter) [`Battery-Capacity`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Battery-Capacity) [`Is-Wind-Turbine-Connected-To-Dwelling-Meter`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Is-Wind-Turbine-Connected-To-Dwelling-Meter) [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating) [`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source) [`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts) [`SAP-Opening-Types`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types) [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation) [`SAP-Lighting`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting) [`SAP-Deselected-Improvements`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Deselected-Improvements) [`SAP-Flat-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Flat-Details) [`SAP-Special-Features`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features) [`Design-Water-Use`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Design-Water-Use) [`SAP-Cooling`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Property-Type"></a>Property-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`Property-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Property-Type)/

- Documentation: *The type of Property, such as House, Flat, Mansion, Maisonette etc.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"0"** - *House*
    - **"1"** - *Bungalow*
    - **"2"** - *Flat*
    - **"3"** - *Maisonette*
    - **"4"** - *Park home*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Built-Form"></a>Built-Form

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`Built-Form`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Built-Form)/

- Documentation: *The building type of the Property e.g. Detached, Semi-Detached, Terrace etc. Together with the Property Type, the Built Form provides a structured description of the property.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *Detached*
    - **"2"** - *Semi-Detached*
    - **"3"** - *End-Terrace*
    - **"4"** - *Mid-Terrace*
    - **"5"** - *Enclosed End-Terrace*
    - **"6"** - *Enclosed Mid-Terrace*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Living-Area"></a>Living-Area

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`Living-Area`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Living-Area)/

- Documentation: *The size of the living area in square metres. The living area is the room marked on a plan as the lounge or living room, or the largest public room (irrespective of usage by particular occupants), together with any rooms not separated from the lounge or living room by doors, and including any cupboards directly accessed from the lounge or living room. Living area does not, however, extend over more than one storey, even when stairs enter the living area directly.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Lowest-Storey-Area"></a>Lowest-Storey-Area

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`Lowest-Storey-Area`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Lowest-Storey-Area)/

- Documentation: *The Area of the lowest storey in square meters including unheated or communal areas such as garages or corridors.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Orientation"></a>Orientation

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`Orientation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Orientation)/

- Documentation: *The orientation of the front of the property.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"0"** - *unknown or unspecified*
    - **"1"** - *North*
    - **"2"** - *North East*
    - **"3"** - *East*
    - **"4"** - *South East*
    - **"5"** - *South*
    - **"6"** - *South West*
    - **"7"** - *West*
    - **"8"** - *North West*
    - **"9"** - *Horizontal (windows and roof windows only)*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Conservatory-Type"></a>Conservatory-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`Conservatory-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Conservatory-Type)/

- Documentation: *Type of conservatory.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *no conservatory*
    - **"2"** - *separated unheated conservatory*
    - **"3"** - *separated heated conservatory*
    - **"4"** - *not separated*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Terrain-Type"></a>Terrain-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`Terrain-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Terrain-Type)/

- Documentation: *Terrain type. Needed for wind-turbines and for applying measures.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *urban*
    - **"2"** - *suburban*
    - **"3"** - *rural*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Has-Special-Feature"></a>Has-Special-Feature

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`Has-Special-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Has-Special-Feature)/

- Documentation: *For backwards compatibility only, do not use.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Special-Feature-Description"></a>Special-Feature-Description

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`Special-Feature-Description`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Special-Feature-Description)/

- Documentation: *For backwards compatibility only, do not use.*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Energy-Saved-Or-Generated"></a>Energy-Saved-Or-Generated

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`Energy-Saved-Or-Generated`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Energy-Saved-Or-Generated)/

- Documentation: *For backwards compatibility only, do not use.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Saved-Or-Generated-Fuel"></a>Saved-Or-Generated-Fuel

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`Saved-Or-Generated-Fuel`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Saved-Or-Generated-Fuel)/

- Documentation: *For backwards compatibility only, do not use.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *Gas: mains gas*
    - **"2"** - *Gas: bulk LPG*
    - **"3"** - *Gas: bottled LPG*
    - **"4"** - *Oil: heating oil*
    - **"7"** - *Gas: biogas*
    - **"8"** - *LNG*
    - **"9"** - *LPG subject to Special Condition 18*
    - **"10"** - *Solid fuel: dual fuel appliance (mineral and wood)*
    - **"11"** - *Solid fuel: house coal*
    - **"12"** - *Solid fuel: manufactured smokeless fuel*
    - **"15"** - *Solid fuel: anthracite*
    - **"20"** - *Solid fuel: wood logs*
    - **"21"** - *Solid fuel: wood chips*
    - **"22"** - *Solid fuel: wood pellets (in bags, for secondary heating)*
    - **"23"** - *Solid fuel: wood pellets (bulk supply in bags, for main heating)*
    - **"36"** - *Electricity: electricity sold to grid*
    - **"37"** - *Electricity: electricity displaced from grid*
    - **"39"** - *Electricity: electricity, unspecified tariff*
    - **"41"** - *Community heating schemes: heat from electric heat pump*
    - **"42"** - *Community heating schemes: heat from boilers - waste combustion*
    - **"43"** - *Community heating schemes: heat from boilers - biomass*
    - **"44"** - *Community heating schemes: heat from boilers - biogas*
    - **"45"** - *Community heating schemes: waste heat from power stations*
    - **"46"** - *Community heating schemes: geothermal heat source*
    - **"47"** - *Community heating schemes: high grade heat recovered from process*
    - **"48"** - *Community heating schemes: heat from CHP*
    - **"49"** - *Community heating schemes: low grade heat recovered from process*
    - **"50"** - *Community heating schemes: electricity for pumping in distribution network*
    - **"51"** - *Community heating schemes: heat from mains gas*
    - **"52"** - *Community heating schemes: heat from LPG*
    - **"53"** - *Community heating schemes: heat from oil*
    - **"54"** - *Community heating schemes: heat from coal*
    - **"55"** - *Community heating schemes: heat from B30D*
    - **"56"** - *Community heating schemes: heat from boilers that can use mineral oil or biodiesel*
    - **"57"** - *Community heating schemes: heat from boilers using biodiesel from any biomass source*
    - **"58"** - *Community heating schemes: biodiesel from vegetable oil only*
    - **"71"** - *biodiesel from any biomass source*
    - **"72"** - *biodiesel from used cooking oil only*
    - **"73"** - *biodiesel from vegetable oil only*
    - **"74"** - *appliances able to use mineral oil or liquid biofuel*
    - **"75"** - *B30K*
    - **"76"** - *bioethanol from any biomass source*
    - **"99"** - *Fuel data from pcdb*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Energy-Used"></a>Energy-Used

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`Energy-Used`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Energy-Used)/

- Documentation: *For backwards compatibility only, do not use.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Energy-Used-Fuel"></a>Energy-Used-Fuel

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`Energy-Used-Fuel`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Energy-Used-Fuel)/

- Documentation: *For backwards compatibility only, do not use.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *Gas: mains gas*
    - **"2"** - *Gas: bulk LPG*
    - **"3"** - *Gas: bottled LPG*
    - **"4"** - *Oil: heating oil*
    - **"7"** - *Gas: biogas*
    - **"8"** - *LNG*
    - **"9"** - *LPG subject to Special Condition 18*
    - **"10"** - *Solid fuel: dual fuel appliance (mineral and wood)*
    - **"11"** - *Solid fuel: house coal*
    - **"12"** - *Solid fuel: manufactured smokeless fuel*
    - **"15"** - *Solid fuel: anthracite*
    - **"20"** - *Solid fuel: wood logs*
    - **"21"** - *Solid fuel: wood chips*
    - **"22"** - *Solid fuel: wood pellets (in bags, for secondary heating)*
    - **"23"** - *Solid fuel: wood pellets (bulk supply in bags, for main heating)*
    - **"36"** - *Electricity: electricity sold to grid*
    - **"37"** - *Electricity: electricity displaced from grid*
    - **"39"** - *Electricity: electricity, unspecified tariff*
    - **"41"** - *Community heating schemes: heat from electric heat pump*
    - **"42"** - *Community heating schemes: heat from boilers - waste combustion*
    - **"43"** - *Community heating schemes: heat from boilers - biomass*
    - **"44"** - *Community heating schemes: heat from boilers - biogas*
    - **"45"** - *Community heating schemes: waste heat from power stations*
    - **"46"** - *Community heating schemes: geothermal heat source*
    - **"47"** - *Community heating schemes: high grade heat recovered from process*
    - **"48"** - *Community heating schemes: heat from CHP*
    - **"49"** - *Community heating schemes: low grade heat recovered from process*
    - **"50"** - *Community heating schemes: electricity for pumping in distribution network*
    - **"51"** - *Community heating schemes: heat from mains gas*
    - **"52"** - *Community heating schemes: heat from LPG*
    - **"53"** - *Community heating schemes: heat from oil*
    - **"54"** - *Community heating schemes: heat from coal*
    - **"55"** - *Community heating schemes: heat from B30D*
    - **"56"** - *Community heating schemes: heat from boilers that can use mineral oil or biodiesel*
    - **"57"** - *Community heating schemes: heat from boilers using biodiesel from any biomass source*
    - **"58"** - *Community heating schemes: biodiesel from vegetable oil only*
    - **"71"** - *biodiesel from any biomass source*
    - **"72"** - *biodiesel from used cooking oil only*
    - **"73"** - *biodiesel from vegetable oil only*
    - **"74"** - *appliances able to use mineral oil or liquid biofuel*
    - **"75"** - *B30K*
    - **"76"** - *bioethanol from any biomass source*
    - **"99"** - *Fuel data from pcdb*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Is-In-Smoke-Control-Area"></a>Is-In-Smoke-Control-Area

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`Is-In-Smoke-Control-Area`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Is-In-Smoke-Control-Area)/

- Documentation: *Is property in a smoke control area? Only if a solid fuel appliance is used.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"false"** - **
    - **"true"** - **
    - **"unknown"** - **
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Cold-Water-Source"></a>Cold-Water-Source

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`Cold-Water-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Cold-Water-Source)/

- Documentation: *What is the cold water source? Either mains or header tank.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *mains*
    - **"2"** - *header tank*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Windows-Overshading"></a>Windows-Overshading

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`Windows-Overshading`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Windows-Overshading)/

- Documentation: *Average amount of overshading of windows.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *very little*
    - **"2"** - *average or unknown*
    - **"3"** - *more than average*
    - **"4"** - *heavy*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Thermal-Mass-Parameter"></a>Thermal-Mass-Parameter

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`Thermal-Mass-Parameter`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Thermal-Mass-Parameter)/

- Documentation: *Average thermal mass parameter for the dwelling in kJ/m2K. If omitted it is calculated using the kappa values of each element.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Additional-Allowable-Electricity-Generation"></a>Additional-Allowable-Electricity-Generation

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`Additional-Allowable-Electricity-Generation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Additional-Allowable-Electricity-Generation)/

- Documentation: *Additional allowable electricity generation applicable to this dwelling in kWh per square metre; only if Zero Carbon Home assessment.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Gas-Smart-Meter-Present"></a>Gas-Smart-Meter-Present

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`Gas-Smart-Meter-Present`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Gas-Smart-Meter-Present)/

- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Electricity-Smart-Meter-Present"></a>Electricity-Smart-Meter-Present

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`Electricity-Smart-Meter-Present`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Electricity-Smart-Meter-Present)/

- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Is-Dwelling-Export-Capable"></a>Is-Dwelling-Export-Capable

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`Is-Dwelling-Export-Capable`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Is-Dwelling-Export-Capable)/

- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/PV-Connection"></a>PV-Connection

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`PV-Connection`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/PV-Connection)/

- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"0"** - *not applicable (FGHRS)*
    - **"1"** - *not connected to dwelling's electricity meter*
    - **"2"** - *connected to dwelling's electricity meter*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/PV-Diverter"></a>PV-Diverter

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`PV-Diverter`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/PV-Diverter)/

- Documentation: *Diverter present.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Battery-Capacity"></a>Battery-Capacity

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`Battery-Capacity`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Battery-Capacity)/

- Documentation: *Battery capacity if diverter present.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Is-Wind-Turbine-Connected-To-Dwelling-Meter"></a>Is-Wind-Turbine-Connected-To-Dwelling-Meter

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`Is-Wind-Turbine-Connected-To-Dwelling-Meter`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Is-Wind-Turbine-Connected-To-Dwelling-Meter)/

- Documentation: *Whether the wind turbine is connected to the Dwelling's meter.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating"></a>SAP-Heating

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/

- Documentation2: *Details of the means by which the Main Building is heated.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Child elements: [`Water-Heating-Code`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Water-Heating-Code) [`Water-Fuel-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Water-Fuel-Type) [`Has-Hot-Water-Cylinder`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Has-Hot-Water-Cylinder) [`Secondary-Heating-Category`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Category) [`Secondary-Heating-Data-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Data-Source) [`Secondary-Heating-Efficiency`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Efficiency) [`Secondary-Heating-Commisioning-Certificate`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Commisioning-Certificate) [`Secondary-Heating-Installation-Engineer`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Installation-Engineer) [`Secondary-Heating-Code`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Code) [`Secondary-Fuel-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Fuel-Type) [`Secondary-Heating-PCDF-Fuel-Index`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-PCDF-Fuel-Index) [`Secondary-Heating-Flue-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Flue-Type) [`Thermal-Store`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Thermal-Store) [`Has-Fixed-Air-Conditioning`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Has-Fixed-Air-Conditioning) [`Immersion-Heating-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Immersion-Heating-Type) [`Is-Heat-Pump-Assisted-By-Immersion`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Heat-Pump-Assisted-By-Immersion) [`Is-Heat-Pump-Installed-To-MIS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Heat-Pump-Installed-To-MIS) [`Is-Immersion-For-Summer-Use`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Immersion-For-Summer-Use) [`Is-Secondary-Heating-HETAS-Approved`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Secondary-Heating-HETAS-Approved) [`Hot-Water-Store-Manufacturer`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Manufacturer) [`Hot-Water-Store-Model`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Model) [`Hot-Water-Store-Commissioning-Certificate`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Commissioning-Certificate) [`Hot-Water-Store-Installer-Engineer-Registration`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Installer-Engineer-Registration) [`Hot-Water-Store-Size`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Size) [`Hot-Water-Store-Heat-Transfer-Area`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Heat-Transfer-Area) [`Hot-Water-Store-Heat-Loss-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Heat-Loss-Source) [`Hot-Water-Store-Heat-Loss`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Heat-Loss) [`Hot-Water-Store-Insulation-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Insulation-Type) [`Hot-Water-Store-Insulation-Thickness`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Insulation-Thickness) [`Is-Thermal-Store-Near-Boiler`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Thermal-Store-Near-Boiler) [`Is-Thermal-Store-Or-CPSU-In-Airing-Cupboard`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Thermal-Store-Or-CPSU-In-Airing-Cupboard) [`Has-Cylinder-Thermostat`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Has-Cylinder-Thermostat) [`Is-Cylinder-In-Heated-Space`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Cylinder-In-Heated-Space) [`Is-Hot-Water-Separately-Timed`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Hot-Water-Separately-Timed) [`Hot-Water-Controls-Manufacturer`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Controls-Manufacturer) [`Hot-Water-Controls-Model`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Controls-Model) [`SAP-Community-Heating-Systems`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems) [`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details) [`SAP-Heating-Design-Water-Use`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Heating-Design-Water-Use) [`Main-Heating-Systems-Interaction`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Systems-Interaction) [`Secondary-Heating-Declared-Values`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values) [`Primary-Pipework-Insulation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Primary-Pipework-Insulation) [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details) [`Instantaneous-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS) [`Storage-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS) [`Shower-Outlets`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets) [`Number-Baths`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Number-Baths) [`Number-Baths-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Number-Baths-WWHRS)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Water-Heating-Code"></a>Water-Heating-Code

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Water-Heating-Code`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Water-Heating-Code)/

- Documentation: *The type of Water Heating present in the Property.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Water-Fuel-Type"></a>Water-Fuel-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Water-Fuel-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Water-Fuel-Type)/

- Documentation: *The type of fuel used to power the central heating e.g. Gas, Electricity. Not used if water system is main or secondary system.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *Gas: mains gas*
    - **"2"** - *Gas: bulk LPG*
    - **"3"** - *Gas: bottled LPG*
    - **"4"** - *Oil: heating oil*
    - **"7"** - *Gas: biogas*
    - **"8"** - *LNG*
    - **"9"** - *LPG subject to Special Condition 18*
    - **"10"** - *Solid fuel: dual fuel appliance (mineral and wood)*
    - **"11"** - *Solid fuel: house coal*
    - **"12"** - *Solid fuel: manufactured smokeless fuel*
    - **"15"** - *Solid fuel: anthracite*
    - **"20"** - *Solid fuel: wood logs*
    - **"21"** - *Solid fuel: wood chips*
    - **"22"** - *Solid fuel: wood pellets (in bags, for secondary heating)*
    - **"23"** - *Solid fuel: wood pellets (bulk supply in bags, for main heating)*
    - **"36"** - *Electricity: electricity sold to grid*
    - **"37"** - *Electricity: electricity displaced from grid*
    - **"39"** - *Electricity: electricity, unspecified tariff*
    - **"41"** - *Community heating schemes: heat from electric heat pump*
    - **"42"** - *Community heating schemes: heat from boilers - waste combustion*
    - **"43"** - *Community heating schemes: heat from boilers - biomass*
    - **"44"** - *Community heating schemes: heat from boilers - biogas*
    - **"45"** - *Community heating schemes: waste heat from power stations*
    - **"46"** - *Community heating schemes: geothermal heat source*
    - **"47"** - *Community heating schemes: high grade heat recovered from process*
    - **"48"** - *Community heating schemes: heat from CHP*
    - **"49"** - *Community heating schemes: low grade heat recovered from process*
    - **"50"** - *Community heating schemes: electricity for pumping in distribution network*
    - **"51"** - *Community heating schemes: heat from mains gas*
    - **"52"** - *Community heating schemes: heat from LPG*
    - **"53"** - *Community heating schemes: heat from oil*
    - **"54"** - *Community heating schemes: heat from coal*
    - **"55"** - *Community heating schemes: heat from B30D*
    - **"56"** - *Community heating schemes: heat from boilers that can use mineral oil or biodiesel*
    - **"57"** - *Community heating schemes: heat from boilers using biodiesel from any biomass source*
    - **"58"** - *Community heating schemes: biodiesel from vegetable oil only*
    - **"71"** - *biodiesel from any biomass source*
    - **"72"** - *biodiesel from used cooking oil only*
    - **"73"** - *biodiesel from vegetable oil only*
    - **"74"** - *appliances able to use mineral oil or liquid biofuel*
    - **"75"** - *B30K*
    - **"76"** - *bioethanol from any biomass source*
    - **"99"** - *Fuel data from pcdb*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Has-Hot-Water-Cylinder"></a>Has-Hot-Water-Cylinder

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Has-Hot-Water-Cylinder`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Has-Hot-Water-Cylinder)/

- Documentation: *Hot water cylinder?*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Category"></a>Secondary-Heating-Category

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Secondary-Heating-Category`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Category)/

- Documentation: *Category of heating system for the secondary heating system.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *none*
    - **"10"** - *room heaters*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Data-Source"></a>Secondary-Heating-Data-Source

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Secondary-Heating-Data-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Data-Source)/

- Documentation: *Source of secondary heating system data; only if secondary heating system.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"2"** - *from manufacturer declaration*
    - **"3"** - *from SAP table*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Efficiency"></a>Secondary-Heating-Efficiency

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Secondary-Heating-Efficiency`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Efficiency)/

- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Commisioning-Certificate"></a>Secondary-Heating-Commisioning-Certificate

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Secondary-Heating-Commisioning-Certificate`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Commisioning-Certificate)/

- Documentation: *Secondary heating system commisioning certificate number.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Installation-Engineer"></a>Secondary-Heating-Installation-Engineer

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Secondary-Heating-Installation-Engineer`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Installation-Engineer)/

- Documentation: *Secondary heating installation engineer registration reference.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Code"></a>Secondary-Heating-Code

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Secondary-Heating-Code`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Code)/

- Documentation: *Type of secondary heating present in the property; only if required and if heating data source is SAP table.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Fuel-Type"></a>Secondary-Fuel-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Secondary-Fuel-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Fuel-Type)/

- Documentation: *The type of fuel used to power the secondary heating e.g. Gas, Electricity; only if required.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *Gas: mains gas*
    - **"2"** - *Gas: bulk LPG*
    - **"3"** - *Gas: bottled LPG*
    - **"4"** - *Oil: heating oil*
    - **"7"** - *Gas: biogas*
    - **"8"** - *LNG*
    - **"9"** - *LPG subject to Special Condition 18*
    - **"10"** - *Solid fuel: dual fuel appliance (mineral and wood)*
    - **"11"** - *Solid fuel: house coal*
    - **"12"** - *Solid fuel: manufactured smokeless fuel*
    - **"15"** - *Solid fuel: anthracite*
    - **"20"** - *Solid fuel: wood logs*
    - **"21"** - *Solid fuel: wood chips*
    - **"22"** - *Solid fuel: wood pellets (in bags, for secondary heating)*
    - **"23"** - *Solid fuel: wood pellets (bulk supply in bags, for main heating)*
    - **"36"** - *Electricity: electricity sold to grid*
    - **"37"** - *Electricity: electricity displaced from grid*
    - **"39"** - *Electricity: electricity, unspecified tariff*
    - **"41"** - *Community heating schemes: heat from electric heat pump*
    - **"42"** - *Community heating schemes: heat from boilers - waste combustion*
    - **"43"** - *Community heating schemes: heat from boilers - biomass*
    - **"44"** - *Community heating schemes: heat from boilers - biogas*
    - **"45"** - *Community heating schemes: waste heat from power stations*
    - **"46"** - *Community heating schemes: geothermal heat source*
    - **"47"** - *Community heating schemes: high grade heat recovered from process*
    - **"48"** - *Community heating schemes: heat from CHP*
    - **"49"** - *Community heating schemes: low grade heat recovered from process*
    - **"50"** - *Community heating schemes: electricity for pumping in distribution network*
    - **"51"** - *Community heating schemes: heat from mains gas*
    - **"52"** - *Community heating schemes: heat from LPG*
    - **"53"** - *Community heating schemes: heat from oil*
    - **"54"** - *Community heating schemes: heat from coal*
    - **"55"** - *Community heating schemes: heat from B30D*
    - **"56"** - *Community heating schemes: heat from boilers that can use mineral oil or biodiesel*
    - **"57"** - *Community heating schemes: heat from boilers using biodiesel from any biomass source*
    - **"58"** - *Community heating schemes: biodiesel from vegetable oil only*
    - **"71"** - *biodiesel from any biomass source*
    - **"72"** - *biodiesel from used cooking oil only*
    - **"73"** - *biodiesel from vegetable oil only*
    - **"74"** - *appliances able to use mineral oil or liquid biofuel*
    - **"75"** - *B30K*
    - **"76"** - *bioethanol from any biomass source*
    - **"99"** - *Fuel data from pcdb*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-PCDF-Fuel-Index"></a>Secondary-Heating-PCDF-Fuel-Index

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Secondary-Heating-PCDF-Fuel-Index`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-PCDF-Fuel-Index)/

- Documentation: *PCDF index number of the fuel type, only if Secondary-Fuel-Type is 99 (fuel from database).*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Flue-Type"></a>Secondary-Heating-Flue-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Secondary-Heating-Flue-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Flue-Type)/

- Documentation: *Secondary flue type; only if secondary efficiency is manufacturer declaration and if there is a flue.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *open flue*
    - **"2"** - *balanced flue*
    - **"3"** - *chimney*
    - **"4"** - *omitted (boiler is in an outhouse, so its flue arrangements are not relevant)*
    - **"5"** - *unknown (there is a flue, but its type could not be determined)*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Thermal-Store"></a>Thermal-Store

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Thermal-Store`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Thermal-Store)/

- Documentation: *The type of thermal store; not used if main heating system is community heating scheme.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *none*
    - **"2"** - *hot water only*
    - **"3"** - *integrated*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Has-Fixed-Air-Conditioning"></a>Has-Fixed-Air-Conditioning

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Has-Fixed-Air-Conditioning`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Has-Fixed-Air-Conditioning)/

- Documentation: *Fixed air conditioning?*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Immersion-Heating-Type"></a>Immersion-Heating-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Immersion-Heating-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Immersion-Heating-Type)/

- Documentation: *The type of immersion heating; only if immersion.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *Dual*
    - **"2"** - *Single*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Heat-Pump-Assisted-By-Immersion"></a>Is-Heat-Pump-Assisted-By-Immersion

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Is-Heat-Pump-Assisted-By-Immersion`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Heat-Pump-Assisted-By-Immersion)/

- Documentation: *Is heat pump assisted by immersion? Applicable only to hot water only heat pumps*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Heat-Pump-Installed-To-MIS"></a>Is-Heat-Pump-Installed-To-MIS

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Is-Heat-Pump-Installed-To-MIS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Heat-Pump-Installed-To-MIS)/

- Documentation: *Is heat pump installed to MIS standard? Only if water heating from hot water only heat pump.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Immersion-For-Summer-Use"></a>Is-Immersion-For-Summer-Use

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Is-Immersion-For-Summer-Use`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Immersion-For-Summer-Use)/

- Documentation: *Immersion for summer use? Only if main heating is solid fuel fire or room heater with boiler.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Secondary-Heating-HETAS-Approved"></a>Is-Secondary-Heating-HETAS-Approved

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Is-Secondary-Heating-HETAS-Approved`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Secondary-Heating-HETAS-Approved)/

- Documentation: *Secondary heating appliance is HETAS approved? Only if solid fuel.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Manufacturer"></a>Hot-Water-Store-Manufacturer

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Hot-Water-Store-Manufacturer`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Manufacturer)/

- Documentation: *Store Manufacturer name.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Model"></a>Hot-Water-Store-Model

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Hot-Water-Store-Model`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Model)/

- Documentation: *Store Model name.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Commissioning-Certificate"></a>Hot-Water-Store-Commissioning-Certificate

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Hot-Water-Store-Commissioning-Certificate`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Commissioning-Certificate)/

- Documentation: *Store comissioning certificate number.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Installer-Engineer-Registration"></a>Hot-Water-Store-Installer-Engineer-Registration

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Hot-Water-Store-Installer-Engineer-Registration`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Installer-Engineer-Registration)/

- Documentation: *Store installer engineer registration number.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Size"></a>Hot-Water-Store-Size

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Hot-Water-Store-Size`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Size)/

- Documentation: *Hot water store size in litres; if there is a hot water store. Store refers to hot water store type which can be cylinder (if thermal store is "none"), hot-water only thermal store or integrated thermal store. Not applicable if (a) combi boiler whose data source database or (b) instantaneous combi boiler or (c) combi boiler from SAP table or (d) instantaneous water heater.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Heat-Transfer-Area"></a>Hot-Water-Store-Heat-Transfer-Area

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Hot-Water-Store-Heat-Transfer-Area`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Heat-Transfer-Area)/

- Documentation: *Used when a heat pump is associated with a separate and specified hot water vessel.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Heat-Loss-Source"></a>Hot-Water-Store-Heat-Loss-Source

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Hot-Water-Store-Heat-Loss-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Heat-Loss-Source)/

- Documentation: *The source of the hot water store heat loss information; if there is a hot water store. Not applicable if (a) combi boiler whose data source database or (b) instantaneous combi boiler or (c) combi boiler from SAP table or (d) instantaneous water heater.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"2"** - *from manufacturer declaration*
    - **"3"** - *from SAP table*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Heat-Loss"></a>Hot-Water-Store-Heat-Loss

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Hot-Water-Store-Heat-Loss`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Heat-Loss)/

- Documentation: *Hot water store declared loss in kWh/day; only if there is a hot water store and if manufacturer declared loss. Not applicable if (a) combi boiler whose data source database or (b) instantaneous combi boiler or (c) combi boiler from SAP table or (d) instantaneous water heater.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Insulation-Type"></a>Hot-Water-Store-Insulation-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Hot-Water-Store-Insulation-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Insulation-Type)/

- Documentation: *Hot water store insulation; only if there is a hot water store and if loss from SAP table. Not applicable if (a) combi boiler whose data source database or (b) instantaneous combi boiler or (c) combi boiler from SAP table or (d) instantaneous water heater.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *factory-applied*
    - **"2"** - *loose jacket*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Insulation-Thickness"></a>Hot-Water-Store-Insulation-Thickness

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Hot-Water-Store-Insulation-Thickness`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Insulation-Thickness)/

- Documentation: *Hot water store insulation thickness in mm; only if there is a hot water store and if loss from SAP table. Not applicable if (a) combi boiler whose data source database or (b) instantaneous combi boiler or (c) combi boiler from SAP table or (d) instantaneous water heater.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Thermal-Store-Near-Boiler"></a>Is-Thermal-Store-Near-Boiler

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Is-Thermal-Store-Near-Boiler`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Thermal-Store-Near-Boiler)/

- Documentation: *Thermal store connected to boiler by no more than 1.5 m of insulated pipework? Only if thermal store. Not applicable if combi boiler or instantaneous water heater.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Thermal-Store-Or-CPSU-In-Airing-Cupboard"></a>Is-Thermal-Store-Or-CPSU-In-Airing-Cupboard

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Is-Thermal-Store-Or-CPSU-In-Airing-Cupboard`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Thermal-Store-Or-CPSU-In-Airing-Cupboard)/

- Documentation: *Thermal store or CPSU in airing cupboard? Only if (a) boiler with integrated or hot-water-only thermal store, or (b) main heating is CPSU.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Has-Cylinder-Thermostat"></a>Has-Cylinder-Thermostat

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Has-Cylinder-Thermostat`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Has-Cylinder-Thermostat)/

- Documentation: *Hot water cylinder thermostat? Not applicable if combi boiler or instantaneous water heater.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Cylinder-In-Heated-Space"></a>Is-Cylinder-In-Heated-Space

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Is-Cylinder-In-Heated-Space`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Cylinder-In-Heated-Space)/

- Documentation: *Hot water cylinder in heated space? Not applicable if combi boiler or instantaneous water heater.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Hot-Water-Separately-Timed"></a>Is-Hot-Water-Separately-Timed

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Is-Hot-Water-Separately-Timed`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Hot-Water-Separately-Timed)/

- Documentation: *Hot water separately timed? Not applicable if combi boiler or instantaneous water heater.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Controls-Manufacturer"></a>Hot-Water-Controls-Manufacturer

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Hot-Water-Controls-Manufacturer`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Controls-Manufacturer)/

- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Controls-Model"></a>Hot-Water-Controls-Model

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Hot-Water-Controls-Model`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Controls-Model)/

- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems"></a>SAP-Community-Heating-Systems

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`SAP-Community-Heating-Systems`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems)/

- Documentation2: *Community heating systems used by the property.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Child elements: [`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System"></a>SAP-Community-Heating-System

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`SAP-Community-Heating-Systems`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems)/[`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)/

- Documentation2: *Details of a community system which heats the Main Building.*
- Parent element: [`SAP-Community-Heating-Systems`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems)
- Child elements: [`Community-Heating-Name`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Name) [`Community-Heating-CO2-Emission-Factor`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-CO2-Emission-Factor) [`Community-Heating-Primary-Energy-Factor`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Primary-Energy-Factor) [`Community-Heating-Use`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Use) [`Is-Community-Heating-Cylinder-In-Dwelling`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Is-Community-Heating-Cylinder-In-Dwelling) [`Is-HIU-In-Dwelling`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Is-HIU-In-Dwelling) [`HIU-Index-Number`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/HIU-Index-Number) [`Community-Heating-Distribution-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Distribution-Type) [`Community-Heat-Sources`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources) [`Community-Heating-Distribution-Loss-Factor`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Distribution-Loss-Factor) [`Charging-Linked-To-Heat-Use`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Charging-Linked-To-Heat-Use) [`Heat-Network-Index-Number`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Heat-Network-Index-Number) [`Sub-Network-Name`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Sub-Network-Name) [`Heat-Network-Existing`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Heat-Network-Existing) [`Heat-Network-Assessed-As-New`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Heat-Network-Assessed-As-New)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **2**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Name"></a>Community-Heating-Name

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`SAP-Community-Heating-Systems`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems)/[`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)/[`Community-Heating-Name`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Name)/

- Documentation: *The name of the community heating system*
- Parent element: [`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-CO2-Emission-Factor"></a>Community-Heating-CO2-Emission-Factor

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`SAP-Community-Heating-Systems`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems)/[`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)/[`Community-Heating-CO2-Emission-Factor`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-CO2-Emission-Factor)/

- Documentation: *the community heating CO2 emission factor*
- Parent element: [`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Primary-Energy-Factor"></a>Community-Heating-Primary-Energy-Factor

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`SAP-Community-Heating-Systems`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems)/[`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)/[`Community-Heating-Primary-Energy-Factor`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Primary-Energy-Factor)/

- Documentation: *The community heating Primary Energy Factor*
- Parent element: [`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Use"></a>Community-Heating-Use

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`SAP-Community-Heating-Systems`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems)/[`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)/[`Community-Heating-Use`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Use)/

- Documentation: *Specifies what kind of heating the community system is used for.*
- Parent element: [`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *space heating only*
    - **"2"** - *water heating only*
    - **"3"** - *space and water heating*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Is-Community-Heating-Cylinder-In-Dwelling"></a>Is-Community-Heating-Cylinder-In-Dwelling

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`SAP-Community-Heating-Systems`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems)/[`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)/[`Is-Community-Heating-Cylinder-In-Dwelling`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Is-Community-Heating-Cylinder-In-Dwelling)/

- Documentation: *Community heating, cylinder in dwelling?*
- Parent element: [`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Is-HIU-In-Dwelling"></a>Is-HIU-In-Dwelling

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`SAP-Community-Heating-Systems`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems)/[`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)/[`Is-HIU-In-Dwelling`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Is-HIU-In-Dwelling)/

- Documentation: *Community heating, HIU in dwelling?*
- Parent element: [`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/HIU-Index-Number"></a>HIU-Index-Number

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`SAP-Community-Heating-Systems`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems)/[`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)/[`HIU-Index-Number`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/HIU-Index-Number)/

- Documentation: *Heat Interface Unit index number, if present.*
- Parent element: [`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Distribution-Type"></a>Community-Heating-Distribution-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`SAP-Community-Heating-Systems`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems)/[`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)/[`Community-Heating-Distribution-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Distribution-Type)/

- Documentation: *Community heating distribution*
- Parent element: [`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"5"** - *calculated*
    - **"6"** - *unknown*
    - **"7"** - *Network not compliant with Code of Practice*
    - **"8"** - *Network compliant with Code of Practice*
    - **"9"** - *Two adjoining dwellings*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources"></a>Community-Heat-Sources

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`SAP-Community-Heating-Systems`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems)/[`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)/[`Community-Heat-Sources`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources)/

- Documentation: *To be provided when there is no Heat-Network-Index-Number.*
- Parent element: [`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)
- Child elements: [`Community-Heat-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source"></a>Community-Heat-Source

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`SAP-Community-Heating-Systems`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems)/[`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)/[`Community-Heat-Sources`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources)/[`Community-Heat-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source)/

- Parent element: [`Community-Heat-Sources`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources)
- Child elements: [`Heat-Source-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Heat-Source-Type) [`Heat-Fraction`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Heat-Fraction) [`Fuel-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Fuel-Type) [`PCDF-Fuel-Index`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/PCDF-Fuel-Index) [`Heat-Efficiency`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Heat-Efficiency) [`Power-Efficiency`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Power-Efficiency) [`Description`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Description) [`CHP-Electricity-Generation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/CHP-Electricity-Generation)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **5**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Heat-Source-Type"></a>Heat-Source-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`SAP-Community-Heating-Systems`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems)/[`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)/[`Community-Heat-Sources`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources)/[`Community-Heat-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source)/[`Heat-Source-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Heat-Source-Type)/

- Parent element: [`Community-Heat-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *CHP*
    - **"2"** - *boilers*
    - **"3"** - *heat pump*
    - **"4"** - *waste heat*
    - **"5"** - *geothermal*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Heat-Fraction"></a>Heat-Fraction

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`SAP-Community-Heating-Systems`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems)/[`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)/[`Community-Heat-Sources`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources)/[`Community-Heat-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source)/[`Heat-Fraction`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Heat-Fraction)/

- Documentation: *Fraction of heat for the system provided by this heat source.*
- Parent element: [`Community-Heat-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Fuel-Type"></a>Fuel-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`SAP-Community-Heating-Systems`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems)/[`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)/[`Community-Heat-Sources`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources)/[`Community-Heat-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source)/[`Fuel-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Fuel-Type)/

- Parent element: [`Community-Heat-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *Gas: mains gas*
    - **"2"** - *Gas: bulk LPG*
    - **"3"** - *Gas: bottled LPG*
    - **"4"** - *Oil: heating oil*
    - **"7"** - *Gas: biogas*
    - **"8"** - *LNG*
    - **"9"** - *LPG subject to Special Condition 18*
    - **"10"** - *Solid fuel: dual fuel appliance (mineral and wood)*
    - **"11"** - *Solid fuel: house coal*
    - **"12"** - *Solid fuel: manufactured smokeless fuel*
    - **"15"** - *Solid fuel: anthracite*
    - **"20"** - *Solid fuel: wood logs*
    - **"21"** - *Solid fuel: wood chips*
    - **"22"** - *Solid fuel: wood pellets (in bags, for secondary heating)*
    - **"23"** - *Solid fuel: wood pellets (bulk supply in bags, for main heating)*
    - **"36"** - *Electricity: electricity sold to grid*
    - **"37"** - *Electricity: electricity displaced from grid*
    - **"39"** - *Electricity: electricity, unspecified tariff*
    - **"41"** - *Community heating schemes: heat from electric heat pump*
    - **"42"** - *Community heating schemes: heat from boilers - waste combustion*
    - **"43"** - *Community heating schemes: heat from boilers - biomass*
    - **"44"** - *Community heating schemes: heat from boilers - biogas*
    - **"45"** - *Community heating schemes: waste heat from power stations*
    - **"46"** - *Community heating schemes: geothermal heat source*
    - **"47"** - *Community heating schemes: high grade heat recovered from process*
    - **"48"** - *Community heating schemes: heat from CHP*
    - **"49"** - *Community heating schemes: low grade heat recovered from process*
    - **"50"** - *Community heating schemes: electricity for pumping in distribution network*
    - **"51"** - *Community heating schemes: heat from mains gas*
    - **"52"** - *Community heating schemes: heat from LPG*
    - **"53"** - *Community heating schemes: heat from oil*
    - **"54"** - *Community heating schemes: heat from coal*
    - **"55"** - *Community heating schemes: heat from B30D*
    - **"56"** - *Community heating schemes: heat from boilers that can use mineral oil or biodiesel*
    - **"57"** - *Community heating schemes: heat from boilers using biodiesel from any biomass source*
    - **"58"** - *Community heating schemes: biodiesel from vegetable oil only*
    - **"71"** - *biodiesel from any biomass source*
    - **"72"** - *biodiesel from used cooking oil only*
    - **"73"** - *biodiesel from vegetable oil only*
    - **"74"** - *appliances able to use mineral oil or liquid biofuel*
    - **"75"** - *B30K*
    - **"76"** - *bioethanol from any biomass source*
    - **"99"** - *Fuel data from pcdb*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/PCDF-Fuel-Index"></a>PCDF-Fuel-Index

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`SAP-Community-Heating-Systems`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems)/[`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)/[`Community-Heat-Sources`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources)/[`Community-Heat-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source)/[`PCDF-Fuel-Index`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/PCDF-Fuel-Index)/

- Parent element: [`Community-Heat-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Heat-Efficiency"></a>Heat-Efficiency

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`SAP-Community-Heating-Systems`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems)/[`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)/[`Community-Heat-Sources`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources)/[`Community-Heat-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source)/[`Heat-Efficiency`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Heat-Efficiency)/

- Documentation: *Heat efficiency in %.*
- Parent element: [`Community-Heat-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Power-Efficiency"></a>Power-Efficiency

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`SAP-Community-Heating-Systems`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems)/[`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)/[`Community-Heat-Sources`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources)/[`Community-Heat-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source)/[`Power-Efficiency`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Power-Efficiency)/

- Documentation: *Power efficiency in %. Include when heat source is CHP.*
- Parent element: [`Community-Heat-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Description"></a>Description

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`SAP-Community-Heating-Systems`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems)/[`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)/[`Community-Heat-Sources`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources)/[`Community-Heat-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source)/[`Description`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Description)/

- Parent element: [`Community-Heat-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/CHP-Electricity-Generation"></a>CHP-Electricity-Generation

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`SAP-Community-Heating-Systems`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems)/[`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)/[`Community-Heat-Sources`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources)/[`Community-Heat-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source)/[`CHP-Electricity-Generation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/CHP-Electricity-Generation)/

- Documentation: *CHP Electricity generation options from table 12f.*
- Parent element: [`Community-Heat-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"81"** - *New CHP, export only.*
    - **"82"** - *New CHP, flexible operation.*
    - **"83"** - *New CHP, standard.*
    - **"84"** - *Existing CHP (2015+), export only.*
    - **"85"** - *Existing CHP (2015+), flexible operation.*
    - **"86"** - *Existing CHP (2015+),standard.*
    - **"87"** - *Existing CHP (pre-2015), export only.*
    - **"88"** - *Existing CHP (pre-2015), flexible operation.*
    - **"89"** - *Existing CHP (pre-2015), standard.*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Distribution-Loss-Factor"></a>Community-Heating-Distribution-Loss-Factor

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`SAP-Community-Heating-Systems`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems)/[`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)/[`Community-Heating-Distribution-Loss-Factor`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Distribution-Loss-Factor)/

- Documentation: *Used when Community-Heating-Distribution-Type is calculated.*
- Parent element: [`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Charging-Linked-To-Heat-Use"></a>Charging-Linked-To-Heat-Use

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`SAP-Community-Heating-Systems`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems)/[`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)/[`Charging-Linked-To-Heat-Use`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Charging-Linked-To-Heat-Use)/

- Documentation: *Used for hot-water-only systems.*
- Parent element: [`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Heat-Network-Index-Number"></a>Heat-Network-Index-Number

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`SAP-Community-Heating-Systems`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems)/[`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)/[`Heat-Network-Index-Number`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Heat-Network-Index-Number)/

- Documentation: *Index number of heat network, if applicable.*
- Parent element: [`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Sub-Network-Name"></a>Sub-Network-Name

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`SAP-Community-Heating-Systems`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems)/[`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)/[`Sub-Network-Name`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Sub-Network-Name)/

- Documentation: *The name by which the sub community heat network is known.*
- Parent element: [`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Heat-Network-Existing"></a>Heat-Network-Existing

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`SAP-Community-Heating-Systems`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems)/[`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)/[`Heat-Network-Existing`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Heat-Network-Existing)/

- Documentation: *Whether the heat network is existing or new.*
- Parent element: [`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Heat-Network-Assessed-As-New"></a>Heat-Network-Assessed-As-New

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`SAP-Community-Heating-Systems`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems)/[`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)/[`Heat-Network-Assessed-As-New`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Heat-Network-Assessed-As-New)/

- Documentation: *Whether the heat network is assessed as a new heat network (post June 2022) for Eng with a standalone gas boiler notional building.*
- Parent element: [`SAP-Community-Heating-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details"></a>Main-Heating-Details

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/

- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Child elements: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating"></a>Main-Heating

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/

- Parent element: [`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)
- Child elements: [`Main-Heating-Number`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Number) [`Main-Heating-Category`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Category) [`Main-Heating-Data-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Data-Source) [`Main-Heating-Index-Number`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Index-Number) [`Main-Heating-Manufacturer`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Manufacturer) [`Main-Heating-Model`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Model) [`Main-Heating-Commissioning-Certificate`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Commissioning-Certificate) [`Main-Heating-Installation-Engineer`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Installation-Engineer) [`Is-Condensing-Boiler`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Condensing-Boiler) [`Condensing-Boiler-Heat-Distribution`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Condensing-Boiler-Heat-Distribution) [`Heat-Pump-Heat-Distribution`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heat-Pump-Heat-Distribution) [`Gas-Or-Oil-Boiler-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Gas-Or-Oil-Boiler-Type) [`Combi-Boiler-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Combi-Boiler-Type) [`Case-Heat-Emission`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Case-Heat-Emission) [`Heat-Transfer-To-Water`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heat-Transfer-To-Water) [`Solid-Fuel-Boiler-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Solid-Fuel-Boiler-Type) [`Main-Heating-Code`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Code) [`Main-Fuel-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Fuel-Type) [`PCDF-Fuel-Index`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/PCDF-Fuel-Index) [`Main-Heating-Control`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Control) [`Heat-Emitter-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heat-Emitter-Type) [`Underfloor-Heat-Emitter-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Underfloor-Heat-Emitter-Type) [`Main-Heating-Flue-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Flue-Type) [`Is-Flue-Fan-Present`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Flue-Fan-Present) [`Is-Central-Heating-Pump-In-Heated-Space`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Central-Heating-Pump-In-Heated-Space) [`Is-Oil-Pump-In-Heated-Space`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Oil-Pump-In-Heated-Space) [`Is-Interlocked-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Interlocked-System) [`Has-Separate-Delayed-Start`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Has-Separate-Delayed-Start) [`Boiler-Fuel-Feed`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Boiler-Fuel-Feed) [`Is-Main-Heating-HETAS-Approved`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Main-Heating-HETAS-Approved) [`Electric-CPSU-Operating-Temperature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Electric-CPSU-Operating-Temperature) [`Main-Heating-Fraction`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Fraction) [`Burner-Control`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Burner-Control) [`Efficiency-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Efficiency-Type) [`Main-Heating-Efficiency-Winter`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Efficiency-Winter) [`Main-Heating-Efficiency-Summer`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Efficiency-Summer) [`Main-Heating-Efficiency`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Efficiency) [`Main-Heating-System-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-System-Type) [`Has-FGHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Has-FGHRS) [`FGHRS-Index-Number`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Index-Number) [`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source) [`Main-Heating-Declared-Values`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values) [`Storage-Heaters`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters) [`Emitter-Temperature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Emitter-Temperature) [`MCS-Installed-Heat-Pump`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/MCS-Installed-Heat-Pump) [`Central-Heating-Pump-Age`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Central-Heating-Pump-Age) [`Control-Index-Number`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Control-Index-Number) [`Heating-Controller-Function`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heating-Controller-Function) [`Heating-Controller-Ecodesign-Class`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heating-Controller-Ecodesign-Class) [`Heating-Controller-Manufacturer`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heating-Controller-Manufacturer) [`Heating-Controller-Model`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heating-Controller-Model)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **2**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Number"></a>Main-Heating-Number

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Main-Heating-Number`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Number)/

- Documentation: *Identifies the main heating as system 1 or system 2. System 1 must always be present, system 2 is included only when there are two systems.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Category"></a>Main-Heating-Category

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Main-Heating-Category`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Category)/

- Documentation: *Category of heating system for the main heating system.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *none*
    - **"2"** - *boiler with radiators or underfloor heating*
    - **"3"** - *micro-cogeneration*
    - **"4"** - *heat pump with radiators or underfloor heating*
    - **"5"** - *heat pump with warm air distribution*
    - **"6"** - *community heating system*
    - **"7"** - *electric storage heaters*
    - **"8"** - *electric underfloor heating*
    - **"9"** - *warm air system (not heat pump)*
    - **"10"** - *room heaters*
    - **"11"** - *other system*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Data-Source"></a>Main-Heating-Data-Source

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Main-Heating-Data-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Data-Source)/

- Documentation: *Source of main heating system data.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *from database*
    - **"2"** - *from manufacturer declaration*
    - **"3"** - *from SAP table*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Index-Number"></a>Main-Heating-Index-Number

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Main-Heating-Index-Number`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Index-Number)/

- Documentation: *The ID of the heating system from the product database, if system from database.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Manufacturer"></a>Main-Heating-Manufacturer

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Main-Heating-Manufacturer`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Manufacturer)/

- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Model"></a>Main-Heating-Model

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Main-Heating-Model`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Model)/

- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Commissioning-Certificate"></a>Main-Heating-Commissioning-Certificate

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Main-Heating-Commissioning-Certificate`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Commissioning-Certificate)/

- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Installation-Engineer"></a>Main-Heating-Installation-Engineer

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Main-Heating-Installation-Engineer`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Installation-Engineer)/

- Documentation: *Main heating installation engineer registration reference.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Condensing-Boiler"></a>Is-Condensing-Boiler

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Is-Condensing-Boiler`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Condensing-Boiler)/

- Documentation: *Is the boiler a condensing boiler? If boiler efficiency is manufacturer declaration.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Condensing-Boiler-Heat-Distribution"></a>Condensing-Boiler-Heat-Distribution

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Condensing-Boiler-Heat-Distribution`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Condensing-Boiler-Heat-Distribution)/

- Documentation: *The temperature distribution of the condensing boiler.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heat-Pump-Heat-Distribution"></a>Heat-Pump-Heat-Distribution

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Heat-Pump-Heat-Distribution`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heat-Pump-Heat-Distribution)/

- Documentation: *The temperature distribution of the heat pump, for wet systems only.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Gas-Or-Oil-Boiler-Type"></a>Gas-Or-Oil-Boiler-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Gas-Or-Oil-Boiler-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Gas-Or-Oil-Boiler-Type)/

- Documentation: *Boiler type; if boiler efficiency is manufacturer declaration and fuel is gas or oil.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *regular*
    - **"2"** - *combi*
    - **"3"** - *CPSU*
    - **"4"** - *range cooker*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Combi-Boiler-Type"></a>Combi-Boiler-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Combi-Boiler-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Combi-Boiler-Type)/

- Documentation: *Combi boiler type; if it is a combi boiler and boiler efficiency is manufacturer declaration.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *instantaneous, no store or keep hot*
    - **"2"** - *primary storage*
    - **"3"** - *secondary storage*
    - **"4"** - *CPSU*
    - **"5"** - *untimed keep-hot by fuel*
    - **"6"** - *timed keep hot by fuel*
    - **"7"** - *untimed keep-hot by electricity*
    - **"8"** - *timed keep hot by electricity*
    - **"9"** - *untimed keep-hot by fuel and electricity*
    - **"10"** - *timed keep hot by fuel and electricity*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Case-Heat-Emission"></a>Case-Heat-Emission

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Case-Heat-Emission`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Case-Heat-Emission)/

- Documentation: *Case heat emission at full load in kW; if it is a range cooker boiler and boiler efficiency is manufacturer declaration.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heat-Transfer-To-Water"></a>Heat-Transfer-To-Water

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Heat-Transfer-To-Water`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heat-Transfer-To-Water)/

- Documentation: *Heat transfer to water at full load in kW; if it is a range cooker boiler and boiler efficiency is manufacturer declaration.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Solid-Fuel-Boiler-Type"></a>Solid-Fuel-Boiler-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Solid-Fuel-Boiler-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Solid-Fuel-Boiler-Type)/

- Documentation: *Boiler type; if boiler efficiency is manufacturer declaration and fuel is solid.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *independent*
    - **"2"** - *open fire*
    - **"3"** - *closed room heater*
    - **"4"** - *range cooker*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Code"></a>Main-Heating-Code

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Main-Heating-Code`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Code)/

- Documentation: *Main heating code; when heating data source is SAP table.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Fuel-Type"></a>Main-Fuel-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Main-Fuel-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Fuel-Type)/

- Documentation: *The type of fuel used to power the central heating e.g. Gas, Electricity; not used if main heating system is community heating scheme.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *Gas: mains gas*
    - **"2"** - *Gas: bulk LPG*
    - **"3"** - *Gas: bottled LPG*
    - **"4"** - *Oil: heating oil*
    - **"7"** - *Gas: biogas*
    - **"8"** - *LNG*
    - **"9"** - *LPG subject to Special Condition 18*
    - **"10"** - *Solid fuel: dual fuel appliance (mineral and wood)*
    - **"11"** - *Solid fuel: house coal*
    - **"12"** - *Solid fuel: manufactured smokeless fuel*
    - **"15"** - *Solid fuel: anthracite*
    - **"20"** - *Solid fuel: wood logs*
    - **"21"** - *Solid fuel: wood chips*
    - **"22"** - *Solid fuel: wood pellets (in bags, for secondary heating)*
    - **"23"** - *Solid fuel: wood pellets (bulk supply in bags, for main heating)*
    - **"36"** - *Electricity: electricity sold to grid*
    - **"37"** - *Electricity: electricity displaced from grid*
    - **"39"** - *Electricity: electricity, unspecified tariff*
    - **"41"** - *Community heating schemes: heat from electric heat pump*
    - **"42"** - *Community heating schemes: heat from boilers - waste combustion*
    - **"43"** - *Community heating schemes: heat from boilers - biomass*
    - **"44"** - *Community heating schemes: heat from boilers - biogas*
    - **"45"** - *Community heating schemes: waste heat from power stations*
    - **"46"** - *Community heating schemes: geothermal heat source*
    - **"47"** - *Community heating schemes: high grade heat recovered from process*
    - **"48"** - *Community heating schemes: heat from CHP*
    - **"49"** - *Community heating schemes: low grade heat recovered from process*
    - **"50"** - *Community heating schemes: electricity for pumping in distribution network*
    - **"51"** - *Community heating schemes: heat from mains gas*
    - **"52"** - *Community heating schemes: heat from LPG*
    - **"53"** - *Community heating schemes: heat from oil*
    - **"54"** - *Community heating schemes: heat from coal*
    - **"55"** - *Community heating schemes: heat from B30D*
    - **"56"** - *Community heating schemes: heat from boilers that can use mineral oil or biodiesel*
    - **"57"** - *Community heating schemes: heat from boilers using biodiesel from any biomass source*
    - **"58"** - *Community heating schemes: biodiesel from vegetable oil only*
    - **"71"** - *biodiesel from any biomass source*
    - **"72"** - *biodiesel from used cooking oil only*
    - **"73"** - *biodiesel from vegetable oil only*
    - **"74"** - *appliances able to use mineral oil or liquid biofuel*
    - **"75"** - *B30K*
    - **"76"** - *bioethanol from any biomass source*
    - **"99"** - *Fuel data from pcdb*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/PCDF-Fuel-Index"></a>PCDF-Fuel-Index

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`PCDF-Fuel-Index`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/PCDF-Fuel-Index)/

- Documentation: *PCDF index number of the fuel type, only if Main-Fuel-Type is 99 (fuel from database).*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Control"></a>Main-Heating-Control

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Main-Heating-Control`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Control)/

- Documentation: *Type of Main Control for the Heating System.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heat-Emitter-Type"></a>Heat-Emitter-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Heat-Emitter-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heat-Emitter-Type)/

- Documentation: *Identifies the means by which the central heating system (if present) emits heat; only when wet system (radiators or underfloor).*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *radiators*
    - **"2"** - *underfloor*
    - **"3"** - *both radiators and underfloor*
    - **"4"** - *fan coil units*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Underfloor-Heat-Emitter-Type"></a>Underfloor-Heat-Emitter-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Underfloor-Heat-Emitter-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Underfloor-Heat-Emitter-Type)/

- Documentation: *Means by which an underfloor heating system (if present) emits heat; only when wet system (underfloor).*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *in concrete slab*
    - **"2"** - *in screed above insulation*
    - **"3"** - *in timber floor*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Flue-Type"></a>Main-Heating-Flue-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Main-Heating-Flue-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Flue-Type)/

- Documentation: *The type of main heating flue; only if flued appliance.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *open flue*
    - **"2"** - *balanced flue*
    - **"3"** - *chimney*
    - **"4"** - *omitted (boiler is in an outhouse, so its flue arrangements are not relevant)*
    - **"5"** - *unknown (there is a flue, but its type could not be determined)*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Flue-Fan-Present"></a>Is-Flue-Fan-Present

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Is-Flue-Fan-Present`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Flue-Fan-Present)/

- Documentation: *Indicates whether the heating system contains a fan flue; only if boiler.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Central-Heating-Pump-In-Heated-Space"></a>Is-Central-Heating-Pump-In-Heated-Space

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Is-Central-Heating-Pump-In-Heated-Space`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Central-Heating-Pump-In-Heated-Space)/

- Documentation: *Central heating pump in heated space? Only when wet system (radiators or underfloor).*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Oil-Pump-In-Heated-Space"></a>Is-Oil-Pump-In-Heated-Space

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Is-Oil-Pump-In-Heated-Space`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Oil-Pump-In-Heated-Space)/

- Documentation: *Oil pump in heated space? Only if oil boiler.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Interlocked-System"></a>Is-Interlocked-System

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Is-Interlocked-System`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Interlocked-System)/

- Documentation: *Interlocked system? Only when wet system (radiators or underfloor).*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Has-Separate-Delayed-Start"></a>Has-Separate-Delayed-Start

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Has-Separate-Delayed-Start`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Has-Separate-Delayed-Start)/

- Documentation: *True if there is a delayed start control separate from a controller in the database.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Boiler-Fuel-Feed"></a>Boiler-Fuel-Feed

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Boiler-Fuel-Feed`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Boiler-Fuel-Feed)/

- Documentation: *The type of boiler fuel feed; only if solid fuel boiler with manufacturer declaration.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *gravity*
    - **"2"** - *manual*
    - **"3"** - *screw*
    - **"4"** - *other*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Main-Heating-HETAS-Approved"></a>Is-Main-Heating-HETAS-Approved

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Is-Main-Heating-HETAS-Approved`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Main-Heating-HETAS-Approved)/

- Documentation: *Main heating appliance is HETAS approved? Only if solid fuel.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Electric-CPSU-Operating-Temperature"></a>Electric-CPSU-Operating-Temperature

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Electric-CPSU-Operating-Temperature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Electric-CPSU-Operating-Temperature)/

- Documentation: *Electric CPSU operating temperature in Celcius; only if main heating is electric CPSU.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Fraction"></a>Main-Heating-Fraction

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Main-Heating-Fraction`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Fraction)/

- Documentation: *Fraction of main heating provided by this system, is 1 if only one main system.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Burner-Control"></a>Burner-Control

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Burner-Control`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Burner-Control)/

- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *unknown*
    - **"2"** - *on/off (gas and oil burners)*
    - **"3"** - *modulating (gas and oil boilers)*
    - **"4"** - *manual (solid fuel boilers)*
    - **"5"** - *electrical (solid fuel boilers)*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Efficiency-Type"></a>Efficiency-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Efficiency-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Efficiency-Type)/

- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *not gas or oil boiler*
    - **"2"** - *SEDBUK(2005)*
    - **"3"** - *SEDBUK(2009)*
    - **"4"** - *winter and summer*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Efficiency-Winter"></a>Main-Heating-Efficiency-Winter

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Main-Heating-Efficiency-Winter`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Efficiency-Winter)/

- Documentation: *To be used if main heating data is manufacturer declaration and Efficiency-Type is winter and summer.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Efficiency-Summer"></a>Main-Heating-Efficiency-Summer

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Main-Heating-Efficiency-Summer`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Efficiency-Summer)/

- Documentation: *To be used if main heating data is manufacturer declaration and Efficiency-Type is winter and summer.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Efficiency"></a>Main-Heating-Efficiency

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Main-Heating-Efficiency`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Efficiency)/

- Documentation: *If main heating is any system other than heat network.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-System-Type"></a>Main-Heating-System-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Main-Heating-System-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-System-Type)/

- Documentation: *Main heating system type or technology, for e.g., combi boiler, air source heat pump, etc.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Has-FGHRS"></a>Has-FGHRS

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Has-FGHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Has-FGHRS)/

- Documentation: *Flue Gas Heat Recovery System.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Index-Number"></a>FGHRS-Index-Number

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`FGHRS-Index-Number`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Index-Number)/

- Documentation: *FGHRS index number; only if FGHRS.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source"></a>FGHRS-Energy-Source

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)/

- Documentation2: *Details of the main Electricity supply to the Property.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Child elements: [`PV-Arrays`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays) [`Wind-Turbines`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines) [`Electricity-Tariff`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Electricity-Tariff) [`Hydro-Electric-Generation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation) [`Hydro-Electric-Certificate`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Certificate) [`Hydro-Electric-Generation-Months`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months) [`Is-Hydro-Output-Connected-To-Dwelling-Meter`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Is-Hydro-Output-Connected-To-Dwelling-Meter)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays"></a>PV-Arrays

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)/[`PV-Arrays`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays)/

- Parent element: [`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)
- Child elements: [`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array"></a>PV-Array

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)/[`PV-Arrays`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays)/[`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array)/

- Parent element: [`PV-Arrays`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays)
- Child elements: [`Peak-Power`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Peak-Power) [`Orientation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Orientation) [`Pitch`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Pitch) [`Overshading`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Overshading) [`MCS-Certificate`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/MCS-Certificate) [`MCS-Certificate-Reference`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/MCS-Certificate-Reference) [`PV-Panel-Manufacturer-Name`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/PV-Panel-Manufacturer-Name) [`Overshading-MCS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Overshading-MCS)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **3**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Peak-Power"></a>Peak-Power

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)/[`PV-Arrays`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays)/[`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array)/[`Peak-Power`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Peak-Power)/

- Documentation: *Peak kW of photovoltaics (PVs) (kWp); 0.0 if none.*
- Parent element: [`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Orientation"></a>Orientation

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)/[`PV-Arrays`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays)/[`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array)/[`Orientation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Orientation)/

- Documentation: *PV orientation; only if peak kWp > 0.*
- Parent element: [`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *North*
    - **"2"** - *North East*
    - **"3"** - *East*
    - **"4"** - *South East*
    - **"5"** - *South*
    - **"6"** - *South West*
    - **"7"** - *West*
    - **"8"** - *North West*
    - **"ND"** - *To be used when the pitch is horizontal*
    - **"NR"** - *not recorded - for backwards compatibility only; do not use*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Pitch"></a>Pitch

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)/[`PV-Arrays`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays)/[`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array)/[`Pitch`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Pitch)/

- Documentation: *PV pitch; only if peak kWp > 0.*
- Parent element: [`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *horizontal*
    - **"2"** - *30 degrees*
    - **"3"** - *45 degrees*
    - **"4"** - *60 degrees*
    - **"5"** - *vertical*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Overshading"></a>Overshading

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)/[`PV-Arrays`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays)/[`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array)/[`Overshading`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Overshading)/

- Documentation: *PV overshading; only if peak kWp > 0 and no MCS certificate.*
- Parent element: [`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *none or very little*
    - **"2"** - *modest*
    - **"3"** - *significant*
    - **"4"** - *heavy*
    - **"5"** - *severe*
    - **"ND"** - *for backwards compatability only; do not use*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/MCS-Certificate"></a>MCS-Certificate

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)/[`PV-Arrays`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays)/[`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array)/[`MCS-Certificate`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/MCS-Certificate)/

- Documentation: *Does the installation have a MCS certificate.*
- Parent element: [`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/MCS-Certificate-Reference"></a>MCS-Certificate-Reference

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)/[`PV-Arrays`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays)/[`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array)/[`MCS-Certificate-Reference`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/MCS-Certificate-Reference)/

- Documentation: *MCS certificate reference number*
- Parent element: [`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/PV-Panel-Manufacturer-Name"></a>PV-Panel-Manufacturer-Name

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)/[`PV-Arrays`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays)/[`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array)/[`PV-Panel-Manufacturer-Name`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/PV-Panel-Manufacturer-Name)/

- Documentation: *Manufacturer of PV panels*
- Parent element: [`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Overshading-MCS"></a>Overshading-MCS

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)/[`PV-Arrays`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays)/[`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array)/[`Overshading-MCS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Overshading-MCS)/

- Documentation: *Overshading factor calculated according to MCS.*
- Parent element: [`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines"></a>Wind-Turbines

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)/[`Wind-Turbines`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines)/

- Parent element: [`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)
- Child elements: [`Wind-Turbine`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine"></a>Wind-Turbine

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)/[`Wind-Turbines`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines)/[`Wind-Turbine`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine)/

- Parent element: [`Wind-Turbines`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines)
- Child elements: [`Wind-Turbine-Manufacturer-Name`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Manufacturer-Name) [`Wind-Turbine-Certificate`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Certificate) [`Wind-Turbine-Rotor-Diameter`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Rotor-Diameter) [`Wind-Turbine-Hub-Height`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Hub-Height)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **99**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Manufacturer-Name"></a>Wind-Turbine-Manufacturer-Name

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)/[`Wind-Turbines`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines)/[`Wind-Turbine`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine)/[`Wind-Turbine-Manufacturer-Name`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Manufacturer-Name)/

- Documentation: *Wind turbine manufacturer name.*
- Parent element: [`Wind-Turbine`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Certificate"></a>Wind-Turbine-Certificate

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)/[`Wind-Turbines`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines)/[`Wind-Turbine`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine)/[`Wind-Turbine-Certificate`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Certificate)/

- Documentation: *Wind turbine certificate.*
- Parent element: [`Wind-Turbine`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Rotor-Diameter"></a>Wind-Turbine-Rotor-Diameter

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)/[`Wind-Turbines`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines)/[`Wind-Turbine`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine)/[`Wind-Turbine-Rotor-Diameter`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Rotor-Diameter)/

- Documentation: *Wind turbine rotor diameter in metres; only if wind turbine.*
- Parent element: [`Wind-Turbine`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Hub-Height"></a>Wind-Turbine-Hub-Height

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)/[`Wind-Turbines`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines)/[`Wind-Turbine`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine)/[`Wind-Turbine-Hub-Height`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Hub-Height)/

- Documentation: *Wind turbine hub height above building in metres; only if wind turbine.*
- Parent element: [`Wind-Turbine`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Electricity-Tariff"></a>Electricity-Tariff

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)/[`Electricity-Tariff`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Electricity-Tariff)/

- Documentation: *Type of electricity tariff.*
- Parent element: [`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *standard tariff*
    - **"2"** - *off-peak 7 hour*
    - **"3"** - *off-peak 10 hour*
    - **"4"** - *24 hour*
    - **"5"** - *off-peak 18 hour*
    - **"ND"** - *not applicable*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation"></a>Hydro-Electric-Generation

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)/[`Hydro-Electric-Generation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation)/

- Documentation: *Electricity generated by hydro-electric generator, in kWh/year. To be provided if Hydro-Electric-Generation-Month is not provided.*
- Parent element: [`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Certificate"></a>Hydro-Electric-Certificate

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)/[`Hydro-Electric-Certificate`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Certificate)/

- Documentation: *Reference to certification of hydro electric output.*
- Parent element: [`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months"></a>Hydro-Electric-Generation-Months

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)/[`Hydro-Electric-Generation-Months`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months)/

- Documentation: *Electricity generated by hydro-electric generator, in kWh/month. To be provided if Hydro-Electric-Generation is not provided.*
- Parent element: [`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)
- Child elements: [`Hydro-Electric-Generation-Month`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month"></a>Hydro-Electric-Generation-Month

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)/[`Hydro-Electric-Generation-Months`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months)/[`Hydro-Electric-Generation-Month`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month)/

- Parent element: [`Hydro-Electric-Generation-Months`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months)
- Child elements: [`Hydro-Month`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month/Hydro-Month) [`Hydro-Value`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month/Hydro-Value)
- Has text value: *False*
- Minimum occurrence: **12**
- Maximum occurrence: **12**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month/Hydro-Month"></a>Hydro-Month

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)/[`Hydro-Electric-Generation-Months`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months)/[`Hydro-Electric-Generation-Month`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month)/[`Hydro-Month`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month/Hydro-Month)/

- Parent element: [`Hydro-Electric-Generation-Month`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"Jan"** - **
    - **"Feb"** - **
    - **"Mar"** - **
    - **"Apr"** - **
    - **"May"** - **
    - **"Jun"** - **
    - **"Jul"** - **
    - **"Aug"** - **
    - **"Sep"** - **
    - **"Oct"** - **
    - **"Nov"** - **
    - **"Dec"** - **
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month/Hydro-Value"></a>Hydro-Value

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)/[`Hydro-Electric-Generation-Months`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months)/[`Hydro-Electric-Generation-Month`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month)/[`Hydro-Value`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month/Hydro-Value)/

- Documentation: *Hydro electricity in kWh in month.*
- Parent element: [`Hydro-Electric-Generation-Month`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Is-Hydro-Output-Connected-To-Dwelling-Meter"></a>Is-Hydro-Output-Connected-To-Dwelling-Meter

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)/[`Is-Hydro-Output-Connected-To-Dwelling-Meter`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Is-Hydro-Output-Connected-To-Dwelling-Meter)/

- Documentation: *Whether the hydro-electric station is connected to dwelling's electricity meter*
- Parent element: [`FGHRS-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values"></a>Main-Heating-Declared-Values

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Main-Heating-Declared-Values`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values)/

- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Child elements: [`Efficiency`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values/Efficiency) [`Make-Model`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values/Make-Model) [`Test-Method`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values/Test-Method)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values/Efficiency"></a>Efficiency

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Main-Heating-Declared-Values`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values)/[`Efficiency`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values/Efficiency)/

- Parent element: [`Main-Heating-Declared-Values`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values/Make-Model"></a>Make-Model

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Main-Heating-Declared-Values`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values)/[`Make-Model`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values/Make-Model)/

- Parent element: [`Main-Heating-Declared-Values`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values/Test-Method"></a>Test-Method

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Main-Heating-Declared-Values`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values)/[`Test-Method`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values/Test-Method)/

- Parent element: [`Main-Heating-Declared-Values`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters"></a>Storage-Heaters

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Storage-Heaters`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters)/

- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Child elements: [`Storage-Heater`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater"></a>Storage-Heater

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Storage-Heaters`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters)/[`Storage-Heater`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater)/

- Parent element: [`Storage-Heaters`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters)
- Child elements: [`Number-Of-Heaters`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater/Number-Of-Heaters) [`Index-Number`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater/Index-Number) [`High-Heat-Retention`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater/High-Heat-Retention)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **4**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater/Number-Of-Heaters"></a>Number-Of-Heaters

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Storage-Heaters`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters)/[`Storage-Heater`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater)/[`Number-Of-Heaters`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater/Number-Of-Heaters)/

- Documentation: *The number of storage heaters with this index number.*
- Parent element: [`Storage-Heater`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater/Index-Number"></a>Index-Number

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Storage-Heaters`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters)/[`Storage-Heater`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater)/[`Index-Number`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater/Index-Number)/

- Documentation: *The index number of the heater from the product database.*
- Parent element: [`Storage-Heater`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater/High-Heat-Retention"></a>High-Heat-Retention

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Storage-Heaters`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters)/[`Storage-Heater`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater)/[`High-Heat-Retention`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater/High-Heat-Retention)/

- Documentation: *Whether heater is high heat retention type.*
- Parent element: [`Storage-Heater`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Emitter-Temperature"></a>Emitter-Temperature

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Emitter-Temperature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Emitter-Temperature)/

- Documentation: *Gas and oil boilers and heat pump from database: 0, 1, 3 or 4 Other heat pump 0, 2 or 4. Other systems NA.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"0"** - *unknown*
    - **"1"** - *over 45degC*
    - **"2"** - *over 35degC*
    - **"3"** - *over 35degC and less than or equal to 45degC*
    - **"4"** - *less than or equal to 35degC*
    - **"NA"** - *not applicable for the heating system*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/MCS-Installed-Heat-Pump"></a>MCS-Installed-Heat-Pump

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`MCS-Installed-Heat-Pump`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/MCS-Installed-Heat-Pump)/

- Documentation: *Whether heat pump was installed under the Microgeneration Certification Scheme.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Central-Heating-Pump-Age"></a>Central-Heating-Pump-Age

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Central-Heating-Pump-Age`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Central-Heating-Pump-Age)/

- Documentation: *Included for systems with a central heating pump, i.e. wet system.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"0"** - *unknown*
    - **"1"** - *2012 or earlier*
    - **"2"** - *2013 or later*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Control-Index-Number"></a>Control-Index-Number

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Control-Index-Number`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Control-Index-Number)/

- Documentation: *The ID of the controller from the product database.*
- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heating-Controller-Function"></a>Heating-Controller-Function

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Heating-Controller-Function`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heating-Controller-Function)/

- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heating-Controller-Ecodesign-Class"></a>Heating-Controller-Ecodesign-Class

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Heating-Controller-Ecodesign-Class`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heating-Controller-Ecodesign-Class)/

- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heating-Controller-Manufacturer"></a>Heating-Controller-Manufacturer

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Heating-Controller-Manufacturer`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heating-Controller-Manufacturer)/

- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heating-Controller-Model"></a>Heating-Controller-Model

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details)/[`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)/[`Heating-Controller-Model`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heating-Controller-Model)/

- Parent element: [`Main-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Heating-Design-Water-Use"></a>SAP-Heating-Design-Water-Use

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`SAP-Heating-Design-Water-Use`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Heating-Design-Water-Use)/

- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *<= 125 litres per person per day*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Systems-Interaction"></a>Main-Heating-Systems-Interaction

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Main-Heating-Systems-Interaction`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Systems-Interaction)/

- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *both main heating systems provide heat to the whole property*
    - **"2"** - *the main heating systems are separate and heat different parts of the property*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values"></a>Secondary-Heating-Declared-Values

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Secondary-Heating-Declared-Values`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values)/

- Documentation: *Use when manufacturer's declared values.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Child elements: [`Efficiency`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values/Efficiency) [`Make-Model`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values/Make-Model) [`Test-Method`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values/Test-Method)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values/Efficiency"></a>Efficiency

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Secondary-Heating-Declared-Values`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values)/[`Efficiency`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values/Efficiency)/

- Parent element: [`Secondary-Heating-Declared-Values`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values/Make-Model"></a>Make-Model

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Secondary-Heating-Declared-Values`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values)/[`Make-Model`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values/Make-Model)/

- Parent element: [`Secondary-Heating-Declared-Values`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values/Test-Method"></a>Test-Method

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Secondary-Heating-Declared-Values`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values)/[`Test-Method`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values/Test-Method)/

- Parent element: [`Secondary-Heating-Declared-Values`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Primary-Pipework-Insulation"></a>Primary-Pipework-Insulation

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Primary-Pipework-Insulation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Primary-Pipework-Insulation)/

- Documentation: *Not applicable to combi boiler or instantaneous water heater.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *not insulated*
    - **"2"** - *first 1 metre from cylinder insulated*
    - **"3"** - *all accessible pipework insulated*
    - **"4"** - *fully insulated*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details"></a>Solar-Heating-Details

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)/

- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Child elements: [`Solar-Heating-Collector-Manufacturer`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Heating-Collector-Manufacturer) [`Solar-Heating-Certificate`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Heating-Certificate) [`Solar-Panel-Aperture-Area`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Aperture-Area) [`Solar-Panel-Collector-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Type) [`Solar-Panel-Collector-Data-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Data-Source) [`Solar-Panel-Collector-Zero-Loss-Efficiency`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Zero-Loss-Efficiency) [`Solar-Panel-Collector-Heat-Loss-Rate`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Heat-Loss-Rate) [`Solar-Panel-Collector-Linear-Heat-Loss-Coefficient`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Linear-Heat-Loss-Coefficient) [`Solar-Panel-Collector-Second-Order-Heat-Loss-Coefficient`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Second-Order-Heat-Loss-Coefficient) [`Solar-Panel-Collector-Orientation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Orientation) [`Solar-Panel-Collector-Pitch`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Pitch) [`Solar-Panel-Collector-Overshading`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Overshading) [`Has-Solar-Powered-Pump`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Has-Solar-Powered-Pump) [`Is-Solar-Store-Combined-Cylinder`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Is-Solar-Store-Combined-Cylinder) [`Solar-Store-Volume`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Store-Volume) [`Collector-Loop-Efficiency`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Collector-Loop-Efficiency) [`Incidence-Angle-Modifier`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Incidence-Angle-Modifier) [`Is-Community-Solar`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Is-Community-Solar) [`Service-Provision`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Service-Provision) [`Overall-Heat-Loss`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Overall-Heat-Loss)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Heating-Collector-Manufacturer"></a>Solar-Heating-Collector-Manufacturer

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)/[`Solar-Heating-Collector-Manufacturer`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Heating-Collector-Manufacturer)/

- Documentation: *Panel manufacturer*
- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Heating-Certificate"></a>Solar-Heating-Certificate

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)/[`Solar-Heating-Certificate`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Heating-Certificate)/

- Documentation: *Solar heating certificate*
- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Aperture-Area"></a>Solar-Panel-Aperture-Area

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)/[`Solar-Panel-Aperture-Area`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Aperture-Area)/

- Documentation: *Panel aperture area in square metres.*
- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Type"></a>Solar-Panel-Collector-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)/[`Solar-Panel-Collector-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Type)/

- Documentation: *Type of solar panel collector.*
- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *unglazed*
    - **"2"** - *flat panel*
    - **"3"** - *evacuated tube*
    - **"ND"** - *for backwards compatability only; do not use*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Data-Source"></a>Solar-Panel-Collector-Data-Source

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)/[`Solar-Panel-Collector-Data-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Data-Source)/

- Documentation: *Source of solar panel collector data.*
- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *default*
    - **"2"** - *declared values*
    - **"ND"** - *for backwards compatability only; do not use*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Zero-Loss-Efficiency"></a>Solar-Panel-Collector-Zero-Loss-Efficiency

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)/[`Solar-Panel-Collector-Zero-Loss-Efficiency`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Zero-Loss-Efficiency)/

- Documentation: *Collector zero-loss efficiency; only if declared values.*
- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Heat-Loss-Rate"></a>Solar-Panel-Collector-Heat-Loss-Rate

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)/[`Solar-Panel-Collector-Heat-Loss-Rate`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Heat-Loss-Rate)/

- Documentation: *Collector heat loss rate; for backward compatibility only, do not use.*
- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Linear-Heat-Loss-Coefficient"></a>Solar-Panel-Collector-Linear-Heat-Loss-Coefficient

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)/[`Solar-Panel-Collector-Linear-Heat-Loss-Coefficient`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Linear-Heat-Loss-Coefficient)/

- Documentation: *Collector linear heat loss coefficient; only if declared values.*
- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Second-Order-Heat-Loss-Coefficient"></a>Solar-Panel-Collector-Second-Order-Heat-Loss-Coefficient

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)/[`Solar-Panel-Collector-Second-Order-Heat-Loss-Coefficient`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Second-Order-Heat-Loss-Coefficient)/

- Documentation: *Collector 2nd order heat loss coefficient; only if declared values.*
- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Orientation"></a>Solar-Panel-Collector-Orientation

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)/[`Solar-Panel-Collector-Orientation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Orientation)/

- Documentation: *Collector orientation.*
- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *North*
    - **"2"** - *North East*
    - **"3"** - *East*
    - **"4"** - *South East*
    - **"5"** - *South*
    - **"6"** - *South West*
    - **"7"** - *West*
    - **"8"** - *North West*
    - **"ND"** - *To be used when the pitch is horizontal*
    - **"NR"** - *not recorded - for backwards compatibility only; do not use*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Pitch"></a>Solar-Panel-Collector-Pitch

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)/[`Solar-Panel-Collector-Pitch`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Pitch)/

- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Overshading"></a>Solar-Panel-Collector-Overshading

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)/[`Solar-Panel-Collector-Overshading`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Overshading)/

- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *none or very little*
    - **"2"** - *modest*
    - **"3"** - *significant*
    - **"4"** - *heavy*
    - **"5"** - *severe*
    - **"ND"** - *for backwards compatability only; do not use*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Has-Solar-Powered-Pump"></a>Has-Solar-Powered-Pump

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)/[`Has-Solar-Powered-Pump`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Has-Solar-Powered-Pump)/

- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Is-Solar-Store-Combined-Cylinder"></a>Is-Solar-Store-Combined-Cylinder

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)/[`Is-Solar-Store-Combined-Cylinder`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Is-Solar-Store-Combined-Cylinder)/

- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Store-Volume"></a>Solar-Store-Volume

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)/[`Solar-Store-Volume`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Store-Volume)/

- Documentation: *Dedicated solar store volume in litres.*
- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Collector-Loop-Efficiency"></a>Collector-Loop-Efficiency

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)/[`Collector-Loop-Efficiency`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Collector-Loop-Efficiency)/

- Documentation: *Collector loop efficiency; only if declared values.*
- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Incidence-Angle-Modifier"></a>Incidence-Angle-Modifier

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)/[`Incidence-Angle-Modifier`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Incidence-Angle-Modifier)/

- Documentation: *Incidence angle modifier; only if declared values.*
- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Is-Community-Solar"></a>Is-Community-Solar

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)/[`Is-Community-Solar`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Is-Community-Solar)/

- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Service-Provision"></a>Service-Provision

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)/[`Service-Provision`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Service-Provision)/

- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *space and water heating*
    - **"2"** - *space heating only*
    - **"3"** - *water heating only*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Overall-Heat-Loss"></a>Overall-Heat-Loss

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)/[`Overall-Heat-Loss`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Overall-Heat-Loss)/

- Documentation: *Overall heat loss coefficient of system; only if declared values.*
- Parent element: [`Solar-Heating-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS"></a>Instantaneous-WWHRS

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Instantaneous-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS)/

- Documentation: *Waste Water Heat Recovery System.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Child elements: [`WWHRS-Index-Number1`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Index-Number1) [`WWHRS-Index-Number2`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Index-Number2) [`WWHRS-Efficiency1`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Efficiency1) [`WWHRS-Manufacturer1`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Manufacturer1) [`WWHRS-Model1`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Model1) [`WWHRS-Efficiency2`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Efficiency2) [`WWHRS-Manufacturer2`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Manufacturer2) [`WWHRS-Model2`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Model2)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Index-Number1"></a>WWHRS-Index-Number1

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Instantaneous-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS)/[`WWHRS-Index-Number1`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Index-Number1)/

- Parent element: [`Instantaneous-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Index-Number2"></a>WWHRS-Index-Number2

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Instantaneous-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS)/[`WWHRS-Index-Number2`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Index-Number2)/

- Documentation: *Omit if no second system.*
- Parent element: [`Instantaneous-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Efficiency1"></a>WWHRS-Efficiency1

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Instantaneous-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS)/[`WWHRS-Efficiency1`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Efficiency1)/

- Parent element: [`Instantaneous-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Manufacturer1"></a>WWHRS-Manufacturer1

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Instantaneous-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS)/[`WWHRS-Manufacturer1`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Manufacturer1)/

- Parent element: [`Instantaneous-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Model1"></a>WWHRS-Model1

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Instantaneous-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS)/[`WWHRS-Model1`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Model1)/

- Parent element: [`Instantaneous-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Efficiency2"></a>WWHRS-Efficiency2

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Instantaneous-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS)/[`WWHRS-Efficiency2`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Efficiency2)/

- Parent element: [`Instantaneous-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Manufacturer2"></a>WWHRS-Manufacturer2

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Instantaneous-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS)/[`WWHRS-Manufacturer2`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Manufacturer2)/

- Parent element: [`Instantaneous-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Model2"></a>WWHRS-Model2

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Instantaneous-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS)/[`WWHRS-Model2`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Model2)/

- Parent element: [`Instantaneous-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS"></a>Storage-WWHRS

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Storage-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS)/

- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Child elements: [`WWHRS-Index-Number`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/WWHRS-Index-Number) [`WWHRS-Store-Volume`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/WWHRS-Store-Volume) [`Storage-WWHRS-Efficiency`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/Storage-WWHRS-Efficiency) [`Storage-WWHRS-Manufacturer`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/Storage-WWHRS-Manufacturer) [`Storage-WWHRS-Model`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/Storage-WWHRS-Model)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/WWHRS-Index-Number"></a>WWHRS-Index-Number

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Storage-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS)/[`WWHRS-Index-Number`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/WWHRS-Index-Number)/

- Parent element: [`Storage-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/WWHRS-Store-Volume"></a>WWHRS-Store-Volume

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Storage-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS)/[`WWHRS-Store-Volume`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/WWHRS-Store-Volume)/

- Documentation: *Dedicated store volume in litres.*
- Parent element: [`Storage-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/Storage-WWHRS-Efficiency"></a>Storage-WWHRS-Efficiency

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Storage-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS)/[`Storage-WWHRS-Efficiency`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/Storage-WWHRS-Efficiency)/

- Parent element: [`Storage-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/Storage-WWHRS-Manufacturer"></a>Storage-WWHRS-Manufacturer

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Storage-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS)/[`Storage-WWHRS-Manufacturer`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/Storage-WWHRS-Manufacturer)/

- Parent element: [`Storage-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/Storage-WWHRS-Model"></a>Storage-WWHRS-Model

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Storage-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS)/[`Storage-WWHRS-Model`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/Storage-WWHRS-Model)/

- Parent element: [`Storage-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets"></a>Shower-Outlets

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Shower-Outlets`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets)/

- Documentation2: *Shower outlets present in the dwelling. If there are more than 5 then only include the 5 with the highest flow rates used.*
- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Child elements: [`Shower-Outlet`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet"></a>Shower-Outlet

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Shower-Outlets`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets)/[`Shower-Outlet`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet)/

- Documentation2: *Various details for each shower outlet.*
- Parent element: [`Shower-Outlets`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets)
- Child elements: [`Shower-Outlet-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-Outlet-Type) [`Shower-Flow-Rate`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-Flow-Rate) [`Shower-Power`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-Power) [`Shower-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-WWHRS)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **5**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-Outlet-Type"></a>Shower-Outlet-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Shower-Outlets`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets)/[`Shower-Outlet`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet)/[`Shower-Outlet-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-Outlet-Type)/

- Documentation: *Hot water type for this shower outlet.*
- Parent element: [`Shower-Outlet`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *Vented hot water system*
    - **"2"** - *Vented hot water system + pump*
    - **"3"** - *Unvented hot water system*
    - **"4"** - *Instantaneous electric shower*
    - **"5"** - *Part G 2015 compliant*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-Flow-Rate"></a>Shower-Flow-Rate

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Shower-Outlets`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets)/[`Shower-Outlet`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet)/[`Shower-Flow-Rate`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-Flow-Rate)/

- Documentation: *The flow rate. Only when a shower is not instantaneous electric. Leave blank if NO flow limiter fitted.*
- Parent element: [`Shower-Outlet`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-Power"></a>Shower-Power

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Shower-Outlets`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets)/[`Shower-Outlet`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet)/[`Shower-Power`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-Power)/

- Documentation: *The shower power, only if shower outlet type is instantaneous electric.*
- Parent element: [`Shower-Outlet`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-WWHRS"></a>Shower-WWHRS

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Shower-Outlets`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets)/[`Shower-Outlet`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet)/[`Shower-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-WWHRS)/

- Documentation: *The WWHRS with which the shower is connected. If shower outlet type is instantaneous electric shower then only a storage WWHRS can be selected or none.*
- Parent element: [`Shower-Outlet`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *none*
    - **"2"** - *Instantaneous WWHRS 1*
    - **"3"** - *Instantaneous WWHRS 2*
    - **"4"** - *Storage WWHRS*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Number-Baths"></a>Number-Baths

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Number-Baths`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Number-Baths)/

- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Number-Baths-WWHRS"></a>Number-Baths-WWHRS

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)/[`Number-Baths-WWHRS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Number-Baths-WWHRS)/

- Parent element: [`SAP-Heating`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source"></a>SAP-Energy-Source

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)/

- Documentation2: *Details of the main Electricity supply to the Property.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Child elements: [`PV-Arrays`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays) [`Wind-Turbines`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines) [`Electricity-Tariff`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Electricity-Tariff) [`Hydro-Electric-Generation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation) [`Hydro-Electric-Certificate`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Certificate) [`Hydro-Electric-Generation-Months`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months) [`Is-Hydro-Output-Connected-To-Dwelling-Meter`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Is-Hydro-Output-Connected-To-Dwelling-Meter)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays"></a>PV-Arrays

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)/[`PV-Arrays`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays)/

- Parent element: [`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)
- Child elements: [`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array"></a>PV-Array

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)/[`PV-Arrays`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays)/[`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array)/

- Parent element: [`PV-Arrays`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays)
- Child elements: [`Peak-Power`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Peak-Power) [`Orientation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Orientation) [`Pitch`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Pitch) [`Overshading`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Overshading) [`MCS-Certificate`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/MCS-Certificate) [`MCS-Certificate-Reference`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/MCS-Certificate-Reference) [`PV-Panel-Manufacturer-Name`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/PV-Panel-Manufacturer-Name) [`Overshading-MCS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Overshading-MCS)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **3**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Peak-Power"></a>Peak-Power

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)/[`PV-Arrays`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays)/[`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array)/[`Peak-Power`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Peak-Power)/

- Documentation: *Peak kW of photovoltaics (PVs) (kWp); 0.0 if none.*
- Parent element: [`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Orientation"></a>Orientation

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)/[`PV-Arrays`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays)/[`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array)/[`Orientation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Orientation)/

- Documentation: *PV orientation; only if peak kWp > 0.*
- Parent element: [`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *North*
    - **"2"** - *North East*
    - **"3"** - *East*
    - **"4"** - *South East*
    - **"5"** - *South*
    - **"6"** - *South West*
    - **"7"** - *West*
    - **"8"** - *North West*
    - **"ND"** - *To be used when the pitch is horizontal*
    - **"NR"** - *not recorded - for backwards compatibility only; do not use*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Pitch"></a>Pitch

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)/[`PV-Arrays`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays)/[`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array)/[`Pitch`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Pitch)/

- Documentation: *PV pitch; only if peak kWp > 0.*
- Parent element: [`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *horizontal*
    - **"2"** - *30 degrees*
    - **"3"** - *45 degrees*
    - **"4"** - *60 degrees*
    - **"5"** - *vertical*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Overshading"></a>Overshading

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)/[`PV-Arrays`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays)/[`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array)/[`Overshading`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Overshading)/

- Documentation: *PV overshading; only if peak kWp > 0 and no MCS certificate.*
- Parent element: [`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *none or very little*
    - **"2"** - *modest*
    - **"3"** - *significant*
    - **"4"** - *heavy*
    - **"5"** - *severe*
    - **"ND"** - *for backwards compatability only; do not use*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/MCS-Certificate"></a>MCS-Certificate

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)/[`PV-Arrays`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays)/[`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array)/[`MCS-Certificate`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/MCS-Certificate)/

- Documentation: *Does the installation have a MCS certificate.*
- Parent element: [`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/MCS-Certificate-Reference"></a>MCS-Certificate-Reference

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)/[`PV-Arrays`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays)/[`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array)/[`MCS-Certificate-Reference`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/MCS-Certificate-Reference)/

- Documentation: *MCS certificate reference number*
- Parent element: [`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/PV-Panel-Manufacturer-Name"></a>PV-Panel-Manufacturer-Name

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)/[`PV-Arrays`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays)/[`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array)/[`PV-Panel-Manufacturer-Name`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/PV-Panel-Manufacturer-Name)/

- Documentation: *Manufacturer of PV panels*
- Parent element: [`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Overshading-MCS"></a>Overshading-MCS

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)/[`PV-Arrays`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays)/[`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array)/[`Overshading-MCS`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Overshading-MCS)/

- Documentation: *Overshading factor calculated according to MCS.*
- Parent element: [`PV-Array`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines"></a>Wind-Turbines

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)/[`Wind-Turbines`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines)/

- Parent element: [`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)
- Child elements: [`Wind-Turbine`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine"></a>Wind-Turbine

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)/[`Wind-Turbines`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines)/[`Wind-Turbine`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine)/

- Parent element: [`Wind-Turbines`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines)
- Child elements: [`Wind-Turbine-Manufacturer-Name`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Manufacturer-Name) [`Wind-Turbine-Certificate`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Certificate) [`Wind-Turbine-Rotor-Diameter`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Rotor-Diameter) [`Wind-Turbine-Hub-Height`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Hub-Height)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **99**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Manufacturer-Name"></a>Wind-Turbine-Manufacturer-Name

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)/[`Wind-Turbines`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines)/[`Wind-Turbine`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine)/[`Wind-Turbine-Manufacturer-Name`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Manufacturer-Name)/

- Documentation: *Wind turbine manufacturer name.*
- Parent element: [`Wind-Turbine`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Certificate"></a>Wind-Turbine-Certificate

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)/[`Wind-Turbines`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines)/[`Wind-Turbine`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine)/[`Wind-Turbine-Certificate`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Certificate)/

- Documentation: *Wind turbine certificate.*
- Parent element: [`Wind-Turbine`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Rotor-Diameter"></a>Wind-Turbine-Rotor-Diameter

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)/[`Wind-Turbines`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines)/[`Wind-Turbine`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine)/[`Wind-Turbine-Rotor-Diameter`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Rotor-Diameter)/

- Documentation: *Wind turbine rotor diameter in metres; only if wind turbine.*
- Parent element: [`Wind-Turbine`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Hub-Height"></a>Wind-Turbine-Hub-Height

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)/[`Wind-Turbines`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines)/[`Wind-Turbine`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine)/[`Wind-Turbine-Hub-Height`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Hub-Height)/

- Documentation: *Wind turbine hub height above building in metres; only if wind turbine.*
- Parent element: [`Wind-Turbine`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Electricity-Tariff"></a>Electricity-Tariff

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)/[`Electricity-Tariff`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Electricity-Tariff)/

- Documentation: *Type of electricity tariff.*
- Parent element: [`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *standard tariff*
    - **"2"** - *off-peak 7 hour*
    - **"3"** - *off-peak 10 hour*
    - **"4"** - *24 hour*
    - **"5"** - *off-peak 18 hour*
    - **"ND"** - *not applicable*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation"></a>Hydro-Electric-Generation

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)/[`Hydro-Electric-Generation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation)/

- Documentation: *Electricity generated by hydro-electric generator, in kWh/year. To be provided if Hydro-Electric-Generation-Month is not provided.*
- Parent element: [`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Certificate"></a>Hydro-Electric-Certificate

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)/[`Hydro-Electric-Certificate`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Certificate)/

- Documentation: *Reference to certification of hydro electric output.*
- Parent element: [`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months"></a>Hydro-Electric-Generation-Months

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)/[`Hydro-Electric-Generation-Months`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months)/

- Documentation: *Electricity generated by hydro-electric generator, in kWh/month. To be provided if Hydro-Electric-Generation is not provided.*
- Parent element: [`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)
- Child elements: [`Hydro-Electric-Generation-Month`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month"></a>Hydro-Electric-Generation-Month

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)/[`Hydro-Electric-Generation-Months`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months)/[`Hydro-Electric-Generation-Month`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month)/

- Parent element: [`Hydro-Electric-Generation-Months`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months)
- Child elements: [`Hydro-Month`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month/Hydro-Month) [`Hydro-Value`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month/Hydro-Value)
- Has text value: *False*
- Minimum occurrence: **12**
- Maximum occurrence: **12**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month/Hydro-Month"></a>Hydro-Month

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)/[`Hydro-Electric-Generation-Months`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months)/[`Hydro-Electric-Generation-Month`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month)/[`Hydro-Month`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month/Hydro-Month)/

- Parent element: [`Hydro-Electric-Generation-Month`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"Jan"** - **
    - **"Feb"** - **
    - **"Mar"** - **
    - **"Apr"** - **
    - **"May"** - **
    - **"Jun"** - **
    - **"Jul"** - **
    - **"Aug"** - **
    - **"Sep"** - **
    - **"Oct"** - **
    - **"Nov"** - **
    - **"Dec"** - **
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month/Hydro-Value"></a>Hydro-Value

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)/[`Hydro-Electric-Generation-Months`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months)/[`Hydro-Electric-Generation-Month`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month)/[`Hydro-Value`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month/Hydro-Value)/

- Documentation: *Hydro electricity in kWh in month.*
- Parent element: [`Hydro-Electric-Generation-Month`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Is-Hydro-Output-Connected-To-Dwelling-Meter"></a>Is-Hydro-Output-Connected-To-Dwelling-Meter

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)/[`Is-Hydro-Output-Connected-To-Dwelling-Meter`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Is-Hydro-Output-Connected-To-Dwelling-Meter)/

- Documentation: *Whether the hydro-electric station is connected to dwelling's electricity meter*
- Parent element: [`SAP-Energy-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts"></a>SAP-Building-Parts

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/

- Documentation2: *Details of the significant building parts that comprise the main habitable building in the property. The main habitable area generally consists of a single main building but can over time be extended to include extensions such as new wings and additional storeys. For the purpose of calculating the overall Energy Assessment for the property details of each distinct Building Part, such as its construction, have to be gathered because different materials have different insulation ratings (obviously) which affects the overall rating.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Child elements: [`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part"></a>SAP-Building-Part

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/

- Documentation2: *A permanent structure that forms part of the Property and is built primarily for human habitation. A Building Part is usually made up of one or more Storey's and may contain a number of Internal Structural Features. An extension is also a Building Part.*
- Parent element: [`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)
- Child elements: [`Building-Part-Number`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Building-Part-Number) [`Identifier`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Identifier) [`Construction-Year`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Construction-Year) [`Construction-Age-Band`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Construction-Age-Band) [`SAP-Openings`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings) [`SAP-Roofs`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs) [`SAP-Floor-Dimensions`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions) [`SAP-Thermal-Bridges`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges) [`SAP-Walls`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **unbounded**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Building-Part-Number"></a>Building-Part-Number

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`Building-Part-Number`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Building-Part-Number)/

- Documentation: *An integer value which uniquely identifies the building part in the property. The value "1" must be assigned to the main dwelling.*
- Parent element: [`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Identifier"></a>Identifier

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`Identifier`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Identifier)/

- Documentation: *Identifier for the Building part - generally only required if there are more that one Building Parts of the same type e.g. "West Wing" and "East Wing" Extensions*
- Documentation2: *A string containing a unique identifier for something. The underlying assumption is that each instance of a class or entity will have a unique identifier assigned to it which can then be assigned to any referencing entity as a reference to the entity instance. This is a very similar concept to XML ID datatype but is locally defined because of the need to extend the datatype with domain specific attributes.*
- Parent element: [`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Construction-Year"></a>Construction-Year

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`Construction-Year`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Construction-Year)/

- Documentation: *The year when this building part was constructed. Not used if 'Construction-Age-Band' is used.*
- Parent element: [`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Construction-Age-Band"></a>Construction-Age-Band

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`Construction-Age-Band`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Construction-Age-Band)/

- Documentation: *The age band when this building part was constructed. Not used if 'Construction-Year' is used.*
- Parent element: [`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"A"** - *England and Wales: before 1900; Scotland: before 1919; Northern Ireland: before 1919*
    - **"B"** - *England and Wales: 1900-1929; Scotland: 1919-1929; Northern Ireland: 1919-1929*
    - **"C"** - *England and Wales: 1930-1949; Scotland: 1930-1949; Northern Ireland: 1930-1949*
    - **"D"** - *England and Wales: 1950-1966; Scotland: 1950-1964; Northern Ireland: 1950-1973*
    - **"E"** - *England and Wales: 1967-1975; Scotland: 1965-1975; Northern Ireland: 1974-1977*
    - **"F"** - *England and Wales: 1976-1982; Scotland: 1976-1983; Northern Ireland: 1978-1985*
    - **"G"** - *England and Wales: 1983-1990; Scotland: 1984-1991; Northern Ireland: 1986-1991*
    - **"H"** - *England and Wales: 1991-1995; Scotland: 1992-1998; Northern Ireland: 1992-1999*
    - **"I"** - *England and Wales: 1996-2002; Scotland: 1999-2002; Northern Ireland: 2000-2006*
    - **"J"** - *England and Wales: 2003-2006; Scotland: 2003-2007; Northern Ireland: not applicable*
    - **"K"** - *England and Wales: 2007-2011; Scotland: 2008-2011; Northern Ireland: 2007-2013*
    - **"L"** - *England and Wales: 2012 onwards; Scotland: 2012 onwards; Northern Ireland: 2014 onwards*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings"></a>SAP-Openings

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Openings`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings)/

- Documentation2: *Exposed openings that make up a particular Building-Part.*
- Parent element: [`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)
- Child elements: [`SAP-Opening`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening"></a>SAP-Opening

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Openings`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings)/[`SAP-Opening`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening)/

- Documentation2: *Various measurements for each exposed opening that makes up a particular Building-Part.*
- Parent element: [`SAP-Openings`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings)
- Child elements: [`Name`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Name) [`Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Type) [`Location`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Location) [`Orientation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Orientation) [`Width`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Width) [`Height`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Height) [`Pitch`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Pitch)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **unbounded**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Name"></a>Name

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Openings`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings)/[`SAP-Opening`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening)/[`Name`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Name)/

- Documentation: *Unique name which identifies this opening. Can be just a number, e.g. "1". However, an opening cannot have the same name as a wall.*
- Parent element: [`SAP-Opening`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Type"></a>Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Openings`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings)/[`SAP-Opening`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening)/[`Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Type)/

- Documentation: *The name of the SAP-Opening-Type for this opening.*
- Parent element: [`SAP-Opening`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Location"></a>Location

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Openings`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings)/[`SAP-Opening`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening)/[`Location`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Location)/

- Documentation: *Name of the wall or roof which contains the opening.*
- Parent element: [`SAP-Opening`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Orientation"></a>Orientation

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Openings`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings)/[`SAP-Opening`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening)/[`Orientation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Orientation)/

- Documentation: *Compass direction in which the opening faces.*
- Parent element: [`SAP-Opening`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"0"** - *unknown or unspecified*
    - **"1"** - *North*
    - **"2"** - *North East*
    - **"3"** - *East*
    - **"4"** - *South East*
    - **"5"** - *South*
    - **"6"** - *South West*
    - **"7"** - *West*
    - **"8"** - *North West*
    - **"9"** - *Horizontal (windows and roof windows only)*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Width"></a>Width

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Openings`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings)/[`SAP-Opening`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening)/[`Width`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Width)/

- Documentation: *The width of the opening in metres. If the Width field is used to record the opening area, set the Height to 1.*
- Parent element: [`SAP-Opening`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Height"></a>Height

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Openings`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings)/[`SAP-Opening`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening)/[`Height`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Height)/

- Documentation: *The height of the opening in metres. If the Height field is used to record the opening area, set the Width to 1.*
- Parent element: [`SAP-Opening`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Pitch"></a>Pitch

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Openings`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings)/[`SAP-Opening`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening)/[`Pitch`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Pitch)/

- Documentation: *Pitch of roof containing roof window.*
- Parent element: [`SAP-Opening`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs"></a>SAP-Roofs

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Roofs`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs)/

- Documentation2: *Exposed roofs that make up a particular Building-Part.*
- Parent element: [`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)
- Child elements: [`SAP-Roof`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof"></a>SAP-Roof

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Roofs`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs)/[`SAP-Roof`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof)/

- Documentation2: *Various measurements for each exposed roof that makes up a particular Building-Part.*
- Parent element: [`SAP-Roofs`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs)
- Child elements: [`Name`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Name) [`Description`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Description) [`Roof-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Roof-Type) [`Total-Roof-Area`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Total-Roof-Area) [`U-Value`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/U-Value) [`Kappa-Value`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Kappa-Value)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **unbounded**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Name"></a>Name

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Roofs`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs)/[`SAP-Roof`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof)/[`Name`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Name)/

- Documentation: *Unique name which identifies this roof. Can be just a number, e.g. "1". However, a roof cannot have the same name as a wall.*
- Parent element: [`SAP-Roof`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Description"></a>Description

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Roofs`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs)/[`SAP-Roof`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof)/[`Description`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Description)/

- Documentation: *Descriptive notes about the roof.*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: [`SAP-Roof`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Roof-Type"></a>Roof-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Roofs`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs)/[`SAP-Roof`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof)/[`Roof-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Roof-Type)/

- Parent element: [`SAP-Roof`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"2"** - *exposed roof*
    - **"4"** - *party ceiling*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Total-Roof-Area"></a>Total-Roof-Area

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Roofs`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs)/[`SAP-Roof`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof)/[`Total-Roof-Area`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Total-Roof-Area)/

- Documentation: *Total roof area in square metres, inclusive of any openings.*
- Parent element: [`SAP-Roof`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/U-Value"></a>U-Value

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Roofs`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs)/[`SAP-Roof`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof)/[`U-Value`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/U-Value)/

- Documentation: *Exposed roof U-value.*
- Parent element: [`SAP-Roof`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Kappa-Value"></a>Kappa-Value

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Roofs`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs)/[`SAP-Roof`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof)/[`Kappa-Value`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Kappa-Value)/

- Documentation: *Heat capacity per unit area in kJ/m2K.*
- Parent element: [`SAP-Roof`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions"></a>SAP-Floor-Dimensions

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Floor-Dimensions`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions)/

- Documentation2: *Storeys that make up a particular Building-Part.*
- Parent element: [`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)
- Child elements: [`SAP-Floor-Dimension`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension"></a>SAP-Floor-Dimension

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Floor-Dimensions`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions)/[`SAP-Floor-Dimension`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension)/

- Documentation2: *Various measurements for the floor of a particular storey.*
- Parent element: [`SAP-Floor-Dimensions`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions)
- Child elements: [`Name`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Name) [`Storey`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Storey) [`Description`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Description) [`Floor-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Floor-Type) [`Total-Floor-Area`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Total-Floor-Area) [`Storey-Height`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Storey-Height) [`Heat-Loss-Area`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Heat-Loss-Area) [`U-Value`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/U-Value) [`Kappa-Value`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Kappa-Value) [`Kappa-Value-From-Below`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Kappa-Value-From-Below)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **unbounded**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Name"></a>Name

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Floor-Dimensions`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions)/[`SAP-Floor-Dimension`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension)/[`Name`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Name)/

- Documentation: *A name describing the floor dimensioned.*
- Parent element: [`SAP-Floor-Dimension`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Storey"></a>Storey

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Floor-Dimensions`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions)/[`SAP-Floor-Dimension`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension)/[`Storey`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Storey)/

- Documentation: *Building storey on which the floor is located.*
- Parent element: [`SAP-Floor-Dimension`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"-1"** - *Lower ground*
    - **"0"** - *Ground*
    - **"1"** - *1st*
    - **"2"** - *2nd*
    - **"3"** - *3rd*
    - **"4"** - *4th*
    - **"5"** - *5th*
    - **"6"** - *6th*
    - **"99"** - *Roof rooms*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Description"></a>Description

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Floor-Dimensions`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions)/[`SAP-Floor-Dimension`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension)/[`Description`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Description)/

- Documentation: *Descriptive notes about the floor.*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: [`SAP-Floor-Dimension`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Floor-Type"></a>Floor-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Floor-Dimensions`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions)/[`SAP-Floor-Dimension`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension)/[`Floor-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Floor-Type)/

- Documentation: *Type of floor (exposure).*
- Parent element: [`SAP-Floor-Dimension`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *basement floor*
    - **"2"** - *ground floor*
    - **"3"** - *upper floor (if heat loss area > 0, this area is an exposed floor)*
    - **"4"** - *party floor*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Total-Floor-Area"></a>Total-Floor-Area

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Floor-Dimensions`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions)/[`SAP-Floor-Dimension`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension)/[`Total-Floor-Area`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Total-Floor-Area)/

- Documentation: *The total floor area of the storey in square metres.*
- Parent element: [`SAP-Floor-Dimension`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Storey-Height"></a>Storey-Height

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Floor-Dimensions`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions)/[`SAP-Floor-Dimension`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension)/[`Storey-Height`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Storey-Height)/

- Documentation: *Average height of the storey in metres.*
- Parent element: [`SAP-Floor-Dimension`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Heat-Loss-Area"></a>Heat-Loss-Area

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Floor-Dimensions`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions)/[`SAP-Floor-Dimension`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension)/[`Heat-Loss-Area`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Heat-Loss-Area)/

- Documentation: *The estimated total heat loss area for the floor in square metres.*
- Parent element: [`SAP-Floor-Dimension`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/U-Value"></a>U-Value

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Floor-Dimensions`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions)/[`SAP-Floor-Dimension`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension)/[`U-Value`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/U-Value)/

- Documentation: *Heat loss floor U-value.*
- Parent element: [`SAP-Floor-Dimension`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Kappa-Value"></a>Kappa-Value

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Floor-Dimensions`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions)/[`SAP-Floor-Dimension`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension)/[`Kappa-Value`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Kappa-Value)/

- Documentation: *Heat capacity of floor per unit area in kJ/m2K.*
- Parent element: [`SAP-Floor-Dimension`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Kappa-Value-From-Below"></a>Kappa-Value-From-Below

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Floor-Dimensions`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions)/[`SAP-Floor-Dimension`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension)/[`Kappa-Value-From-Below`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Kappa-Value-From-Below)/

- Documentation: *Heat capacity of ceiling below. Applies to the non-heat-loss area of an upper floor.*
- Parent element: [`SAP-Floor-Dimension`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges"></a>SAP-Thermal-Bridges

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Thermal-Bridges`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges)/

- Documentation2: *Thermal bridges that make up a particular Building-Part.*
- Parent element: [`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)
- Child elements: [`Thermal-Bridge-Code`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/Thermal-Bridge-Code) [`User-Defined-Y-Value`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/User-Defined-Y-Value) [`Calculation-Reference`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/Calculation-Reference) [`SAP-Thermal-Bridge`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/Thermal-Bridge-Code"></a>Thermal-Bridge-Code

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Thermal-Bridges`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges)/[`Thermal-Bridge-Code`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/Thermal-Bridge-Code)/

- Documentation: *Code which indicates how the thermal bridge data has been recorded.*
- Parent element: [`SAP-Thermal-Bridges`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *default*
    - **"2"** - *2002 regulations. For backwards compatibility only, do not use.*
    - **"3"** - *accredited. For backwards compatibility only, do not use.*
    - **"4"** - *user defined (global y-value)*
    - **"5"** - *user defined (individual values)*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/User-Defined-Y-Value"></a>User-Defined-Y-Value

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Thermal-Bridges`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges)/[`User-Defined-Y-Value`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/User-Defined-Y-Value)/

- Documentation: *Global y-value for all thermal bridges in watts per square metre per kelvin; only if thermal bridge code is: user defined (global y-value)*
- Parent element: [`SAP-Thermal-Bridges`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/Calculation-Reference"></a>Calculation-Reference

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Thermal-Bridges`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges)/[`Calculation-Reference`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/Calculation-Reference)/

- Documentation: *Reference to the details of the calculation of the global y-value; only if thermal bridging is user defined global y-value.*
- Parent element: [`SAP-Thermal-Bridges`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge"></a>SAP-Thermal-Bridge

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Thermal-Bridges`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges)/[`SAP-Thermal-Bridge`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge)/

- Documentation2: *Various measurements for each thermal bridge that makes up a particular Building-Part.*
- Parent element: [`SAP-Thermal-Bridges`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges)
- Child elements: [`Thermal-Bridge-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Thermal-Bridge-Type) [`Length`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Length) [`Psi-Value`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Psi-Value) [`Psi-Value-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Psi-Value-Source) [`Psi-Value-Calculation-Reference`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Psi-Value-Calculation-Reference)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **unbounded**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Thermal-Bridge-Type"></a>Thermal-Bridge-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Thermal-Bridges`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges)/[`SAP-Thermal-Bridge`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge)/[`Thermal-Bridge-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Thermal-Bridge-Type)/

- Documentation: *Code to indicate a particular type of thermal bridge; only if thermal bridge code is: user defined (individual values).*
- Parent element: [`SAP-Thermal-Bridge`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"ND"** - *not defined (for backward compatibility only, do not use)*
    - **"E1"** - *Steel lintel with perforated steel base plate*
    - **"E2"** - *Other lintels (including other steel lintels)*
    - **"E3"** - *Sill*
    - **"E4"** - *Jamb*
    - **"E5"** - *Ground floor (normal)*
    - **"E6"** - *Intermediate floor within a dwelling*
    - **"E7"** - *Party floor between dwellings (in blocks of flats)*
    - **"E8"** - *Balcony within a dwelling, wall insulation continuous*
    - **"E9"** - *Balcony between dwellings, wall insulation continuous*
    - **"E10"** - *Eaves (insulation at ceiling level)*
    - **"E11"** - *Eaves (insulation at rafter level)*
    - **"E12"** - *Gable (insulation at ceiling level)*
    - **"E13"** - *Gable (insulation at rafter level)*
    - **"E14"** - *Flat roof*
    - **"E15"** - *Flat roof with parapet*
    - **"E16"** - *Corner (normal)*
    - **"E17"** - *Corner (inverted - internal area greater than external area)*
    - **"E18"** - *Party wall between dwellings*
    - **"E19"** - *Ground floor (inverted)*
    - **"E20"** - *Exposed floor (normal)*
    - **"E21"** - *Exposed floor (inverted)*
    - **"E22"** - *Basement floor*
    - **"E23"** - *Balcony within or between dwellings, balcony support penetrates wall insulation*
    - **"E24"** - *Eaves (insulation at ceiling level - inverted)*
    - **"E25"** - *Staggered party wall between dwellings*
    - **"P1"** - *Ground floor*
    - **"P2"** - *Intermediate floor within a dwelling*
    - **"P3"** - *Intermediate floor between dwellings (in blocks of flats)*
    - **"P4"** - *Roof (insulation at ceiling level)*
    - **"P5"** - *Roof (insulation at rafter level)*
    - **"P6"** - *Ground floor (inverted)*
    - **"P7"** - *Exposed floor (normal)*
    - **"P8"** - *Exposed floor (inverted)*
    - **"R1"** - *Head of roof window*
    - **"R2"** - *Sill of roof window*
    - **"R3"** - *Jamb of roof window*
    - **"R4"** - *Ridge (vaulted ceiling)*
    - **"R5"** - *Ridge (inverted)*
    - **"R6"** - *Flat ceiling*
    - **"R7"** - *Flat ceiling (inverted)*
    - **"R8"** - *Roof to wall (rafter)*
    - **"R9"** - *Roof to wall (flat ceiling)*
    - **"R10"** - *All other roof or room-in-roof junctions*
    - **"R11"** - *Upstands or kerbs of rooflights*
    - **"O1"** - *other type 1*
    - **"O2"** - *other type 2*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Length"></a>Length

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Thermal-Bridges`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges)/[`SAP-Thermal-Bridge`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge)/[`Length`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Length)/

- Documentation: *Length of the thermal bridge in metres; only if thermal bridge code is: user defined (individual values).*
- Parent element: [`SAP-Thermal-Bridge`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Psi-Value"></a>Psi-Value

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Thermal-Bridges`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges)/[`SAP-Thermal-Bridge`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge)/[`Psi-Value`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Psi-Value)/

- Documentation: *Linear thermal transmittance (psi-value); only if thermal bridging is user defined individual values.*
- Parent element: [`SAP-Thermal-Bridge`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Psi-Value-Source"></a>Psi-Value-Source

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Thermal-Bridges`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges)/[`SAP-Thermal-Bridge`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge)/[`Psi-Value-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Psi-Value-Source)/

- Parent element: [`SAP-Thermal-Bridge`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *calculated by person with suitable expertise*
    - **"2"** - *government-approved scheme*
    - **"3"** - *not government-approved scheme*
    - **"4"** - *SAP table default*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Psi-Value-Calculation-Reference"></a>Psi-Value-Calculation-Reference

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Thermal-Bridges`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges)/[`SAP-Thermal-Bridge`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge)/[`Psi-Value-Calculation-Reference`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Psi-Value-Calculation-Reference)/

- Documentation: *Reference to the details of the calculation of the psi-value.*
- Parent element: [`SAP-Thermal-Bridge`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls"></a>SAP-Walls

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Walls`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls)/

- Documentation2: *Exposed walls that make up a particular Storey.*
- Parent element: [`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)
- Child elements: [`SAP-Wall`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall"></a>SAP-Wall

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Walls`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls)/[`SAP-Wall`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall)/

- Documentation2: *Various measurements for each wall of a particular storey.*
- Parent element: [`SAP-Walls`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls)
- Child elements: [`Name`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Name) [`Description`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Description) [`Wall-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Wall-Type) [`Total-Wall-Area`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Total-Wall-Area) [`U-Value`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/U-Value) [`Is-Curtain-Walling`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Is-Curtain-Walling) [`Kappa-Value`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Kappa-Value)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **unbounded**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Name"></a>Name

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Walls`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls)/[`SAP-Wall`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall)/[`Name`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Name)/

- Documentation: *Unique name which identifies this wall within its storey. Can be just a number, e.g. "1". However, a wall cannot have the same name as an opening or a roof.*
- Parent element: [`SAP-Wall`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Description"></a>Description

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Walls`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls)/[`SAP-Wall`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall)/[`Description`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Description)/

- Documentation: *Descriptive notes about the wall.*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: [`SAP-Wall`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Wall-Type"></a>Wall-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Walls`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls)/[`SAP-Wall`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall)/[`Wall-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Wall-Type)/

- Documentation: *Type of wall (exposure).*
- Parent element: [`SAP-Wall`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *basement wall*
    - **"2"** - *exposed wall*
    - **"3"** - *sheltered wall*
    - **"4"** - *party wall*
    - **"5"** - *internal wall*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Total-Wall-Area"></a>Total-Wall-Area

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Walls`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls)/[`SAP-Wall`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall)/[`Total-Wall-Area`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Total-Wall-Area)/

- Documentation: *Total wall area in square metres, inclusive of any openings.*
- Parent element: [`SAP-Wall`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/U-Value"></a>U-Value

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Walls`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls)/[`SAP-Wall`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall)/[`U-Value`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/U-Value)/

- Documentation: *Exposed wall U-value.*
- Parent element: [`SAP-Wall`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Is-Curtain-Walling"></a>Is-Curtain-Walling

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Walls`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls)/[`SAP-Wall`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall)/[`Is-Curtain-Walling`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Is-Curtain-Walling)/

- Documentation: *Whether the wall is curtain walling, i.e. a facade construction consisting of a frame of aluminium vertical and horizontal members, infilled with glazing units and opaque panels.*
- Parent element: [`SAP-Wall`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Kappa-Value"></a>Kappa-Value

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Building-Parts`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts)/[`SAP-Building-Part`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part)/[`SAP-Walls`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls)/[`SAP-Wall`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall)/[`Kappa-Value`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Kappa-Value)/

- Documentation: *Heat capacity per unit area in kJ/m2K.*
- Parent element: [`SAP-Wall`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types"></a>SAP-Opening-Types

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Opening-Types`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types)/

- Documentation2: *Types of exposed openings that make up a particular property. Opening types are used to capture common features shared by multiple openings, to avoid having to record the same data explicitly for each opening.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Child elements: [`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type"></a>SAP-Opening-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Opening-Types`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types)/[`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)/

- Documentation2: *Various measurements for a particular type of exposed opening that makes up a particular property. Opening types are used to capture common features shared by multiple openings, to avoid having to record the same data explicitly for each opening.*
- Parent element: [`SAP-Opening-Types`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types)
- Child elements: [`Name`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Name) [`Description`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Description) [`Data-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Data-Source) [`Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Type) [`Glazing-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Glazing-Type) [`Glazing-Gap`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Glazing-Gap) [`IsArgonFilled`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/IsArgonFilled) [`IsKryptonFilled`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/IsKryptonFilled) [`Frame-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Frame-Type) [`Solar-Transmittance`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Solar-Transmittance) [`Frame-Factor`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Frame-Factor) [`U-Value`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/U-Value)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **unbounded**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Name"></a>Name

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Opening-Types`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types)/[`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)/[`Name`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Name)/

- Documentation: *Unique name which identifies this opening type. Can be just a number, e.g. "1".*
- Parent element: [`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Description"></a>Description

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Opening-Types`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types)/[`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)/[`Description`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Description)/

- Documentation: *Descriptive notes about the opening type.*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: [`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Data-Source"></a>Data-Source

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Opening-Types`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types)/[`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)/[`Data-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Data-Source)/

- Documentation: *The source of the data for this type of opening.*
- Parent element: [`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"2"** - *manufacturer declaration*
    - **"3"** - *SAP table*
    - **"4"** - *BFRC data*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Type"></a>Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Opening-Types`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types)/[`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)/[`Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Type)/

- Documentation: *The (physical) type of opening that this opening type represents.*
- Parent element: [`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *solid door*
    - **"2"** - *semi-glazed door*
    - **"3"** - *door to corridor*
    - **"4"** - *window*
    - **"5"** - *roof window*
    - **"6"** - *rooflight*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Glazing-Type"></a>Glazing-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Opening-Types`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types)/[`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)/[`Glazing-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Glazing-Type)/

- Documentation: *The type of glazing; if U-value is from BFRC or manufacturer declaration, give as one of - single - double - triple.*
- Parent element: [`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *not applicable (non-glazed door)*
    - **"2"** - *single*
    - **"3"** - *double*
    - **"4"** - *double low-E hard 0.2*
    - **"5"** - *double low-E hard 0.15*
    - **"6"** - *double low-E soft 0.1*
    - **"7"** - *double low-E soft 0.05*
    - **"8"** - *triple*
    - **"9"** - *triple low-E hard 0.2*
    - **"10"** - *triple low-E hard 0.15*
    - **"11"** - *triple low-E soft 0.1*
    - **"12"** - *triple low-E soft 0.05*
    - **"13"** - *secondary glazing*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Glazing-Gap"></a>Glazing-Gap

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Opening-Types`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types)/[`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)/[`Glazing-Gap`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Glazing-Gap)/

- Documentation: *Gap between glass panes; only if SAP table and double, triple glazed or secondary glazing.*
- Parent element: [`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *6 mm*
    - **"2"** - *12 mm*
    - **"3"** - *16 mm or more*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/IsArgonFilled"></a>IsArgonFilled

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Opening-Types`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types)/[`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)/[`IsArgonFilled`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/IsArgonFilled)/

- Documentation: *Is the opening argon-filled? Only if SAP table.*
- Parent element: [`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/IsKryptonFilled"></a>IsKryptonFilled

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Opening-Types`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types)/[`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)/[`IsKryptonFilled`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/IsKryptonFilled)/

- Documentation: *Is the opening krypton-filled? Only if SAP table.*
- Parent element: [`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Frame-Type"></a>Frame-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Opening-Types`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types)/[`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)/[`Frame-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Frame-Type)/

- Documentation: *The type of frame, only if data source is SAP table and it is a window, roof window or half-glazed door.*
- Parent element: [`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *wood*
    - **"2"** - *PVC*
    - **"3"** - *metal no break*
    - **"4"** - *metal 4 mm break*
    - **"5"** - *metal 8 mm break*
    - **"6"** - *metal 12 mm break*
    - **"7"** - *metal 20 mm break*
    - **"8"** - *metal 32 mm break*
    - **"9"** - *unknown*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Solar-Transmittance"></a>Solar-Transmittance

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Opening-Types`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types)/[`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)/[`Solar-Transmittance`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Solar-Transmittance)/

- Documentation: *The solar transmittance; not if a door.*
- Parent element: [`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Frame-Factor"></a>Frame-Factor

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Opening-Types`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types)/[`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)/[`Frame-Factor`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Frame-Factor)/

- Documentation: *The frame factor; not if a door.*
- Parent element: [`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/U-Value"></a>U-Value

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Opening-Types`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types)/[`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)/[`U-Value`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/U-Value)/

- Documentation: *The U-value. For rooflights, the U-value should be in the horizontal plane.*
- Parent element: [`SAP-Opening-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation"></a>SAP-Ventilation

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/

- Documentation2: *Details of the means by which the building is ventilated*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Child elements: [`Closed-Flues-Count`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Closed-Flues-Count) [`Open-Flues-Count`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Open-Flues-Count) [`Boilers-Flues-Count`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Boilers-Flues-Count) [`Other-Flues-Count`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Other-Flues-Count) [`Open-Chimneys-Count`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Open-Chimneys-Count) [`Blocked-Chimneys-Count`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Blocked-Chimneys-Count) [`Fans-Vents-Count`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Fans-Vents-Count) [`Flueless-Gas-Fires-Count`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Flueless-Gas-Fires-Count) [`Pressure-Test`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Pressure-Test) [`Pressure-Test-Certificate-Number`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Pressure-Test-Certificate-Number) [`Air-Permeability`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Air-Permeability) [`Ground-Floor-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Ground-Floor-Type) [`Wall-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Wall-Type) [`Has-Draught-Lobby`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Has-Draught-Lobby) [`DraughtStripping`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/DraughtStripping) [`Sheltered-Sides-Count`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Sheltered-Sides-Count) [`Ventilation-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Ventilation-Type) [`Mechanical-Ventilation-Data-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Ventilation-Data-Source) [`Mechanical-Vent-System-Index-Number`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-System-Index-Number) [`Mechanical-Vent-Commissioning-Certificate-Number`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Commissioning-Certificate-Number) [`Mechanical-Vent-Installation-Engineer`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Installation-Engineer) [`Mechanical-Vent-System-Make-Model`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-System-Make-Model) [`Wet-Rooms-Count`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Wet-Rooms-Count) [`Mechanical-Vent-Specific-Fan-Power`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Specific-Fan-Power) [`Mechanical-Vent-Heat-Recovery-Efficiency`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Heat-Recovery-Efficiency) [`Mechanical-Vent-Duct-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Duct-Type) [`Mechanical-Vent-Duct-Insulation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Duct-Insulation) [`Mechanical-Vent-Duct-Insulation-Level`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Duct-Insulation-Level) [`Mechanical-Vent-Duct-Placement`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Duct-Placement) [`Mechanical-Vent-Measured-Installation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Measured-Installation) [`Kitchen-Room-Fans-Count`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Room-Fans-Count) [`Kitchen-Room-Fans-Specific-Power`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Room-Fans-Specific-Power) [`Non-Kitchen-Room-Fans-Count`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Room-Fans-Count) [`Non-Kitchen-Room-Fans-Specific-Power`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Room-Fans-Specific-Power) [`Kitchen-Duct-Fans-Count`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Duct-Fans-Count) [`Kitchen-Duct-Fans-Specific-Power`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Duct-Fans-Specific-Power) [`Non-Kitchen-Duct-Fans-Count`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Duct-Fans-Count) [`Non-Kitchen-Duct-Fans-Specific-Power`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Duct-Fans-Specific-Power) [`Kitchen-Wall-Fans-Count`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Wall-Fans-Count) [`Kitchen-Wall-Fans-Specific-Power`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Wall-Fans-Specific-Power) [`Non-Kitchen-Wall-Fans-Count`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Wall-Fans-Count) [`Non-Kitchen-Wall-Fans-Specific-Power`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Wall-Fans-Specific-Power) [`Extract-Fans-Count`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Extract-Fans-Count) [`PSV-Count`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/PSV-Count) [`Is-Mechanical-Vent-Approved-Installer-Scheme`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Is-Mechanical-Vent-Approved-Installer-Scheme) [`Mechanical-Vent-Ducts-Index-Number`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Ducts-Index-Number)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Closed-Flues-Count"></a>Closed-Flues-Count

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Closed-Flues-Count`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Closed-Flues-Count)/

- Documentation: *The number of Closed Flues or chimneys in the Property.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Open-Flues-Count"></a>Open-Flues-Count

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Open-Flues-Count`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Open-Flues-Count)/

- Documentation: *The number of Open Flues in the Property.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Boilers-Flues-Count"></a>Boilers-Flues-Count

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Boilers-Flues-Count`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Boilers-Flues-Count)/

- Documentation: *The number of Boiler Flues or chimneys in the Property.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Other-Flues-Count"></a>Other-Flues-Count

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Other-Flues-Count`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Other-Flues-Count)/

- Documentation: *The number of Other Flues or chimneys in the Property.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Open-Chimneys-Count"></a>Open-Chimneys-Count

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Open-Chimneys-Count`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Open-Chimneys-Count)/

- Documentation: *The number of Open Chimneys in the Property.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Blocked-Chimneys-Count"></a>Blocked-Chimneys-Count

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Blocked-Chimneys-Count`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Blocked-Chimneys-Count)/

- Documentation: *The number of Blocked Chimneys in the Property.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Fans-Vents-Count"></a>Fans-Vents-Count

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Fans-Vents-Count`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Fans-Vents-Count)/

- Documentation: *For backward compatibility only, do not use.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Flueless-Gas-Fires-Count"></a>Flueless-Gas-Fires-Count

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Flueless-Gas-Fires-Count`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Flueless-Gas-Fires-Count)/

- Documentation: *The number of flueless gas fires in the Property.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Pressure-Test"></a>Pressure-Test

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Pressure-Test`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Pressure-Test)/

- Documentation: *Whether there has been a pressure test, or whether an assumed value is used for the air permeability.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *yes (new dwelling, value measured in this dwelling)*
    - **"2"** - *yes (new dwelling, design value)*
    - **"3"** - *no test, value assumed for calculation (new dwelling)*
    - **"4"** - *no test, SAP algorithm used (existing dwelling)*
    - **"5"** - *average for other dwellings of the same type (new dwelling)*
    - **"6"** - *yes (existing dwelling)*
    - **"7"** - *yes (measured value) - low-pressure pulse*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Pressure-Test-Certificate-Number"></a>Pressure-Test-Certificate-Number

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Pressure-Test-Certificate-Number`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Pressure-Test-Certificate-Number)/

- Documentation: *The pressure test certificate number or test engineer reference.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Air-Permeability"></a>Air-Permeability

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Air-Permeability`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Air-Permeability)/

- Documentation: *Air permeability; only if pressure test (yes or assumed).*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Ground-Floor-Type"></a>Ground-Floor-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Ground-Floor-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Ground-Floor-Type)/

- Documentation: *The type of ground floor; nly if no pressure test.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *not suspended timber*
    - **"2"** - *suspended timber, sealed*
    - **"3"** - *suspended timber, unsealed*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Wall-Type"></a>Wall-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Wall-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Wall-Type)/

- Documentation: *The construction of the walls; only if no pressure test.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *steel or timber frame*
    - **"2"** - *other*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Has-Draught-Lobby"></a>Has-Draught-Lobby

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Has-Draught-Lobby`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Has-Draught-Lobby)/

- Documentation: *Is there a draft lobby? Only if no pressure test.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/DraughtStripping"></a>DraughtStripping

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`DraughtStripping`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/DraughtStripping)/

- Documentation: *Draughtstripping percentage; only if no pressure test.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Sheltered-Sides-Count"></a>Sheltered-Sides-Count

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Sheltered-Sides-Count`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Sheltered-Sides-Count)/

- Documentation: *The number of sheltered sides in the Property.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Ventilation-Type"></a>Ventilation-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Ventilation-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Ventilation-Type)/

- Documentation: *The type of ventilation.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *natural with intermittent extract fans*
    - **"2"** - *natural with passive vents*
    - **"3"** - *positive input from loft*
    - **"4"** - *positive input from outside*
    - **"5"** - *mechanical extract, centralised (MEV c)*
    - **"6"** - *mechanical extract, decentralised (MEV dc)*
    - **"7"** - *balanced without heat recovery (MV)*
    - **"8"** - *balanced with heat recovery (MVHR)*
    - **"9"** - *natural with intermittent extract fans and/or passive vents. For backwards compatibility only, do not use.*
    - **"10"** - *natural with intermittent extract fans and passive vents*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Ventilation-Data-Source"></a>Mechanical-Ventilation-Data-Source

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Mechanical-Ventilation-Data-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Ventilation-Data-Source)/

- Documentation: *Source of mechanical ventilation data; only if mechanical ventilation.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *from database*
    - **"2"** - *from manufacturer declaration*
    - **"3"** - *from SAP table*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-System-Index-Number"></a>Mechanical-Vent-System-Index-Number

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Mechanical-Vent-System-Index-Number`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-System-Index-Number)/

- Documentation: *Mechanical vent system index number; if mechanical vent data from database (MEV c, MEV dc, MV, MVHR).*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Commissioning-Certificate-Number"></a>Mechanical-Vent-Commissioning-Certificate-Number

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Mechanical-Vent-Commissioning-Certificate-Number`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Commissioning-Certificate-Number)/

- Documentation: *Mechanical ventilation Commissioning certificate number .*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Installation-Engineer"></a>Mechanical-Vent-Installation-Engineer

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Mechanical-Vent-Installation-Engineer`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Installation-Engineer)/

- Documentation: *Mechanical ventilation installation engineer registration reference.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-System-Make-Model"></a>Mechanical-Vent-System-Make-Model

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Mechanical-Vent-System-Make-Model`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-System-Make-Model)/

- Documentation: *Mechanical ventilation system make and model.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Wet-Rooms-Count"></a>Wet-Rooms-Count

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Wet-Rooms-Count`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Wet-Rooms-Count)/

- Documentation: *Number of wet rooms, including the kitchen; if mech vent data from manufacturer declaration or database (MEV c, MV, MVHR).*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Specific-Fan-Power"></a>Mechanical-Vent-Specific-Fan-Power

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Mechanical-Vent-Specific-Fan-Power`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Specific-Fan-Power)/

- Documentation: *Mechanical vent specific fan power in watts per (litres per second); if mechanical vent data (PIV from outside, MEV c or dc, MV, MVHR).*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Heat-Recovery-Efficiency"></a>Mechanical-Vent-Heat-Recovery-Efficiency

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Mechanical-Vent-Heat-Recovery-Efficiency`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Heat-Recovery-Efficiency)/

- Documentation: *Mechanical vent heat recovery efficiency percentage; if mechanical vent (MVHR).*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Duct-Type"></a>Mechanical-Vent-Duct-Type

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Mechanical-Vent-Duct-Type`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Duct-Type)/

- Documentation: *Mechanical vent duct type; if MEV c, MV or MVHR.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *flexible*
    - **"2"** - *rigid*
    - **"3"** - *semi-rigid*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Duct-Insulation"></a>Mechanical-Vent-Duct-Insulation

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Mechanical-Vent-Duct-Insulation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Duct-Insulation)/

- Documentation: *Mechanical vent duct insulation; if MVHR.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *not insulated*
    - **"2"** - *insulated*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Duct-Insulation-Level"></a>Mechanical-Vent-Duct-Insulation-Level

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Mechanical-Vent-Duct-Insulation-Level`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Duct-Insulation-Level)/

- Documentation: *Mechanical vent duct insulation; if MVHR.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *level 1*
    - **"2"** - *level 2*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Duct-Placement"></a>Mechanical-Vent-Duct-Placement

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Mechanical-Vent-Duct-Placement`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Duct-Placement)/

- Documentation: *Mechanical ventilation duct insulation; if MVHR.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *inside heated envelope*
    - **"2"** - *outside heated envelope*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Measured-Installation"></a>Mechanical-Vent-Measured-Installation

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Mechanical-Vent-Measured-Installation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Measured-Installation)/

- Documentation: *Mechanical ventilation SPF measured in situ; if MVHR or balanced.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Room-Fans-Count"></a>Kitchen-Room-Fans-Count

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Kitchen-Room-Fans-Count`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Room-Fans-Count)/

- Documentation: *MEV dc, number of fans in room, kitchen; if mechanical vent data from database or manufacturer declaration (MEV dc).*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Room-Fans-Specific-Power"></a>Kitchen-Room-Fans-Specific-Power

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Kitchen-Room-Fans-Specific-Power`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Room-Fans-Specific-Power)/

- Documentation: *MEV dc, specific fan power of fans in room, kitchen, in watts per (litres per second); if mechanical vent data from manufacturer declaration (MEV dc).*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Room-Fans-Count"></a>Non-Kitchen-Room-Fans-Count

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Non-Kitchen-Room-Fans-Count`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Room-Fans-Count)/

- Documentation: *MEV dc, number of fans in room, rooms other than kitchen; if mechanical vent data from database or manufacturer declaration (MEV dc).*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Room-Fans-Specific-Power"></a>Non-Kitchen-Room-Fans-Specific-Power

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Non-Kitchen-Room-Fans-Specific-Power`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Room-Fans-Specific-Power)/

- Documentation: *MEV dc, specific fan power of fans in room, rooms other than kitchen, in watts per (litres per second); if mechanical vent data from manufacturer declaration (MEV dc).*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Duct-Fans-Count"></a>Kitchen-Duct-Fans-Count

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Kitchen-Duct-Fans-Count`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Duct-Fans-Count)/

- Documentation: *MEV dc, number of fans via duct, kitchen; if mechanical vent data from database or manufacturer declaration (MEV dc).*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Duct-Fans-Specific-Power"></a>Kitchen-Duct-Fans-Specific-Power

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Kitchen-Duct-Fans-Specific-Power`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Duct-Fans-Specific-Power)/

- Documentation: *MEV dc, specific fan power of fans via duct, kitchen, in watts per (litres per second); if mechanical vent data from manufacturer declaration (MEV dc).*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Duct-Fans-Count"></a>Non-Kitchen-Duct-Fans-Count

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Non-Kitchen-Duct-Fans-Count`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Duct-Fans-Count)/

- Documentation: *MEV dc, number of fans via duct, rooms other than kitchen; if mechanical vent data from database or manufacturer declaration (MEV dc).*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Duct-Fans-Specific-Power"></a>Non-Kitchen-Duct-Fans-Specific-Power

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Non-Kitchen-Duct-Fans-Specific-Power`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Duct-Fans-Specific-Power)/

- Documentation: *MEV dc, specific fan power of fans via duct, rooms other than kitchen, in watts per (litres per second); if mechanical vent data from manufacturer declaration (MEV dc).*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Wall-Fans-Count"></a>Kitchen-Wall-Fans-Count

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Kitchen-Wall-Fans-Count`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Wall-Fans-Count)/

- Documentation: *MEV dc, number of fans through wall, kitchen; if mechanical vent data from database or manufacturer declaration (MEV dc).*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Wall-Fans-Specific-Power"></a>Kitchen-Wall-Fans-Specific-Power

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Kitchen-Wall-Fans-Specific-Power`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Wall-Fans-Specific-Power)/

- Documentation: *MEV dc, specific fan power of fans through wall, kitchen, in watts per (litres per second); if mechanical vent data from manufacturer declaration (MEV dc).*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Wall-Fans-Count"></a>Non-Kitchen-Wall-Fans-Count

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Non-Kitchen-Wall-Fans-Count`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Wall-Fans-Count)/

- Documentation: *MEV dc, number of fans through wall, rooms other than kitchen; if mechanical vent data from database or manufacturer declaration (MEV dc).*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Wall-Fans-Specific-Power"></a>Non-Kitchen-Wall-Fans-Specific-Power

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Non-Kitchen-Wall-Fans-Specific-Power`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Wall-Fans-Specific-Power)/

- Documentation: *MEV dc, specific fan power of fans through wall, rooms other than kitchen, in watts per (litres per second); if mechanical vent data from manufacturer declaration (MEV dc).*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Extract-Fans-Count"></a>Extract-Fans-Count

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Extract-Fans-Count`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Extract-Fans-Count)/

- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/PSV-Count"></a>PSV-Count

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`PSV-Count`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/PSV-Count)/

- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Is-Mechanical-Vent-Approved-Installer-Scheme"></a>Is-Mechanical-Vent-Approved-Installer-Scheme

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Is-Mechanical-Vent-Approved-Installer-Scheme`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Is-Mechanical-Vent-Approved-Installer-Scheme)/

- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Ducts-Index-Number"></a>Mechanical-Vent-Ducts-Index-Number

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)/[`Mechanical-Vent-Ducts-Index-Number`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Ducts-Index-Number)/

- Documentation: *Mechanical vent ducts index number; if applicable.*
- Parent element: [`SAP-Ventilation`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting"></a>SAP-Lighting

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Lighting`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting)/

- Documentation2: *Details of the main lighting for the property*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Child elements: [`Fixed-Lights`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights"></a>Fixed-Lights

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Lighting`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting)/[`Fixed-Lights`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights)/

- Documentation: *The record of a lighting type within the building.*
- Documentation2: *Fixed lighting present in the property.*
- Parent element: [`SAP-Lighting`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting)
- Child elements: [`Fixed-Light`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light"></a>Fixed-Light

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Lighting`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting)/[`Fixed-Lights`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights)/[`Fixed-Light`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light)/

- Documentation2: *Various details for each fixed lighting type in the property.*
- Parent element: [`Fixed-Lights`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights)
- Child elements: [`Lighting-Efficacy`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light/Lighting-Efficacy) [`Lighting-Power`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light/Lighting-Power) [`Lighting-Outlets`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light/Lighting-Outlets)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **unbounded**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light/Lighting-Efficacy"></a>Lighting-Efficacy

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Lighting`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting)/[`Fixed-Lights`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights)/[`Fixed-Light`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light)/[`Lighting-Efficacy`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light/Lighting-Efficacy)/

- Documentation: *The efficacy of the lighting type in lumens/Watt.*
- Parent element: [`Fixed-Light`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light/Lighting-Power"></a>Lighting-Power

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Lighting`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting)/[`Fixed-Lights`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights)/[`Fixed-Light`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light)/[`Lighting-Power`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light/Lighting-Power)/

- Documentation: *The power of the selected lighting type in Watts.*
- Parent element: [`Fixed-Light`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light/Lighting-Outlets"></a>Lighting-Outlets

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Lighting`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting)/[`Fixed-Lights`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights)/[`Fixed-Light`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light)/[`Lighting-Outlets`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light/Lighting-Outlets)/

- Documentation: *The number of light fitting outlets of that type.*
- Parent element: [`Fixed-Light`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Deselected-Improvements"></a>SAP-Deselected-Improvements

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Deselected-Improvements`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Deselected-Improvements)/

- Documentation2: *There are 22 possible improvement measures, designated from A to V. This must record measures deselected by DEA (A to V is the full set, only E, N, U and V are considered at the moment for new build).*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Child elements: [`Deselected-Improvement-Measure`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Deselected-Improvements/Deselected-Improvement-Measure)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Deselected-Improvements/Deselected-Improvement-Measure"></a>Deselected-Improvement-Measure

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Deselected-Improvements`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Deselected-Improvements)/[`Deselected-Improvement-Measure`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Deselected-Improvements/Deselected-Improvement-Measure)/

- Parent element: [`SAP-Deselected-Improvements`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Deselected-Improvements)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"A"** - *Loft insulation*
    - **"A2"** - *Flat roof insulation*
    - **"A3"** - *Room-in-roof insulation*
    - **"B"** - *Cavity wall insulation*
    - **"C"** - *Hot water cylinder insulation*
    - **"D"** - *Draughtproofing*
    - **"E"** - *Low energy lights*
    - **"F"** - *Cylinder thermostat*
    - **"G"** - *Heating controls for wet central heating system*
    - **"H"** - *Heating controls for warm air system*
    - **"I"** - *Upgrade boiler, same fuel*
    - **"J"** - *Biomass boiler*
    - **"J2"** - *Biomass boiler as alternative improvement*
    - **"K"** - *Biomass room heater with boiler*
    - **"L"** - *New or replacement fan-assisted storage heaters*
    - **"L2"** - *New or replacement high heat retention storage heaters*
    - **"M"** - *Replacement warm-air unit*
    - **"N"** - *Solar water heating*
    - **"O"** - *Replacement double glazed windows*
    - **"O3"** - *Replacement double glazing units*
    - **"P"** - *Secondary glazing*
    - **"Q"** - *Solid wall insulation*
    - **"Q2"** - *External insulation with cavity wall insulation*
    - **"R"** - *Condensing oil boiler*
    - **"S"** - *Change heating to Band A gas condensing boiler (no fuel switch)*
    - **"T"** - *Change heating to Band A gas condensing boiler (fuel switch)*
    - **"T2"** - *Flue gas heat recovery*
    - **"U"** - *Photovoltaics*
    - **"V"** - *Wind turbine (roof mounted)*
    - **"V2"** - *Wind turbine (on mast)*
    - **"W"** - *Floor insulation*
    - **"X"** - *Insulated doors*
    - **"Y"** - *Instantaneous waste water heat recovery*
    - **"Y2"** - *Storage waste water heat recovery*
    - **"Z1"** - *Air or ground source heat pump*
    - **"Z2"** - *Air or ground source heat pump with underfloor heating*
    - **"Z3"** - *Micro-CHP*
- Minimum occurrence: **1**
- Maximum occurrence: **unbounded**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Flat-Details"></a>SAP-Flat-Details

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Flat-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Flat-Details)/

- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Child elements: [`Level`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Flat-Details/Level) [`Storeys`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Flat-Details/Storeys)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Flat-Details/Level"></a>Level

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Flat-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Flat-Details)/[`Level`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Flat-Details/Level)/

- Documentation: *Indication of where a flat is located in a building.*
- Parent element: [`SAP-Flat-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Flat-Details)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"0"** - *basement*
    - **"1"** - *ground floor*
    - **"2"** - *mid floor*
    - **"3"** - *top floor*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Flat-Details/Storeys"></a>Storeys

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Flat-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Flat-Details)/[`Storeys`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Flat-Details/Storeys)/

- Documentation: *Count of number of storeys present in the block of flats.*
- Parent element: [`SAP-Flat-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Flat-Details)
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features"></a>SAP-Special-Features

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Special-Features`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features)/

- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Child elements: [`SAP-Special-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature"></a>SAP-Special-Feature

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Special-Features`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features)/[`SAP-Special-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature)/

- Parent element: [`SAP-Special-Features`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features)
- Child elements: [`Description`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Description) [`Energy-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature) [`Emissions-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **unbounded**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Description"></a>Description

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Special-Features`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features)/[`SAP-Special-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature)/[`Description`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Description)/

- Parent element: [`SAP-Special-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature"></a>Energy-Feature

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Special-Features`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features)/[`SAP-Special-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature)/[`Energy-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature)/

- Parent element: [`SAP-Special-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature)
- Child elements: [`Energy-Saved-Or-Generated`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Energy-Saved-Or-Generated) [`Saved-Or-Generated-Fuel`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Saved-Or-Generated-Fuel) [`Energy-Used`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Energy-Used) [`Energy-Used-Fuel`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Energy-Used-Fuel) [`Air-Change-Rates`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Energy-Saved-Or-Generated"></a>Energy-Saved-Or-Generated

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Special-Features`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features)/[`SAP-Special-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature)/[`Energy-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature)/[`Energy-Saved-Or-Generated`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Energy-Saved-Or-Generated)/

- Documentation: *Energy saved or generated in kWh/year.*
- Parent element: [`Energy-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Saved-Or-Generated-Fuel"></a>Saved-Or-Generated-Fuel

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Special-Features`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features)/[`SAP-Special-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature)/[`Energy-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature)/[`Saved-Or-Generated-Fuel`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Saved-Or-Generated-Fuel)/

- Parent element: [`Energy-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *Gas: mains gas*
    - **"2"** - *Gas: bulk LPG*
    - **"3"** - *Gas: bottled LPG*
    - **"4"** - *Oil: heating oil*
    - **"7"** - *Gas: biogas*
    - **"8"** - *LNG*
    - **"9"** - *LPG subject to Special Condition 18*
    - **"10"** - *Solid fuel: dual fuel appliance (mineral and wood)*
    - **"11"** - *Solid fuel: house coal*
    - **"12"** - *Solid fuel: manufactured smokeless fuel*
    - **"15"** - *Solid fuel: anthracite*
    - **"20"** - *Solid fuel: wood logs*
    - **"21"** - *Solid fuel: wood chips*
    - **"22"** - *Solid fuel: wood pellets (in bags, for secondary heating)*
    - **"23"** - *Solid fuel: wood pellets (bulk supply in bags, for main heating)*
    - **"36"** - *Electricity: electricity sold to grid*
    - **"37"** - *Electricity: electricity displaced from grid*
    - **"39"** - *Electricity: electricity, unspecified tariff*
    - **"41"** - *Community heating schemes: heat from electric heat pump*
    - **"42"** - *Community heating schemes: heat from boilers - waste combustion*
    - **"43"** - *Community heating schemes: heat from boilers - biomass*
    - **"44"** - *Community heating schemes: heat from boilers - biogas*
    - **"45"** - *Community heating schemes: waste heat from power stations*
    - **"46"** - *Community heating schemes: geothermal heat source*
    - **"47"** - *Community heating schemes: high grade heat recovered from process*
    - **"48"** - *Community heating schemes: heat from CHP*
    - **"49"** - *Community heating schemes: low grade heat recovered from process*
    - **"50"** - *Community heating schemes: electricity for pumping in distribution network*
    - **"51"** - *Community heating schemes: heat from mains gas*
    - **"52"** - *Community heating schemes: heat from LPG*
    - **"53"** - *Community heating schemes: heat from oil*
    - **"54"** - *Community heating schemes: heat from coal*
    - **"55"** - *Community heating schemes: heat from B30D*
    - **"56"** - *Community heating schemes: heat from boilers that can use mineral oil or biodiesel*
    - **"57"** - *Community heating schemes: heat from boilers using biodiesel from any biomass source*
    - **"58"** - *Community heating schemes: biodiesel from vegetable oil only*
    - **"71"** - *biodiesel from any biomass source*
    - **"72"** - *biodiesel from used cooking oil only*
    - **"73"** - *biodiesel from vegetable oil only*
    - **"74"** - *appliances able to use mineral oil or liquid biofuel*
    - **"75"** - *B30K*
    - **"76"** - *bioethanol from any biomass source*
    - **"99"** - *Fuel data from pcdb*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Energy-Used"></a>Energy-Used

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Special-Features`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features)/[`SAP-Special-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature)/[`Energy-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature)/[`Energy-Used`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Energy-Used)/

- Documentation: *Energy used in kWh/year.*
- Parent element: [`Energy-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Energy-Used-Fuel"></a>Energy-Used-Fuel

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Special-Features`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features)/[`SAP-Special-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature)/[`Energy-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature)/[`Energy-Used-Fuel`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Energy-Used-Fuel)/

- Parent element: [`Energy-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *Gas: mains gas*
    - **"2"** - *Gas: bulk LPG*
    - **"3"** - *Gas: bottled LPG*
    - **"4"** - *Oil: heating oil*
    - **"7"** - *Gas: biogas*
    - **"8"** - *LNG*
    - **"9"** - *LPG subject to Special Condition 18*
    - **"10"** - *Solid fuel: dual fuel appliance (mineral and wood)*
    - **"11"** - *Solid fuel: house coal*
    - **"12"** - *Solid fuel: manufactured smokeless fuel*
    - **"15"** - *Solid fuel: anthracite*
    - **"20"** - *Solid fuel: wood logs*
    - **"21"** - *Solid fuel: wood chips*
    - **"22"** - *Solid fuel: wood pellets (in bags, for secondary heating)*
    - **"23"** - *Solid fuel: wood pellets (bulk supply in bags, for main heating)*
    - **"36"** - *Electricity: electricity sold to grid*
    - **"37"** - *Electricity: electricity displaced from grid*
    - **"39"** - *Electricity: electricity, unspecified tariff*
    - **"41"** - *Community heating schemes: heat from electric heat pump*
    - **"42"** - *Community heating schemes: heat from boilers - waste combustion*
    - **"43"** - *Community heating schemes: heat from boilers - biomass*
    - **"44"** - *Community heating schemes: heat from boilers - biogas*
    - **"45"** - *Community heating schemes: waste heat from power stations*
    - **"46"** - *Community heating schemes: geothermal heat source*
    - **"47"** - *Community heating schemes: high grade heat recovered from process*
    - **"48"** - *Community heating schemes: heat from CHP*
    - **"49"** - *Community heating schemes: low grade heat recovered from process*
    - **"50"** - *Community heating schemes: electricity for pumping in distribution network*
    - **"51"** - *Community heating schemes: heat from mains gas*
    - **"52"** - *Community heating schemes: heat from LPG*
    - **"53"** - *Community heating schemes: heat from oil*
    - **"54"** - *Community heating schemes: heat from coal*
    - **"55"** - *Community heating schemes: heat from B30D*
    - **"56"** - *Community heating schemes: heat from boilers that can use mineral oil or biodiesel*
    - **"57"** - *Community heating schemes: heat from boilers using biodiesel from any biomass source*
    - **"58"** - *Community heating schemes: biodiesel from vegetable oil only*
    - **"71"** - *biodiesel from any biomass source*
    - **"72"** - *biodiesel from used cooking oil only*
    - **"73"** - *biodiesel from vegetable oil only*
    - **"74"** - *appliances able to use mineral oil or liquid biofuel*
    - **"75"** - *B30K*
    - **"76"** - *bioethanol from any biomass source*
    - **"99"** - *Fuel data from pcdb*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates"></a>Air-Change-Rates

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Special-Features`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features)/[`SAP-Special-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature)/[`Energy-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature)/[`Air-Change-Rates`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates)/

- Documentation: *For Appendix Q procedure that provides air change rates. Only one Special Feature can have data on air change rates.*
- Parent element: [`Energy-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature)
- Child elements: [`Air-Change-Rate`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate"></a>Air-Change-Rate

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Special-Features`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features)/[`SAP-Special-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature)/[`Energy-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature)/[`Air-Change-Rates`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates)/[`Air-Change-Rate`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate)/

- Parent element: [`Air-Change-Rates`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates)
- Child elements: [`Air-Change-Rate-Month`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate/Air-Change-Rate-Month) [`Air-Change-Rate-Value`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate/Air-Change-Rate-Value)
- Has text value: *False*
- Minimum occurrence: **12**
- Maximum occurrence: **12**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate/Air-Change-Rate-Month"></a>Air-Change-Rate-Month

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Special-Features`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features)/[`SAP-Special-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature)/[`Energy-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature)/[`Air-Change-Rates`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates)/[`Air-Change-Rate`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate)/[`Air-Change-Rate-Month`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate/Air-Change-Rate-Month)/

- Parent element: [`Air-Change-Rate`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"Jan"** - **
    - **"Feb"** - **
    - **"Mar"** - **
    - **"Apr"** - **
    - **"May"** - **
    - **"Jun"** - **
    - **"Jul"** - **
    - **"Aug"** - **
    - **"Sep"** - **
    - **"Oct"** - **
    - **"Nov"** - **
    - **"Dec"** - **
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate/Air-Change-Rate-Value"></a>Air-Change-Rate-Value

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Special-Features`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features)/[`SAP-Special-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature)/[`Energy-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature)/[`Air-Change-Rates`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates)/[`Air-Change-Rate`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate)/[`Air-Change-Rate-Value`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate/Air-Change-Rate-Value)/

- Documentation: *Air change rate in month.*
- Parent element: [`Air-Change-Rate`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature"></a>Emissions-Feature

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Special-Features`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features)/[`SAP-Special-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature)/[`Emissions-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature)/

- Parent element: [`SAP-Special-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature)
- Child elements: [`Emissions-Saved`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature/Emissions-Saved) [`Emissions-Created`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature/Emissions-Created)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature/Emissions-Saved"></a>Emissions-Saved

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Special-Features`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features)/[`SAP-Special-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature)/[`Emissions-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature)/[`Emissions-Saved`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature/Emissions-Saved)/

- Documentation: *Emissions saved in kg/year.*
- Parent element: [`Emissions-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature/Emissions-Created"></a>Emissions-Created

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Special-Features`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features)/[`SAP-Special-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature)/[`Emissions-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature)/[`Emissions-Created`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature/Emissions-Created)/

- Documentation: *Additional emissions in kg/year.*
- Parent element: [`Emissions-Feature`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Design-Water-Use"></a>Design-Water-Use

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`Design-Water-Use`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Design-Water-Use)/

- Documentation: *Design limit for total water use.*
- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *<= 125 litres per person per day*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling"></a>SAP-Cooling

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Cooling`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling)/

- Parent element: [`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)
- Child elements: [`Cooled-Area`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling/Cooled-Area) [`Cooling-System-Data-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling/Cooling-System-Data-Source) [`Cooling-System-Class`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling/Cooling-System-Class) [`System-Energy-Efficiency-Ratio`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling/System-Energy-Efficiency-Ratio)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling/Cooled-Area"></a>Cooled-Area

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Cooling`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling)/[`Cooled-Area`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling/Cooled-Area)/

- Parent element: [`SAP-Cooling`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling/Cooling-System-Data-Source"></a>Cooling-System-Data-Source

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Cooling`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling)/[`Cooling-System-Data-Source`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling/Cooling-System-Data-Source)/

- Parent element: [`SAP-Cooling`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"1"** - *from database*
    - **"2"** - *from manufacturer declaration*
    - **"3"** - *from SAP table*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling/Cooling-System-Class"></a>Cooling-System-Class

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Cooling`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling)/[`Cooling-System-Class`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling/Cooling-System-Class)/

- Documentation: *Data set includes either class or SEER, not both.*
- Parent element: [`SAP-Cooling`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling)
- Has text value: *True*
- Data type: *<class 'str'>*
- codes:
    - **"A+++"** - **
    - **"A++"** - **
    - **"A+"** - **
    - **"A"** - **
    - **"B"** - **
    - **"C"** - **
    - **"D"** - **
    - **"E"** - **
    - **"F"** - **
    - **"G"** - **
    - **"ND"** - **
    - **"Unknown"** - **
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling/System-Energy-Efficiency-Ratio"></a>System-Energy-Efficiency-Ratio

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`SAP10-Data`](#SAP-Compliance-Report/SAP-Report/SAP10-Data)/[`SAP-Property-Details`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details)/[`SAP-Cooling`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling)/[`System-Energy-Efficiency-Ratio`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling/System-Energy-Efficiency-Ratio)/

- Documentation: *SEER.*
- Parent element: [`SAP-Cooling`](#SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/PDF"></a>PDF

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`PDF`](#SAP-Compliance-Report/SAP-Report/PDF)/

- Documentation: *DEPRECATED - DO NOT USE This element is allowed for backwards-compatibility but any data sent here will not be read, processed or stored by the register.*
- Parent element: [`SAP-Report`](#SAP-Compliance-Report/SAP-Report)
- Has text value: *True*
- Data type: *<function b64encode at 0x000001D4B225D5E0>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Insurance-Details"></a>Insurance-Details

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Insurance-Details`](#SAP-Compliance-Report/SAP-Report/Insurance-Details)/

- Documentation2: *Details of the Professional Indemnity Insurance policy used to provide cover against a compensation claim against any particular Home Condition Report. A particular Home Condition Report may be covered by an Professional Indemnity Insurance policy in one of three different ways: * The Home Inspector has personal Professional Indemnity Insurance and the Home Condition Report is covered by this. * The Home Condition Report is covered by an umbrella Professional Indemnity Insurance policy held by the Home Condition Report Supplier that assigned the inspection to the Home Inspector. * An individual insurance policy is taken out to cover the individual report such as the case where the property is unusual and falls outside the Home Inspectors normal Professional Indemnity Insurance policy. A Home Inspector may use any or all of these methods to providing Professional Indemnity Insurance for a Home Condition Report on a case-by-case basis.*
- Parent element: [`SAP-Report`](#SAP-Compliance-Report/SAP-Report)
- Child elements: [`Insurer`](#SAP-Compliance-Report/SAP-Report/Insurance-Details/Insurer) [`Policy-No`](#SAP-Compliance-Report/SAP-Report/Insurance-Details/Policy-No) [`Effective-Date`](#SAP-Compliance-Report/SAP-Report/Insurance-Details/Effective-Date) [`Expiry-Date`](#SAP-Compliance-Report/SAP-Report/Insurance-Details/Expiry-Date) [`PI-Limit`](#SAP-Compliance-Report/SAP-Report/Insurance-Details/PI-Limit)
- Has text value: *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Insurance-Details/Insurer"></a>Insurer

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Insurance-Details`](#SAP-Compliance-Report/SAP-Report/Insurance-Details)/[`Insurer`](#SAP-Compliance-Report/SAP-Report/Insurance-Details/Insurer)/

- Documentation: *The name of the insurance company that underwrites / issued the insurance policy*
- Parent element: [`Insurance-Details`](#SAP-Compliance-Report/SAP-Report/Insurance-Details)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Insurance-Details/Policy-No"></a>Policy-No

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Insurance-Details`](#SAP-Compliance-Report/SAP-Report/Insurance-Details)/[`Policy-No`](#SAP-Compliance-Report/SAP-Report/Insurance-Details/Policy-No)/

- Documentation: *The policy number of the insurance policy*
- Parent element: [`Insurance-Details`](#SAP-Compliance-Report/SAP-Report/Insurance-Details)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Insurance-Details/Effective-Date"></a>Effective-Date

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Insurance-Details`](#SAP-Compliance-Report/SAP-Report/Insurance-Details)/[`Effective-Date`](#SAP-Compliance-Report/SAP-Report/Insurance-Details/Effective-Date)/

- Documentation: *The date that the insurance policy becomes effective (commences cover)*
- Parent element: [`Insurance-Details`](#SAP-Compliance-Report/SAP-Report/Insurance-Details)
- Has text value: *True*
- Data type: *<built-in method fromisoformat of type object at 0x00007FFB580DD990>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Insurance-Details/Expiry-Date"></a>Expiry-Date

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Insurance-Details`](#SAP-Compliance-Report/SAP-Report/Insurance-Details)/[`Expiry-Date`](#SAP-Compliance-Report/SAP-Report/Insurance-Details/Expiry-Date)/

- Documentation: *The date that the insurance policy is supposed to expire.*
- Parent element: [`Insurance-Details`](#SAP-Compliance-Report/SAP-Report/Insurance-Details)
- Has text value: *True*
- Data type: *<built-in method fromisoformat of type object at 0x00007FFB580DD990>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/Insurance-Details/PI-Limit"></a>PI-Limit

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`Insurance-Details`](#SAP-Compliance-Report/SAP-Report/Insurance-Details)/[`PI-Limit`](#SAP-Compliance-Report/SAP-Report/Insurance-Details/PI-Limit)/

- Documentation: *The upper limit of the Professional Indemnity cover provided by the insurance policy.*
- Documentation2: *Extension of a Decimal value for use with monetary values where a currency code needs to be specified. The currency code is actually metadata about the value so, in line with good XML practice, the Currency Code is declared as an XML-Attribute of the Money datatype rather than as a separate XML-Element. The currency attribute should then include a list of valid currencies codes that are supported.*
- Parent element: [`Insurance-Details`](#SAP-Compliance-Report/SAP-Report/Insurance-Details)
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/SAP-Report/ExternalDefinitions-Revision-Number"></a>ExternalDefinitions-Revision-Number

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`SAP-Report`](#SAP-Compliance-Report/SAP-Report)/[`ExternalDefinitions-Revision-Number`](#SAP-Compliance-Report/SAP-Report/ExternalDefinitions-Revision-Number)/

- Documentation: *A number indicating the version of related ExternalDefinitions.xsd*
- Parent element: [`SAP-Report`](#SAP-Compliance-Report/SAP-Report)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/Client-Name"></a>Client-Name

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`Client-Name`](#SAP-Compliance-Report/Client-Name)/

- Documentation: *Name of the client. External to the EPC schema for GDPR purposes.*
- Parent element: [`SAP-Compliance-Report`](#SAP-Compliance-Report)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/Client-Company"></a>Client-Company

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`Client-Company`](#SAP-Compliance-Report/Client-Company)/

- Documentation: *Company name of the client. External to the EPC schema for GDPR purposes.*
- Parent element: [`SAP-Compliance-Report`](#SAP-Compliance-Report)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/Client-Address"></a>Client-Address

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`Client-Address`](#SAP-Compliance-Report/Client-Address)/

- Documentation: *Address of the client. External to the EPC schema for GDPR purposes.*
- Documentation2: *An address is composed of a number of structured elements such as Postcode, Post-Town, Street etc.*
- Parent element: [`SAP-Compliance-Report`](#SAP-Compliance-Report)
- Child elements: [`Address-Line-1`](#SAP-Compliance-Report/Client-Address/Address-Line-1) [`Address-Line-2`](#SAP-Compliance-Report/Client-Address/Address-Line-2) [`Address-Line-3`](#SAP-Compliance-Report/Client-Address/Address-Line-3) [`Post-Town`](#SAP-Compliance-Report/Client-Address/Post-Town) [`Postcode`](#SAP-Compliance-Report/Client-Address/Postcode)
- Has text value: *False*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/Client-Address/Address-Line-1"></a>Address-Line-1

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`Client-Address`](#SAP-Compliance-Report/Client-Address)/[`Address-Line-1`](#SAP-Compliance-Report/Client-Address/Address-Line-1)/

- Parent element: [`Client-Address`](#SAP-Compliance-Report/Client-Address)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/Client-Address/Address-Line-2"></a>Address-Line-2

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`Client-Address`](#SAP-Compliance-Report/Client-Address)/[`Address-Line-2`](#SAP-Compliance-Report/Client-Address/Address-Line-2)/

- Parent element: [`Client-Address`](#SAP-Compliance-Report/Client-Address)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/Client-Address/Address-Line-3"></a>Address-Line-3

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`Client-Address`](#SAP-Compliance-Report/Client-Address)/[`Address-Line-3`](#SAP-Compliance-Report/Client-Address/Address-Line-3)/

- Parent element: [`Client-Address`](#SAP-Compliance-Report/Client-Address)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/Client-Address/Post-Town"></a>Post-Town

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`Client-Address`](#SAP-Compliance-Report/Client-Address)/[`Post-Town`](#SAP-Compliance-Report/Client-Address/Post-Town)/

- Parent element: [`Client-Address`](#SAP-Compliance-Report/Client-Address)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/Client-Address/Postcode"></a>Postcode

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`Client-Address`](#SAP-Compliance-Report/Client-Address)/[`Postcode`](#SAP-Compliance-Report/Client-Address/Postcode)/

- Documentation: *The Postcode for the Address*
- Parent element: [`Client-Address`](#SAP-Compliance-Report/Client-Address)
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: **1**
- Maximum occurrence: **1**

## <a name="SAP-Compliance-Report/Is-Multiple-Compliance"></a>Is-Multiple-Compliance

[`SAP-Compliance-Report`](#SAP-Compliance-Report)/[`Is-Multiple-Compliance`](#SAP-Compliance-Report/Is-Multiple-Compliance)/

- Documentation: *Is the compliance report part of a multiple compliance calculation.*
- Parent element: [`SAP-Compliance-Report`](#SAP-Compliance-Report)
- Has text value: *True*
- Data type: *<class 'bool'>*
- codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: **0**
- Maximum occurrence: **1**

