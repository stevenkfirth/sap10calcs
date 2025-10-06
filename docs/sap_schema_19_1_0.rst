.. _sap_xml_reference:

SAP XML reference
=================

This page contains the documentation for the XML schema `SAP-Schema-19.1.0 <https://github.com/communitiesuk/epb-register-api/tree/master/api/schemas/xml/SAP-Schema-19.1.0/SAP>`__.

This XML schema describes the format of the XML input files for SAP 10.2 calculations.

The root XML element can be either a :ref:`SAP-Compliance-Report` or a :ref:`SAP-Compliance-Report/SAP-Report` element.

.. _SAP-Compliance-Report:

SAP-Compliance-Report
---------------------

<:ref:`SAP-Compliance-Report`>/

- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report`> <:ref:`SAP-Compliance-Report/Client-Name`> <:ref:`SAP-Compliance-Report/Client-Company`> <:ref:`SAP-Compliance-Report/Client-Address`> <:ref:`SAP-Compliance-Report/Is-Multiple-Compliance`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report:

SAP-Report
----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/

- Documentation: *The SAP report corresponding to the compliance report.*
- Parent element: <:ref:`SAP-Compliance-Report`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Schema-Version-Original`> <:ref:`SAP-Compliance-Report/SAP-Report/Schema-Version-Current`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP-Version`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP-Data-Version`> <:ref:`SAP-Compliance-Report/SAP-Report/PCDF-Revision-Number`> <:ref:`SAP-Compliance-Report/SAP-Report/Calculation-Software-Name`> <:ref:`SAP-Compliance-Report/SAP-Report/Calculation-Software-Version`> <:ref:`SAP-Compliance-Report/SAP-Report/User-Interface-Name`> <:ref:`SAP-Compliance-Report/SAP-Report/User-Interface-Version`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`> <:ref:`SAP-Compliance-Report/SAP-Report/PDF`> <:ref:`SAP-Compliance-Report/SAP-Report/Insurance-Details`> <:ref:`SAP-Compliance-Report/SAP-Report/ExternalDefinitions-Revision-Number`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Schema-Version-Original:

Schema-Version-Original
-----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Schema-Version-Original`>/

- Documentation: *The schema version that the data conformed to when it was lodged.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Schema-Version-Current:

Schema-Version-Current
----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Schema-Version-Current`>/

- Documentation: *The schema version to which the data conforms. This node is inserted by the register when a retrieval is requested. It must not be present in a lodgement being sent to the register.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP-Version:

SAP-Version
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP-Version`>/

- Documentation: *SAP version that was used for the calculation.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report`>
- Has text value: *True*
- Codes:
    - **"9.80"** - *SAP 2005 version 9.80, dated October 2005*
    - **"9.81"** - *SAP version 9.81, dated January 2008*
    - **"9.82"** - *SAP version 9.82, dated Jun 2008*
    - **"9.83"** - *SAP version 9.83, dated Jun 2009*
    - **"9.90"** - *SAP version 9.90, dated Mar 2010*
    - **"9.91"** - *SAP version 9.91, dated Jan 2012*
    - **"9.92"** - *SAP version 9.92, dated Oct 2013*
    - **"10.2"** - *SAP version 10.2, dated Oct 2020*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP-Data-Version:

SAP-Data-Version
----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP-Data-Version`>/

- Documentation: *Version of SAP that was used to define the input data for the calculation.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report`>
- Has text value: *True*
- Codes:
    - **"9.80"** - *SAP 2005 version 9.80, dated October 2005*
    - **"9.81"** - *SAP version 9.81, dated January 2008*
    - **"9.82"** - *SAP version 9.82, dated Jun 2008*
    - **"9.83"** - *SAP version 9.83, dated Jun 2009*
    - **"9.90"** - *SAP version 9.90, dated Mar 2010*
    - **"9.91"** - *SAP version 9.91, dated Jan 2012*
    - **"9.92"** - *SAP version 9.92, dated Oct 2013*
    - **"10.2"** - *SAP version 10.2, dated Oct 2020*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/PCDF-Revision-Number:

PCDF-Revision-Number
--------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/PCDF-Revision-Number`>/

- Documentation: *Revision Number of the PCDF file used for the calculations.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Calculation-Software-Name:

Calculation-Software-Name
-------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Calculation-Software-Name`>/

- Documentation: *Name of the software used to perform the SAP calculation.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Calculation-Software-Version:

Calculation-Software-Version
----------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Calculation-Software-Version`>/

- Documentation: *Version of the software used to perform the SAP calculation.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/User-Interface-Name:

User-Interface-Name
-------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/User-Interface-Name`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/User-Interface-Version:

User-Interface-Version
----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/User-Interface-Version`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header:

Report-Header
-------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/

- Documentation2: *Report Header contains all the identification and searchable details for the Report.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/RRN`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Inspection-Date`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Report-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Completion-Date`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Registration-Date`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Status`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Language-Code`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Tenure`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Transaction-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Seller-Commission-Report`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Region-Code`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Country-Code`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Related-Party-Disclosure`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/RRN:

RRN
---

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/RRN`>/

- Documentation: *Report Reference Number is the unique report Identifier that the report will be publicly known by. The RRN is allocated to the Report at the point that it is registered and will be algorithmically derived from the natural key characteristics of the Home Condition Report i.e. The Unique Property Reference Number (UPRN) and Inspection Date.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Inspection-Date:

Inspection-Date
---------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Inspection-Date`>/

- Documentation: *The date that the inspection was actually carried out by the Home Inspector.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>
- Has text value: *True*
- Data type: *Date string (ISO format)*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Report-Type:

Report-Type
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Report-Type`>/

- Documentation: *The type of Home Inspection that was carried out. Initially the only allowed type will be a Home Condition Report inspection but this may be extended in the future to cover Energy Assessment Only inspections.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>
- Has text value: *True*
- Codes:
    - **"1"** - *Home Condition Report*
    - **"2"** - *RdSAP Energy Performance Certificate*
    - **"3"** - *SAP Energy Performance Certificate*
    - **"4"** - *Interim RdSAP Energy Performance Certificate (to be superseded by SAP EPC)*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Completion-Date:

Completion-Date
---------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Completion-Date`>/

- Documentation: *The date that the Home Inspector completed the report. This will be after the Inspection Date but generally before the Registration Date.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>
- Has text value: *True*
- Data type: *Date string (ISO format)*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Registration-Date:

Registration-Date
-----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Registration-Date`>/

- Documentation: *The date that the report was submitted to the HCR Registration Organisation for lodging in the HCR Register.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>
- Has text value: *True*
- Data type: *Date string (ISO format)*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Status:

Status
------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Status`>/

- Documentation: *The Status of the Report. A Home Condition Report can have a number of distinct states depending on whereabouts in its overall lifecycle the HCR is - see Home Condition Report Statechart for more details.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>
- Has text value: *True*
- Codes:
    - **"cancelled"** - *Cancelled*
    - **"entered"** - *entered on the register*
    - **"appeal"** - *under appeal*
    - **"removed"** - *removed*
    - **"rejected"** - *rejected*
    - **"under investigation"** - *under investigation*
    - **"not for issue"** - *not for issue*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Language-Code:

Language-Code
-------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Language-Code`>/

- Documentation: *The language that the report is written in.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>
- Has text value: *True*
- Codes:
    - **"1"** - *English*
    - **"2"** - *Welsh*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Tenure:

Tenure
------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Tenure`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>
- Has text value: *True*
- Codes:
    - **"1"** - *owner-occupied*
    - **"2"** - *rented (social)*
    - **"3"** - *rented (private)*
    - **"ND"** - *unknown*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Transaction-Type:

Transaction-Type
----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Transaction-Type`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>
- Has text value: *True*
- Codes:
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
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Seller-Commission-Report:

Seller-Commission-Report
------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Seller-Commission-Report`>/

- Documentation: *Indicates that the HCR was commissioned by the Seller of the Property or their Agent. This is required in order to differentiate these reports from Buyer commisioned reports which are not eligible for inclusion in a Home Information Pack*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>
- Has text value: *True*
- Codes:
    - **"Y"** - *Yes*
    - **"N"** - *No*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Property-Type:

Property-Type
-------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property-Type`>/

- Documentation: *Describes the type of Property that is being inspected. This should be the same as the Property-Type recorded in the Property-Details section.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>
- Has text value: *True*
- Codes:
    - **"0"** - *House*
    - **"1"** - *Bungalow*
    - **"2"** - *Flat*
    - **"3"** - *Maisonette*
    - **"4"** - *Park home*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector:

Home-Inspector
--------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector`>/

- Documentation2: *A Certified Home Inspector is a person certified by a Certification Scheme - that is they exist on the Home Inspector Register - as being qualified to carry out a Home Inspection and produce a Home Condition Report. The exact criteria for fit + proper are laid down in regulations and the Business Standards and it is the responsibility of the Certification Scheme to carry out sufficient checks to ensure those criteria are adhered to. Although covered by a different regulatory regime a Home Inspector and Energy Assessor serve synonymous roles in the product of a Home Condition Report or Energy Performance Certificate respectively.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Name`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Notify-Lodgement`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Web-Site`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/E-Mail`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Fax`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Telephone`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Company-Name`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Scheme-Name`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Scheme-Web-Site`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Identification-Number`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Name:

Name
----

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Name`>/

- Documentation: *The name by which the Home Inspector is registered. This is a structured name containing prefix, first name + surname.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Notify-Lodgement:

Notify-Lodgement
----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Notify-Lodgement`>/

- Documentation: *Indicates whether the assessor wants to be notified that a the report has been lodged in the register*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector`>
- Has text value: *True*
- Codes:
    - **"Y"** - *Yes*
    - **"N"** - *No*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address:

Contact-Address
---------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address`>/

- Documentation: *The address that any written correspondence can be sent to. This is not the same as the Registered Address because it may, of course, be a Post Office Box.*
- Documentation2: *An address is composed of a number of structured elements such as Postcode, Post-Town, Street etc.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Address-Line-1`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Address-Line-2`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Address-Line-3`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Post-Town`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Postcode`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Address-Line-1:

Address-Line-1
--------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Address-Line-1`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Address-Line-2:

Address-Line-2
--------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Address-Line-2`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Address-Line-3:

Address-Line-3
--------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Address-Line-3`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Post-Town:

Post-Town
---------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Post-Town`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Postcode:

Postcode
--------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address/Postcode`>/

- Documentation: *The Postcode for the Address*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Contact-Address`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Web-Site:

Web-Site
--------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Web-Site`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/E-Mail:

E-Mail
------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/E-Mail`>/

- Documentation: *the E-Mail address that the Authorised User can be contacted at.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Fax:

Fax
---

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Fax`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Telephone:

Telephone
---------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Telephone`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Company-Name:

Company-Name
------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Company-Name`>/

- Documentation: *The Name of the Company that the assessor is employed by.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Scheme-Name:

Scheme-Name
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Scheme-Name`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Scheme-Web-Site:

Scheme-Web-Site
---------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Scheme-Web-Site`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Identification-Number:

Identification-Number
---------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Identification-Number`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Identification-Number/Certificate-Number`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Identification-Number/Membership-Number`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Identification-Number/Certificate-Number:

Certificate-Number
------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Identification-Number`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Identification-Number/Certificate-Number`>/

- Documentation: *The unique identifier assigned to the assessor by the scheme by which they can be identified throughout their membership of the scheme.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Identification-Number`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Identification-Number/Membership-Number:

Membership-Number
-----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Identification-Number`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Identification-Number/Membership-Number`>/

- Documentation: *For Scottish DEAs only*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Home-Inspector/Identification-Number`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Property:

Property
--------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property`>/

- Documentation2: *A discrete identifiable possession, such as a piece of real-estate, to which its owner has legal title. For the Home Information Pack legislation the types of property are restricted to residential properties. It should be observed that "a property is a property is a property" and all real-estate properties, whether residential or commercial or whether being sold for the first or the nth time will have a very similar conceptual structure and similar rules and constraints. As such the broad description of a Property can be regarded as a framework, containing a set of extension points, that can be expanded as necessary to cover additional detail.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property/UPRN`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property/Site-Reference`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property/Plot-Reference`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address:

Address
-------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address`>/

- Documentation: *Address for the property.*
- Documentation2: *An address is composed of a number of structured elements such as Postcode, Post-Town, Street etc.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Address-Line-1`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Address-Line-2`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Address-Line-3`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Post-Town`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Postcode`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Address-Line-1:

Address-Line-1
--------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Address-Line-1`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Address-Line-2:

Address-Line-2
--------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Address-Line-2`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Address-Line-3:

Address-Line-3
--------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Address-Line-3`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Post-Town:

Post-Town
---------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Post-Town`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Postcode:

Postcode
--------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address/Postcode`>/

- Documentation: *The Postcode for the Address*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property/Address`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Property/UPRN:

UPRN
----

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property/UPRN`>/

- Documentation: *Unique Property Reference Number*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Property/Site-Reference:

Site-Reference
--------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property/Site-Reference`>/

- Documentation: *A site reference*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Property/Plot-Reference:

Plot-Reference
--------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property/Plot-Reference`>/

- Documentation: *A plot reference*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Property`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Region-Code:

Region-Code
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Region-Code`>/

- Documentation: *Region within the UK.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>
- Has text value: *True*
- Codes:
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
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Country-Code:

Country-Code
------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Country-Code`>/

- Documentation: *Country within the UK.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>
- Has text value: *True*
- Codes:
    - **"EAW"** - *England and Wales, for backwards compatibility only.*
    - **"ENG"** - *England*
    - **"WLS"** - *Wales*
    - **"SCT"** - *Scotland*
    - **"NIR"** - *Northern Ireland*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Related-Party-Disclosure:

Related-Party-Disclosure
------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Related-Party-Disclosure`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Related-Party-Disclosure/Related-Party-Disclosure-Text`> <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Related-Party-Disclosure/Related-Party-Disclosure-Number`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Related-Party-Disclosure/Related-Party-Disclosure-Text:

Related-Party-Disclosure-Text
-----------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Related-Party-Disclosure`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Related-Party-Disclosure/Related-Party-Disclosure-Text`>/

- Documentation: *For backward compatibility only.*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Related-Party-Disclosure`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Report-Header/Related-Party-Disclosure/Related-Party-Disclosure-Number:

Related-Party-Disclosure-Number
-------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Related-Party-Disclosure`>/<:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Related-Party-Disclosure/Related-Party-Disclosure-Number`>/

- Documentation: *Code indicating any potential conflicts of interest or commercial relationships with other parties.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Report-Header/Related-Party-Disclosure`>
- Has text value: *True*
- Codes:
    - **"1"** - *No related party*
    - **"2"** - *Relative of homeowner or of occupier of the property*
    - **"3"** - *Residing at the property*
    - **"4"** - *Financial interest in the property*
    - **"5"** - *Owner or Director of the organisation dealing with the property transaction*
    - **"6"** - *Employed by the professional dealing with the property transaction*
    - **"7"** - *Relative of the professional dealing with the property transaction*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment:

Energy-Assessment
-----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/

- Documentation2: *Energy Efficiency Assessment Report is an inspection report whose purpose is to assess the energy efficiency of the inspected property and provide energy ratings for the significant heat-loss features of the property. The report also identifies a number of potential improvements that may be made to the property in order to increase the energy efficiency.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Assessment-Date`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/LZC-Energy-Sources`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Assessment-Date:

Assessment-Date
---------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Assessment-Date`>/

- Documentation: *Date of assessment.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>
- Has text value: *True*
- Data type: *Date string (ISO format)*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary:

Property-Summary
----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Has-Fixed-Air-Conditioning`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Has-Hot-Water-Cylinder`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Has-Heated-Separate-Conservatory`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Dwelling-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Total-Floor-Area`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Multiple-Glazed-Percentage`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Multiple-Glazed-Percentage-NR`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Is-Zero-Carbon-Home`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls:

Walls
-----

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls/Description`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls/Energy-Efficiency-Rating`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls/Environmental-Efficiency-Rating`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *unbounded*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls/Description:

Description
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls/Description`>/

- Documentation: *Overall description of the property feature*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls/Energy-Efficiency-Rating:

Energy-Efficiency-Rating
------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls/Energy-Efficiency-Rating`>/

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls`>
- Has text value: *True*
- Codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls/Environmental-Efficiency-Rating:

Environmental-Efficiency-Rating
-------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls/Environmental-Efficiency-Rating`>/

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Walls`>
- Has text value: *True*
- Codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof:

Roof
----

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof/Description`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof/Energy-Efficiency-Rating`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof/Environmental-Efficiency-Rating`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *unbounded*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof/Description:

Description
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof/Description`>/

- Documentation: *Overall description of the property feature*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof/Energy-Efficiency-Rating:

Energy-Efficiency-Rating
------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof/Energy-Efficiency-Rating`>/

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof`>
- Has text value: *True*
- Codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof/Environmental-Efficiency-Rating:

Environmental-Efficiency-Rating
-------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof/Environmental-Efficiency-Rating`>/

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Roof`>
- Has text value: *True*
- Codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor:

Floor
-----

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor/Description`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor/Energy-Efficiency-Rating`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor/Environmental-Efficiency-Rating`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *unbounded*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor/Description:

Description
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor/Description`>/

- Documentation: *Overall description of the property feature*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor/Energy-Efficiency-Rating:

Energy-Efficiency-Rating
------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor/Energy-Efficiency-Rating`>/

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor`>
- Has text value: *True*
- Codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor/Environmental-Efficiency-Rating:

Environmental-Efficiency-Rating
-------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor/Environmental-Efficiency-Rating`>/

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Floor`>
- Has text value: *True*
- Codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows:

Windows
-------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows/Description`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows/Energy-Efficiency-Rating`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows/Environmental-Efficiency-Rating`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows/Description:

Description
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows/Description`>/

- Documentation: *Overall description of the property feature*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows/Energy-Efficiency-Rating:

Energy-Efficiency-Rating
------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows/Energy-Efficiency-Rating`>/

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows`>
- Has text value: *True*
- Codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows/Environmental-Efficiency-Rating:

Environmental-Efficiency-Rating
-------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows/Environmental-Efficiency-Rating`>/

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Windows`>
- Has text value: *True*
- Codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating:

Main-Heating
------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating/Description`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating/Energy-Efficiency-Rating`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating/Environmental-Efficiency-Rating`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *2*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating/Description:

Description
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating/Description`>/

- Documentation: *Overall description of the property feature*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating/Energy-Efficiency-Rating:

Energy-Efficiency-Rating
------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating/Energy-Efficiency-Rating`>/

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating`>
- Has text value: *True*
- Codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating/Environmental-Efficiency-Rating:

Environmental-Efficiency-Rating
-------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating/Environmental-Efficiency-Rating`>/

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating`>
- Has text value: *True*
- Codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls:

Main-Heating-Controls
---------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls/Description`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls/Energy-Efficiency-Rating`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls/Environmental-Efficiency-Rating`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *2*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls/Description:

Description
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls/Description`>/

- Documentation: *Overall description of the property feature*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls/Energy-Efficiency-Rating:

Energy-Efficiency-Rating
------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls/Energy-Efficiency-Rating`>/

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls`>
- Has text value: *True*
- Codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls/Environmental-Efficiency-Rating:

Environmental-Efficiency-Rating
-------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls/Environmental-Efficiency-Rating`>/

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls`>
- Has text value: *True*
- Codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating:

Secondary-Heating
-----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating/Description`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating/Energy-Efficiency-Rating`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating/Environmental-Efficiency-Rating`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating/Description:

Description
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating/Description`>/

- Documentation: *Overall description of the property feature*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating/Energy-Efficiency-Rating:

Energy-Efficiency-Rating
------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating/Energy-Efficiency-Rating`>/

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating`>
- Has text value: *True*
- Codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating/Environmental-Efficiency-Rating:

Environmental-Efficiency-Rating
-------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating/Environmental-Efficiency-Rating`>/

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating`>
- Has text value: *True*
- Codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water:

Hot-Water
---------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water/Description`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water/Energy-Efficiency-Rating`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water/Environmental-Efficiency-Rating`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water/Description:

Description
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water/Description`>/

- Documentation: *Overall description of the property feature*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water/Energy-Efficiency-Rating:

Energy-Efficiency-Rating
------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water/Energy-Efficiency-Rating`>/

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water`>
- Has text value: *True*
- Codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water/Environmental-Efficiency-Rating:

Environmental-Efficiency-Rating
-------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water/Environmental-Efficiency-Rating`>/

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Hot-Water`>
- Has text value: *True*
- Codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting:

Lighting
--------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting/Description`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting/Energy-Efficiency-Rating`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting/Environmental-Efficiency-Rating`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting/Description:

Description
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting/Description`>/

- Documentation: *Overall description of the property feature*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting/Energy-Efficiency-Rating:

Energy-Efficiency-Rating
------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting/Energy-Efficiency-Rating`>/

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting`>
- Has text value: *True*
- Codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting/Environmental-Efficiency-Rating:

Environmental-Efficiency-Rating
-------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting/Environmental-Efficiency-Rating`>/

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Lighting`>
- Has text value: *True*
- Codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness:

Air-Tightness
-------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness/Description`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness/Energy-Efficiency-Rating`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness/Environmental-Efficiency-Rating`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness/Description:

Description
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness/Description`>/

- Documentation: *Overall description of the property feature*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness/Energy-Efficiency-Rating:

Energy-Efficiency-Rating
------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness/Energy-Efficiency-Rating`>/

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness`>
- Has text value: *True*
- Codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness/Environmental-Efficiency-Rating:

Environmental-Efficiency-Rating
-------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness/Environmental-Efficiency-Rating`>/

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Air-Tightness`>
- Has text value: *True*
- Codes:
    - **"0"** - *N/A*
    - **"1"** - *Very Poor*
    - **"2"** - *Poor*
    - **"3"** - *Average*
    - **"4"** - *Good*
    - **"5"** - *Very Good*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Has-Fixed-Air-Conditioning:

Has-Fixed-Air-Conditioning
--------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Has-Fixed-Air-Conditioning`>/

- Documentation: *Fixed air conditioning?*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Has-Hot-Water-Cylinder:

Has-Hot-Water-Cylinder
----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Has-Hot-Water-Cylinder`>/

- Documentation: *Hot water cylinder?*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Has-Heated-Separate-Conservatory:

Has-Heated-Separate-Conservatory
--------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Has-Heated-Separate-Conservatory`>/

- Documentation: *Heated separate conservatory?*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Dwelling-Type:

Dwelling-Type
-------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Dwelling-Type`>/

- Documentation: *Is a string such as Detached house or Top-floor flat*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Total-Floor-Area:

Total-Floor-Area
----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Total-Floor-Area`>/

- Documentation: *Is a number such as 125*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Multiple-Glazed-Percentage:

Multiple-Glazed-Percentage
--------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Multiple-Glazed-Percentage`>/

- Documentation: *Fraction of windows that are multiply glazed to nearest 1%.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Multiple-Glazed-Percentage-NR:

Multiple-Glazed-Percentage-NR
-----------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Multiple-Glazed-Percentage-NR`>/

- Documentation: *For backward compatibility only, do not use.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Is-Zero-Carbon-Home:

Is-Zero-Carbon-Home
-------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary/Is-Zero-Carbon-Home`>/

- Documentation: *Is dwelling a Zero Carbon Home?*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Property-Summary`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use:

Energy-Use
----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>/

- Documentation: *Calculated results from the energy assessment.*
- Documentation2: *Part of an Energy Report summarising the results of the various energy calculations made by the Home Inspector.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/DER`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/TER`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/DPER`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/TPER`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/DFEE`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/TFEE`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Rating-Current`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Rating-Potential`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Rating-Average`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Environmental-Impact-Current`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Environmental-Impact-Potential`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Consumption-Current`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Consumption-Potential`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/CO2-Emissions-Current`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/CO2-Emissions-Current-Per-Floor-Area`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/CO2-Emissions-Potential`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Lighting-Cost-Current`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Lighting-Cost-Potential`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Heating-Cost-Current`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Heating-Cost-Potential`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Hot-Water-Cost-Current`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Hot-Water-Cost-Potential`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/DER:

DER
---

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/DER`>/

- Documentation: *The DER of the Property*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/TER:

TER
---

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/TER`>/

- Documentation: *The TER of the Property*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/DPER:

DPER
----

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/DPER`>/

- Documentation: *The DPER of the Property*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/TPER:

TPER
----

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/TPER`>/

- Documentation: *The TPER of the Property*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/DFEE:

DFEE
----

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/DFEE`>/

- Documentation: *The DFEE of the Property*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/TFEE:

TFEE
----

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/TFEE`>/

- Documentation: *The TFEE of the Property*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Rating-Current:

Energy-Rating-Current
---------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Rating-Current`>/

- Documentation: *The Current Energy Rating of the Property*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Rating-Potential:

Energy-Rating-Potential
-----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Rating-Potential`>/

- Documentation: *The overall Energy Rating for the Property being assessed.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Rating-Average:

Energy-Rating-Average
---------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Rating-Average`>/

- Documentation: *Average SAP rating for the country concerned. 0 if unknown or not applicable*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Environmental-Impact-Current:

Environmental-Impact-Current
----------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Environmental-Impact-Current`>/

- Documentation: *The estimated current Environmental Impact Rating of the property*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Environmental-Impact-Potential:

Environmental-Impact-Potential
------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Environmental-Impact-Potential`>/

- Documentation: *The estimated potential Environmental Impact Rating of the property*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Consumption-Current:

Energy-Consumption-Current
--------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Consumption-Current`>/

- Documentation: *Estimated total energy consumption for the Property in a 12 month period. Value is Kilowatt Hours per Square Metre (kWh/m2)*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Consumption-Potential:

Energy-Consumption-Potential
----------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Energy-Consumption-Potential`>/

- Documentation: *Estimated total energy consumption for the Property in a 12 month period. Value is Kilowatt Hours per Square Metre (kWh/m2)*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/CO2-Emissions-Current:

CO2-Emissions-Current
---------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/CO2-Emissions-Current`>/

- Documentation: *CO2 emissions per year in tonnes/year.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/CO2-Emissions-Current-Per-Floor-Area:

CO2-Emissions-Current-Per-Floor-Area
------------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/CO2-Emissions-Current-Per-Floor-Area`>/

- Documentation: *CO2 emissions per square metre floor area per year in kg/m2.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/CO2-Emissions-Potential:

CO2-Emissions-Potential
-----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/CO2-Emissions-Potential`>/

- Documentation: *Estimated value in Tonnes per Year of the total CO2 emissions produced by the Property in 12 month period.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Lighting-Cost-Current:

Lighting-Cost-Current
---------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Lighting-Cost-Current`>/

- Documentation: *The current estimated cost of Lighting for the property*
- Documentation2: *Extension of a Decimal value for use with monetary values where a currency code needs to be specified. The currency code is actually metadata about the value so, in line with good XML practice, the Currency Code is declared as an XML-Attribute of the Money datatype rather than as a separate XML-Element. The currency attribute should then include a list of valid currencies codes that are supported.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Lighting-Cost-Potential:

Lighting-Cost-Potential
-----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Lighting-Cost-Potential`>/

- Documentation: *The current estimated cost of Lighting for the property*
- Documentation2: *Extension of a Decimal value for use with monetary values where a currency code needs to be specified. The currency code is actually metadata about the value so, in line with good XML practice, the Currency Code is declared as an XML-Attribute of the Money datatype rather than as a separate XML-Element. The currency attribute should then include a list of valid currencies codes that are supported.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Heating-Cost-Current:

Heating-Cost-Current
--------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Heating-Cost-Current`>/

- Documentation: *The current estimated cost of Heating for the property*
- Documentation2: *Extension of a Decimal value for use with monetary values where a currency code needs to be specified. The currency code is actually metadata about the value so, in line with good XML practice, the Currency Code is declared as an XML-Attribute of the Money datatype rather than as a separate XML-Element. The currency attribute should then include a list of valid currencies codes that are supported.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Heating-Cost-Potential:

Heating-Cost-Potential
----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Heating-Cost-Potential`>/

- Documentation: *The current estimated cost of Heating for the property*
- Documentation2: *Extension of a Decimal value for use with monetary values where a currency code needs to be specified. The currency code is actually metadata about the value so, in line with good XML practice, the Currency Code is declared as an XML-Attribute of the Money datatype rather than as a separate XML-Element. The currency attribute should then include a list of valid currencies codes that are supported.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Hot-Water-Cost-Current:

Hot-Water-Cost-Current
----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Hot-Water-Cost-Current`>/

- Documentation: *|The current estimated cost of Hot Water for the property*
- Documentation2: *Extension of a Decimal value for use with monetary values where a currency code needs to be specified. The currency code is actually metadata about the value so, in line with good XML practice, the Currency Code is declared as an XML-Attribute of the Money datatype rather than as a separate XML-Element. The currency attribute should then include a list of valid currencies codes that are supported.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Hot-Water-Cost-Potential:

Hot-Water-Cost-Potential
------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use/Hot-Water-Cost-Potential`>/

- Documentation: *|The current estimated cost of Hot Water for the property*
- Documentation2: *Extension of a Decimal value for use with monetary values where a currency code needs to be specified. The currency code is actually metadata about the value so, in line with good XML practice, the Currency Code is declared as an XML-Attribute of the Money datatype rather than as a separate XML-Element. The currency attribute should then include a list of valid currencies codes that are supported.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements:

Suggested-Improvements
----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements`>/

- Documentation: *Improvement measures listed on the EPC.*
- Documentation2: *Part of an Energy Report that describes the a set of improvements that the Home Inspector considers would contribute to the overall energy rating of the property.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement:

Improvement
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Sequence`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Category`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Typical-Saving`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Energy-Performance-Rating`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Environmental-Impact-Rating`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Indicative-Cost`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Green-Deal-Category`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *unbounded*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Sequence:

Sequence
--------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Sequence`>/

- Documentation: *Sequence of the Suggested Improvements within the set of Suggested Improvements. This is used to order the Recommendations on the output HCR / EPC so that the cumulative Ratings make sense. The Improved Energy Ratings that result from carrying out a Suggested Improvement are cumulative and assume that the improvements have been installed in the order they appear in the list. Hence they must be sequenced.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Category:

Improvement-Category
--------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Category`>/

- Documentation: *The category of improvement. This identifies where on the report the recommendation is printed.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>
- Has text value: *True*
- Codes:
    - **"1"** - *Lower cost - this is for backwards compatibility only and should not be used*
    - **"2"** - *Higher cost - this is for backwards compatibility only and should not be used*
    - **"3"** - *Further measure - this is for backwards compatibility only and should not be used*
    - **"4"** - *Deselected. This is for backwards compatibility only and should not be used.*
    - **"5"** - *Normal measure*
    - **"6"** - *Alternative measure*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Type:

Improvement-Type
----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Type`>/

- Documentation: *Suggested work to be carried out on the Property to improve its energy efficiency. This should be a enumerated list of acceptable improvements but it hasn't yet been defined.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>
- Has text value: *True*
- Codes:
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
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Typical-Saving:

Typical-Saving
--------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Typical-Saving`>/

- Documentation: *Typical savings (in British Pounds) per year if the suggested improvement is carried out. 0 if not assessed*
- Documentation2: *Extension of a Decimal value for use with monetary values where a currency code needs to be specified. The currency code is actually metadata about the value so, in line with good XML practice, the Currency Code is declared as an XML-Attribute of the Money datatype rather than as a separate XML-Element. The currency attribute should then include a list of valid currencies codes that are supported.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Energy-Performance-Rating:

Energy-Performance-Rating
-------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Energy-Performance-Rating`>/

- Documentation: *The estimated Energy performance rating of the Property after the Suggested Improvement has been carried out providing any preceding Suggested Improvement has also been carried out. 0 if not assessed*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Environmental-Impact-Rating:

Environmental-Impact-Rating
---------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Environmental-Impact-Rating`>/

- Documentation: *The estimated Environmental Impact rating of the Property after the Suggested Improvement has been carried out providing any preceding Suggested Improvement has also been carried out. 0 if not assessed*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details:

Improvement-Details
-------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Number`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts:

Improvement-Texts
-----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts`>/

- Documentation: *For backward compatability only*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Summary`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Heading`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Description`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Summary:

Improvement-Summary
-------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Summary`>/

- Documentation: *A short description of the suggested improvement.*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Heading:

Improvement-Heading
-------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Heading`>/

- Documentation: *Text to precede the improvement description. If this field is not provided the 'Improvement-Summary' is used instead.*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Description:

Improvement-Description
-----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Description`>/

- Documentation: *Detailed description of the suggested improvement.*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Number:

Improvement-Number
------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Number`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details`>
- Has text value: *True*
- Codes:
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
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Indicative-Cost:

Indicative-Cost
---------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Indicative-Cost`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Green-Deal-Category:

Green-Deal-Category
-------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Green-Deal-Category`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>
- Has text value: *True*
- Codes:
    - **"1"** - *1. Not eligible for Green Deal*
    - **"2"** - *2. Eligible with additional finance*
    - **"3"** - *3. Eligible without additional finance*
    - **"NI"** - *Not assessed. Use for alternative measures and for new dwelling EPCs*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/LZC-Energy-Sources:

LZC-Energy-Sources
------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/LZC-Energy-Sources`>/

- Documentation2: *Details of low and zero carbon energy source(s) for the property, if any.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/LZC-Energy-Sources/LZC-Energy-Source`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/LZC-Energy-Sources/LZC-Energy-Source:

LZC-Energy-Source
-----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/LZC-Energy-Sources`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/LZC-Energy-Sources/LZC-Energy-Source`>/

- Documentation: *Low and zero carbon energy source(s) for the property.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/LZC-Energy-Sources`>
- Has text value: *True*
- Codes:
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
- Minimum occurrence: *1*
- Maximum occurrence: *unbounded*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive:

Renewable-Heat-Incentive
------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-New-Dwelling`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-New-Dwelling:

RHI-New-Dwelling
----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-New-Dwelling`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-New-Dwelling/Space-Heating`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-New-Dwelling/Water-Heating`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-New-Dwelling/Space-Heating:

Space-Heating
-------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-New-Dwelling`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-New-Dwelling/Space-Heating`>/

- Documentation: *Space heating requirement.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-New-Dwelling`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-New-Dwelling/Water-Heating:

Water-Heating
-------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-New-Dwelling`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-New-Dwelling/Water-Heating`>/

- Documentation: *Water heating requirement.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-New-Dwelling`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling:

RHI-Existing-Dwelling
---------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Space-Heating-Existing-Dwelling`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Space-Heating-With-Loft-Insulation`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Space-Heating-With-Cavity-Insulation`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Space-Heating-With-Loft-And-Cavity-Insulation`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Water-Heating`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Impact-Of-Loft-Insulation`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Impact-Of-Cavity-Insulation`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Impact-Of-Solid-Wall-Insulation`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Space-Heating-Existing-Dwelling:

Space-Heating-Existing-Dwelling
-------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Space-Heating-Existing-Dwelling`>/

- Documentation: *Space heating requirement for existing dwelling.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Space-Heating-With-Loft-Insulation:

Space-Heating-With-Loft-Insulation
----------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Space-Heating-With-Loft-Insulation`>/

- Documentation: *Space heating requirement after implementation of loft insulation recommendation, omit if loft insulation not recommended. For backwards compatibility only, do not use*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Space-Heating-With-Cavity-Insulation:

Space-Heating-With-Cavity-Insulation
------------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Space-Heating-With-Cavity-Insulation`>/

- Documentation: *Space heating requirement after implementation of cavity insulation recommendation, omit if cavity insulation not recommended. For backwards compatibility only, do not use*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Space-Heating-With-Loft-And-Cavity-Insulation:

Space-Heating-With-Loft-And-Cavity-Insulation
---------------------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Space-Heating-With-Loft-And-Cavity-Insulation`>/

- Documentation: *Space heating requirement after implementation of loft and cavity insulation recommendations, same as existing dwelling if neither is recommended. For backwards compatibility only, do not use*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Water-Heating:

Water-Heating
-------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Water-Heating`>/

- Documentation: *Water heating requirement.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Impact-Of-Loft-Insulation:

Impact-Of-Loft-Insulation
-------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Impact-Of-Loft-Insulation`>/

- Documentation: *Reduction in space heating requirement with loft insulation (as negative value). Omit if not applicable*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Impact-Of-Cavity-Insulation:

Impact-Of-Cavity-Insulation
---------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Impact-Of-Cavity-Insulation`>/

- Documentation: *Reduction in space heating requirement with cavity insulation (as negative value). Omit if not applicable*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Impact-Of-Solid-Wall-Insulation:

Impact-Of-Solid-Wall-Insulation
-------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling/Impact-Of-Solid-Wall-Insulation`>/

- Documentation: *Reduction in space heating requirement with solid wall insulation (as negative value). Omit if not applicable*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Renewable-Heat-Incentive/RHI-Existing-Dwelling`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package:

Green-Deal-Package
------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package`>/

- Documentation: *Improvements that can form a Green Deal package*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Electricity-Saving`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Gas-Saving`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Other-Fuel-Saving`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement:

Green-Deal-Improvement
----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement`>/

- Documentation: *Improvements from Suggested-Improvements in the Green Deal package*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement/Improvement-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement/Improvement-Number`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *unbounded*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement/Improvement-Type:

Improvement-Type
----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement/Improvement-Type`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement`>
- Has text value: *True*
- Codes:
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
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement/Improvement-Number:

Improvement-Number
------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement/Improvement-Number`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement`>
- Has text value: *True*
- Codes:
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
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Electricity-Saving:

Electricity-Saving
------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Electricity-Saving`>/

- Documentation: *Total electricity saving for the package*
- Documentation2: *Extension of a Decimal value for use with monetary values where a currency code needs to be specified. The currency code is actually metadata about the value so, in line with good XML practice, the Currency Code is declared as an XML-Attribute of the Money datatype rather than as a separate XML-Element. The currency attribute should then include a list of valid currencies codes that are supported.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Gas-Saving:

Gas-Saving
----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Gas-Saving`>/

- Documentation: *Total gas saving for the package*
- Documentation2: *Extension of a Decimal value for use with monetary values where a currency code needs to be specified. The currency code is actually metadata about the value so, in line with good XML practice, the Currency Code is declared as an XML-Attribute of the Money datatype rather than as a separate XML-Element. The currency attribute should then include a list of valid currencies codes that are supported.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Other-Fuel-Saving:

Other-Fuel-Saving
-----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package/Other-Fuel-Saving`>/

- Documentation: *Total other saving for the package*
- Documentation2: *Extension of a Decimal value for use with monetary values where a currency code needs to be specified. The currency code is actually metadata about the value so, in line with good XML practice, the Currency Code is declared as an XML-Attribute of the Money datatype rather than as a separate XML-Element. The currency attribute should then include a list of valid currencies codes that are supported.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Green-Deal-Package`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements:

Alternative-Improvements
------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements`>/

- Documentation: *Alternative improvements to some of those given in Suggested-Improvements*
- Documentation2: *Part of an Energy Report that describes the a set of improvements that the Home Inspector considers would contribute to the overall energy rating of the property.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement:

Improvement
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Sequence`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Category`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Typical-Saving`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Energy-Performance-Rating`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Environmental-Impact-Rating`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Indicative-Cost`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Green-Deal-Category`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *unbounded*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Sequence:

Sequence
--------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Sequence`>/

- Documentation: *Sequence of the Suggested Improvements within the set of Suggested Improvements. This is used to order the Recommendations on the output HCR / EPC so that the cumulative Ratings make sense. The Improved Energy Ratings that result from carrying out a Suggested Improvement are cumulative and assume that the improvements have been installed in the order they appear in the list. Hence they must be sequenced.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Category:

Improvement-Category
--------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Category`>/

- Documentation: *The category of improvement. This identifies where on the report the recommendation is printed.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>
- Has text value: *True*
- Codes:
    - **"1"** - *Lower cost - this is for backwards compatibility only and should not be used*
    - **"2"** - *Higher cost - this is for backwards compatibility only and should not be used*
    - **"3"** - *Further measure - this is for backwards compatibility only and should not be used*
    - **"4"** - *Deselected. This is for backwards compatibility only and should not be used.*
    - **"5"** - *Normal measure*
    - **"6"** - *Alternative measure*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Type:

Improvement-Type
----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Type`>/

- Documentation: *Suggested work to be carried out on the Property to improve its energy efficiency. This should be a enumerated list of acceptable improvements but it hasn't yet been defined.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>
- Has text value: *True*
- Codes:
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
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Typical-Saving:

Typical-Saving
--------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Typical-Saving`>/

- Documentation: *Typical savings (in British Pounds) per year if the suggested improvement is carried out. 0 if not assessed*
- Documentation2: *Extension of a Decimal value for use with monetary values where a currency code needs to be specified. The currency code is actually metadata about the value so, in line with good XML practice, the Currency Code is declared as an XML-Attribute of the Money datatype rather than as a separate XML-Element. The currency attribute should then include a list of valid currencies codes that are supported.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Energy-Performance-Rating:

Energy-Performance-Rating
-------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Energy-Performance-Rating`>/

- Documentation: *The estimated Energy performance rating of the Property after the Suggested Improvement has been carried out providing any preceding Suggested Improvement has also been carried out. 0 if not assessed*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Environmental-Impact-Rating:

Environmental-Impact-Rating
---------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Environmental-Impact-Rating`>/

- Documentation: *The estimated Environmental Impact rating of the Property after the Suggested Improvement has been carried out providing any preceding Suggested Improvement has also been carried out. 0 if not assessed*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details:

Improvement-Details
-------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Number`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts:

Improvement-Texts
-----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts`>/

- Documentation: *For backward compatability only*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Summary`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Heading`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Description`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Summary:

Improvement-Summary
-------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Summary`>/

- Documentation: *A short description of the suggested improvement.*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Heading:

Improvement-Heading
-------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Heading`>/

- Documentation: *Text to precede the improvement description. If this field is not provided the 'Improvement-Summary' is used instead.*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Description:

Improvement-Description
-----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Description`>/

- Documentation: *Detailed description of the suggested improvement.*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Number:

Improvement-Number
------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Number`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details`>
- Has text value: *True*
- Codes:
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
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Indicative-Cost:

Indicative-Cost
---------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Indicative-Cost`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Green-Deal-Category:

Green-Deal-Category
-------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Green-Deal-Category`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>
- Has text value: *True*
- Codes:
    - **"1"** - *1. Not eligible for Green Deal*
    - **"2"** - *2. Eligible with additional finance*
    - **"3"** - *3. Eligible without additional finance*
    - **"NI"** - *Not assessed. Use for alternative measures and for new dwelling EPCs*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum:

Addendum
--------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/Cavity-Fill-Recommended`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/Stone-Walls`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/System-Build`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/Access-Issues`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/High-Exposure`> <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/Narrow-Cavities`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/Cavity-Fill-Recommended:

Cavity-Fill-Recommended
-----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/Cavity-Fill-Recommended`>/

- Documentation: *Cavity fill is recommended*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/Stone-Walls:

Stone-Walls
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/Stone-Walls`>/

- Documentation: *Stone walls present, not insulated*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/System-Build:

System-Build
------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/System-Build`>/

- Documentation: *System build present*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/Access-Issues:

Access-Issues
-------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/Access-Issues`>/

- Documentation: *Dwelling has access issues for cavity wall insulation. Include only when at least one of Cavity-Fill-Recommended, Stone-Walls, System-Build is also present*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/High-Exposure:

High-Exposure
-------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/High-Exposure`>/

- Documentation: *Dwelling may be exposed to wind-driven rain. Include only when at least one of Cavity-Fill-Recommended, Stone-Walls, System-Build is also present*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/Narrow-Cavities:

Narrow-Cavities
---------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum`>/<:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum/Narrow-Cavities`>/

- Documentation: *Dwelling may have narrow cavities. Include only when Cavity-Fill-Recommended is also present*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Energy-Assessment/Addendum`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data:

SAP10-Data
----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/

- Documentation2: *These are the specific data-items collected by the HI / EA needed to perform the SAP calculation.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/Data-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/Data-Type:

Data-Type
---------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/Data-Type`>/

- Documentation: *Type of SAP data that has been collected.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>
- Has text value: *True*
- Codes:
    - **"1"** - *new dwelling as designed*
    - **"2"** - *new dwelling as built*
    - **"3"** - *new extension to existing dwelling*
    - **"4"** - *new dwelling created by change of use*
    - **"5"** - *existing dwelling*
    - **"6"** - *other*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details:

SAP-Property-Details
--------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/

- Documentation2: *Various measurements a particular Property.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Property-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Built-Form`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Living-Area`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Lowest-Storey-Area`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Orientation`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Conservatory-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Terrain-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Has-Special-Feature`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Special-Feature-Description`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Energy-Saved-Or-Generated`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Saved-Or-Generated-Fuel`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Energy-Used`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Energy-Used-Fuel`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Is-In-Smoke-Control-Area`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Cold-Water-Source`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Windows-Overshading`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Thermal-Mass-Parameter`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Additional-Allowable-Electricity-Generation`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Gas-Smart-Meter-Present`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Electricity-Smart-Meter-Present`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Is-Dwelling-Export-Capable`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/PV-Connection`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/PV-Diverter`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Battery-Capacity`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Is-Wind-Turbine-Connected-To-Dwelling-Meter`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Deselected-Improvements`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Flat-Details`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Design-Water-Use`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Property-Type:

Property-Type
-------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Property-Type`>/

- Documentation: *The type of Property, such as House, Flat, Mansion, Maisonette etc.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Has text value: *True*
- Codes:
    - **"0"** - *House*
    - **"1"** - *Bungalow*
    - **"2"** - *Flat*
    - **"3"** - *Maisonette*
    - **"4"** - *Park home*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Built-Form:

Built-Form
----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Built-Form`>/

- Documentation: *The building type of the Property e.g. Detached, Semi-Detached, Terrace etc. Together with the Property Type, the Built Form provides a structured description of the property.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Has text value: *True*
- Codes:
    - **"1"** - *Detached*
    - **"2"** - *Semi-Detached*
    - **"3"** - *End-Terrace*
    - **"4"** - *Mid-Terrace*
    - **"5"** - *Enclosed End-Terrace*
    - **"6"** - *Enclosed Mid-Terrace*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Living-Area:

Living-Area
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Living-Area`>/

- Documentation: *The size of the living area in square metres. The living area is the room marked on a plan as the lounge or living room, or the largest public room (irrespective of usage by particular occupants), together with any rooms not separated from the lounge or living room by doors, and including any cupboards directly accessed from the lounge or living room. Living area does not, however, extend over more than one storey, even when stairs enter the living area directly.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Lowest-Storey-Area:

Lowest-Storey-Area
------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Lowest-Storey-Area`>/

- Documentation: *The Area of the lowest storey in square meters including unheated or communal areas such as garages or corridors.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Orientation:

Orientation
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Orientation`>/

- Documentation: *The orientation of the front of the property.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Has text value: *True*
- Codes:
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
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Conservatory-Type:

Conservatory-Type
-----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Conservatory-Type`>/

- Documentation: *Type of conservatory.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Has text value: *True*
- Codes:
    - **"1"** - *no conservatory*
    - **"2"** - *separated unheated conservatory*
    - **"3"** - *separated heated conservatory*
    - **"4"** - *not separated*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Terrain-Type:

Terrain-Type
------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Terrain-Type`>/

- Documentation: *Terrain type. Needed for wind-turbines and for applying measures.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Has text value: *True*
- Codes:
    - **"1"** - *urban*
    - **"2"** - *suburban*
    - **"3"** - *rural*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Has-Special-Feature:

Has-Special-Feature
-------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Has-Special-Feature`>/

- Documentation: *For backwards compatibility only, do not use.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Special-Feature-Description:

Special-Feature-Description
---------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Special-Feature-Description`>/

- Documentation: *For backwards compatibility only, do not use.*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Energy-Saved-Or-Generated:

Energy-Saved-Or-Generated
-------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Energy-Saved-Or-Generated`>/

- Documentation: *For backwards compatibility only, do not use.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Saved-Or-Generated-Fuel:

Saved-Or-Generated-Fuel
-----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Saved-Or-Generated-Fuel`>/

- Documentation: *For backwards compatibility only, do not use.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Has text value: *True*
- Codes:
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
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Energy-Used:

Energy-Used
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Energy-Used`>/

- Documentation: *For backwards compatibility only, do not use.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Energy-Used-Fuel:

Energy-Used-Fuel
----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Energy-Used-Fuel`>/

- Documentation: *For backwards compatibility only, do not use.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Has text value: *True*
- Codes:
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
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Is-In-Smoke-Control-Area:

Is-In-Smoke-Control-Area
------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Is-In-Smoke-Control-Area`>/

- Documentation: *Is property in a smoke control area? Only if a solid fuel appliance is used.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Has text value: *True*
- Codes:
    - **"false"** - **
    - **"true"** - **
    - **"unknown"** - **
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Cold-Water-Source:

Cold-Water-Source
-----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Cold-Water-Source`>/

- Documentation: *What is the cold water source? Either mains or header tank.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Has text value: *True*
- Codes:
    - **"1"** - *mains*
    - **"2"** - *header tank*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Windows-Overshading:

Windows-Overshading
-------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Windows-Overshading`>/

- Documentation: *Average amount of overshading of windows.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Has text value: *True*
- Codes:
    - **"1"** - *very little*
    - **"2"** - *average or unknown*
    - **"3"** - *more than average*
    - **"4"** - *heavy*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Thermal-Mass-Parameter:

Thermal-Mass-Parameter
----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Thermal-Mass-Parameter`>/

- Documentation: *Average thermal mass parameter for the dwelling in kJ/m2K. If omitted it is calculated using the kappa values of each element.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Additional-Allowable-Electricity-Generation:

Additional-Allowable-Electricity-Generation
-------------------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Additional-Allowable-Electricity-Generation`>/

- Documentation: *Additional allowable electricity generation applicable to this dwelling in kWh per square metre; only if Zero Carbon Home assessment.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Gas-Smart-Meter-Present:

Gas-Smart-Meter-Present
-----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Gas-Smart-Meter-Present`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Electricity-Smart-Meter-Present:

Electricity-Smart-Meter-Present
-------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Electricity-Smart-Meter-Present`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Is-Dwelling-Export-Capable:

Is-Dwelling-Export-Capable
--------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Is-Dwelling-Export-Capable`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/PV-Connection:

PV-Connection
-------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/PV-Connection`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Has text value: *True*
- Codes:
    - **"0"** - *not applicable (FGHRS)*
    - **"1"** - *not connected to dwelling's electricity meter*
    - **"2"** - *connected to dwelling's electricity meter*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/PV-Diverter:

PV-Diverter
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/PV-Diverter`>/

- Documentation: *Diverter present.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Battery-Capacity:

Battery-Capacity
----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Battery-Capacity`>/

- Documentation: *Battery capacity if diverter present.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Is-Wind-Turbine-Connected-To-Dwelling-Meter:

Is-Wind-Turbine-Connected-To-Dwelling-Meter
-------------------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Is-Wind-Turbine-Connected-To-Dwelling-Meter`>/

- Documentation: *Whether the wind turbine is connected to the Dwelling's meter.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating:

SAP-Heating
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/

- Documentation2: *Details of the means by which the Main Building is heated.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Water-Heating-Code`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Water-Fuel-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Has-Hot-Water-Cylinder`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Category`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Data-Source`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Efficiency`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Commisioning-Certificate`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Installation-Engineer`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Code`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Fuel-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-PCDF-Fuel-Index`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Flue-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Thermal-Store`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Has-Fixed-Air-Conditioning`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Immersion-Heating-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Heat-Pump-Assisted-By-Immersion`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Heat-Pump-Installed-To-MIS`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Immersion-For-Summer-Use`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Secondary-Heating-HETAS-Approved`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Manufacturer`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Model`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Commissioning-Certificate`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Installer-Engineer-Registration`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Size`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Heat-Transfer-Area`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Heat-Loss-Source`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Heat-Loss`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Insulation-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Insulation-Thickness`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Thermal-Store-Near-Boiler`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Thermal-Store-Or-CPSU-In-Airing-Cupboard`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Has-Cylinder-Thermostat`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Cylinder-In-Heated-Space`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Hot-Water-Separately-Timed`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Controls-Manufacturer`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Controls-Model`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Heating-Design-Water-Use`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Systems-Interaction`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Primary-Pipework-Insulation`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Number-Baths`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Number-Baths-WWHRS`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Water-Heating-Code:

Water-Heating-Code
------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Water-Heating-Code`>/

- Documentation: *The type of Water Heating present in the Property.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Water-Fuel-Type:

Water-Fuel-Type
---------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Water-Fuel-Type`>/

- Documentation: *The type of fuel used to power the central heating e.g. Gas, Electricity. Not used if water system is main or secondary system.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Codes:
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
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Has-Hot-Water-Cylinder:

Has-Hot-Water-Cylinder
----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Has-Hot-Water-Cylinder`>/

- Documentation: *Hot water cylinder?*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Category:

Secondary-Heating-Category
--------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Category`>/

- Documentation: *Category of heating system for the secondary heating system.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Codes:
    - **"1"** - *none*
    - **"10"** - *room heaters*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Data-Source:

Secondary-Heating-Data-Source
-----------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Data-Source`>/

- Documentation: *Source of secondary heating system data; only if secondary heating system.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Codes:
    - **"2"** - *from manufacturer declaration*
    - **"3"** - *from SAP table*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Efficiency:

Secondary-Heating-Efficiency
----------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Efficiency`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Commisioning-Certificate:

Secondary-Heating-Commisioning-Certificate
------------------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Commisioning-Certificate`>/

- Documentation: *Secondary heating system commisioning certificate number.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Installation-Engineer:

Secondary-Heating-Installation-Engineer
---------------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Installation-Engineer`>/

- Documentation: *Secondary heating installation engineer registration reference.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Code:

Secondary-Heating-Code
----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Code`>/

- Documentation: *Type of secondary heating present in the property; only if required and if heating data source is SAP table.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Fuel-Type:

Secondary-Fuel-Type
-------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Fuel-Type`>/

- Documentation: *The type of fuel used to power the secondary heating e.g. Gas, Electricity; only if required.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Codes:
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
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-PCDF-Fuel-Index:

Secondary-Heating-PCDF-Fuel-Index
---------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-PCDF-Fuel-Index`>/

- Documentation: *PCDF index number of the fuel type, only if Secondary-Fuel-Type is 99 (fuel from database).*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Flue-Type:

Secondary-Heating-Flue-Type
---------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Flue-Type`>/

- Documentation: *Secondary flue type; only if secondary efficiency is manufacturer declaration and if there is a flue.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Codes:
    - **"1"** - *open flue*
    - **"2"** - *balanced flue*
    - **"3"** - *chimney*
    - **"4"** - *omitted (boiler is in an outhouse, so its flue arrangements are not relevant)*
    - **"5"** - *unknown (there is a flue, but its type could not be determined)*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Thermal-Store:

Thermal-Store
-------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Thermal-Store`>/

- Documentation: *The type of thermal store; not used if main heating system is community heating scheme.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Codes:
    - **"1"** - *none*
    - **"2"** - *hot water only*
    - **"3"** - *integrated*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Has-Fixed-Air-Conditioning:

Has-Fixed-Air-Conditioning
--------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Has-Fixed-Air-Conditioning`>/

- Documentation: *Fixed air conditioning?*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Immersion-Heating-Type:

Immersion-Heating-Type
----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Immersion-Heating-Type`>/

- Documentation: *The type of immersion heating; only if immersion.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Codes:
    - **"1"** - *Dual*
    - **"2"** - *Single*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Heat-Pump-Assisted-By-Immersion:

Is-Heat-Pump-Assisted-By-Immersion
----------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Heat-Pump-Assisted-By-Immersion`>/

- Documentation: *Is heat pump assisted by immersion? Applicable only to hot water only heat pumps*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Heat-Pump-Installed-To-MIS:

Is-Heat-Pump-Installed-To-MIS
-----------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Heat-Pump-Installed-To-MIS`>/

- Documentation: *Is heat pump installed to MIS standard? Only if water heating from hot water only heat pump.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Immersion-For-Summer-Use:

Is-Immersion-For-Summer-Use
---------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Immersion-For-Summer-Use`>/

- Documentation: *Immersion for summer use? Only if main heating is solid fuel fire or room heater with boiler.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Secondary-Heating-HETAS-Approved:

Is-Secondary-Heating-HETAS-Approved
-----------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Secondary-Heating-HETAS-Approved`>/

- Documentation: *Secondary heating appliance is HETAS approved? Only if solid fuel.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Manufacturer:

Hot-Water-Store-Manufacturer
----------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Manufacturer`>/

- Documentation: *Store Manufacturer name.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Model:

Hot-Water-Store-Model
---------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Model`>/

- Documentation: *Store Model name.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Commissioning-Certificate:

Hot-Water-Store-Commissioning-Certificate
-----------------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Commissioning-Certificate`>/

- Documentation: *Store comissioning certificate number.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Installer-Engineer-Registration:

Hot-Water-Store-Installer-Engineer-Registration
-----------------------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Installer-Engineer-Registration`>/

- Documentation: *Store installer engineer registration number.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Size:

Hot-Water-Store-Size
--------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Size`>/

- Documentation: *Hot water store size in litres; if there is a hot water store. Store refers to hot water store type which can be cylinder (if thermal store is "none"), hot-water only thermal store or integrated thermal store. Not applicable if (a) combi boiler whose data source database or (b) instantaneous combi boiler or (c) combi boiler from SAP table or (d) instantaneous water heater.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Heat-Transfer-Area:

Hot-Water-Store-Heat-Transfer-Area
----------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Heat-Transfer-Area`>/

- Documentation: *Used when a heat pump is associated with a separate and specified hot water vessel.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Heat-Loss-Source:

Hot-Water-Store-Heat-Loss-Source
--------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Heat-Loss-Source`>/

- Documentation: *The source of the hot water store heat loss information; if there is a hot water store. Not applicable if (a) combi boiler whose data source database or (b) instantaneous combi boiler or (c) combi boiler from SAP table or (d) instantaneous water heater.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Codes:
    - **"2"** - *from manufacturer declaration*
    - **"3"** - *from SAP table*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Heat-Loss:

Hot-Water-Store-Heat-Loss
-------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Heat-Loss`>/

- Documentation: *Hot water store declared loss in kWh/day; only if there is a hot water store and if manufacturer declared loss. Not applicable if (a) combi boiler whose data source database or (b) instantaneous combi boiler or (c) combi boiler from SAP table or (d) instantaneous water heater.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Insulation-Type:

Hot-Water-Store-Insulation-Type
-------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Insulation-Type`>/

- Documentation: *Hot water store insulation; only if there is a hot water store and if loss from SAP table. Not applicable if (a) combi boiler whose data source database or (b) instantaneous combi boiler or (c) combi boiler from SAP table or (d) instantaneous water heater.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Codes:
    - **"1"** - *factory-applied*
    - **"2"** - *loose jacket*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Insulation-Thickness:

Hot-Water-Store-Insulation-Thickness
------------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Store-Insulation-Thickness`>/

- Documentation: *Hot water store insulation thickness in mm; only if there is a hot water store and if loss from SAP table. Not applicable if (a) combi boiler whose data source database or (b) instantaneous combi boiler or (c) combi boiler from SAP table or (d) instantaneous water heater.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Thermal-Store-Near-Boiler:

Is-Thermal-Store-Near-Boiler
----------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Thermal-Store-Near-Boiler`>/

- Documentation: *Thermal store connected to boiler by no more than 1.5 m of insulated pipework? Only if thermal store. Not applicable if combi boiler or instantaneous water heater.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Thermal-Store-Or-CPSU-In-Airing-Cupboard:

Is-Thermal-Store-Or-CPSU-In-Airing-Cupboard
-------------------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Thermal-Store-Or-CPSU-In-Airing-Cupboard`>/

- Documentation: *Thermal store or CPSU in airing cupboard? Only if (a) boiler with integrated or hot-water-only thermal store, or (b) main heating is CPSU.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Has-Cylinder-Thermostat:

Has-Cylinder-Thermostat
-----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Has-Cylinder-Thermostat`>/

- Documentation: *Hot water cylinder thermostat? Not applicable if combi boiler or instantaneous water heater.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Cylinder-In-Heated-Space:

Is-Cylinder-In-Heated-Space
---------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Cylinder-In-Heated-Space`>/

- Documentation: *Hot water cylinder in heated space? Not applicable if combi boiler or instantaneous water heater.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Hot-Water-Separately-Timed:

Is-Hot-Water-Separately-Timed
-----------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Is-Hot-Water-Separately-Timed`>/

- Documentation: *Hot water separately timed? Not applicable if combi boiler or instantaneous water heater.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Controls-Manufacturer:

Hot-Water-Controls-Manufacturer
-------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Controls-Manufacturer`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Controls-Model:

Hot-Water-Controls-Model
------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Hot-Water-Controls-Model`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems:

SAP-Community-Heating-Systems
-----------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems`>/

- Documentation2: *Community heating systems used by the property.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System:

SAP-Community-Heating-System
----------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>/

- Documentation2: *Details of a community system which heats the Main Building.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Name`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-CO2-Emission-Factor`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Primary-Energy-Factor`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Use`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Is-Community-Heating-Cylinder-In-Dwelling`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Is-HIU-In-Dwelling`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/HIU-Index-Number`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Distribution-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Distribution-Loss-Factor`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Charging-Linked-To-Heat-Use`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Heat-Network-Index-Number`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Sub-Network-Name`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Heat-Network-Existing`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Heat-Network-Assessed-As-New`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *2*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Name:

Community-Heating-Name
----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Name`>/

- Documentation: *The name of the community heating system*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-CO2-Emission-Factor:

Community-Heating-CO2-Emission-Factor
-------------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-CO2-Emission-Factor`>/

- Documentation: *the community heating CO2 emission factor*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Primary-Energy-Factor:

Community-Heating-Primary-Energy-Factor
---------------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Primary-Energy-Factor`>/

- Documentation: *The community heating Primary Energy Factor*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Use:

Community-Heating-Use
---------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Use`>/

- Documentation: *Specifies what kind of heating the community system is used for.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>
- Has text value: *True*
- Codes:
    - **"1"** - *space heating only*
    - **"2"** - *water heating only*
    - **"3"** - *space and water heating*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Is-Community-Heating-Cylinder-In-Dwelling:

Is-Community-Heating-Cylinder-In-Dwelling
-----------------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Is-Community-Heating-Cylinder-In-Dwelling`>/

- Documentation: *Community heating, cylinder in dwelling?*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Is-HIU-In-Dwelling:

Is-HIU-In-Dwelling
------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Is-HIU-In-Dwelling`>/

- Documentation: *Community heating, HIU in dwelling?*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/HIU-Index-Number:

HIU-Index-Number
----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/HIU-Index-Number`>/

- Documentation: *Heat Interface Unit index number, if present.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Distribution-Type:

Community-Heating-Distribution-Type
-----------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Distribution-Type`>/

- Documentation: *Community heating distribution*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>
- Has text value: *True*
- Codes:
    - **"5"** - *calculated*
    - **"6"** - *unknown*
    - **"7"** - *Network not compliant with Code of Practice*
    - **"8"** - *Network compliant with Code of Practice*
    - **"9"** - *Two adjoining dwellings*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources:

Community-Heat-Sources
----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources`>/

- Documentation: *To be provided when there is no Heat-Network-Index-Number.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source:

Community-Heat-Source
---------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Heat-Source-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Heat-Fraction`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Fuel-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/PCDF-Fuel-Index`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Heat-Efficiency`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Power-Efficiency`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Description`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/CHP-Electricity-Generation`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *5*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Heat-Source-Type:

Heat-Source-Type
----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Heat-Source-Type`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source`>
- Has text value: *True*
- Codes:
    - **"1"** - *CHP*
    - **"2"** - *boilers*
    - **"3"** - *heat pump*
    - **"4"** - *waste heat*
    - **"5"** - *geothermal*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Heat-Fraction:

Heat-Fraction
-------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Heat-Fraction`>/

- Documentation: *Fraction of heat for the system provided by this heat source.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Fuel-Type:

Fuel-Type
---------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Fuel-Type`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source`>
- Has text value: *True*
- Codes:
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
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/PCDF-Fuel-Index:

PCDF-Fuel-Index
---------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/PCDF-Fuel-Index`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Heat-Efficiency:

Heat-Efficiency
---------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Heat-Efficiency`>/

- Documentation: *Heat efficiency in %.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Power-Efficiency:

Power-Efficiency
----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Power-Efficiency`>/

- Documentation: *Power efficiency in %. Include when heat source is CHP.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Description:

Description
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/Description`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/CHP-Electricity-Generation:

CHP-Electricity-Generation
--------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source/CHP-Electricity-Generation`>/

- Documentation: *CHP Electricity generation options from table 12f.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heat-Sources/Community-Heat-Source`>
- Has text value: *True*
- Codes:
    - **"81"** - *New CHP, export only.*
    - **"82"** - *New CHP, flexible operation.*
    - **"83"** - *New CHP, standard.*
    - **"84"** - *Existing CHP (2015+), export only.*
    - **"85"** - *Existing CHP (2015+), flexible operation.*
    - **"86"** - *Existing CHP (2015+),standard.*
    - **"87"** - *Existing CHP (pre-2015), export only.*
    - **"88"** - *Existing CHP (pre-2015), flexible operation.*
    - **"89"** - *Existing CHP (pre-2015), standard.*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Distribution-Loss-Factor:

Community-Heating-Distribution-Loss-Factor
------------------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Community-Heating-Distribution-Loss-Factor`>/

- Documentation: *Used when Community-Heating-Distribution-Type is calculated.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Charging-Linked-To-Heat-Use:

Charging-Linked-To-Heat-Use
---------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Charging-Linked-To-Heat-Use`>/

- Documentation: *Used for hot-water-only systems.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Heat-Network-Index-Number:

Heat-Network-Index-Number
-------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Heat-Network-Index-Number`>/

- Documentation: *Index number of heat network, if applicable.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Sub-Network-Name:

Sub-Network-Name
----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Sub-Network-Name`>/

- Documentation: *The name by which the sub community heat network is known.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Heat-Network-Existing:

Heat-Network-Existing
---------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Heat-Network-Existing`>/

- Documentation: *Whether the heat network is existing or new.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Heat-Network-Assessed-As-New:

Heat-Network-Assessed-As-New
----------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System/Heat-Network-Assessed-As-New`>/

- Documentation: *Whether the heat network is assessed as a new heat network (post June 2022) for Eng with a standalone gas boiler notional building.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Community-Heating-Systems/SAP-Community-Heating-System`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details:

Main-Heating-Details
--------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating:

Main-Heating
------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Number`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Category`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Data-Source`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Index-Number`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Manufacturer`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Model`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Commissioning-Certificate`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Installation-Engineer`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Condensing-Boiler`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Condensing-Boiler-Heat-Distribution`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heat-Pump-Heat-Distribution`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Gas-Or-Oil-Boiler-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Combi-Boiler-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Case-Heat-Emission`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heat-Transfer-To-Water`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Solid-Fuel-Boiler-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Code`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Fuel-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/PCDF-Fuel-Index`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Control`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heat-Emitter-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Underfloor-Heat-Emitter-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Flue-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Flue-Fan-Present`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Central-Heating-Pump-In-Heated-Space`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Oil-Pump-In-Heated-Space`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Interlocked-System`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Has-Separate-Delayed-Start`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Boiler-Fuel-Feed`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Main-Heating-HETAS-Approved`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Electric-CPSU-Operating-Temperature`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Fraction`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Burner-Control`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Efficiency-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Efficiency-Winter`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Efficiency-Summer`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Efficiency`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-System-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Has-FGHRS`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Index-Number`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Emitter-Temperature`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/MCS-Installed-Heat-Pump`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Central-Heating-Pump-Age`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Control-Index-Number`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heating-Controller-Function`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heating-Controller-Ecodesign-Class`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heating-Controller-Manufacturer`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heating-Controller-Model`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *2*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Number:

Main-Heating-Number
-------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Number`>/

- Documentation: *Identifies the main heating as system 1 or system 2. System 1 must always be present, system 2 is included only when there are two systems.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Category:

Main-Heating-Category
---------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Category`>/

- Documentation: *Category of heating system for the main heating system.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Codes:
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
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Data-Source:

Main-Heating-Data-Source
------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Data-Source`>/

- Documentation: *Source of main heating system data.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Codes:
    - **"1"** - *from database*
    - **"2"** - *from manufacturer declaration*
    - **"3"** - *from SAP table*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Index-Number:

Main-Heating-Index-Number
-------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Index-Number`>/

- Documentation: *The ID of the heating system from the product database, if system from database.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Manufacturer:

Main-Heating-Manufacturer
-------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Manufacturer`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Model:

Main-Heating-Model
------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Model`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Commissioning-Certificate:

Main-Heating-Commissioning-Certificate
--------------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Commissioning-Certificate`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Installation-Engineer:

Main-Heating-Installation-Engineer
----------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Installation-Engineer`>/

- Documentation: *Main heating installation engineer registration reference.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Condensing-Boiler:

Is-Condensing-Boiler
--------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Condensing-Boiler`>/

- Documentation: *Is the boiler a condensing boiler? If boiler efficiency is manufacturer declaration.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Condensing-Boiler-Heat-Distribution:

Condensing-Boiler-Heat-Distribution
-----------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Condensing-Boiler-Heat-Distribution`>/

- Documentation: *The temperature distribution of the condensing boiler.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heat-Pump-Heat-Distribution:

Heat-Pump-Heat-Distribution
---------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heat-Pump-Heat-Distribution`>/

- Documentation: *The temperature distribution of the heat pump, for wet systems only.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Gas-Or-Oil-Boiler-Type:

Gas-Or-Oil-Boiler-Type
----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Gas-Or-Oil-Boiler-Type`>/

- Documentation: *Boiler type; if boiler efficiency is manufacturer declaration and fuel is gas or oil.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Codes:
    - **"1"** - *regular*
    - **"2"** - *combi*
    - **"3"** - *CPSU*
    - **"4"** - *range cooker*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Combi-Boiler-Type:

Combi-Boiler-Type
-----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Combi-Boiler-Type`>/

- Documentation: *Combi boiler type; if it is a combi boiler and boiler efficiency is manufacturer declaration.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Codes:
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
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Case-Heat-Emission:

Case-Heat-Emission
------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Case-Heat-Emission`>/

- Documentation: *Case heat emission at full load in kW; if it is a range cooker boiler and boiler efficiency is manufacturer declaration.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heat-Transfer-To-Water:

Heat-Transfer-To-Water
----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heat-Transfer-To-Water`>/

- Documentation: *Heat transfer to water at full load in kW; if it is a range cooker boiler and boiler efficiency is manufacturer declaration.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Solid-Fuel-Boiler-Type:

Solid-Fuel-Boiler-Type
----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Solid-Fuel-Boiler-Type`>/

- Documentation: *Boiler type; if boiler efficiency is manufacturer declaration and fuel is solid.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Codes:
    - **"1"** - *independent*
    - **"2"** - *open fire*
    - **"3"** - *closed room heater*
    - **"4"** - *range cooker*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Code:

Main-Heating-Code
-----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Code`>/

- Documentation: *Main heating code; when heating data source is SAP table.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Fuel-Type:

Main-Fuel-Type
--------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Fuel-Type`>/

- Documentation: *The type of fuel used to power the central heating e.g. Gas, Electricity; not used if main heating system is community heating scheme.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Codes:
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
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/PCDF-Fuel-Index:

PCDF-Fuel-Index
---------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/PCDF-Fuel-Index`>/

- Documentation: *PCDF index number of the fuel type, only if Main-Fuel-Type is 99 (fuel from database).*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Control:

Main-Heating-Control
--------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Control`>/

- Documentation: *Type of Main Control for the Heating System.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heat-Emitter-Type:

Heat-Emitter-Type
-----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heat-Emitter-Type`>/

- Documentation: *Identifies the means by which the central heating system (if present) emits heat; only when wet system (radiators or underfloor).*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Codes:
    - **"1"** - *radiators*
    - **"2"** - *underfloor*
    - **"3"** - *both radiators and underfloor*
    - **"4"** - *fan coil units*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Underfloor-Heat-Emitter-Type:

Underfloor-Heat-Emitter-Type
----------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Underfloor-Heat-Emitter-Type`>/

- Documentation: *Means by which an underfloor heating system (if present) emits heat; only when wet system (underfloor).*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Codes:
    - **"1"** - *in concrete slab*
    - **"2"** - *in screed above insulation*
    - **"3"** - *in timber floor*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Flue-Type:

Main-Heating-Flue-Type
----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Flue-Type`>/

- Documentation: *The type of main heating flue; only if flued appliance.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Codes:
    - **"1"** - *open flue*
    - **"2"** - *balanced flue*
    - **"3"** - *chimney*
    - **"4"** - *omitted (boiler is in an outhouse, so its flue arrangements are not relevant)*
    - **"5"** - *unknown (there is a flue, but its type could not be determined)*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Flue-Fan-Present:

Is-Flue-Fan-Present
-------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Flue-Fan-Present`>/

- Documentation: *Indicates whether the heating system contains a fan flue; only if boiler.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Central-Heating-Pump-In-Heated-Space:

Is-Central-Heating-Pump-In-Heated-Space
---------------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Central-Heating-Pump-In-Heated-Space`>/

- Documentation: *Central heating pump in heated space? Only when wet system (radiators or underfloor).*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Oil-Pump-In-Heated-Space:

Is-Oil-Pump-In-Heated-Space
---------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Oil-Pump-In-Heated-Space`>/

- Documentation: *Oil pump in heated space? Only if oil boiler.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Interlocked-System:

Is-Interlocked-System
---------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Interlocked-System`>/

- Documentation: *Interlocked system? Only when wet system (radiators or underfloor).*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Has-Separate-Delayed-Start:

Has-Separate-Delayed-Start
--------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Has-Separate-Delayed-Start`>/

- Documentation: *True if there is a delayed start control separate from a controller in the database.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Boiler-Fuel-Feed:

Boiler-Fuel-Feed
----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Boiler-Fuel-Feed`>/

- Documentation: *The type of boiler fuel feed; only if solid fuel boiler with manufacturer declaration.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Codes:
    - **"1"** - *gravity*
    - **"2"** - *manual*
    - **"3"** - *screw*
    - **"4"** - *other*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Main-Heating-HETAS-Approved:

Is-Main-Heating-HETAS-Approved
------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Is-Main-Heating-HETAS-Approved`>/

- Documentation: *Main heating appliance is HETAS approved? Only if solid fuel.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Electric-CPSU-Operating-Temperature:

Electric-CPSU-Operating-Temperature
-----------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Electric-CPSU-Operating-Temperature`>/

- Documentation: *Electric CPSU operating temperature in Celcius; only if main heating is electric CPSU.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Fraction:

Main-Heating-Fraction
---------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Fraction`>/

- Documentation: *Fraction of main heating provided by this system, is 1 if only one main system.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Burner-Control:

Burner-Control
--------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Burner-Control`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Codes:
    - **"1"** - *unknown*
    - **"2"** - *on/off (gas and oil burners)*
    - **"3"** - *modulating (gas and oil boilers)*
    - **"4"** - *manual (solid fuel boilers)*
    - **"5"** - *electrical (solid fuel boilers)*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Efficiency-Type:

Efficiency-Type
---------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Efficiency-Type`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Codes:
    - **"1"** - *not gas or oil boiler*
    - **"2"** - *SEDBUK(2005)*
    - **"3"** - *SEDBUK(2009)*
    - **"4"** - *winter and summer*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Efficiency-Winter:

Main-Heating-Efficiency-Winter
------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Efficiency-Winter`>/

- Documentation: *To be used if main heating data is manufacturer declaration and Efficiency-Type is winter and summer.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Efficiency-Summer:

Main-Heating-Efficiency-Summer
------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Efficiency-Summer`>/

- Documentation: *To be used if main heating data is manufacturer declaration and Efficiency-Type is winter and summer.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Efficiency:

Main-Heating-Efficiency
-----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Efficiency`>/

- Documentation: *If main heating is any system other than heat network.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-System-Type:

Main-Heating-System-Type
------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-System-Type`>/

- Documentation: *Main heating system type or technology, for e.g., combi boiler, air source heat pump, etc.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Has-FGHRS:

Has-FGHRS
---------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Has-FGHRS`>/

- Documentation: *Flue Gas Heat Recovery System.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Index-Number:

FGHRS-Index-Number
------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Index-Number`>/

- Documentation: *FGHRS index number; only if FGHRS.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source:

FGHRS-Energy-Source
-------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source`>/

- Documentation2: *Details of the main Electricity supply to the Property.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Electricity-Tariff`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Certificate`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Is-Hydro-Output-Connected-To-Dwelling-Meter`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays:

PV-Arrays
---------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array:

PV-Array
--------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Peak-Power`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Orientation`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Pitch`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Overshading`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/MCS-Certificate`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/MCS-Certificate-Reference`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/PV-Panel-Manufacturer-Name`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Overshading-MCS`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *3*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Peak-Power:

Peak-Power
----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Peak-Power`>/

- Documentation: *Peak kW of photovoltaics (PVs) (kWp); 0.0 if none.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Orientation:

Orientation
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Orientation`>/

- Documentation: *PV orientation; only if peak kWp > 0.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array`>
- Has text value: *True*
- Codes:
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
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Pitch:

Pitch
-----

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Pitch`>/

- Documentation: *PV pitch; only if peak kWp > 0.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array`>
- Has text value: *True*
- Codes:
    - **"1"** - *horizontal*
    - **"2"** - *30 degrees*
    - **"3"** - *45 degrees*
    - **"4"** - *60 degrees*
    - **"5"** - *vertical*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Overshading:

Overshading
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Overshading`>/

- Documentation: *PV overshading; only if peak kWp > 0 and no MCS certificate.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array`>
- Has text value: *True*
- Codes:
    - **"1"** - *none or very little*
    - **"2"** - *modest*
    - **"3"** - *significant*
    - **"4"** - *heavy*
    - **"5"** - *severe*
    - **"ND"** - *for backwards compatability only; do not use*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/MCS-Certificate:

MCS-Certificate
---------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/MCS-Certificate`>/

- Documentation: *Does the installation have a MCS certificate.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/MCS-Certificate-Reference:

MCS-Certificate-Reference
-------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/MCS-Certificate-Reference`>/

- Documentation: *MCS certificate reference number*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/PV-Panel-Manufacturer-Name:

PV-Panel-Manufacturer-Name
--------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/PV-Panel-Manufacturer-Name`>/

- Documentation: *Manufacturer of PV panels*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Overshading-MCS:

Overshading-MCS
---------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array/Overshading-MCS`>/

- Documentation: *Overshading factor calculated according to MCS.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/PV-Arrays/PV-Array`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines:

Wind-Turbines
-------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine:

Wind-Turbine
------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Manufacturer-Name`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Certificate`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Rotor-Diameter`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Hub-Height`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *99*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Manufacturer-Name:

Wind-Turbine-Manufacturer-Name
------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Manufacturer-Name`>/

- Documentation: *Wind turbine manufacturer name.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Certificate:

Wind-Turbine-Certificate
------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Certificate`>/

- Documentation: *Wind turbine certificate.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Rotor-Diameter:

Wind-Turbine-Rotor-Diameter
---------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Rotor-Diameter`>/

- Documentation: *Wind turbine rotor diameter in metres; only if wind turbine.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Hub-Height:

Wind-Turbine-Hub-Height
-----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Hub-Height`>/

- Documentation: *Wind turbine hub height above building in metres; only if wind turbine.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Wind-Turbines/Wind-Turbine`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Electricity-Tariff:

Electricity-Tariff
------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Electricity-Tariff`>/

- Documentation: *Type of electricity tariff.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source`>
- Has text value: *True*
- Codes:
    - **"1"** - *standard tariff*
    - **"2"** - *off-peak 7 hour*
    - **"3"** - *off-peak 10 hour*
    - **"4"** - *24 hour*
    - **"5"** - *off-peak 18 hour*
    - **"ND"** - *not applicable*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation:

Hydro-Electric-Generation
-------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation`>/

- Documentation: *Electricity generated by hydro-electric generator, in kWh/year. To be provided if Hydro-Electric-Generation-Month is not provided.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Certificate:

Hydro-Electric-Certificate
--------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Certificate`>/

- Documentation: *Reference to certification of hydro electric output.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months:

Hydro-Electric-Generation-Months
--------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months`>/

- Documentation: *Electricity generated by hydro-electric generator, in kWh/month. To be provided if Hydro-Electric-Generation is not provided.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month:

Hydro-Electric-Generation-Month
-------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month/Hydro-Month`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month/Hydro-Value`>
- Has text value: *False*
- Minimum occurrence: *12*
- Maximum occurrence: *12*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month/Hydro-Month:

Hydro-Month
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month/Hydro-Month`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month`>
- Has text value: *True*
- Codes:
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
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month/Hydro-Value:

Hydro-Value
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month/Hydro-Value`>/

- Documentation: *Hydro electricity in kWh in month.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Is-Hydro-Output-Connected-To-Dwelling-Meter:

Is-Hydro-Output-Connected-To-Dwelling-Meter
-------------------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source/Is-Hydro-Output-Connected-To-Dwelling-Meter`>/

- Documentation: *Whether the hydro-electric station is connected to dwelling's electricity meter*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Energy-Source`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values:

Main-Heating-Declared-Values
----------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values/Efficiency`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values/Make-Model`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values/Test-Method`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values/Efficiency:

Efficiency
----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values/Efficiency`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values/Make-Model:

Make-Model
----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values/Make-Model`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values/Test-Method:

Test-Method
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values/Test-Method`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Declared-Values`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters:

Storage-Heaters
---------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater:

Storage-Heater
--------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater/Number-Of-Heaters`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater/Index-Number`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater/High-Heat-Retention`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *4*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater/Number-Of-Heaters:

Number-Of-Heaters
-----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater/Number-Of-Heaters`>/

- Documentation: *The number of storage heaters with this index number.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater/Index-Number:

Index-Number
------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater/Index-Number`>/

- Documentation: *The index number of the heater from the product database.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater/High-Heat-Retention:

High-Heat-Retention
-------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater/High-Heat-Retention`>/

- Documentation: *Whether heater is high heat retention type.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Emitter-Temperature:

Emitter-Temperature
-------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Emitter-Temperature`>/

- Documentation: *Gas and oil boilers and heat pump from database: 0, 1, 3 or 4 Other heat pump 0, 2 or 4. Other systems NA.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Codes:
    - **"0"** - *unknown*
    - **"1"** - *over 45degC*
    - **"2"** - *over 35degC*
    - **"3"** - *over 35degC and less than or equal to 45degC*
    - **"4"** - *less than or equal to 35degC*
    - **"NA"** - *not applicable for the heating system*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/MCS-Installed-Heat-Pump:

MCS-Installed-Heat-Pump
-----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/MCS-Installed-Heat-Pump`>/

- Documentation: *Whether heat pump was installed under the Microgeneration Certification Scheme.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Central-Heating-Pump-Age:

Central-Heating-Pump-Age
------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Central-Heating-Pump-Age`>/

- Documentation: *Included for systems with a central heating pump, i.e. wet system.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Codes:
    - **"0"** - *unknown*
    - **"1"** - *2012 or earlier*
    - **"2"** - *2013 or later*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Control-Index-Number:

Control-Index-Number
--------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Control-Index-Number`>/

- Documentation: *The ID of the controller from the product database.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heating-Controller-Function:

Heating-Controller-Function
---------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heating-Controller-Function`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heating-Controller-Ecodesign-Class:

Heating-Controller-Ecodesign-Class
----------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heating-Controller-Ecodesign-Class`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heating-Controller-Manufacturer:

Heating-Controller-Manufacturer
-------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heating-Controller-Manufacturer`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heating-Controller-Model:

Heating-Controller-Model
------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heating-Controller-Model`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Heating-Design-Water-Use:

SAP-Heating-Design-Water-Use
----------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/SAP-Heating-Design-Water-Use`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Codes:
    - **"1"** - *<= 125 litres per person per day*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Systems-Interaction:

Main-Heating-Systems-Interaction
--------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Systems-Interaction`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Codes:
    - **"1"** - *both main heating systems provide heat to the whole property*
    - **"2"** - *the main heating systems are separate and heat different parts of the property*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values:

Secondary-Heating-Declared-Values
---------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values`>/

- Documentation: *Use when manufacturer's declared values.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values/Efficiency`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values/Make-Model`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values/Test-Method`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values/Efficiency:

Efficiency
----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values/Efficiency`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values/Make-Model:

Make-Model
----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values/Make-Model`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values/Test-Method:

Test-Method
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values/Test-Method`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Declared-Values`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Primary-Pipework-Insulation:

Primary-Pipework-Insulation
---------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Primary-Pipework-Insulation`>/

- Documentation: *Not applicable to combi boiler or instantaneous water heater.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Codes:
    - **"1"** - *not insulated*
    - **"2"** - *first 1 metre from cylinder insulated*
    - **"3"** - *all accessible pipework insulated*
    - **"4"** - *fully insulated*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details:

Solar-Heating-Details
---------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Heating-Collector-Manufacturer`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Heating-Certificate`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Aperture-Area`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Data-Source`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Zero-Loss-Efficiency`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Heat-Loss-Rate`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Linear-Heat-Loss-Coefficient`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Second-Order-Heat-Loss-Coefficient`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Orientation`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Pitch`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Overshading`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Has-Solar-Powered-Pump`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Is-Solar-Store-Combined-Cylinder`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Store-Volume`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Collector-Loop-Efficiency`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Incidence-Angle-Modifier`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Is-Community-Solar`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Service-Provision`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Overall-Heat-Loss`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Heating-Collector-Manufacturer:

Solar-Heating-Collector-Manufacturer
------------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Heating-Collector-Manufacturer`>/

- Documentation: *Panel manufacturer*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Heating-Certificate:

Solar-Heating-Certificate
-------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Heating-Certificate`>/

- Documentation: *Solar heating certificate*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Aperture-Area:

Solar-Panel-Aperture-Area
-------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Aperture-Area`>/

- Documentation: *Panel aperture area in square metres.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Type:

Solar-Panel-Collector-Type
--------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Type`>/

- Documentation: *Type of solar panel collector.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>
- Has text value: *True*
- Codes:
    - **"1"** - *unglazed*
    - **"2"** - *flat panel*
    - **"3"** - *evacuated tube*
    - **"ND"** - *for backwards compatability only; do not use*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Data-Source:

Solar-Panel-Collector-Data-Source
---------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Data-Source`>/

- Documentation: *Source of solar panel collector data.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>
- Has text value: *True*
- Codes:
    - **"1"** - *default*
    - **"2"** - *declared values*
    - **"ND"** - *for backwards compatability only; do not use*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Zero-Loss-Efficiency:

Solar-Panel-Collector-Zero-Loss-Efficiency
------------------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Zero-Loss-Efficiency`>/

- Documentation: *Collector zero-loss efficiency; only if declared values.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Heat-Loss-Rate:

Solar-Panel-Collector-Heat-Loss-Rate
------------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Heat-Loss-Rate`>/

- Documentation: *Collector heat loss rate; for backward compatibility only, do not use.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Linear-Heat-Loss-Coefficient:

Solar-Panel-Collector-Linear-Heat-Loss-Coefficient
--------------------------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Linear-Heat-Loss-Coefficient`>/

- Documentation: *Collector linear heat loss coefficient; only if declared values.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Second-Order-Heat-Loss-Coefficient:

Solar-Panel-Collector-Second-Order-Heat-Loss-Coefficient
--------------------------------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Second-Order-Heat-Loss-Coefficient`>/

- Documentation: *Collector 2nd order heat loss coefficient; only if declared values.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Orientation:

Solar-Panel-Collector-Orientation
---------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Orientation`>/

- Documentation: *Collector orientation.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>
- Has text value: *True*
- Codes:
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
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Pitch:

Solar-Panel-Collector-Pitch
---------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Pitch`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Overshading:

Solar-Panel-Collector-Overshading
---------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Panel-Collector-Overshading`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>
- Has text value: *True*
- Codes:
    - **"1"** - *none or very little*
    - **"2"** - *modest*
    - **"3"** - *significant*
    - **"4"** - *heavy*
    - **"5"** - *severe*
    - **"ND"** - *for backwards compatability only; do not use*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Has-Solar-Powered-Pump:

Has-Solar-Powered-Pump
----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Has-Solar-Powered-Pump`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Is-Solar-Store-Combined-Cylinder:

Is-Solar-Store-Combined-Cylinder
--------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Is-Solar-Store-Combined-Cylinder`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Store-Volume:

Solar-Store-Volume
------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Solar-Store-Volume`>/

- Documentation: *Dedicated solar store volume in litres.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Collector-Loop-Efficiency:

Collector-Loop-Efficiency
-------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Collector-Loop-Efficiency`>/

- Documentation: *Collector loop efficiency; only if declared values.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Incidence-Angle-Modifier:

Incidence-Angle-Modifier
------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Incidence-Angle-Modifier`>/

- Documentation: *Incidence angle modifier; only if declared values.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Is-Community-Solar:

Is-Community-Solar
------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Is-Community-Solar`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Service-Provision:

Service-Provision
-----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Service-Provision`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>
- Has text value: *True*
- Codes:
    - **"1"** - *space and water heating*
    - **"2"** - *space heating only*
    - **"3"** - *water heating only*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Overall-Heat-Loss:

Overall-Heat-Loss
-----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details/Overall-Heat-Loss`>/

- Documentation: *Overall heat loss coefficient of system; only if declared values.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Solar-Heating-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS:

Instantaneous-WWHRS
-------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS`>/

- Documentation: *Waste Water Heat Recovery System.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Index-Number1`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Index-Number2`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Efficiency1`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Manufacturer1`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Model1`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Efficiency2`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Manufacturer2`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Model2`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Index-Number1:

WWHRS-Index-Number1
-------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Index-Number1`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Index-Number2:

WWHRS-Index-Number2
-------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Index-Number2`>/

- Documentation: *Omit if no second system.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Efficiency1:

WWHRS-Efficiency1
-----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Efficiency1`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Manufacturer1:

WWHRS-Manufacturer1
-------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Manufacturer1`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Model1:

WWHRS-Model1
------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Model1`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Efficiency2:

WWHRS-Efficiency2
-----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Efficiency2`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Manufacturer2:

WWHRS-Manufacturer2
-------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Manufacturer2`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Model2:

WWHRS-Model2
------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Model2`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS:

Storage-WWHRS
-------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/WWHRS-Index-Number`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/WWHRS-Store-Volume`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/Storage-WWHRS-Efficiency`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/Storage-WWHRS-Manufacturer`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/Storage-WWHRS-Model`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/WWHRS-Index-Number:

WWHRS-Index-Number
------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/WWHRS-Index-Number`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/WWHRS-Store-Volume:

WWHRS-Store-Volume
------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/WWHRS-Store-Volume`>/

- Documentation: *Dedicated store volume in litres.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/Storage-WWHRS-Efficiency:

Storage-WWHRS-Efficiency
------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/Storage-WWHRS-Efficiency`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/Storage-WWHRS-Manufacturer:

Storage-WWHRS-Manufacturer
--------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/Storage-WWHRS-Manufacturer`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/Storage-WWHRS-Model:

Storage-WWHRS-Model
-------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/Storage-WWHRS-Model`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets:

Shower-Outlets
--------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets`>/

- Documentation2: *Shower outlets present in the dwelling. If there are more than 5 then only include the 5 with the highest flow rates used.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet:

Shower-Outlet
-------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet`>/

- Documentation2: *Various details for each shower outlet.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-Outlet-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-Flow-Rate`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-Power`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-WWHRS`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *5*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-Outlet-Type:

Shower-Outlet-Type
------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-Outlet-Type`>/

- Documentation: *Hot water type for this shower outlet.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet`>
- Has text value: *True*
- Codes:
    - **"1"** - *Vented hot water system*
    - **"2"** - *Vented hot water system + pump*
    - **"3"** - *Unvented hot water system*
    - **"4"** - *Instantaneous electric shower*
    - **"5"** - *Part G 2015 compliant*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-Flow-Rate:

Shower-Flow-Rate
----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-Flow-Rate`>/

- Documentation: *The flow rate. Only when a shower is not instantaneous electric. Leave blank if NO flow limiter fitted.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-Power:

Shower-Power
------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-Power`>/

- Documentation: *The shower power, only if shower outlet type is instantaneous electric.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-WWHRS:

Shower-WWHRS
------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-WWHRS`>/

- Documentation: *The WWHRS with which the shower is connected. If shower outlet type is instantaneous electric shower then only a storage WWHRS can be selected or none.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet`>
- Has text value: *True*
- Codes:
    - **"1"** - *none*
    - **"2"** - *Instantaneous WWHRS 1*
    - **"3"** - *Instantaneous WWHRS 2*
    - **"4"** - *Storage WWHRS*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Number-Baths:

Number-Baths
------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Number-Baths`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Number-Baths-WWHRS:

Number-Baths-WWHRS
------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating/Number-Baths-WWHRS`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source:

SAP-Energy-Source
-----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source`>/

- Documentation2: *Details of the main Electricity supply to the Property.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Electricity-Tariff`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Certificate`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Is-Hydro-Output-Connected-To-Dwelling-Meter`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays:

PV-Arrays
---------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array:

PV-Array
--------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Peak-Power`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Orientation`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Pitch`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Overshading`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/MCS-Certificate`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/MCS-Certificate-Reference`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/PV-Panel-Manufacturer-Name`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Overshading-MCS`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *3*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Peak-Power:

Peak-Power
----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Peak-Power`>/

- Documentation: *Peak kW of photovoltaics (PVs) (kWp); 0.0 if none.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Orientation:

Orientation
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Orientation`>/

- Documentation: *PV orientation; only if peak kWp > 0.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array`>
- Has text value: *True*
- Codes:
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
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Pitch:

Pitch
-----

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Pitch`>/

- Documentation: *PV pitch; only if peak kWp > 0.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array`>
- Has text value: *True*
- Codes:
    - **"1"** - *horizontal*
    - **"2"** - *30 degrees*
    - **"3"** - *45 degrees*
    - **"4"** - *60 degrees*
    - **"5"** - *vertical*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Overshading:

Overshading
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Overshading`>/

- Documentation: *PV overshading; only if peak kWp > 0 and no MCS certificate.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array`>
- Has text value: *True*
- Codes:
    - **"1"** - *none or very little*
    - **"2"** - *modest*
    - **"3"** - *significant*
    - **"4"** - *heavy*
    - **"5"** - *severe*
    - **"ND"** - *for backwards compatability only; do not use*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/MCS-Certificate:

MCS-Certificate
---------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/MCS-Certificate`>/

- Documentation: *Does the installation have a MCS certificate.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/MCS-Certificate-Reference:

MCS-Certificate-Reference
-------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/MCS-Certificate-Reference`>/

- Documentation: *MCS certificate reference number*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/PV-Panel-Manufacturer-Name:

PV-Panel-Manufacturer-Name
--------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/PV-Panel-Manufacturer-Name`>/

- Documentation: *Manufacturer of PV panels*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Overshading-MCS:

Overshading-MCS
---------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array/Overshading-MCS`>/

- Documentation: *Overshading factor calculated according to MCS.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/PV-Arrays/PV-Array`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines:

Wind-Turbines
-------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine:

Wind-Turbine
------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Manufacturer-Name`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Certificate`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Rotor-Diameter`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Hub-Height`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *99*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Manufacturer-Name:

Wind-Turbine-Manufacturer-Name
------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Manufacturer-Name`>/

- Documentation: *Wind turbine manufacturer name.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Certificate:

Wind-Turbine-Certificate
------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Certificate`>/

- Documentation: *Wind turbine certificate.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Rotor-Diameter:

Wind-Turbine-Rotor-Diameter
---------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Rotor-Diameter`>/

- Documentation: *Wind turbine rotor diameter in metres; only if wind turbine.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Hub-Height:

Wind-Turbine-Hub-Height
-----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine/Wind-Turbine-Hub-Height`>/

- Documentation: *Wind turbine hub height above building in metres; only if wind turbine.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines/Wind-Turbine`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Electricity-Tariff:

Electricity-Tariff
------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Electricity-Tariff`>/

- Documentation: *Type of electricity tariff.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source`>
- Has text value: *True*
- Codes:
    - **"1"** - *standard tariff*
    - **"2"** - *off-peak 7 hour*
    - **"3"** - *off-peak 10 hour*
    - **"4"** - *24 hour*
    - **"5"** - *off-peak 18 hour*
    - **"ND"** - *not applicable*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation:

Hydro-Electric-Generation
-------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation`>/

- Documentation: *Electricity generated by hydro-electric generator, in kWh/year. To be provided if Hydro-Electric-Generation-Month is not provided.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Certificate:

Hydro-Electric-Certificate
--------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Certificate`>/

- Documentation: *Reference to certification of hydro electric output.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months:

Hydro-Electric-Generation-Months
--------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months`>/

- Documentation: *Electricity generated by hydro-electric generator, in kWh/month. To be provided if Hydro-Electric-Generation is not provided.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month:

Hydro-Electric-Generation-Month
-------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month/Hydro-Month`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month/Hydro-Value`>
- Has text value: *False*
- Minimum occurrence: *12*
- Maximum occurrence: *12*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month/Hydro-Month:

Hydro-Month
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month/Hydro-Month`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month`>
- Has text value: *True*
- Codes:
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
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month/Hydro-Value:

Hydro-Value
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month/Hydro-Value`>/

- Documentation: *Hydro electricity in kWh in month.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation-Months/Hydro-Electric-Generation-Month`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Is-Hydro-Output-Connected-To-Dwelling-Meter:

Is-Hydro-Output-Connected-To-Dwelling-Meter
-------------------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source/Is-Hydro-Output-Connected-To-Dwelling-Meter`>/

- Documentation: *Whether the hydro-electric station is connected to dwelling's electricity meter*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Energy-Source`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts:

SAP-Building-Parts
------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/

- Documentation2: *Details of the significant building parts that comprise the main habitable building in the property. The main habitable area generally consists of a single main building but can over time be extended to include extensions such as new wings and additional storeys. For the purpose of calculating the overall Energy Assessment for the property details of each distinct Building Part, such as its construction, have to be gathered because different materials have different insulation ratings (obviously) which affects the overall rating.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part:

SAP-Building-Part
-----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/

- Documentation2: *A permanent structure that forms part of the Property and is built primarily for human habitation. A Building Part is usually made up of one or more Storey's and may contain a number of Internal Structural Features. An extension is also a Building Part.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Building-Part-Number`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Identifier`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Construction-Year`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Construction-Age-Band`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *unbounded*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Building-Part-Number:

Building-Part-Number
--------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Building-Part-Number`>/

- Documentation: *An integer value which uniquely identifies the building part in the property. The value "1" must be assigned to the main dwelling.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Identifier:

Identifier
----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Identifier`>/

- Documentation: *Identifier for the Building part - generally only required if there are more that one Building Parts of the same type e.g. "West Wing" and "East Wing" Extensions*
- Documentation2: *A string containing a unique identifier for something. The underlying assumption is that each instance of a class or entity will have a unique identifier assigned to it which can then be assigned to any referencing entity as a reference to the entity instance. This is a very similar concept to XML ID datatype but is locally defined because of the need to extend the datatype with domain specific attributes.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Construction-Year:

Construction-Year
-----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Construction-Year`>/

- Documentation: *The year when this building part was constructed. Not used if 'Construction-Age-Band' is used.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Construction-Age-Band:

Construction-Age-Band
---------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Construction-Age-Band`>/

- Documentation: *The age band when this building part was constructed. Not used if 'Construction-Year' is used.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Has text value: *True*
- Codes:
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
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings:

SAP-Openings
------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings`>/

- Documentation2: *Exposed openings that make up a particular Building-Part.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening:

SAP-Opening
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening`>/

- Documentation2: *Various measurements for each exposed opening that makes up a particular Building-Part.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Name`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Type`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Location`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Orientation`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Width`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Height`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Pitch`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *unbounded*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Name:

Name
----

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Name`>/

- Documentation: *Unique name which identifies this opening. Can be just a number, e.g. "1". However, an opening cannot have the same name as a wall.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Type:

Type
----

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Type`>/

- Documentation: *The name of the SAP-Opening-Type for this opening.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Location:

Location
--------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Location`>/

- Documentation: *Name of the wall or roof which contains the opening.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Orientation:

Orientation
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Orientation`>/

- Documentation: *Compass direction in which the opening faces.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening`>
- Has text value: *True*
- Codes:
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
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Width:

Width
-----

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Width`>/

- Documentation: *The width of the opening in metres. If the Width field is used to record the opening area, set the Height to 1.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Height:

Height
------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Height`>/

- Documentation: *The height of the opening in metres. If the Height field is used to record the opening area, set the Width to 1.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Pitch:

Pitch
-----

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening/Pitch`>/

- Documentation: *Pitch of roof containing roof window.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Openings/SAP-Opening`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs:

SAP-Roofs
---------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs`>/

- Documentation2: *Exposed roofs that make up a particular Building-Part.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof:

SAP-Roof
--------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof`>/

- Documentation2: *Various measurements for each exposed roof that makes up a particular Building-Part.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Name`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Description`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Roof-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Total-Roof-Area`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/U-Value`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Kappa-Value`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *unbounded*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Name:

Name
----

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Name`>/

- Documentation: *Unique name which identifies this roof. Can be just a number, e.g. "1". However, a roof cannot have the same name as a wall.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Description:

Description
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Description`>/

- Documentation: *Descriptive notes about the roof.*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Roof-Type:

Roof-Type
---------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Roof-Type`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof`>
- Has text value: *True*
- Codes:
    - **"2"** - *exposed roof*
    - **"4"** - *party ceiling*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Total-Roof-Area:

Total-Roof-Area
---------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Total-Roof-Area`>/

- Documentation: *Total roof area in square metres, inclusive of any openings.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/U-Value:

U-Value
-------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/U-Value`>/

- Documentation: *Exposed roof U-value.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Kappa-Value:

Kappa-Value
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof/Kappa-Value`>/

- Documentation: *Heat capacity per unit area in kJ/m2K.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Roofs/SAP-Roof`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions:

SAP-Floor-Dimensions
--------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions`>/

- Documentation2: *Storeys that make up a particular Building-Part.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension:

SAP-Floor-Dimension
-------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>/

- Documentation2: *Various measurements for the floor of a particular storey.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Name`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Storey`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Description`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Floor-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Total-Floor-Area`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Storey-Height`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Heat-Loss-Area`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/U-Value`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Kappa-Value`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Kappa-Value-From-Below`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *unbounded*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Name:

Name
----

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Name`>/

- Documentation: *A name describing the floor dimensioned.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Storey:

Storey
------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Storey`>/

- Documentation: *Building storey on which the floor is located.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>
- Has text value: *True*
- Codes:
    - **"-1"** - *Lower ground*
    - **"0"** - *Ground*
    - **"1"** - *1st*
    - **"2"** - *2nd*
    - **"3"** - *3rd*
    - **"4"** - *4th*
    - **"5"** - *5th*
    - **"6"** - *6th*
    - **"99"** - *Roof rooms*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Description:

Description
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Description`>/

- Documentation: *Descriptive notes about the floor.*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Floor-Type:

Floor-Type
----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Floor-Type`>/

- Documentation: *Type of floor (exposure).*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>
- Has text value: *True*
- Codes:
    - **"1"** - *basement floor*
    - **"2"** - *ground floor*
    - **"3"** - *upper floor (if heat loss area > 0, this area is an exposed floor)*
    - **"4"** - *party floor*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Total-Floor-Area:

Total-Floor-Area
----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Total-Floor-Area`>/

- Documentation: *The total floor area of the storey in square metres.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Storey-Height:

Storey-Height
-------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Storey-Height`>/

- Documentation: *Average height of the storey in metres.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Heat-Loss-Area:

Heat-Loss-Area
--------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Heat-Loss-Area`>/

- Documentation: *The estimated total heat loss area for the floor in square metres.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/U-Value:

U-Value
-------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/U-Value`>/

- Documentation: *Heat loss floor U-value.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Kappa-Value:

Kappa-Value
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Kappa-Value`>/

- Documentation: *Heat capacity of floor per unit area in kJ/m2K.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Kappa-Value-From-Below:

Kappa-Value-From-Below
----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Kappa-Value-From-Below`>/

- Documentation: *Heat capacity of ceiling below. Applies to the non-heat-loss area of an upper floor.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges:

SAP-Thermal-Bridges
-------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges`>/

- Documentation2: *Thermal bridges that make up a particular Building-Part.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/Thermal-Bridge-Code`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/User-Defined-Y-Value`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/Calculation-Reference`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/Thermal-Bridge-Code:

Thermal-Bridge-Code
-------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/Thermal-Bridge-Code`>/

- Documentation: *Code which indicates how the thermal bridge data has been recorded.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges`>
- Has text value: *True*
- Codes:
    - **"1"** - *default*
    - **"2"** - *2002 regulations. For backwards compatibility only, do not use.*
    - **"3"** - *accredited. For backwards compatibility only, do not use.*
    - **"4"** - *user defined (global y-value)*
    - **"5"** - *user defined (individual values)*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/User-Defined-Y-Value:

User-Defined-Y-Value
--------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/User-Defined-Y-Value`>/

- Documentation: *Global y-value for all thermal bridges in watts per square metre per kelvin; only if thermal bridge code is: user defined (global y-value)*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/Calculation-Reference:

Calculation-Reference
---------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/Calculation-Reference`>/

- Documentation: *Reference to the details of the calculation of the global y-value; only if thermal bridging is user defined global y-value.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge:

SAP-Thermal-Bridge
------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge`>/

- Documentation2: *Various measurements for each thermal bridge that makes up a particular Building-Part.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Thermal-Bridge-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Length`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Psi-Value`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Psi-Value-Source`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Psi-Value-Calculation-Reference`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *unbounded*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Thermal-Bridge-Type:

Thermal-Bridge-Type
-------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Thermal-Bridge-Type`>/

- Documentation: *Code to indicate a particular type of thermal bridge; only if thermal bridge code is: user defined (individual values).*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge`>
- Has text value: *True*
- Codes:
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
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Length:

Length
------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Length`>/

- Documentation: *Length of the thermal bridge in metres; only if thermal bridge code is: user defined (individual values).*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Psi-Value:

Psi-Value
---------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Psi-Value`>/

- Documentation: *Linear thermal transmittance (psi-value); only if thermal bridging is user defined individual values.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Psi-Value-Source:

Psi-Value-Source
----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Psi-Value-Source`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge`>
- Has text value: *True*
- Codes:
    - **"1"** - *calculated by person with suitable expertise*
    - **"2"** - *government-approved scheme*
    - **"3"** - *not government-approved scheme*
    - **"4"** - *SAP table default*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Psi-Value-Calculation-Reference:

Psi-Value-Calculation-Reference
-------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge/Psi-Value-Calculation-Reference`>/

- Documentation: *Reference to the details of the calculation of the psi-value.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Thermal-Bridges/SAP-Thermal-Bridge`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls:

SAP-Walls
---------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls`>/

- Documentation2: *Exposed walls that make up a particular Storey.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall:

SAP-Wall
--------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall`>/

- Documentation2: *Various measurements for each wall of a particular storey.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Name`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Description`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Wall-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Total-Wall-Area`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/U-Value`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Is-Curtain-Walling`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Kappa-Value`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *unbounded*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Name:

Name
----

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Name`>/

- Documentation: *Unique name which identifies this wall within its storey. Can be just a number, e.g. "1". However, a wall cannot have the same name as an opening or a roof.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Description:

Description
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Description`>/

- Documentation: *Descriptive notes about the wall.*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Wall-Type:

Wall-Type
---------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Wall-Type`>/

- Documentation: *Type of wall (exposure).*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall`>
- Has text value: *True*
- Codes:
    - **"1"** - *basement wall*
    - **"2"** - *exposed wall*
    - **"3"** - *sheltered wall*
    - **"4"** - *party wall*
    - **"5"** - *internal wall*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Total-Wall-Area:

Total-Wall-Area
---------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Total-Wall-Area`>/

- Documentation: *Total wall area in square metres, inclusive of any openings.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/U-Value:

U-Value
-------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/U-Value`>/

- Documentation: *Exposed wall U-value.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Is-Curtain-Walling:

Is-Curtain-Walling
------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Is-Curtain-Walling`>/

- Documentation: *Whether the wall is curtain walling, i.e. a facade construction consisting of a frame of aluminium vertical and horizontal members, infilled with glazing units and opaque panels.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Kappa-Value:

Kappa-Value
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall/Kappa-Value`>/

- Documentation: *Heat capacity per unit area in kJ/m2K.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Walls/SAP-Wall`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types:

SAP-Opening-Types
-----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types`>/

- Documentation2: *Types of exposed openings that make up a particular property. Opening types are used to capture common features shared by multiple openings, to avoid having to record the same data explicitly for each opening.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type:

SAP-Opening-Type
----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type`>/

- Documentation2: *Various measurements for a particular type of exposed opening that makes up a particular property. Opening types are used to capture common features shared by multiple openings, to avoid having to record the same data explicitly for each opening.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Name`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Description`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Data-Source`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Type`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Glazing-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Glazing-Gap`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/IsArgonFilled`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/IsKryptonFilled`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Frame-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Solar-Transmittance`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Frame-Factor`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/U-Value`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *unbounded*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Name:

Name
----

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Name`>/

- Documentation: *Unique name which identifies this opening type. Can be just a number, e.g. "1".*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Description:

Description
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Description`>/

- Documentation: *Descriptive notes about the opening type.*
- Documentation2: *String value with a language code for natural-language text.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Data-Source:

Data-Source
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Data-Source`>/

- Documentation: *The source of the data for this type of opening.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type`>
- Has text value: *True*
- Codes:
    - **"2"** - *manufacturer declaration*
    - **"3"** - *SAP table*
    - **"4"** - *BFRC data*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Type:

Type
----

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Type`>/

- Documentation: *The (physical) type of opening that this opening type represents.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type`>
- Has text value: *True*
- Codes:
    - **"1"** - *solid door*
    - **"2"** - *semi-glazed door*
    - **"3"** - *door to corridor*
    - **"4"** - *window*
    - **"5"** - *roof window*
    - **"6"** - *rooflight*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Glazing-Type:

Glazing-Type
------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Glazing-Type`>/

- Documentation: *The type of glazing; if U-value is from BFRC or manufacturer declaration, give as one of - single - double - triple.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type`>
- Has text value: *True*
- Codes:
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
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Glazing-Gap:

Glazing-Gap
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Glazing-Gap`>/

- Documentation: *Gap between glass panes; only if SAP table and double, triple glazed or secondary glazing.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type`>
- Has text value: *True*
- Codes:
    - **"1"** - *6 mm*
    - **"2"** - *12 mm*
    - **"3"** - *16 mm or more*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/IsArgonFilled:

IsArgonFilled
-------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/IsArgonFilled`>/

- Documentation: *Is the opening argon-filled? Only if SAP table.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/IsKryptonFilled:

IsKryptonFilled
---------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/IsKryptonFilled`>/

- Documentation: *Is the opening krypton-filled? Only if SAP table.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Frame-Type:

Frame-Type
----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Frame-Type`>/

- Documentation: *The type of frame, only if data source is SAP table and it is a window, roof window or half-glazed door.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type`>
- Has text value: *True*
- Codes:
    - **"1"** - *wood*
    - **"2"** - *PVC*
    - **"3"** - *metal no break*
    - **"4"** - *metal 4 mm break*
    - **"5"** - *metal 8 mm break*
    - **"6"** - *metal 12 mm break*
    - **"7"** - *metal 20 mm break*
    - **"8"** - *metal 32 mm break*
    - **"9"** - *unknown*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Solar-Transmittance:

Solar-Transmittance
-------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Solar-Transmittance`>/

- Documentation: *The solar transmittance; not if a door.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Frame-Factor:

Frame-Factor
------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/Frame-Factor`>/

- Documentation: *The frame factor; not if a door.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/U-Value:

U-Value
-------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type/U-Value`>/

- Documentation: *The U-value. For rooflights, the U-value should be in the horizontal plane.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Opening-Types/SAP-Opening-Type`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation:

SAP-Ventilation
---------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/

- Documentation2: *Details of the means by which the building is ventilated*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Closed-Flues-Count`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Open-Flues-Count`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Boilers-Flues-Count`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Other-Flues-Count`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Open-Chimneys-Count`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Blocked-Chimneys-Count`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Fans-Vents-Count`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Flueless-Gas-Fires-Count`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Pressure-Test`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Pressure-Test-Certificate-Number`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Air-Permeability`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Ground-Floor-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Wall-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Has-Draught-Lobby`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/DraughtStripping`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Sheltered-Sides-Count`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Ventilation-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Ventilation-Data-Source`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-System-Index-Number`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Commissioning-Certificate-Number`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Installation-Engineer`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-System-Make-Model`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Wet-Rooms-Count`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Specific-Fan-Power`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Heat-Recovery-Efficiency`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Duct-Type`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Duct-Insulation`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Duct-Insulation-Level`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Duct-Placement`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Measured-Installation`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Room-Fans-Count`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Room-Fans-Specific-Power`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Room-Fans-Count`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Room-Fans-Specific-Power`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Duct-Fans-Count`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Duct-Fans-Specific-Power`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Duct-Fans-Count`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Duct-Fans-Specific-Power`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Wall-Fans-Count`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Wall-Fans-Specific-Power`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Wall-Fans-Count`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Wall-Fans-Specific-Power`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Extract-Fans-Count`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/PSV-Count`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Is-Mechanical-Vent-Approved-Installer-Scheme`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Ducts-Index-Number`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Closed-Flues-Count:

Closed-Flues-Count
------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Closed-Flues-Count`>/

- Documentation: *The number of Closed Flues or chimneys in the Property.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Open-Flues-Count:

Open-Flues-Count
----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Open-Flues-Count`>/

- Documentation: *The number of Open Flues in the Property.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Boilers-Flues-Count:

Boilers-Flues-Count
-------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Boilers-Flues-Count`>/

- Documentation: *The number of Boiler Flues or chimneys in the Property.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Other-Flues-Count:

Other-Flues-Count
-----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Other-Flues-Count`>/

- Documentation: *The number of Other Flues or chimneys in the Property.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Open-Chimneys-Count:

Open-Chimneys-Count
-------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Open-Chimneys-Count`>/

- Documentation: *The number of Open Chimneys in the Property.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Blocked-Chimneys-Count:

Blocked-Chimneys-Count
----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Blocked-Chimneys-Count`>/

- Documentation: *The number of Blocked Chimneys in the Property.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Fans-Vents-Count:

Fans-Vents-Count
----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Fans-Vents-Count`>/

- Documentation: *For backward compatibility only, do not use.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Flueless-Gas-Fires-Count:

Flueless-Gas-Fires-Count
------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Flueless-Gas-Fires-Count`>/

- Documentation: *The number of flueless gas fires in the Property.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Pressure-Test:

Pressure-Test
-------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Pressure-Test`>/

- Documentation: *Whether there has been a pressure test, or whether an assumed value is used for the air permeability.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Codes:
    - **"1"** - *yes (new dwelling, value measured in this dwelling)*
    - **"2"** - *yes (new dwelling, design value)*
    - **"3"** - *no test, value assumed for calculation (new dwelling)*
    - **"4"** - *no test, SAP algorithm used (existing dwelling)*
    - **"5"** - *average for other dwellings of the same type (new dwelling)*
    - **"6"** - *yes (existing dwelling)*
    - **"7"** - *yes (measured value) - low-pressure pulse*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Pressure-Test-Certificate-Number:

Pressure-Test-Certificate-Number
--------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Pressure-Test-Certificate-Number`>/

- Documentation: *The pressure test certificate number or test engineer reference.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Air-Permeability:

Air-Permeability
----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Air-Permeability`>/

- Documentation: *Air permeability; only if pressure test (yes or assumed).*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Ground-Floor-Type:

Ground-Floor-Type
-----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Ground-Floor-Type`>/

- Documentation: *The type of ground floor; nly if no pressure test.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Codes:
    - **"1"** - *not suspended timber*
    - **"2"** - *suspended timber, sealed*
    - **"3"** - *suspended timber, unsealed*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Wall-Type:

Wall-Type
---------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Wall-Type`>/

- Documentation: *The construction of the walls; only if no pressure test.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Codes:
    - **"1"** - *steel or timber frame*
    - **"2"** - *other*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Has-Draught-Lobby:

Has-Draught-Lobby
-----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Has-Draught-Lobby`>/

- Documentation: *Is there a draft lobby? Only if no pressure test.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/DraughtStripping:

DraughtStripping
----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/DraughtStripping`>/

- Documentation: *Draughtstripping percentage; only if no pressure test.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Sheltered-Sides-Count:

Sheltered-Sides-Count
---------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Sheltered-Sides-Count`>/

- Documentation: *The number of sheltered sides in the Property.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Ventilation-Type:

Ventilation-Type
----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Ventilation-Type`>/

- Documentation: *The type of ventilation.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Codes:
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
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Ventilation-Data-Source:

Mechanical-Ventilation-Data-Source
----------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Ventilation-Data-Source`>/

- Documentation: *Source of mechanical ventilation data; only if mechanical ventilation.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Codes:
    - **"1"** - *from database*
    - **"2"** - *from manufacturer declaration*
    - **"3"** - *from SAP table*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-System-Index-Number:

Mechanical-Vent-System-Index-Number
-----------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-System-Index-Number`>/

- Documentation: *Mechanical vent system index number; if mechanical vent data from database (MEV c, MEV dc, MV, MVHR).*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Commissioning-Certificate-Number:

Mechanical-Vent-Commissioning-Certificate-Number
------------------------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Commissioning-Certificate-Number`>/

- Documentation: *Mechanical ventilation Commissioning certificate number .*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Installation-Engineer:

Mechanical-Vent-Installation-Engineer
-------------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Installation-Engineer`>/

- Documentation: *Mechanical ventilation installation engineer registration reference.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-System-Make-Model:

Mechanical-Vent-System-Make-Model
---------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-System-Make-Model`>/

- Documentation: *Mechanical ventilation system make and model.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Wet-Rooms-Count:

Wet-Rooms-Count
---------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Wet-Rooms-Count`>/

- Documentation: *Number of wet rooms, including the kitchen; if mech vent data from manufacturer declaration or database (MEV c, MV, MVHR).*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Specific-Fan-Power:

Mechanical-Vent-Specific-Fan-Power
----------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Specific-Fan-Power`>/

- Documentation: *Mechanical vent specific fan power in watts per (litres per second); if mechanical vent data (PIV from outside, MEV c or dc, MV, MVHR).*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Heat-Recovery-Efficiency:

Mechanical-Vent-Heat-Recovery-Efficiency
----------------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Heat-Recovery-Efficiency`>/

- Documentation: *Mechanical vent heat recovery efficiency percentage; if mechanical vent (MVHR).*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Duct-Type:

Mechanical-Vent-Duct-Type
-------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Duct-Type`>/

- Documentation: *Mechanical vent duct type; if MEV c, MV or MVHR.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Codes:
    - **"1"** - *flexible*
    - **"2"** - *rigid*
    - **"3"** - *semi-rigid*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Duct-Insulation:

Mechanical-Vent-Duct-Insulation
-------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Duct-Insulation`>/

- Documentation: *Mechanical vent duct insulation; if MVHR.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Codes:
    - **"1"** - *not insulated*
    - **"2"** - *insulated*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Duct-Insulation-Level:

Mechanical-Vent-Duct-Insulation-Level
-------------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Duct-Insulation-Level`>/

- Documentation: *Mechanical vent duct insulation; if MVHR.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Codes:
    - **"1"** - *level 1*
    - **"2"** - *level 2*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Duct-Placement:

Mechanical-Vent-Duct-Placement
------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Duct-Placement`>/

- Documentation: *Mechanical ventilation duct insulation; if MVHR.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Codes:
    - **"1"** - *inside heated envelope*
    - **"2"** - *outside heated envelope*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Measured-Installation:

Mechanical-Vent-Measured-Installation
-------------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Measured-Installation`>/

- Documentation: *Mechanical ventilation SPF measured in situ; if MVHR or balanced.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Room-Fans-Count:

Kitchen-Room-Fans-Count
-----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Room-Fans-Count`>/

- Documentation: *MEV dc, number of fans in room, kitchen; if mechanical vent data from database or manufacturer declaration (MEV dc).*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Room-Fans-Specific-Power:

Kitchen-Room-Fans-Specific-Power
--------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Room-Fans-Specific-Power`>/

- Documentation: *MEV dc, specific fan power of fans in room, kitchen, in watts per (litres per second); if mechanical vent data from manufacturer declaration (MEV dc).*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Room-Fans-Count:

Non-Kitchen-Room-Fans-Count
---------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Room-Fans-Count`>/

- Documentation: *MEV dc, number of fans in room, rooms other than kitchen; if mechanical vent data from database or manufacturer declaration (MEV dc).*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Room-Fans-Specific-Power:

Non-Kitchen-Room-Fans-Specific-Power
------------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Room-Fans-Specific-Power`>/

- Documentation: *MEV dc, specific fan power of fans in room, rooms other than kitchen, in watts per (litres per second); if mechanical vent data from manufacturer declaration (MEV dc).*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Duct-Fans-Count:

Kitchen-Duct-Fans-Count
-----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Duct-Fans-Count`>/

- Documentation: *MEV dc, number of fans via duct, kitchen; if mechanical vent data from database or manufacturer declaration (MEV dc).*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Duct-Fans-Specific-Power:

Kitchen-Duct-Fans-Specific-Power
--------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Duct-Fans-Specific-Power`>/

- Documentation: *MEV dc, specific fan power of fans via duct, kitchen, in watts per (litres per second); if mechanical vent data from manufacturer declaration (MEV dc).*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Duct-Fans-Count:

Non-Kitchen-Duct-Fans-Count
---------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Duct-Fans-Count`>/

- Documentation: *MEV dc, number of fans via duct, rooms other than kitchen; if mechanical vent data from database or manufacturer declaration (MEV dc).*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Duct-Fans-Specific-Power:

Non-Kitchen-Duct-Fans-Specific-Power
------------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Duct-Fans-Specific-Power`>/

- Documentation: *MEV dc, specific fan power of fans via duct, rooms other than kitchen, in watts per (litres per second); if mechanical vent data from manufacturer declaration (MEV dc).*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Wall-Fans-Count:

Kitchen-Wall-Fans-Count
-----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Wall-Fans-Count`>/

- Documentation: *MEV dc, number of fans through wall, kitchen; if mechanical vent data from database or manufacturer declaration (MEV dc).*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Wall-Fans-Specific-Power:

Kitchen-Wall-Fans-Specific-Power
--------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Kitchen-Wall-Fans-Specific-Power`>/

- Documentation: *MEV dc, specific fan power of fans through wall, kitchen, in watts per (litres per second); if mechanical vent data from manufacturer declaration (MEV dc).*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Wall-Fans-Count:

Non-Kitchen-Wall-Fans-Count
---------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Wall-Fans-Count`>/

- Documentation: *MEV dc, number of fans through wall, rooms other than kitchen; if mechanical vent data from database or manufacturer declaration (MEV dc).*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Wall-Fans-Specific-Power:

Non-Kitchen-Wall-Fans-Specific-Power
------------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Non-Kitchen-Wall-Fans-Specific-Power`>/

- Documentation: *MEV dc, specific fan power of fans through wall, rooms other than kitchen, in watts per (litres per second); if mechanical vent data from manufacturer declaration (MEV dc).*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Extract-Fans-Count:

Extract-Fans-Count
------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Extract-Fans-Count`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/PSV-Count:

PSV-Count
---------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/PSV-Count`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Is-Mechanical-Vent-Approved-Installer-Scheme:

Is-Mechanical-Vent-Approved-Installer-Scheme
--------------------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Is-Mechanical-Vent-Approved-Installer-Scheme`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Ducts-Index-Number:

Mechanical-Vent-Ducts-Index-Number
----------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation/Mechanical-Vent-Ducts-Index-Number`>/

- Documentation: *Mechanical vent ducts index number; if applicable.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Ventilation`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting:

SAP-Lighting
------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting`>/

- Documentation2: *Details of the main lighting for the property*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights:

Fixed-Lights
------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights`>/

- Documentation: *The record of a lighting type within the building.*
- Documentation2: *Fixed lighting present in the property.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light:

Fixed-Light
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light`>/

- Documentation2: *Various details for each fixed lighting type in the property.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light/Lighting-Efficacy`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light/Lighting-Power`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light/Lighting-Outlets`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *unbounded*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light/Lighting-Efficacy:

Lighting-Efficacy
-----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light/Lighting-Efficacy`>/

- Documentation: *The efficacy of the lighting type in lumens/Watt.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light/Lighting-Power:

Lighting-Power
--------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light/Lighting-Power`>/

- Documentation: *The power of the selected lighting type in Watts.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light/Lighting-Outlets:

Lighting-Outlets
----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light/Lighting-Outlets`>/

- Documentation: *The number of light fitting outlets of that type.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Lighting/Fixed-Lights/Fixed-Light`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Deselected-Improvements:

SAP-Deselected-Improvements
---------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Deselected-Improvements`>/

- Documentation2: *There are 22 possible improvement measures, designated from A to V. This must record measures deselected by DEA (A to V is the full set, only E, N, U and V are considered at the moment for new build).*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Deselected-Improvements/Deselected-Improvement-Measure`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Deselected-Improvements/Deselected-Improvement-Measure:

Deselected-Improvement-Measure
------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Deselected-Improvements`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Deselected-Improvements/Deselected-Improvement-Measure`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Deselected-Improvements`>
- Has text value: *True*
- Codes:
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
- Minimum occurrence: *1*
- Maximum occurrence: *unbounded*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Flat-Details:

SAP-Flat-Details
----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Flat-Details`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Flat-Details/Level`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Flat-Details/Storeys`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Flat-Details/Level:

Level
-----

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Flat-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Flat-Details/Level`>/

- Documentation: *Indication of where a flat is located in a building.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Flat-Details`>
- Has text value: *True*
- Codes:
    - **"0"** - *basement*
    - **"1"** - *ground floor*
    - **"2"** - *mid floor*
    - **"3"** - *top floor*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Flat-Details/Storeys:

Storeys
-------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Flat-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Flat-Details/Storeys`>/

- Documentation: *Count of number of storeys present in the block of flats.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Flat-Details`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features:

SAP-Special-Features
--------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature:

SAP-Special-Feature
-------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Description`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *unbounded*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Description:

Description
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Description`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature:

Energy-Feature
--------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Energy-Saved-Or-Generated`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Saved-Or-Generated-Fuel`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Energy-Used`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Energy-Used-Fuel`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Energy-Saved-Or-Generated:

Energy-Saved-Or-Generated
-------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Energy-Saved-Or-Generated`>/

- Documentation: *Energy saved or generated in kWh/year.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Saved-Or-Generated-Fuel:

Saved-Or-Generated-Fuel
-----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Saved-Or-Generated-Fuel`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature`>
- Has text value: *True*
- Codes:
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
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Energy-Used:

Energy-Used
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Energy-Used`>/

- Documentation: *Energy used in kWh/year.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Energy-Used-Fuel:

Energy-Used-Fuel
----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Energy-Used-Fuel`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature`>
- Has text value: *True*
- Codes:
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
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates:

Air-Change-Rates
----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates`>/

- Documentation: *For Appendix Q procedure that provides air change rates. Only one Special Feature can have data on air change rates.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate:

Air-Change-Rate
---------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate/Air-Change-Rate-Month`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate/Air-Change-Rate-Value`>
- Has text value: *False*
- Minimum occurrence: *12*
- Maximum occurrence: *12*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate/Air-Change-Rate-Month:

Air-Change-Rate-Month
---------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate/Air-Change-Rate-Month`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate`>
- Has text value: *True*
- Codes:
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
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate/Air-Change-Rate-Value:

Air-Change-Rate-Value
---------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate/Air-Change-Rate-Value`>/

- Documentation: *Air change rate in month.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature:

Emissions-Feature
-----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature/Emissions-Saved`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature/Emissions-Created`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature/Emissions-Saved:

Emissions-Saved
---------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature/Emissions-Saved`>/

- Documentation: *Emissions saved in kg/year.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature/Emissions-Created:

Emissions-Created
-----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature/Emissions-Created`>/

- Documentation: *Additional emissions in kg/year.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Design-Water-Use:

Design-Water-Use
----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/Design-Water-Use`>/

- Documentation: *Design limit for total water use.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Has text value: *True*
- Codes:
    - **"1"** - *<= 125 litres per person per day*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling:

SAP-Cooling
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling/Cooled-Area`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling/Cooling-System-Data-Source`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling/Cooling-System-Class`> <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling/System-Energy-Efficiency-Ratio`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling/Cooled-Area:

Cooled-Area
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling/Cooled-Area`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling/Cooling-System-Data-Source:

Cooling-System-Data-Source
--------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling/Cooling-System-Data-Source`>/

- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling`>
- Has text value: *True*
- Codes:
    - **"1"** - *from database*
    - **"2"** - *from manufacturer declaration*
    - **"3"** - *from SAP table*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling/Cooling-System-Class:

Cooling-System-Class
--------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling/Cooling-System-Class`>/

- Documentation: *Data set includes either class or SEER, not both.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling`>
- Has text value: *True*
- Codes:
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
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling/System-Energy-Efficiency-Ratio:

System-Energy-Efficiency-Ratio
------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling`>/<:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling/System-Energy-Efficiency-Ratio`>/

- Documentation: *SEER.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/SAP10-Data/SAP-Property-Details/SAP-Cooling`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/PDF:

PDF
---

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/PDF`>/

- Documentation: *DEPRECATED - DO NOT USE This element is allowed for backwards-compatibility but any data sent here will not be read, processed or stored by the register.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report`>
- Has text value: *True*
- Data type: *<function b64encode at 0x000001EE417E0680>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Insurance-Details:

Insurance-Details
-----------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Insurance-Details`>/

- Documentation2: *Details of the Professional Indemnity Insurance policy used to provide cover against a compensation claim against any particular Home Condition Report. A particular Home Condition Report may be covered by an Professional Indemnity Insurance policy in one of three different ways: * The Home Inspector has personal Professional Indemnity Insurance and the Home Condition Report is covered by this. * The Home Condition Report is covered by an umbrella Professional Indemnity Insurance policy held by the Home Condition Report Supplier that assigned the inspection to the Home Inspector. * An individual insurance policy is taken out to cover the individual report such as the case where the property is unusual and falls outside the Home Inspectors normal Professional Indemnity Insurance policy. A Home Inspector may use any or all of these methods to providing Professional Indemnity Insurance for a Home Condition Report on a case-by-case basis.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report`>
- Child elements: <:ref:`SAP-Compliance-Report/SAP-Report/Insurance-Details/Insurer`> <:ref:`SAP-Compliance-Report/SAP-Report/Insurance-Details/Policy-No`> <:ref:`SAP-Compliance-Report/SAP-Report/Insurance-Details/Effective-Date`> <:ref:`SAP-Compliance-Report/SAP-Report/Insurance-Details/Expiry-Date`> <:ref:`SAP-Compliance-Report/SAP-Report/Insurance-Details/PI-Limit`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Insurance-Details/Insurer:

Insurer
-------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Insurance-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/Insurance-Details/Insurer`>/

- Documentation: *The name of the insurance company that underwrites / issued the insurance policy*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Insurance-Details`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Insurance-Details/Policy-No:

Policy-No
---------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Insurance-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/Insurance-Details/Policy-No`>/

- Documentation: *The policy number of the insurance policy*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Insurance-Details`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Insurance-Details/Effective-Date:

Effective-Date
--------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Insurance-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/Insurance-Details/Effective-Date`>/

- Documentation: *The date that the insurance policy becomes effective (commences cover)*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Insurance-Details`>
- Has text value: *True*
- Data type: *Date string (ISO format)*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Insurance-Details/Expiry-Date:

Expiry-Date
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Insurance-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/Insurance-Details/Expiry-Date`>/

- Documentation: *The date that the insurance policy is supposed to expire.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Insurance-Details`>
- Has text value: *True*
- Data type: *Date string (ISO format)*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/Insurance-Details/PI-Limit:

PI-Limit
--------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/Insurance-Details`>/<:ref:`SAP-Compliance-Report/SAP-Report/Insurance-Details/PI-Limit`>/

- Documentation: *The upper limit of the Professional Indemnity cover provided by the insurance policy.*
- Documentation2: *Extension of a Decimal value for use with monetary values where a currency code needs to be specified. The currency code is actually metadata about the value so, in line with good XML practice, the Currency Code is declared as an XML-Attribute of the Money datatype rather than as a separate XML-Element. The currency attribute should then include a list of valid currencies codes that are supported.*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report/Insurance-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/SAP-Report/ExternalDefinitions-Revision-Number:

ExternalDefinitions-Revision-Number
-----------------------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report`>/<:ref:`SAP-Compliance-Report/SAP-Report/ExternalDefinitions-Revision-Number`>/

- Documentation: *A number indicating the version of related ExternalDefinitions.xsd*
- Parent element: <:ref:`SAP-Compliance-Report/SAP-Report`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/Client-Name:

Client-Name
-----------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/Client-Name`>/

- Documentation: *Name of the client. External to the EPC schema for GDPR purposes.*
- Parent element: <:ref:`SAP-Compliance-Report`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/Client-Company:

Client-Company
--------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/Client-Company`>/

- Documentation: *Company name of the client. External to the EPC schema for GDPR purposes.*
- Parent element: <:ref:`SAP-Compliance-Report`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/Client-Address:

Client-Address
--------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/Client-Address`>/

- Documentation: *Address of the client. External to the EPC schema for GDPR purposes.*
- Documentation2: *An address is composed of a number of structured elements such as Postcode, Post-Town, Street etc.*
- Parent element: <:ref:`SAP-Compliance-Report`>
- Child elements: <:ref:`SAP-Compliance-Report/Client-Address/Address-Line-1`> <:ref:`SAP-Compliance-Report/Client-Address/Address-Line-2`> <:ref:`SAP-Compliance-Report/Client-Address/Address-Line-3`> <:ref:`SAP-Compliance-Report/Client-Address/Post-Town`> <:ref:`SAP-Compliance-Report/Client-Address/Postcode`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/Client-Address/Address-Line-1:

Address-Line-1
--------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/Client-Address`>/<:ref:`SAP-Compliance-Report/Client-Address/Address-Line-1`>/

- Parent element: <:ref:`SAP-Compliance-Report/Client-Address`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/Client-Address/Address-Line-2:

Address-Line-2
--------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/Client-Address`>/<:ref:`SAP-Compliance-Report/Client-Address/Address-Line-2`>/

- Parent element: <:ref:`SAP-Compliance-Report/Client-Address`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/Client-Address/Address-Line-3:

Address-Line-3
--------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/Client-Address`>/<:ref:`SAP-Compliance-Report/Client-Address/Address-Line-3`>/

- Parent element: <:ref:`SAP-Compliance-Report/Client-Address`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/Client-Address/Post-Town:

Post-Town
---------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/Client-Address`>/<:ref:`SAP-Compliance-Report/Client-Address/Post-Town`>/

- Parent element: <:ref:`SAP-Compliance-Report/Client-Address`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/Client-Address/Postcode:

Postcode
--------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/Client-Address`>/<:ref:`SAP-Compliance-Report/Client-Address/Postcode`>/

- Documentation: *The Postcode for the Address*
- Parent element: <:ref:`SAP-Compliance-Report/Client-Address`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _SAP-Compliance-Report/Is-Multiple-Compliance:

Is-Multiple-Compliance
----------------------

<:ref:`SAP-Compliance-Report`>/<:ref:`SAP-Compliance-Report/Is-Multiple-Compliance`>/

- Documentation: *Is the compliance report part of a multiple compliance calculation.*
- Parent element: <:ref:`SAP-Compliance-Report`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

