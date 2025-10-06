.. _rdsap_xml_reference:

RdSAP XML reference
===================

This page contains the documentation for the XML schema `RdSAP-Schema-21.0.0 <https://github.com/communitiesuk/epb-register-api/tree/master/api/schemas/xml/RdSAP-Schema-21.0.0/RdSAP>`__.

This XML schema describes the format of the XML input files for RdSAP 10 calculations.

The root XML element is a :ref:`RdSAP-Report` element.

.. _RdSAP-Report:

RdSAP-Report
------------

<:ref:`RdSAP-Report`>/

- Child elements: <:ref:`RdSAP-Report/Calculation-Software-Name`> <:ref:`RdSAP-Report/Calculation-Software-Version`> <:ref:`RdSAP-Report/User-Interface-Name`> <:ref:`RdSAP-Report/User-Interface-Version`> <:ref:`RdSAP-Report/Schema-Version-Original`> <:ref:`RdSAP-Report/Schema-Version-Current`> <:ref:`RdSAP-Report/SAP-Version`> <:ref:`RdSAP-Report/PCDF-Revision-Number`> <:ref:`RdSAP-Report/Previous-EPC-Check`> <:ref:`RdSAP-Report/Energy-Assessment`> <:ref:`RdSAP-Report/SAP-Data`> <:ref:`RdSAP-Report/Report-Header`> <:ref:`RdSAP-Report/Insurance-Details`> <:ref:`RdSAP-Report/ExternalDefinitions-Revision-Number`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Calculation-Software-Name:

Calculation-Software-Name
-------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Calculation-Software-Name`>/

- Documentation: *Name of the software used to perform the SAP calculation.*
- Parent element: <:ref:`RdSAP-Report`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Calculation-Software-Version:

Calculation-Software-Version
----------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Calculation-Software-Version`>/

- Documentation: *Version of the software used to perform the SAP calculation.*
- Parent element: <:ref:`RdSAP-Report`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/User-Interface-Name:

User-Interface-Name
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/User-Interface-Name`>/

- Documentation: *The name of the user interface used for data entry. This can be the same as Calculation-Software-Name, or different.*
- Parent element: <:ref:`RdSAP-Report`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/User-Interface-Version:

User-Interface-Version
----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/User-Interface-Version`>/

- Documentation: *The version of the user interface used for data entry. This can be the same as Calculation-Software-Version, or different.*
- Parent element: <:ref:`RdSAP-Report`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Schema-Version-Original:

Schema-Version-Original
-----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Schema-Version-Original`>/

- Documentation: *The schema version that the data conformed to when it was lodged.*
- Parent element: <:ref:`RdSAP-Report`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Schema-Version-Current:

Schema-Version-Current
----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Schema-Version-Current`>/

- Documentation: *The schema version to which the data conforms. This node is inserted by the register when a retrieval is requested. It must not be present in a lodgement being sent to the register.*
- Parent element: <:ref:`RdSAP-Report`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Version:

SAP-Version
-----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Version`>/

- Documentation: *Version of RdSAP that was used for the assessment.*
- Parent element: <:ref:`RdSAP-Report`>
- Has text value: *True*
- Codes:
    - **"9.80"** - *SAP 2005 version 9.80, dated October 2005*
    - **"9.81"** - *SAP version 9.81, dated January 2008*
    - **"9.82"** - *SAP version 9.82, dated Jun 2008*
    - **"9.83"** - *SAP version 9.83, dated Jun 2009*
    - **"9.90"** - *SAP version 9.90, dated March 2010*
    - **"9.91"** - *SAP version 9.91, dated January 2012*
    - **"9.92"** - *SAP version 9.92, dated Oct 2013*
    - **"9.93"** - *SAP version 9.93, dated Jun 2017*
    - **"9.94"** - *SAP version 9.94, dated Feb 2019*
    - **"10.2"** - *SAP version 10.2, dated April 2023*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/PCDF-Revision-Number:

PCDF-Revision-Number
--------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/PCDF-Revision-Number`>/

- Parent element: <:ref:`RdSAP-Report`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Previous-EPC-Check:

Previous-EPC-Check
------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Previous-EPC-Check`>/

- Parent element: <:ref:`RdSAP-Report`>
- Child elements: <:ref:`RdSAP-Report/Previous-EPC-Check/Previous-EPC-Checked`> <:ref:`RdSAP-Report/Previous-EPC-Check/Previous-EPC-Exists`> <:ref:`RdSAP-Report/Previous-EPC-Check/Previous-EPC-Reason-Code`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Previous-EPC-Check/Previous-EPC-Checked:

Previous-EPC-Checked
--------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Previous-EPC-Check`>/<:ref:`RdSAP-Report/Previous-EPC-Check/Previous-EPC-Checked`>/

- Documentation: *Confirm a check for the existence of an EPC before carrying out another energy assessment.*
- Parent element: <:ref:`RdSAP-Report/Previous-EPC-Check`>
- Has text value: *True*
- Codes:
    - **"Y"** - *Confirm a check for the existence of an EPC before carrying out another energy assessment*
    - **"NR"** - *not recorded; for backwards compatibility only, do not use*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Previous-EPC-Check/Previous-EPC-Exists:

Previous-EPC-Exists
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Previous-EPC-Check`>/<:ref:`RdSAP-Report/Previous-EPC-Check/Previous-EPC-Exists`>/

- Documentation: *Does an EPC exist at the point of carrying out this energy assessment.*
- Parent element: <:ref:`RdSAP-Report/Previous-EPC-Check`>
- Has text value: *True*
- Codes:
    - **"Y"** - *A previous EPC exists*
    - **"N"** - *A previous EPC does not exist*
    - **"NR"** - *not recorded; for backwards compatibility only, do not use*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Previous-EPC-Check/Previous-EPC-Reason-Code:

Previous-EPC-Reason-Code
------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Previous-EPC-Check`>/<:ref:`RdSAP-Report/Previous-EPC-Check/Previous-EPC-Reason-Code`>/

- Documentation: *Reason for not using a previous RdSAP EPC.*
- Parent element: <:ref:`RdSAP-Report/Previous-EPC-Check`>
- Has text value: *True*
- Codes:
    - **"1"** - *EPC has expired*
    - **"2"** - *Building fabric and/or services has changed since the last EPC assessment and a new EPC has been commissioned for that building*
    - **"3"** - *Assessor instructed to produce a new EPC upon request from building owner/tenant/landlord after confirming to the requestor that a valid EPC already exists*
    - **"4"** - *Duplicate EPC produced by systematic or human error*
    - **"5"** - *Replacement of an erroneous EPC where the original EPC has been marked 'not for issue'*
    - **"6"** - *Replacement of an erroneous EPC where the original EPC has not been marked 'not for issue'*
    - **"7"** - *Green Deal Advice Report: existing EPC pre-dates 1 April 2012*
    - **"8"** - *Green Deal Advice Report: previous EPC is inaccurate*
    - **"9"** - *Renewable Heat Incentive (RHI): existing EPC is more than 24 months old on the date of RHI application*
    - **"10"** - *Feed-In-Tariff: householder has chosen to undertake energy efficiency measures to improve the previous EPC rating before installing solar panels and applying for FITs*
    - **"11"** - *Rental purposes: existing EPC is more than 10 years old or is below an E rating*
    - **"12"** - *A valid EPC is required to demonstrate that the building has an EPC rating of E, F or G to determine if the householder is eligible for Energy Company Obligation scheme measures*
    - **"13"** - *A valid EPC is required to demonstrate that the building has an EPC rating of D to determine if the householder is eligible for Energy Company Obligation scheme innovation measures*
    - **"14"** - *A valid EPC is required to demonstrate that the building has an EPC rating of E, F or G to determine if the social housing tenant is eligible for the Energy Company Obligation scheme First Time Central Heating measures*
    - **"15"** - *A valid EPC less than 12 weeks old is needed to support production of a Home Report for the marketed sale of the dwelling*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment:

Energy-Assessment
-----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/

- Documentation2: *Energy Efficiency Assessment Report is an inspection report whose purpose is to assess the energy efficiency of the inspected property and provide energy ratings for the significant heat-loss features of the property. The report also identifies a number of potential improvements that may be made to the property in order to increase the energy efficiency.*
- Parent element: <:ref:`RdSAP-Report`>
- Child elements: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`> <:ref:`RdSAP-Report/Energy-Assessment/Energy-Use`> <:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements`> <:ref:`RdSAP-Report/Energy-Assessment/LZC-Energy-Sources`> <:ref:`RdSAP-Report/Energy-Assessment/Addendum`> <:ref:`RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive`> <:ref:`RdSAP-Report/Energy-Assessment/Green-Deal-Package`> <:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Property-Summary:

Property-Summary
----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/

- Parent element: <:ref:`RdSAP-Report/Energy-Assessment`>
- Child elements: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Wall`> <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Roof`> <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Floor`> <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Window`> <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Air-Tightness`> <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Main-Heating`> <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls`> <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Hot-Water`> <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Lighting`> <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating`> <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Has-Hot-Water-Cylinder`> <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Has-Heated-Separate-Conservatory`> <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Dwelling-Type`> <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Total-Floor-Area`> <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Has-Fixed-Air-Conditioning`> <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Multiple-Glazed-Proportion`> <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Multiple-Glazed-Proportion-NR`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Wall:

Wall
----

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Wall`>/

- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>
- Child elements: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Wall/Description`> <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Wall/Energy-Efficiency-Rating`> <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Wall/Environmental-Efficiency-Rating`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *unbounded*

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Wall/Description:

Description
-----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Wall`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Wall/Description`>/

- Documentation: *Overall description of the property feature*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Wall`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Wall/Energy-Efficiency-Rating:

Energy-Efficiency-Rating
------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Wall`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Wall/Energy-Efficiency-Rating`>/

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Wall`>
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

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Wall/Environmental-Efficiency-Rating:

Environmental-Efficiency-Rating
-------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Wall`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Wall/Environmental-Efficiency-Rating`>/

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Wall`>
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

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Roof:

Roof
----

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Roof`>/

- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>
- Child elements: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Roof/Description`> <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Roof/Energy-Efficiency-Rating`> <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Roof/Environmental-Efficiency-Rating`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *unbounded*

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Roof/Description:

Description
-----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Roof`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Roof/Description`>/

- Documentation: *Overall description of the property feature*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Roof`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Roof/Energy-Efficiency-Rating:

Energy-Efficiency-Rating
------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Roof`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Roof/Energy-Efficiency-Rating`>/

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Roof`>
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

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Roof/Environmental-Efficiency-Rating:

Environmental-Efficiency-Rating
-------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Roof`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Roof/Environmental-Efficiency-Rating`>/

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Roof`>
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

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Floor:

Floor
-----

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Floor`>/

- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>
- Child elements: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Floor/Description`> <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Floor/Energy-Efficiency-Rating`> <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Floor/Environmental-Efficiency-Rating`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *unbounded*

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Floor/Description:

Description
-----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Floor`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Floor/Description`>/

- Documentation: *Overall description of the property feature*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Floor`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Floor/Energy-Efficiency-Rating:

Energy-Efficiency-Rating
------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Floor`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Floor/Energy-Efficiency-Rating`>/

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Floor`>
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

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Floor/Environmental-Efficiency-Rating:

Environmental-Efficiency-Rating
-------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Floor`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Floor/Environmental-Efficiency-Rating`>/

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Floor`>
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

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Window:

Window
------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Window`>/

- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>
- Child elements: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Window/Description`> <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Window/Energy-Efficiency-Rating`> <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Window/Environmental-Efficiency-Rating`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Window/Description:

Description
-----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Window`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Window/Description`>/

- Documentation: *Overall description of the property feature*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Window`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Window/Energy-Efficiency-Rating:

Energy-Efficiency-Rating
------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Window`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Window/Energy-Efficiency-Rating`>/

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Window`>
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

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Window/Environmental-Efficiency-Rating:

Environmental-Efficiency-Rating
-------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Window`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Window/Environmental-Efficiency-Rating`>/

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Window`>
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

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Air-Tightness:

Air-Tightness
-------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Air-Tightness`>/

- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>
- Child elements: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Air-Tightness/Description`> <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Air-Tightness/Energy-Efficiency-Rating`> <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Air-Tightness/Environmental-Efficiency-Rating`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Air-Tightness/Description:

Description
-----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Air-Tightness`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Air-Tightness/Description`>/

- Documentation: *Overall description of the property feature*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Air-Tightness`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Air-Tightness/Energy-Efficiency-Rating:

Energy-Efficiency-Rating
------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Air-Tightness`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Air-Tightness/Energy-Efficiency-Rating`>/

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Air-Tightness`>
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

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Air-Tightness/Environmental-Efficiency-Rating:

Environmental-Efficiency-Rating
-------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Air-Tightness`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Air-Tightness/Environmental-Efficiency-Rating`>/

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Air-Tightness`>
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

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Main-Heating:

Main-Heating
------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Main-Heating`>/

- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>
- Child elements: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Main-Heating/Description`> <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Main-Heating/Energy-Efficiency-Rating`> <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Main-Heating/Environmental-Efficiency-Rating`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *2*

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Main-Heating/Description:

Description
-----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Main-Heating`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Main-Heating/Description`>/

- Documentation: *Overall description of the property feature*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Main-Heating/Energy-Efficiency-Rating:

Energy-Efficiency-Rating
------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Main-Heating`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Main-Heating/Energy-Efficiency-Rating`>/

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Main-Heating`>
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

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Main-Heating/Environmental-Efficiency-Rating:

Environmental-Efficiency-Rating
-------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Main-Heating`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Main-Heating/Environmental-Efficiency-Rating`>/

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Main-Heating`>
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

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls:

Main-Heating-Controls
---------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls`>/

- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>
- Child elements: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls/Description`> <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls/Energy-Efficiency-Rating`> <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls/Environmental-Efficiency-Rating`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *2*

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls/Description:

Description
-----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls/Description`>/

- Documentation: *Overall description of the property feature*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls/Energy-Efficiency-Rating:

Energy-Efficiency-Rating
------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls/Energy-Efficiency-Rating`>/

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls`>
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

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls/Environmental-Efficiency-Rating:

Environmental-Efficiency-Rating
-------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls/Environmental-Efficiency-Rating`>/

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Main-Heating-Controls`>
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

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Hot-Water:

Hot-Water
---------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Hot-Water`>/

- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>
- Child elements: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Hot-Water/Description`> <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Hot-Water/Energy-Efficiency-Rating`> <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Hot-Water/Environmental-Efficiency-Rating`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Hot-Water/Description:

Description
-----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Hot-Water`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Hot-Water/Description`>/

- Documentation: *Overall description of the property feature*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Hot-Water`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Hot-Water/Energy-Efficiency-Rating:

Energy-Efficiency-Rating
------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Hot-Water`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Hot-Water/Energy-Efficiency-Rating`>/

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Hot-Water`>
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

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Hot-Water/Environmental-Efficiency-Rating:

Environmental-Efficiency-Rating
-------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Hot-Water`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Hot-Water/Environmental-Efficiency-Rating`>/

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Hot-Water`>
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

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Lighting:

Lighting
--------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Lighting`>/

- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>
- Child elements: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Lighting/Description`> <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Lighting/Energy-Efficiency-Rating`> <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Lighting/Environmental-Efficiency-Rating`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Lighting/Description:

Description
-----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Lighting`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Lighting/Description`>/

- Documentation: *Overall description of the property feature*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Lighting`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Lighting/Energy-Efficiency-Rating:

Energy-Efficiency-Rating
------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Lighting`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Lighting/Energy-Efficiency-Rating`>/

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Lighting`>
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

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Lighting/Environmental-Efficiency-Rating:

Environmental-Efficiency-Rating
-------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Lighting`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Lighting/Environmental-Efficiency-Rating`>/

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Lighting`>
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

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating:

Secondary-Heating
-----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating`>/

- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>
- Child elements: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating/Description`> <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating/Energy-Efficiency-Rating`> <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating/Environmental-Efficiency-Rating`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating/Description:

Description
-----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating/Description`>/

- Documentation: *Overall description of the property feature*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating/Energy-Efficiency-Rating:

Energy-Efficiency-Rating
------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating/Energy-Efficiency-Rating`>/

- Documentation: *Overall summary of the energy efficiency of the property feature.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating`>
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

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating/Environmental-Efficiency-Rating:

Environmental-Efficiency-Rating
-------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating/Environmental-Efficiency-Rating`>/

- Documentation: *Summary of the environmental efficiency of the property feature*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Secondary-Heating`>
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

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Has-Hot-Water-Cylinder:

Has-Hot-Water-Cylinder
----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Has-Hot-Water-Cylinder`>/

- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Has-Heated-Separate-Conservatory:

Has-Heated-Separate-Conservatory
--------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Has-Heated-Separate-Conservatory`>/

- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Dwelling-Type:

Dwelling-Type
-------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Dwelling-Type`>/

- Documentation: *A string such as Detached house or Top-floor flat*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Total-Floor-Area:

Total-Floor-Area
----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Total-Floor-Area`>/

- Documentation: *A number such as 125*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Has-Fixed-Air-Conditioning:

Has-Fixed-Air-Conditioning
--------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Has-Fixed-Air-Conditioning`>/

- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Multiple-Glazed-Proportion:

Multiple-Glazed-Proportion
--------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Multiple-Glazed-Proportion`>/

- Documentation: *If all windows measured, fraction of windows that are multiply glazed to nearest 1%. If windows not measured, same as SAP-Data\Energy-Assessment\Property-Summary\Multiple-Glazed-Proportion.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Property-Summary/Multiple-Glazed-Proportion-NR:

Multiple-Glazed-Proportion-NR
-----------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>/<:ref:`RdSAP-Report/Energy-Assessment/Property-Summary/Multiple-Glazed-Proportion-NR`>/

- Documentation: *For backward compatibility only, do not use.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Property-Summary`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Energy-Use:

Energy-Use
----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Energy-Use`>/

- Documentation2: *Part of an Energy Report summarising the results of the various energy calculations made by the Home Inspector.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment`>
- Child elements: <:ref:`RdSAP-Report/Energy-Assessment/Energy-Use/Energy-Rating-Current`> <:ref:`RdSAP-Report/Energy-Assessment/Energy-Use/Energy-Rating-Potential`> <:ref:`RdSAP-Report/Energy-Assessment/Energy-Use/Energy-Rating-Average`> <:ref:`RdSAP-Report/Energy-Assessment/Energy-Use/Environmental-Impact-Current`> <:ref:`RdSAP-Report/Energy-Assessment/Energy-Use/Environmental-Impact-Potential`> <:ref:`RdSAP-Report/Energy-Assessment/Energy-Use/Energy-Consumption-Current`> <:ref:`RdSAP-Report/Energy-Assessment/Energy-Use/Energy-Consumption-Potential`> <:ref:`RdSAP-Report/Energy-Assessment/Energy-Use/CO2-Emissions-Current`> <:ref:`RdSAP-Report/Energy-Assessment/Energy-Use/CO2-Emissions-Current-Per-Floor-Area`> <:ref:`RdSAP-Report/Energy-Assessment/Energy-Use/CO2-Emissions-Potential`> <:ref:`RdSAP-Report/Energy-Assessment/Energy-Use/Lighting-Cost-Current`> <:ref:`RdSAP-Report/Energy-Assessment/Energy-Use/Lighting-Cost-Potential`> <:ref:`RdSAP-Report/Energy-Assessment/Energy-Use/Heating-Cost-Current`> <:ref:`RdSAP-Report/Energy-Assessment/Energy-Use/Heating-Cost-Potential`> <:ref:`RdSAP-Report/Energy-Assessment/Energy-Use/Hot-Water-Cost-Current`> <:ref:`RdSAP-Report/Energy-Assessment/Energy-Use/Hot-Water-Cost-Potential`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Energy-Use/Energy-Rating-Current:

Energy-Rating-Current
---------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`RdSAP-Report/Energy-Assessment/Energy-Use/Energy-Rating-Current`>/

- Documentation: *The Current Energy Rating of the Property*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Energy-Use/Energy-Rating-Potential:

Energy-Rating-Potential
-----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`RdSAP-Report/Energy-Assessment/Energy-Use/Energy-Rating-Potential`>/

- Documentation: *The overall Energy Rating for the Property being assessed.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Energy-Use/Energy-Rating-Average:

Energy-Rating-Average
---------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`RdSAP-Report/Energy-Assessment/Energy-Use/Energy-Rating-Average`>/

- Documentation: *Average SAP rating for the country concerned. 0 if unknown or not applicable*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Energy-Use/Environmental-Impact-Current:

Environmental-Impact-Current
----------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`RdSAP-Report/Energy-Assessment/Energy-Use/Environmental-Impact-Current`>/

- Documentation: *The estimated current Environmental Impact Rating of the property*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Energy-Use/Environmental-Impact-Potential:

Environmental-Impact-Potential
------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`RdSAP-Report/Energy-Assessment/Energy-Use/Environmental-Impact-Potential`>/

- Documentation: *The estimated potential Environmental Impact Rating of the property*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Energy-Use/Energy-Consumption-Current:

Energy-Consumption-Current
--------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`RdSAP-Report/Energy-Assessment/Energy-Use/Energy-Consumption-Current`>/

- Documentation: *Estimated total energy consumption for the Property in a 12 month period. Value is Kilowatt Hours per Square Metre (kWh/m2)*
- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Energy-Use/Energy-Consumption-Potential:

Energy-Consumption-Potential
----------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`RdSAP-Report/Energy-Assessment/Energy-Use/Energy-Consumption-Potential`>/

- Documentation: *Estimated total energy consumption for the Property in a 12 month period. Value is Kilowatt Hours per Square Metre (kWh/m2)*
- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Energy-Use/CO2-Emissions-Current:

CO2-Emissions-Current
---------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`RdSAP-Report/Energy-Assessment/Energy-Use/CO2-Emissions-Current`>/

- Documentation: *CO2 emissions per year in tonnes/year.*
- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Energy-Use/CO2-Emissions-Current-Per-Floor-Area:

CO2-Emissions-Current-Per-Floor-Area
------------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`RdSAP-Report/Energy-Assessment/Energy-Use/CO2-Emissions-Current-Per-Floor-Area`>/

- Documentation: *CO2 emissions per square metre floor area per year in kg/m2.*
- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Energy-Use/CO2-Emissions-Potential:

CO2-Emissions-Potential
-----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`RdSAP-Report/Energy-Assessment/Energy-Use/CO2-Emissions-Potential`>/

- Documentation: *Estimated value in Tonnes per Year of the total CO2 emissions produced by the Property in 12 month period.*
- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Energy-Use/Lighting-Cost-Current:

Lighting-Cost-Current
---------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`RdSAP-Report/Energy-Assessment/Energy-Use/Lighting-Cost-Current`>/

- Documentation: *The current estimated cost of Lighting for the property*
- Documentation2: *Extension of a Decimal value for use with monetary values where a currency code needs to be specified. The currency code is actually metadata about the value so, in line with good XML practice, the Currency Code is declared as an XML-Attribute of the Money datatype rather than as a separate XML-Element. The currency attribute should then include a list of valid currencies codes that are supported.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Energy-Use/Lighting-Cost-Potential:

Lighting-Cost-Potential
-----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`RdSAP-Report/Energy-Assessment/Energy-Use/Lighting-Cost-Potential`>/

- Documentation: *The current estimated cost of Lighting for the property*
- Documentation2: *Extension of a Decimal value for use with monetary values where a currency code needs to be specified. The currency code is actually metadata about the value so, in line with good XML practice, the Currency Code is declared as an XML-Attribute of the Money datatype rather than as a separate XML-Element. The currency attribute should then include a list of valid currencies codes that are supported.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Energy-Use/Heating-Cost-Current:

Heating-Cost-Current
--------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`RdSAP-Report/Energy-Assessment/Energy-Use/Heating-Cost-Current`>/

- Documentation: *The current estimated cost of Heating for the property*
- Documentation2: *Extension of a Decimal value for use with monetary values where a currency code needs to be specified. The currency code is actually metadata about the value so, in line with good XML practice, the Currency Code is declared as an XML-Attribute of the Money datatype rather than as a separate XML-Element. The currency attribute should then include a list of valid currencies codes that are supported.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Energy-Use/Heating-Cost-Potential:

Heating-Cost-Potential
----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`RdSAP-Report/Energy-Assessment/Energy-Use/Heating-Cost-Potential`>/

- Documentation: *The current estimated cost of Heating for the property*
- Documentation2: *Extension of a Decimal value for use with monetary values where a currency code needs to be specified. The currency code is actually metadata about the value so, in line with good XML practice, the Currency Code is declared as an XML-Attribute of the Money datatype rather than as a separate XML-Element. The currency attribute should then include a list of valid currencies codes that are supported.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Energy-Use/Hot-Water-Cost-Current:

Hot-Water-Cost-Current
----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`RdSAP-Report/Energy-Assessment/Energy-Use/Hot-Water-Cost-Current`>/

- Documentation: *|The current estimated cost of Hot Water for the property*
- Documentation2: *Extension of a Decimal value for use with monetary values where a currency code needs to be specified. The currency code is actually metadata about the value so, in line with good XML practice, the Currency Code is declared as an XML-Attribute of the Money datatype rather than as a separate XML-Element. The currency attribute should then include a list of valid currencies codes that are supported.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Energy-Use/Hot-Water-Cost-Potential:

Hot-Water-Cost-Potential
------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Energy-Use`>/<:ref:`RdSAP-Report/Energy-Assessment/Energy-Use/Hot-Water-Cost-Potential`>/

- Documentation: *|The current estimated cost of Hot Water for the property*
- Documentation2: *Extension of a Decimal value for use with monetary values where a currency code needs to be specified. The currency code is actually metadata about the value so, in line with good XML practice, the Currency Code is declared as an XML-Attribute of the Money datatype rather than as a separate XML-Element. The currency attribute should then include a list of valid currencies codes that are supported.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Energy-Use`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Suggested-Improvements:

Suggested-Improvements
----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements`>/

- Documentation2: *Part of an Energy Report that describes the a set of improvements that the Home Inspector considers would contribute to the overall energy rating of the property.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment`>
- Child elements: <:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement:

Improvement
-----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>/

- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements`>
- Child elements: <:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Sequence`> <:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Category`> <:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Type`> <:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Typical-Saving`> <:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Energy-Performance-Rating`> <:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Environmental-Impact-Rating`> <:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details`> <:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Indicative-Cost`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *unbounded*

.. _RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Sequence:

Sequence
--------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Sequence`>/

- Documentation: *Sequence of the Suggested Improvements within the set of Suggested Improvements. This is used to order the Recommendations on the output HCR / EPC so that the cumulative Ratings make sense. The Improved Energy Ratings that result from carrying out a Suggested Improvement are cumulative and assume that the improvements have been installed in the order they appear in the list. Hence they must be sequenced.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Category:

Improvement-Category
--------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Category`>/

- Documentation: *The category of improvement. This identifies where on the report the recommendation is printed.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>
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

.. _RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Type:

Improvement-Type
----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Type`>/

- Documentation: *Suggested work to be carried out on the Property to improve its energy efficiency.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>
- Has text value: *True*
- Codes:
    - **"A"** - *Loft Insulation*
    - **"A2"** - *Flat roof insulation*
    - **"A3"** - *Room-in-roof insulation*
    - **"B"** - *Cavity wall insulation*
    - **"B4"** - *Party wall insulation*
    - **"C"** - *Hot water cylinder insulation*
    - **"D"** - *Draughtproofing*
    - **"E"** - *Low energy lights*
    - **"F"** - *Cylinder thermostat*
    - **"G"** - *Heating controls for wet central heating system*
    - **"G2"** - *Water heating controls*
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
    - **"U1"** - *PV Battery*
    - **"U2"** - *PV Diverter*
    - **"V"** - *Wind turbine (roof mounted)*
    - **"V2"** - *Wind turbine (on mast)*
    - **"W"** - *Floor insulation; for backwards compatibility only, do not use*
    - **"W1"** - *Insulation of suspended floor*
    - **"W2"** - *Insulation of solid ground floor*
    - **"X"** - *Insulated doors*
    - **"Y"** - *Instantaneous waste water heat recovery*
    - **"Y2"** - *Storage waste water heat recovery*
    - **"Z1"** - *Air or ground source heat pump*
    - **"Z2"** - *Air or ground source heat pump with underfloor heating*
    - **"Z3"** - *Micro-CHP*
    - **"NR"** - *Not recorded*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Typical-Saving:

Typical-Saving
--------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Typical-Saving`>/

- Documentation: *Typical savings (in British Pounds) per year if the suggested improvement is carried out. 0 if not assessed*
- Documentation2: *Extension of a Decimal value for use with monetary values where a currency code needs to be specified. The currency code is actually metadata about the value so, in line with good XML practice, the Currency Code is declared as an XML-Attribute of the Money datatype rather than as a separate XML-Element. The currency attribute should then include a list of valid currencies codes that are supported.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Energy-Performance-Rating:

Energy-Performance-Rating
-------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Energy-Performance-Rating`>/

- Documentation: *The estimated Energy performance rating of the Property after the Suggested Improvement has been carried out providing any preceding Suggested Improvement has also been carried out. 0 if not assessed*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Environmental-Impact-Rating:

Environmental-Impact-Rating
---------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Environmental-Impact-Rating`>/

- Documentation: *The estimated Environmental Impact rating of the Property after the Suggested Improvement has been carried out providing any preceding Suggested Improvement has also been carried out. 0 if not assessed*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details:

Improvement-Details
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details`>/

- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>
- Child elements: <:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts`> <:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Number`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts:

Improvement-Texts
-----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts`>/

- Documentation: *For backward compatibility only*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details`>
- Child elements: <:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Summary`> <:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Heading`> <:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Description`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Summary:

Improvement-Summary
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Summary`>/

- Documentation: *A short description of the suggested improvement.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Heading:

Improvement-Heading
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Heading`>/

- Documentation: *Text to precede the improvement description. If this field is not provided the 'Improvement-Summary' is used instead.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Description:

Improvement-Description
-----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Description`>/

- Documentation: *Detailed description of the suggested improvement.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Texts`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Number:

Improvement-Number
------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details/Improvement-Number`>/

- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Improvement-Details`>
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
    - **"45"** - *Flat roof or sloping ceiling insulation*
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
    - **"56"** - *Replacement glazing units*
    - **"57"** - *Suspended floor insulation*
    - **"58"** - *Solid floor insulation*
    - **"59"** - *High heat retention storage heaters and dual immersion cylinder*
    - **"60"** - *High heat retention storage heaters*
    - **"61"** - *High heat retention storage heaters and dual immersion cylinder*
    - **"62"** - *High heat retention storage heaters*
    - **"63"** - *Party wall insulation*
    - **"65"** - *Internal insulation with cavity wall insulation*
    - **"66"** - *Heating controls for wet central heating system*
    - **"70"** - *Water Heating Controls*
    - **"72"** - *PV Battery*
    - **"73"** - *PV Diverter*
    - **"75"** - *Ground source heat pump with radiators*
    - **"76"** - *Ground source heat pump with underfloor heating*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Indicative-Cost:

Indicative-Cost
---------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>/<:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement/Indicative-Cost`>/

- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Suggested-Improvements/Improvement`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/LZC-Energy-Sources:

LZC-Energy-Sources
------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/LZC-Energy-Sources`>/

- Parent element: <:ref:`RdSAP-Report/Energy-Assessment`>
- Child elements: <:ref:`RdSAP-Report/Energy-Assessment/LZC-Energy-Sources/LZC-Energy-Source`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/LZC-Energy-Sources/LZC-Energy-Source:

LZC-Energy-Source
-----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/LZC-Energy-Sources`>/<:ref:`RdSAP-Report/Energy-Assessment/LZC-Energy-Sources/LZC-Energy-Source`>/

- Documentation: *Low and zero carbon energy source(s) for the property.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/LZC-Energy-Sources`>
- Has text value: *True*
- Codes:
    - **"1"** - *Biomass main heating*
    - **"2"** - *Biomass community heating*
    - **"3"** - *Biomass community heating for some of heat generation*
    - **"4"** - *Biomass secondary heating*
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

.. _RdSAP-Report/Energy-Assessment/Addendum:

Addendum
--------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Addendum`>/

- Parent element: <:ref:`RdSAP-Report/Energy-Assessment`>
- Child elements: <:ref:`RdSAP-Report/Energy-Assessment/Addendum/Addendum-Number`> <:ref:`RdSAP-Report/Energy-Assessment/Addendum/Cavity-Fill-Recommended`> <:ref:`RdSAP-Report/Energy-Assessment/Addendum/Stone-Walls`> <:ref:`RdSAP-Report/Energy-Assessment/Addendum/System-Build`> <:ref:`RdSAP-Report/Energy-Assessment/Addendum/Access-Issues`> <:ref:`RdSAP-Report/Energy-Assessment/Addendum/High-Exposure`> <:ref:`RdSAP-Report/Energy-Assessment/Addendum/Narrow-Cavities`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Addendum/Addendum-Number:

Addendum-Number
---------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Addendum`>/<:ref:`RdSAP-Report/Energy-Assessment/Addendum/Addendum-Number`>/

- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Addendum`>
- Has text value: *True*
- Codes:
    - **"1"** - *1. Wall type does not correspond to options available in RdSAP*
    - **"2"** - *2. Room heater specified for water heating instead of a range cooker*
    - **"3"** - *3. Space heating from individual system and water heating from community system*
    - **"4"** - *4. Dwelling has a swimming pool*
    - **"5"** - *5. Dwelling has micro-CHP not found in database*
    - **"6"** - *6. Storage heater or dual immersion, and single electric meter*
    - **"7"** - *7. Heating controlled by TRVs only*
    - **"8"** - *8. PVs or wind turbine present on the property (England, Wales or Scotland)*
    - **"9"** - *9. Two main heating systems and heating system upgrade is recommended*
    - **"10"** - *10. Dual electricity meter selected but there is also an electricity meter for standard tariff*
    - **"11"** - *11. Single electricity meter selected but there is also an electricity meter for an off-peak tariff*
    - **"12"** - *12. Dwelling is using a biomass fuel that is not in the RdSAP fuel options*
    - **"13"** - *13. Park Home*
    - **"14"** - *14. Dwelling has a special energy saving feature*
- Minimum occurrence: *0*
- Maximum occurrence: *unbounded*

.. _RdSAP-Report/Energy-Assessment/Addendum/Cavity-Fill-Recommended:

Cavity-Fill-Recommended
-----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Addendum`>/<:ref:`RdSAP-Report/Energy-Assessment/Addendum/Cavity-Fill-Recommended`>/

- Documentation: *Cavity fill is recommended*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Addendum`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Addendum/Stone-Walls:

Stone-Walls
-----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Addendum`>/<:ref:`RdSAP-Report/Energy-Assessment/Addendum/Stone-Walls`>/

- Documentation: *Stone walls present, not insulated*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Addendum`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Addendum/System-Build:

System-Build
------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Addendum`>/<:ref:`RdSAP-Report/Energy-Assessment/Addendum/System-Build`>/

- Documentation: *System build present*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Addendum`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Addendum/Access-Issues:

Access-Issues
-------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Addendum`>/<:ref:`RdSAP-Report/Energy-Assessment/Addendum/Access-Issues`>/

- Documentation: *Dwelling has access issues for cavity wall insulation. Include only when at least one of Cavity-Fill-Recommended, Stone-Walls, System-Build is also present*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Addendum`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Addendum/High-Exposure:

High-Exposure
-------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Addendum`>/<:ref:`RdSAP-Report/Energy-Assessment/Addendum/High-Exposure`>/

- Documentation: *Dwelling may be exposed to wind-driven rain. Include only when at least one of Cavity-Fill-Recommended, Stone-Walls, System-Build is also present*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Addendum`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Addendum/Narrow-Cavities:

Narrow-Cavities
---------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Addendum`>/<:ref:`RdSAP-Report/Energy-Assessment/Addendum/Narrow-Cavities`>/

- Documentation: *Dwelling may have narrow cavities. Include only when Cavity-Fill-Recommended is also present*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Addendum`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive:

Renewable-Heat-Incentive
------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive`>/

- Parent element: <:ref:`RdSAP-Report/Energy-Assessment`>
- Child elements: <:ref:`RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive/Space-Heating-Existing-Dwelling`> <:ref:`RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive/Space-Heating-With-Loft-Insulation`> <:ref:`RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive/Space-Heating-With-Cavity-Insulation`> <:ref:`RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive/Space-Heating-With-Loft-And-Cavity-Insulation`> <:ref:`RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive/Water-Heating`> <:ref:`RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive/Impact-Of-Loft-Insulation`> <:ref:`RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive/Impact-Of-Cavity-Insulation`> <:ref:`RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive/Impact-Of-Solid-Wall-Insulation`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive/Space-Heating-Existing-Dwelling:

Space-Heating-Existing-Dwelling
-------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive`>/<:ref:`RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive/Space-Heating-Existing-Dwelling`>/

- Documentation: *Space heating requirement for existing dwelling.*
- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive/Space-Heating-With-Loft-Insulation:

Space-Heating-With-Loft-Insulation
----------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive`>/<:ref:`RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive/Space-Heating-With-Loft-Insulation`>/

- Documentation: *Space heating requirement after implementation of loft insulation recommendation, omit if loft insulation not recommended. For backwards compatibility only, do not use*
- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive/Space-Heating-With-Cavity-Insulation:

Space-Heating-With-Cavity-Insulation
------------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive`>/<:ref:`RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive/Space-Heating-With-Cavity-Insulation`>/

- Documentation: *Space heating requirement after implementation of cavity insulation recommendation, omit if cavity insulation not recommended. For backwards compatibility only, do not use*
- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive/Space-Heating-With-Loft-And-Cavity-Insulation:

Space-Heating-With-Loft-And-Cavity-Insulation
---------------------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive`>/<:ref:`RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive/Space-Heating-With-Loft-And-Cavity-Insulation`>/

- Documentation: *Space heating requirement after implementation of loft and cavity insulation recommendations, same as existing dwelling if neither is recommended. For backwards compatibility only, do not use*
- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive/Water-Heating:

Water-Heating
-------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive`>/<:ref:`RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive/Water-Heating`>/

- Documentation: *Water heating requirement.*
- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive/Impact-Of-Loft-Insulation:

Impact-Of-Loft-Insulation
-------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive`>/<:ref:`RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive/Impact-Of-Loft-Insulation`>/

- Documentation: *Reduction in space heating requirement with loft insulation (as negative value). Omit if not applicable*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive/Impact-Of-Cavity-Insulation:

Impact-Of-Cavity-Insulation
---------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive`>/<:ref:`RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive/Impact-Of-Cavity-Insulation`>/

- Documentation: *Reduction in space heating requirement with cavity insulation (as negative value). Omit if not applicable*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive/Impact-Of-Solid-Wall-Insulation:

Impact-Of-Solid-Wall-Insulation
-------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive`>/<:ref:`RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive/Impact-Of-Solid-Wall-Insulation`>/

- Documentation: *Reduction in space heating requirement with solid wall insulation (as negative value). Omit if not applicable*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Renewable-Heat-Incentive`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Green-Deal-Package:

Green-Deal-Package
------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Green-Deal-Package`>/

- Documentation: *Improvements that can form a Green Deal package*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment`>
- Child elements: <:ref:`RdSAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement`> <:ref:`RdSAP-Report/Energy-Assessment/Green-Deal-Package/Electricity-Saving`> <:ref:`RdSAP-Report/Energy-Assessment/Green-Deal-Package/Gas-Saving`> <:ref:`RdSAP-Report/Energy-Assessment/Green-Deal-Package/Other-Fuel-Saving`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement:

Green-Deal-Improvement
----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Green-Deal-Package`>/<:ref:`RdSAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement`>/

- Documentation: *Improvements from Suggested-Improvements in the Green Deal package*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Green-Deal-Package`>
- Child elements: <:ref:`RdSAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement/Improvement-Type`> <:ref:`RdSAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement/Improvement-Number`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *unbounded*

.. _RdSAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement/Improvement-Type:

Improvement-Type
----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Green-Deal-Package`>/<:ref:`RdSAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement`>/<:ref:`RdSAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement/Improvement-Type`>/

- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement`>
- Has text value: *True*
- Codes:
    - **"A"** - *Loft Insulation*
    - **"A2"** - *Flat roof insulation*
    - **"A3"** - *Room-in-roof insulation*
    - **"B"** - *Cavity wall insulation*
    - **"B4"** - *Party wall insulation*
    - **"C"** - *Hot water cylinder insulation*
    - **"D"** - *Draughtproofing*
    - **"E"** - *Low energy lights*
    - **"F"** - *Cylinder thermostat*
    - **"G"** - *Heating controls for wet central heating system*
    - **"G2"** - *Water heating controls*
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
    - **"U1"** - *PV Battery*
    - **"U2"** - *PV Diverter*
    - **"V"** - *Wind turbine (roof mounted)*
    - **"V2"** - *Wind turbine (on mast)*
    - **"W"** - *Floor insulation; for backwards compatibility only, do not use*
    - **"W1"** - *Insulation of suspended floor*
    - **"W2"** - *Insulation of solid ground floor*
    - **"X"** - *Insulated doors*
    - **"Y"** - *Instantaneous waste water heat recovery*
    - **"Y2"** - *Storage waste water heat recovery*
    - **"Z1"** - *Air or ground source heat pump*
    - **"Z2"** - *Air or ground source heat pump with underfloor heating*
    - **"Z3"** - *Micro-CHP*
    - **"NR"** - *Not recorded*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement/Improvement-Number:

Improvement-Number
------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Green-Deal-Package`>/<:ref:`RdSAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement`>/<:ref:`RdSAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement/Improvement-Number`>/

- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Green-Deal-Package/Green-Deal-Improvement`>
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
    - **"45"** - *Flat roof or sloping ceiling insulation*
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
    - **"56"** - *Replacement glazing units*
    - **"57"** - *Suspended floor insulation*
    - **"58"** - *Solid floor insulation*
    - **"59"** - *High heat retention storage heaters and dual immersion cylinder*
    - **"60"** - *High heat retention storage heaters*
    - **"61"** - *High heat retention storage heaters and dual immersion cylinder*
    - **"62"** - *High heat retention storage heaters*
    - **"63"** - *Party wall insulation*
    - **"65"** - *Internal insulation with cavity wall insulation*
    - **"66"** - *Heating controls for wet central heating system*
    - **"70"** - *Water Heating Controls*
    - **"72"** - *PV Battery*
    - **"73"** - *PV Diverter*
    - **"75"** - *Ground source heat pump with radiators*
    - **"76"** - *Ground source heat pump with underfloor heating*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Green-Deal-Package/Electricity-Saving:

Electricity-Saving
------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Green-Deal-Package`>/<:ref:`RdSAP-Report/Energy-Assessment/Green-Deal-Package/Electricity-Saving`>/

- Documentation: *Total electricity saving for the package*
- Documentation2: *Extension of a Decimal value for use with monetary values where a currency code needs to be specified. The currency code is actually metadata about the value so, in line with good XML practice, the Currency Code is declared as an XML-Attribute of the Money datatype rather than as a separate XML-Element. The currency attribute should then include a list of valid currencies codes that are supported.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Green-Deal-Package`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Green-Deal-Package/Gas-Saving:

Gas-Saving
----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Green-Deal-Package`>/<:ref:`RdSAP-Report/Energy-Assessment/Green-Deal-Package/Gas-Saving`>/

- Documentation: *Total gas saving for the package*
- Documentation2: *Extension of a Decimal value for use with monetary values where a currency code needs to be specified. The currency code is actually metadata about the value so, in line with good XML practice, the Currency Code is declared as an XML-Attribute of the Money datatype rather than as a separate XML-Element. The currency attribute should then include a list of valid currencies codes that are supported.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Green-Deal-Package`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Green-Deal-Package/Other-Fuel-Saving:

Other-Fuel-Saving
-----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Green-Deal-Package`>/<:ref:`RdSAP-Report/Energy-Assessment/Green-Deal-Package/Other-Fuel-Saving`>/

- Documentation: *Total other saving for the package*
- Documentation2: *Extension of a Decimal value for use with monetary values where a currency code needs to be specified. The currency code is actually metadata about the value so, in line with good XML practice, the Currency Code is declared as an XML-Attribute of the Money datatype rather than as a separate XML-Element. The currency attribute should then include a list of valid currencies codes that are supported.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Green-Deal-Package`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Alternative-Improvements:

Alternative-Improvements
------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements`>/

- Documentation: *Alternative improvements to some of those given in Suggested-Improvements*
- Documentation2: *Part of an Energy Report that describes the a set of improvements that the Home Inspector considers would contribute to the overall energy rating of the property.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment`>
- Child elements: <:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement:

Improvement
-----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>/

- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements`>
- Child elements: <:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Sequence`> <:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Category`> <:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Type`> <:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Typical-Saving`> <:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Energy-Performance-Rating`> <:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Environmental-Impact-Rating`> <:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details`> <:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Indicative-Cost`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *unbounded*

.. _RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Sequence:

Sequence
--------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Sequence`>/

- Documentation: *Sequence of the Suggested Improvements within the set of Suggested Improvements. This is used to order the Recommendations on the output HCR / EPC so that the cumulative Ratings make sense. The Improved Energy Ratings that result from carrying out a Suggested Improvement are cumulative and assume that the improvements have been installed in the order they appear in the list. Hence they must be sequenced.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Category:

Improvement-Category
--------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Category`>/

- Documentation: *The category of improvement. This identifies where on the report the recommendation is printed.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>
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

.. _RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Type:

Improvement-Type
----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Type`>/

- Documentation: *Suggested work to be carried out on the Property to improve its energy efficiency.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>
- Has text value: *True*
- Codes:
    - **"A"** - *Loft Insulation*
    - **"A2"** - *Flat roof insulation*
    - **"A3"** - *Room-in-roof insulation*
    - **"B"** - *Cavity wall insulation*
    - **"B4"** - *Party wall insulation*
    - **"C"** - *Hot water cylinder insulation*
    - **"D"** - *Draughtproofing*
    - **"E"** - *Low energy lights*
    - **"F"** - *Cylinder thermostat*
    - **"G"** - *Heating controls for wet central heating system*
    - **"G2"** - *Water heating controls*
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
    - **"U1"** - *PV Battery*
    - **"U2"** - *PV Diverter*
    - **"V"** - *Wind turbine (roof mounted)*
    - **"V2"** - *Wind turbine (on mast)*
    - **"W"** - *Floor insulation; for backwards compatibility only, do not use*
    - **"W1"** - *Insulation of suspended floor*
    - **"W2"** - *Insulation of solid ground floor*
    - **"X"** - *Insulated doors*
    - **"Y"** - *Instantaneous waste water heat recovery*
    - **"Y2"** - *Storage waste water heat recovery*
    - **"Z1"** - *Air or ground source heat pump*
    - **"Z2"** - *Air or ground source heat pump with underfloor heating*
    - **"Z3"** - *Micro-CHP*
    - **"NR"** - *Not recorded*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Typical-Saving:

Typical-Saving
--------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Typical-Saving`>/

- Documentation: *Typical savings (in British Pounds) per year if the suggested improvement is carried out. 0 if not assessed*
- Documentation2: *Extension of a Decimal value for use with monetary values where a currency code needs to be specified. The currency code is actually metadata about the value so, in line with good XML practice, the Currency Code is declared as an XML-Attribute of the Money datatype rather than as a separate XML-Element. The currency attribute should then include a list of valid currencies codes that are supported.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Energy-Performance-Rating:

Energy-Performance-Rating
-------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Energy-Performance-Rating`>/

- Documentation: *The estimated Energy performance rating of the Property after the Suggested Improvement has been carried out providing any preceding Suggested Improvement has also been carried out. 0 if not assessed*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Environmental-Impact-Rating:

Environmental-Impact-Rating
---------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Environmental-Impact-Rating`>/

- Documentation: *The estimated Environmental Impact rating of the Property after the Suggested Improvement has been carried out providing any preceding Suggested Improvement has also been carried out. 0 if not assessed*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details:

Improvement-Details
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details`>/

- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>
- Child elements: <:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts`> <:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Number`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts:

Improvement-Texts
-----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts`>/

- Documentation: *For backward compatibility only*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details`>
- Child elements: <:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Summary`> <:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Heading`> <:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Description`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Summary:

Improvement-Summary
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Summary`>/

- Documentation: *A short description of the suggested improvement.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Heading:

Improvement-Heading
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Heading`>/

- Documentation: *Text to precede the improvement description. If this field is not provided the 'Improvement-Summary' is used instead.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Description:

Improvement-Description
-----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts/Improvement-Description`>/

- Documentation: *Detailed description of the suggested improvement.*
- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Texts`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Number:

Improvement-Number
------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details/Improvement-Number`>/

- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Improvement-Details`>
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
    - **"45"** - *Flat roof or sloping ceiling insulation*
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
    - **"56"** - *Replacement glazing units*
    - **"57"** - *Suspended floor insulation*
    - **"58"** - *Solid floor insulation*
    - **"59"** - *High heat retention storage heaters and dual immersion cylinder*
    - **"60"** - *High heat retention storage heaters*
    - **"61"** - *High heat retention storage heaters and dual immersion cylinder*
    - **"62"** - *High heat retention storage heaters*
    - **"63"** - *Party wall insulation*
    - **"65"** - *Internal insulation with cavity wall insulation*
    - **"66"** - *Heating controls for wet central heating system*
    - **"70"** - *Water Heating Controls*
    - **"72"** - *PV Battery*
    - **"73"** - *PV Diverter*
    - **"75"** - *Ground source heat pump with radiators*
    - **"76"** - *Ground source heat pump with underfloor heating*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Indicative-Cost:

Indicative-Cost
---------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Energy-Assessment`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>/<:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement/Indicative-Cost`>/

- Parent element: <:ref:`RdSAP-Report/Energy-Assessment/Alternative-Improvements/Improvement`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data:

SAP-Data
--------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/

- Documentation2: *These are the specific data-items collected by the HI / EA needed to perform the SAP calculation.*
- Parent element: <:ref:`RdSAP-Report`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details:

SAP-Property-Details
--------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Built-Form`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Extensions-Count`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Habitable-Room-Count`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Heated-Room-Count`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Low-Energy-Fixed-Lighting-Bulbs-Count`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Incandescent-Fixed-Lighting-Bulbs-Count`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/LED-Fixed-Lighting-Bulbs-Count`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/CFL-Fixed-Lighting-Bulbs-Count`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Measurement-Type`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Property-Type`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Solar-Water-Heating`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Wet-Rooms-Count`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Pressure-Test`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Pressure-Test-Certificate-Number`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Air-Permeability`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Has-Draught-Lobby`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Open-Chimneys-Count`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Blocked-Chimneys-Count`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Open-Flues-Count`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Closed-Flues-Count`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Boilers-Flues-Count`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Other-Flues-Count`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Extract-Fans-Count`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/PSV-Count`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Flueless-Gas-Fires-Count`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Mechanical-Ventilation-Index-Number`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Mechanical-Ventilation`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Mechanical-Vent-Duct-Type`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Mechanical-Vent-Duct-Placement`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Mechanical-Vent-Duct-Insulation`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Mechanical-Vent-Duct-Insulation-Level`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Mechanical-Vent-Measured-Installation`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Is-Mechanical-Vent-Approved-Installer-Scheme`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Kitchen-Room-Fans-Count`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Non-Kitchen-Room-Fans-Count`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Kitchen-Duct-Fans-Count`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Non-Kitchen-Duct-Fans-Count`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Kitchen-Wall-Fans-Count`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Non-Kitchen-Wall-Fans-Count`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Conservatory-Type`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Flat-Details`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Windows-Transmission-Details`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Deselected-Improvements`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Door-Count`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Insulated-Door-Count`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Draughtproofed-Door-Count`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Insulated-Door-U-Value`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Percent-Draughtproofed`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Built-Form:

Built-Form
----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Built-Form`>/

- Documentation: *The building type of the Property e.g. Detached, Semi-Detached, Terrace etc. Together with the Property Type, the Build Form produces a structured description of the property.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Codes:
    - **"1"** - *Detached*
    - **"2"** - *Semi-Detached*
    - **"3"** - *End-Terrace*
    - **"4"** - *Mid-Terrace*
    - **"5"** - *Enclosed End-Terrace*
    - **"6"** - *Enclosed Mid-Terrace*
    - **"NR"** - *Not Recorded*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Extensions-Count:

Extensions-Count
----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Extensions-Count`>/

- Documentation: *The number of extensions added to the house.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Habitable-Room-Count:

Habitable-Room-Count
--------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Habitable-Room-Count`>/

- Documentation: *Count of the number of habitable rooms within the property. This is the number of Reception Rooms (including Living Rooms, Sitting Rooms, Dining Rooms), Bedrooms, Study and similar rooms but excludes hall, stairs, kitchen, utility rooms, bathrooms, cloakrooms, en-suites and similar rooms.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Heated-Room-Count:

Heated-Room-Count
-----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Heated-Room-Count`>/

- Documentation: *The numbewr of heated rooms in the property if more than half of the abitable rooms are not heated.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Low-Energy-Fixed-Lighting-Bulbs-Count:

Low-Energy-Fixed-Lighting-Bulbs-Count
-------------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Low-Energy-Fixed-Lighting-Bulbs-Count`>/

- Documentation: *If exact number of CFL and LED not known, provide number of low energy fixed lighting outlets.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Incandescent-Fixed-Lighting-Bulbs-Count:

Incandescent-Fixed-Lighting-Bulbs-Count
---------------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Incandescent-Fixed-Lighting-Bulbs-Count`>/

- Documentation: *Number of incandescent fixed bulbs.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/LED-Fixed-Lighting-Bulbs-Count:

LED-Fixed-Lighting-Bulbs-Count
------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/LED-Fixed-Lighting-Bulbs-Count`>/

- Documentation: *Number of LED fixed bulbs.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/CFL-Fixed-Lighting-Bulbs-Count:

CFL-Fixed-Lighting-Bulbs-Count
------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/CFL-Fixed-Lighting-Bulbs-Count`>/

- Documentation: *Number of CFL fixed bulbs.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Measurement-Type:

Measurement-Type
----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Measurement-Type`>/

- Documentation: *Indicates the type of measurements taken to calculate floor areas e.g. "Internal" or "External".*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Codes:
    - **"1"** - *Internal*
    - **"2"** - *External*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Property-Type:

Property-Type
-------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Property-Type`>/

- Documentation: *Describes the type of property such as House, Flat, Mansion, Maisonette etc. This is actually the type differentiator for Property but only a limited number of property types, notably Apartment and Apartment Block, have any specific characteristics and warrant their own definition.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Codes:
    - **"0"** - *House*
    - **"1"** - *Bungalow*
    - **"2"** - *Flat*
    - **"3"** - *Maisonette*
    - **"4"** - *Park home*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Solar-Water-Heating:

Solar-Water-Heating
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Solar-Water-Heating`>/

- Documentation: *Indicates whether the heating in the Property is solar powered.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Codes:
    - **"Y"** - *Yes*
    - **"N"** - *No*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Wet-Rooms-Count:

Wet-Rooms-Count
---------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Wet-Rooms-Count`>/

- Documentation: *Relevant when mechanical ventilation system is from PCDB.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Pressure-Test:

Pressure-Test
-------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Pressure-Test`>/

- Documentation: *Whether there has been a pressure test, or whether an assumed value is used for the air permeability.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Codes:
    - **"4"** - *no test, SAP algorithm used*
    - **"6"** - *yes - measured at 50 Pa*
    - **"7"** - *yes - measured at 4 Pa*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Pressure-Test-Certificate-Number:

Pressure-Test-Certificate-Number
--------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Pressure-Test-Certificate-Number`>/

- Documentation: *The pressure test certificate number or test engineer reference.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Air-Permeability:

Air-Permeability
----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Air-Permeability`>/

- Documentation: *Air permeability; only if pressure test (yes or assumed).*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Has-Draught-Lobby:

Has-Draught-Lobby
-----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Has-Draught-Lobby`>/

- Documentation: *Is there a draft lobby? Only if no pressure test.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Open-Chimneys-Count:

Open-Chimneys-Count
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Open-Chimneys-Count`>/

- Documentation: *The number of Open Chimneys in the Property.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Blocked-Chimneys-Count:

Blocked-Chimneys-Count
----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Blocked-Chimneys-Count`>/

- Documentation: *The number of Blocked Chimneys in the Property.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Open-Flues-Count:

Open-Flues-Count
----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Open-Flues-Count`>/

- Documentation: *The number of Open Flues in the Property.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Closed-Flues-Count:

Closed-Flues-Count
------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Closed-Flues-Count`>/

- Documentation: *Chimney/Flues attached to closed fires.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Boilers-Flues-Count:

Boilers-Flues-Count
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Boilers-Flues-Count`>/

- Documentation: *The number of Boiler Flues or chimneys in the Property.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Other-Flues-Count:

Other-Flues-Count
-----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Other-Flues-Count`>/

- Documentation: *The number of Other Flues or chimneys in the Property.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Extract-Fans-Count:

Extract-Fans-Count
------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Extract-Fans-Count`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/PSV-Count:

PSV-Count
---------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/PSV-Count`>/

- Documentation: *Number of passive vents.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Flueless-Gas-Fires-Count:

Flueless-Gas-Fires-Count
------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Flueless-Gas-Fires-Count`>/

- Documentation: *The number of flueless gas fires in the Property.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Mechanical-Ventilation-Index-Number:

Mechanical-Ventilation-Index-Number
-----------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Mechanical-Ventilation-Index-Number`>/

- Documentation: *Relevant when mechanical ventilation system is from PCDB.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Mechanical-Ventilation:

Mechanical-Ventilation
----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Mechanical-Ventilation`>/

- Documentation: *Identifies the type of mechanical ventilation the property has. This is required for the RdSAP calculation.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Codes:
    - **"0"** - *natural*
    - **"1"** - *mechanical ventilation without heat recovery (MV)*
    - **"2"** - *mechanical extract, decentralised (MEV dc)*
    - **"3"** - *mechanical extract, centralised (MEV c)*
    - **"4"** - *mechanical ventilation with heat recovery (MVHR)*
    - **"5"** - *positive input from loft*
    - **"6"** - *positive input from outside*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Mechanical-Vent-Duct-Type:

Mechanical-Vent-Duct-Type
-------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Mechanical-Vent-Duct-Type`>/

- Documentation: *Mechanical vent duct type; if MEV c, MV or MVHR from PCDB.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Codes:
    - **"1"** - *flexible*
    - **"2"** - *rigid*
    - **"3"** - *semi-rigid*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Mechanical-Vent-Duct-Placement:

Mechanical-Vent-Duct-Placement
------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Mechanical-Vent-Duct-Placement`>/

- Documentation: *Mechanical ventilation duct insulation; if MVHR from PCDB.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Codes:
    - **"1"** - *inside heated envelope*
    - **"2"** - *outside heated envelope*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Mechanical-Vent-Duct-Insulation:

Mechanical-Vent-Duct-Insulation
-------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Mechanical-Vent-Duct-Insulation`>/

- Documentation: *Relevant when mechanical ventilation system is from PCDB.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Codes:
    - **"1"** - *not insulated*
    - **"2"** - *insulated*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Mechanical-Vent-Duct-Insulation-Level:

Mechanical-Vent-Duct-Insulation-Level
-------------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Mechanical-Vent-Duct-Insulation-Level`>/

- Documentation: *Mechanical vent duct insulation; if MVHR from PCDB.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Codes:
    - **"1"** - *level 1*
    - **"2"** - *level 2*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Mechanical-Vent-Measured-Installation:

Mechanical-Vent-Measured-Installation
-------------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Mechanical-Vent-Measured-Installation`>/

- Documentation: *Mechanical ventilation SPF measured in situ; if MVHR or balanced from pcdb.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Is-Mechanical-Vent-Approved-Installer-Scheme:

Is-Mechanical-Vent-Approved-Installer-Scheme
--------------------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Is-Mechanical-Vent-Approved-Installer-Scheme`>/

- Documentation: *If MVHR from pcdb.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Kitchen-Room-Fans-Count:

Kitchen-Room-Fans-Count
-----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Kitchen-Room-Fans-Count`>/

- Documentation: *MEV dc, number of fans in room, kitchen; if mechanical vent data from database or manufacturer declaration (MEV dc).*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Non-Kitchen-Room-Fans-Count:

Non-Kitchen-Room-Fans-Count
---------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Non-Kitchen-Room-Fans-Count`>/

- Documentation: *MEV dc, number of fans in room, rooms other than kitchen; if mechanical vent data from database or manufacturer declaration (MEV dc).*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Kitchen-Duct-Fans-Count:

Kitchen-Duct-Fans-Count
-----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Kitchen-Duct-Fans-Count`>/

- Documentation: *MEV dc, number of fans via duct, kitchen; if mechanical vent data from database or manufacturer declaration (MEV dc).*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Non-Kitchen-Duct-Fans-Count:

Non-Kitchen-Duct-Fans-Count
---------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Non-Kitchen-Duct-Fans-Count`>/

- Documentation: *MEV dc, number of fans via duct, rooms other than kitchen; if mechanical vent data from database or manufacturer declaration (MEV dc).*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Kitchen-Wall-Fans-Count:

Kitchen-Wall-Fans-Count
-----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Kitchen-Wall-Fans-Count`>/

- Documentation: *MEV dc, number of fans through wall, kitchen; if mechanical vent data from database or manufacturer declaration (MEV dc).*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Non-Kitchen-Wall-Fans-Count:

Non-Kitchen-Wall-Fans-Count
---------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Non-Kitchen-Wall-Fans-Count`>/

- Documentation: *MEV dc, number of fans through wall, rooms other than kitchen; if mechanical vent data from database or manufacturer declaration (MEV dc).*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Conservatory-Type:

Conservatory-Type
-----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Conservatory-Type`>/

- Documentation: *Type of Conservatory*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Codes:
    - **"1"** - *no conservatory*
    - **"2"** - *separated unheated conservatory*
    - **"3"** - *separated heated conservatory*
    - **"4"** - *not separated*
    - **"5"** - *not recorded - this is for backwards compatibility only and should not be used*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating:

SAP-Heating
-----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/

- Documentation2: *Details of the means by which the Main Building is heated.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Secondary-Fuel-Type`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Water-Heating-Fuel`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Type`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Water-Heating-Code`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Immersion-Heating-Type`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Cylinder-Size`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Cylinder-Size-Measured`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Cylinder-Insulation-Type`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Cylinder-Heat-Loss`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Cylinder-Insulation-Thickness`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Cylinder-Thermostat`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Has-Fixed-Air-Conditioning`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Number-Baths`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Number-Baths-WWHRS`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Community-DHW-Network-Index-Number`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Community-DHW-Sub-Network-Name`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Community-DHW-Distribution-Type`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Community-DHW-CHP-Electricity-Generation`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Secondary-Fuel-Type:

Secondary-Fuel-Type
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Secondary-Fuel-Type`>/

- Documentation: *The secondary type of fuel used to power the central heating e.g. Gas, Electricity*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Codes:
    - **"0"** - *To be used only when there is no heating/hot-water system or data is from a community network*
    - **"1"** - *mains gas - this is for backwards compatibility only and should not be used*
    - **"2"** - *LPG - this is for backwards compatibility only and should not be used*
    - **"3"** - *bottled LPG*
    - **"4"** - *oil - this is for backwards compatibility only and should not be used*
    - **"5"** - *anthracite*
    - **"6"** - *wood logs*
    - **"7"** - *bulk wood pellets*
    - **"8"** - *wood chips*
    - **"9"** - *dual fuel - mineral + wood*
    - **"10"** - *electricity - this is for backwards compatibility only and should not be used*
    - **"11"** - *waste combustion - this is for backwards compatibility only and should not be used*
    - **"12"** - *biomass - this is for backwards compatibility only and should not be used*
    - **"13"** - *biogas - landfill - this is for backwards compatibility only and should not be used*
    - **"14"** - *house coal - this is for backwards compatibility only and should not be used*
    - **"15"** - *smokeless coal*
    - **"16"** - *wood pellets in bags for secondary heating*
    - **"17"** - *LPG special condition*
    - **"18"** - *B30K (not community)*
    - **"19"** - *bioethanol*
    - **"20"** - *mains gas (community)*
    - **"21"** - *LPG (community)*
    - **"22"** - *oil (community)*
    - **"23"** - *B30D (community)*
    - **"24"** - *coal (community)*
    - **"25"** - *electricity (community)*
    - **"26"** - *mains gas (not community)*
    - **"27"** - *LPG (not community)*
    - **"28"** - *oil (not community)*
    - **"29"** - *electricity (not community)*
    - **"30"** - *waste combustion (community)*
    - **"31"** - *biomass (community)*
    - **"32"** - *biogas (community)*
    - **"33"** - *house coal (not community)*
    - **"34"** - *biodiesel from any biomass source*
    - **"35"** - *biodiesel from used cooking oil only*
    - **"36"** - *biodiesel from vegetable oil only (not community)*
    - **"37"** - *appliances able to use mineral oil or liquid biofuel*
    - **"51"** - *biogas (not community)*
    - **"56"** - *heat from boilers that can use mineral oil or biodiesel (community)*
    - **"57"** - *heat from boilers using biodiesel from any biomass source (community)*
    - **"58"** - *biodiesel from vegetable oil only (community)*
    - **"99"** - *from heat network data (community)*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Water-Heating-Fuel:

Water-Heating-Fuel
------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Water-Heating-Fuel`>/

- Documentation: *The type of fuel used to heat the water e.g. Gas, Electricity*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Codes:
    - **"0"** - *To be used only when there is no heating/hot-water system or data is from a community network*
    - **"1"** - *mains gas - this is for backwards compatibility only and should not be used*
    - **"2"** - *LPG - this is for backwards compatibility only and should not be used*
    - **"3"** - *bottled LPG*
    - **"4"** - *oil - this is for backwards compatibility only and should not be used*
    - **"5"** - *anthracite*
    - **"6"** - *wood logs*
    - **"7"** - *bulk wood pellets*
    - **"8"** - *wood chips*
    - **"9"** - *dual fuel - mineral + wood*
    - **"10"** - *electricity - this is for backwards compatibility only and should not be used*
    - **"11"** - *waste combustion - this is for backwards compatibility only and should not be used*
    - **"12"** - *biomass - this is for backwards compatibility only and should not be used*
    - **"13"** - *biogas - landfill - this is for backwards compatibility only and should not be used*
    - **"14"** - *house coal - this is for backwards compatibility only and should not be used*
    - **"15"** - *smokeless coal*
    - **"16"** - *wood pellets in bags for secondary heating*
    - **"17"** - *LPG special condition*
    - **"18"** - *B30K (not community)*
    - **"19"** - *bioethanol*
    - **"20"** - *mains gas (community)*
    - **"21"** - *LPG (community)*
    - **"22"** - *oil (community)*
    - **"23"** - *B30D (community)*
    - **"24"** - *coal (community)*
    - **"25"** - *electricity (community)*
    - **"26"** - *mains gas (not community)*
    - **"27"** - *LPG (not community)*
    - **"28"** - *oil (not community)*
    - **"29"** - *electricity (not community)*
    - **"30"** - *waste combustion (community)*
    - **"31"** - *biomass (community)*
    - **"32"** - *biogas (community)*
    - **"33"** - *house coal (not community)*
    - **"34"** - *biodiesel from any biomass source*
    - **"35"** - *biodiesel from used cooking oil only*
    - **"36"** - *biodiesel from vegetable oil only (not community)*
    - **"37"** - *appliances able to use mineral oil or liquid biofuel*
    - **"51"** - *biogas (not community)*
    - **"56"** - *heat from boilers that can use mineral oil or biodiesel (community)*
    - **"57"** - *heat from boilers using biodiesel from any biomass source (community)*
    - **"58"** - *biodiesel from vegetable oil only (community)*
    - **"99"** - *from heat network data (community)*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Type:

Secondary-Heating-Type
----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Secondary-Heating-Type`>/

- Documentation: *Type of secondary heating (if any) present in the property.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Water-Heating-Code:

Water-Heating-Code
------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Water-Heating-Code`>/

- Documentation: *Describes the type of Water Heating present in the Property.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Immersion-Heating-Type:

Immersion-Heating-Type
----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Immersion-Heating-Type`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Codes:
    - **"1"** - *Dual*
    - **"2"** - *Single*
    - **"NA"** - *not applicable*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Cylinder-Size:

Cylinder-Size
-------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Cylinder-Size`>/

- Documentation: *The size of the Hot Water Cylinder - taken from a range of standard sizes.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Codes:
    - **"0"** - *No Access*
    - **"1"** - *No Cylinder*
    - **"2"** - *Normal - up to 130 litres*
    - **"3"** - *Medium - between 131 and 170 litres*
    - **"4"** - *Large - greater than 170 litres.*
    - **"5"** - *actual size included in Solar-Water-Heating-Details*
    - **"6"** - *Exact cylinder volume if known*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Cylinder-Size-Measured:

Cylinder-Size-Measured
----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Cylinder-Size-Measured`>/

- Documentation: *Exact cylinder size if known. When Cylinder-Size code is 6.*
- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Cylinder-Insulation-Type:

Cylinder-Insulation-Type
------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Cylinder-Insulation-Type`>/

- Documentation: *the type of insulation surrounding the Hot Water Cylinder*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Codes:
    - **"0"** - *None*
    - **"1"** - *factory-applied*
    - **"2"** - *loose jacket*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Cylinder-Heat-Loss:

Cylinder-Heat-Loss
------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Cylinder-Heat-Loss`>/

- Documentation: *Cylinder declared loss in kWh/day; only if there is a hot water store and if manufacturer declared loss.*
- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Cylinder-Insulation-Thickness:

Cylinder-Insulation-Thickness
-----------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Cylinder-Insulation-Thickness`>/

- Documentation: *Average thickness of the insulation surrounding the Hot Water Cylinder.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Codes:
    - **"0"** - *0mm*
    - **"12"** - *12mm*
    - **"25"** - *25 mm*
    - **"38"** - *38 mm*
    - **"50"** - *50 mm*
    - **"80"** - *80 mm*
    - **"120"** - *120mm*
    - **"160"** - *160mm*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Cylinder-Thermostat:

Cylinder-Thermostat
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Cylinder-Thermostat`>/

- Documentation: *Whether the cylinder has a thermostat. Omit if no cylinder.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Codes:
    - **"Y"** - *Yes*
    - **"N"** - *No*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Has-Fixed-Air-Conditioning:

Has-Fixed-Air-Conditioning
--------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Has-Fixed-Air-Conditioning`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details:

Main-Heating-Details
--------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating:

Main-Heating
------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Number`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Category`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Fuel-Type`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Control`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Index-Number`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Data-Source`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/SAP-Main-Heating-Code`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Boiler-Ignition-Type`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Boiler-Flue-Type`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Fan-Flue-Present`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heat-Emitter-Type`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Fraction`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Has-FGHRS`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Index-Number`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-PV-Peak-Power`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-PV-Orientation`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-PV-Pitch`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-PV-Overshading`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Compensating-Controller-Index-Number`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/TTZC-Index-Number`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Community-Heat-Network-Index-Number`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Community-Heat-Sub-Network-Name`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Community-Heat-Distribution-Type`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Community-Heat-CHP-Electricity-Generation`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Emitter-Temperature`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/MCS-Installed-Heat-Pump`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Central-Heating-Pump-Age`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *2*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Number:

Main-Heating-Number
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Number`>/

- Documentation: *Identifies the main heating as system 1 or system 2. System 1 must always be present, system 2 is included only when there are two systems.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Category:

Main-Heating-Category
---------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Category`>/

- Documentation: *Category of heating system for the main heating system.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
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
    - **"12"** - *not recorded*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Fuel-Type:

Main-Fuel-Type
--------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Fuel-Type`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Codes:
    - **"0"** - *To be used only when there is no heating/hot-water system or data is from a community network*
    - **"1"** - *mains gas - this is for backwards compatibility only and should not be used*
    - **"2"** - *LPG - this is for backwards compatibility only and should not be used*
    - **"3"** - *bottled LPG*
    - **"4"** - *oil - this is for backwards compatibility only and should not be used*
    - **"5"** - *anthracite*
    - **"6"** - *wood logs*
    - **"7"** - *bulk wood pellets*
    - **"8"** - *wood chips*
    - **"9"** - *dual fuel - mineral + wood*
    - **"10"** - *electricity - this is for backwards compatibility only and should not be used*
    - **"11"** - *waste combustion - this is for backwards compatibility only and should not be used*
    - **"12"** - *biomass - this is for backwards compatibility only and should not be used*
    - **"13"** - *biogas - landfill - this is for backwards compatibility only and should not be used*
    - **"14"** - *house coal - this is for backwards compatibility only and should not be used*
    - **"15"** - *smokeless coal*
    - **"16"** - *wood pellets in bags for secondary heating*
    - **"17"** - *LPG special condition*
    - **"18"** - *B30K (not community)*
    - **"19"** - *bioethanol*
    - **"20"** - *mains gas (community)*
    - **"21"** - *LPG (community)*
    - **"22"** - *oil (community)*
    - **"23"** - *B30D (community)*
    - **"24"** - *coal (community)*
    - **"25"** - *electricity (community)*
    - **"26"** - *mains gas (not community)*
    - **"27"** - *LPG (not community)*
    - **"28"** - *oil (not community)*
    - **"29"** - *electricity (not community)*
    - **"30"** - *waste combustion (community)*
    - **"31"** - *biomass (community)*
    - **"32"** - *biogas (community)*
    - **"33"** - *house coal (not community)*
    - **"34"** - *biodiesel from any biomass source*
    - **"35"** - *biodiesel from used cooking oil only*
    - **"36"** - *biodiesel from vegetable oil only (not community)*
    - **"37"** - *appliances able to use mineral oil or liquid biofuel*
    - **"51"** - *biogas (not community)*
    - **"56"** - *heat from boilers that can use mineral oil or biodiesel (community)*
    - **"57"** - *heat from boilers using biodiesel from any biomass source (community)*
    - **"58"** - *biodiesel from vegetable oil only (community)*
    - **"99"** - *from heat network data (community)*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Control:

Main-Heating-Control
--------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Control`>/

- Documentation: *Type of Main Control for the Heating System.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Index-Number:

Main-Heating-Index-Number
-------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Index-Number`>/

- Documentation: *The ID of the heating system from the product database, if system from database.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Data-Source:

Main-Heating-Data-Source
------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Data-Source`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Codes:
    - **"1"** - *database*
    - **"2"** - *SAP Table*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/SAP-Main-Heating-Code:

SAP-Main-Heating-Code
---------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/SAP-Main-Heating-Code`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Boiler-Ignition-Type:

Boiler-Ignition-Type
--------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Boiler-Ignition-Type`>/

- Documentation: *Only relevant for boilers 1998 or later.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Codes:
    - **"1"** - *auto-ignition*
    - **"2"** - *permanent pilot light*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Boiler-Flue-Type:

Boiler-Flue-Type
----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Boiler-Flue-Type`>/

- Documentation: *Indicates the flue type of the heating system.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Codes:
    - **"1"** - *open*
    - **"2"** - *room-sealed*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Fan-Flue-Present:

Fan-Flue-Present
----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Fan-Flue-Present`>/

- Documentation: *Indicates whether the heating system contains a fan flue. This is required by RdSAP and should be part of the 3-letter codes but isn't.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Codes:
    - **"Y"** - *Yes*
    - **"N"** - *No*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heat-Emitter-Type:

Heat-Emitter-Type
-----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Heat-Emitter-Type`>/

- Documentation: *Identifies the means by which the central heating system (if present) emits heat.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Codes:
    - **"0"** - *not radiators or underfloor*
    - **"1"** - *radiators*
    - **"2"** - *underfloor*
    - **"3"** - *fan coil units*
    - **"4"** - *both radiators and underfloor*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Fraction:

Main-Heating-Fraction
---------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Main-Heating-Fraction`>/

- Documentation: *Fraction of total floor area served by this system.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Has-FGHRS:

Has-FGHRS
---------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Has-FGHRS`>/

- Documentation: *Flue Gas Heat Recovery System*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Codes:
    - **"Y"** - *Yes*
    - **"N"** - *No*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Index-Number:

FGHRS-Index-Number
------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-Index-Number`>/

- Documentation: *FGHRS index number; only if FGHRS*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-PV-Peak-Power:

FGHRS-PV-Peak-Power
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-PV-Peak-Power`>/

- Documentation: *Applies only for FGHRS with its own PV supply*
- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-PV-Orientation:

FGHRS-PV-Orientation
--------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-PV-Orientation`>/

- Documentation: *Applies only for FGHRS with its own PV supply*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
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
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-PV-Pitch:

FGHRS-PV-Pitch
--------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-PV-Pitch`>/

- Documentation: *Applies only for FGHRS with its own PV supply*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Codes:
    - **"1"** - *horizontal*
    - **"2"** - *30 degrees*
    - **"3"** - *45 degrees*
    - **"4"** - *60 degrees*
    - **"5"** - *vertical*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-PV-Overshading:

FGHRS-PV-Overshading
--------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/FGHRS-PV-Overshading`>/

- Documentation: *Applies only for FGHRS with its own PV supply*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Codes:
    - **"1"** - *none or very little*
    - **"2"** - *modest*
    - **"3"** - *significant*
    - **"4"** - *heavy*
    - **"5"** - *severe*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Compensating-Controller-Index-Number:

Compensating-Controller-Index-Number
------------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Compensating-Controller-Index-Number`>/

- Documentation: *The ID of the controller from the product database.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/TTZC-Index-Number:

TTZC-Index-Number
-----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/TTZC-Index-Number`>/

- Documentation: *The ID of the time and temperature zone control from the product database.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Community-Heat-Network-Index-Number:

Community-Heat-Network-Index-Number
-----------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Community-Heat-Network-Index-Number`>/

- Documentation: *index number of heat network, if applicable, community space heating or community space and water heating.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Community-Heat-Sub-Network-Name:

Community-Heat-Sub-Network-Name
-------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Community-Heat-Sub-Network-Name`>/

- Documentation: *only if heat network from pcdb. The name by which the sub community heat network is known.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Community-Heat-Distribution-Type:

Community-Heat-Distribution-Type
--------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Community-Heat-Distribution-Type`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Codes:
    - **"5"** - *calculated*
    - **"6"** - *unknown*
    - **"9"** - *Two adjoining dwellings*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Community-Heat-CHP-Electricity-Generation:

Community-Heat-CHP-Electricity-Generation
-----------------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Community-Heat-CHP-Electricity-Generation`>/

- Documentation: *Only if community heating not from pcdb and a heat source with CHP. CHP Electricity generation options from table 12f.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
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

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters:

Storage-Heaters
---------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater:

Storage-Heater
--------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater/Number-Of-Heaters`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater/Index-Number`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater/High-Heat-Retention`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *4*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater/Number-Of-Heaters:

Number-Of-Heaters
-----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater/Number-Of-Heaters`>/

- Documentation: *The number of storage heaters with this index number.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater/Index-Number:

Index-Number
------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater/Index-Number`>/

- Documentation: *The index number of the heater from the product database.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater/High-Heat-Retention:

High-Heat-Retention
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater/High-Heat-Retention`>/

- Documentation: *Whether heater is high heat retention type.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Storage-Heaters/Storage-Heater`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Emitter-Temperature:

Emitter-Temperature
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Emitter-Temperature`>/

- Documentation: *0, 1, 3 or 4 applicable to condensing boilers and heat pumps. Other systems NA.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Codes:
    - **"0"** - *unknown*
    - **"1"** - *over 45degC*
    - **"3"** - *over 35degC and less than or equal to 45degC*
    - **"4"** - *less than or equal to 35degC*
    - **"NA"** - *not applicable for the heating system*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/MCS-Installed-Heat-Pump:

MCS-Installed-Heat-Pump
-----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/MCS-Installed-Heat-Pump`>/

- Documentation: *Whether heat pump was installed under the Microgeneration Certification Scheme.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Central-Heating-Pump-Age:

Central-Heating-Pump-Age
------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating/Central-Heating-Pump-Age`>/

- Documentation: *Included for systems with a central heating pump, i.e. wet system.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Main-Heating-Details/Main-Heating`>
- Has text value: *True*
- Codes:
    - **"0"** - *unknown*
    - **"1"** - *2012 or earlier*
    - **"2"** - *2013 or later*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details:

Solar-Water-Heating-Details
---------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>/

- Documentation: *Included only when details are known*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Panel-Collector-Data-Source`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Panel-Collector-Orientation`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Panel-Collector-Pitch`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Panel-Collector-Overshading`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Water-Pump`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Store-Volume-Details-Known`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Collector-Details`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Volume-Details`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Shower-Types`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Collector-Loop-Efficiency`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Incidence-Angle-Modifier`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Is-Community-Solar`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Service-Provision`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Overall-Heat-Loss`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Panel-Collector-Data-Source:

Solar-Panel-Collector-Data-Source
---------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Panel-Collector-Data-Source`>/

- Documentation: *Source of solar panel collector data.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>
- Has text value: *True*
- Codes:
    - **"1"** - *default*
    - **"2"** - *declared values*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Panel-Collector-Orientation:

Solar-Panel-Collector-Orientation
---------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Panel-Collector-Orientation`>/

- Documentation: *Collector orientation.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>
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
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Panel-Collector-Pitch:

Solar-Panel-Collector-Pitch
---------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Panel-Collector-Pitch`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>
- Has text value: *True*
- Codes:
    - **"1"** - *horizontal*
    - **"2"** - *30 degrees*
    - **"3"** - *45 degrees*
    - **"4"** - *60 degrees*
    - **"5"** - *vertical*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Panel-Collector-Overshading:

Solar-Panel-Collector-Overshading
---------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Panel-Collector-Overshading`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>
- Has text value: *True*
- Codes:
    - **"1"** - *none or very little*
    - **"2"** - *modest*
    - **"3"** - *significant*
    - **"4"** - *heavy*
    - **"5"** - *severe*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Water-Pump:

Solar-Water-Pump
----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Water-Pump`>/

- Documentation: *Energy source for pumping water through the solar system*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>
- Has text value: *True*
- Codes:
    - **"0"** - *unknown*
    - **"1"** - *electrically powered*
    - **"2"** - *PV powered*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Store-Volume-Details-Known:

Store-Volume-Details-Known
--------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Store-Volume-Details-Known`>/

- Documentation: *When Y the total store volume, dedicated solar volume and combined cylinder are to be provided*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>
- Has text value: *True*
- Codes:
    - **"Y"** - *Yes*
    - **"N"** - *No*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Collector-Details:

Solar-Collector-Details
-----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Collector-Details`>/

- Documentation: *Include when collector details known.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Collector-Details/Aperture-Area`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Collector-Details/Collector-Type`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Collector-Details/Zero-Loss-Efficiency`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Collector-Details/Heat-Loss-Rate`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Collector-Details/Linear-Heat-Loss-Coefficient`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Collector-Details/Second-Order-Heat-Loss-Coefficient`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Collector-Details/Aperture-Area:

Aperture-Area
-------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Collector-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Collector-Details/Aperture-Area`>/

- Documentation: *Panel aperture area in square metres.*
- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Collector-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Collector-Details/Collector-Type:

Collector-Type
--------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Collector-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Collector-Details/Collector-Type`>/

- Documentation: *Type of solar panel collector.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Collector-Details`>
- Has text value: *True*
- Codes:
    - **"1"** - *unglazed*
    - **"2"** - *flat panel*
    - **"3"** - *evacuated tube*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Collector-Details/Zero-Loss-Efficiency:

Zero-Loss-Efficiency
--------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Collector-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Collector-Details/Zero-Loss-Efficiency`>/

- Documentation: *Collector zero-loss efficiency.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Collector-Details`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Collector-Details/Heat-Loss-Rate:

Heat-Loss-Rate
--------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Collector-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Collector-Details/Heat-Loss-Rate`>/

- Documentation: *Collector heat loss rate; for backward compatibility only, do not use.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Collector-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Collector-Details/Linear-Heat-Loss-Coefficient:

Linear-Heat-Loss-Coefficient
----------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Collector-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Collector-Details/Linear-Heat-Loss-Coefficient`>/

- Documentation: *Collector linear heat loss coefficient.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Collector-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Collector-Details/Second-Order-Heat-Loss-Coefficient:

Second-Order-Heat-Loss-Coefficient
----------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Collector-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Collector-Details/Second-Order-Heat-Loss-Coefficient`>/

- Documentation: *Collector 2nd order heat loss coefficient.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Collector-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Volume-Details:

Solar-Volume-Details
--------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Volume-Details`>/

- Documentation: *Include when volume details known.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Volume-Details/Total-Store-Volume`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Volume-Details/Dedicated-Solar-Volume`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Volume-Details/Combined-Cylinder`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Volume-Details/Total-Store-Volume:

Total-Store-Volume
------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Volume-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Volume-Details/Total-Store-Volume`>/

- Documentation: *Total volume of hot water store in litres.*
- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Volume-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Volume-Details/Dedicated-Solar-Volume:

Dedicated-Solar-Volume
----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Volume-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Volume-Details/Dedicated-Solar-Volume`>/

- Documentation: *Volume of hot water store dedicated to solar heated water, in litres.*
- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Volume-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Volume-Details/Combined-Cylinder:

Combined-Cylinder
-----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Volume-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Volume-Details/Combined-Cylinder`>/

- Documentation: *If combined cylinder the total hot water store volume is inclusive of the dedicated solar volume.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Solar-Volume-Details`>
- Has text value: *True*
- Codes:
    - **"Y"** - *Yes*
    - **"N"** - *No*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Shower-Types:

Shower-Types
------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Shower-Types`>/

- Documentation: *Type of showers in the property.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>
- Has text value: *True*
- Codes:
    - **"0"** - *unknown - for backward compatibility only, do not use*
    - **"1"** - *non-electric shower(s) only*
    - **"2"** - *electric shower(s) only*
    - **"3"** - *both electric and non-electric showers*
    - **"4"** - *no shower*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Collector-Loop-Efficiency:

Collector-Loop-Efficiency
-------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Collector-Loop-Efficiency`>/

- Documentation: *Collector loop efficiency; only if declared values.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Incidence-Angle-Modifier:

Incidence-Angle-Modifier
------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Incidence-Angle-Modifier`>/

- Documentation: *Incidence angle modifier; only if declared values.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Is-Community-Solar:

Is-Community-Solar
------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Is-Community-Solar`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Service-Provision:

Service-Provision
-----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Service-Provision`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>
- Has text value: *True*
- Codes:
    - **"1"** - *space and water heating*
    - **"2"** - *space heating only*
    - **"3"** - *water heating only*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Overall-Heat-Loss:

Overall-Heat-Loss
-----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details/Overall-Heat-Loss`>/

- Documentation: *Overall heat loss coefficient of system; only if declared values.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Solar-Water-Heating-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS:

Instantaneous-WWHRS
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS`>/

- Documentation: *Waste Water Heat Recovery Systems*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Index-Number1`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Index-Number2`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Index-Number1:

WWHRS-Index-Number1
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Index-Number1`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Index-Number2:

WWHRS-Index-Number2
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS/WWHRS-Index-Number2`>/

- Documentation: *Omit if no second system.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Instantaneous-WWHRS`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS:

Storage-WWHRS
-------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/WWHRS-Index-Number`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/WWHRS-Store-Volume`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/WWHRS-Index-Number:

WWHRS-Index-Number
------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/WWHRS-Index-Number`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/WWHRS-Store-Volume:

WWHRS-Store-Volume
------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS/WWHRS-Store-Volume`>/

- Documentation: *Dedicated store volume in litres.*
- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Storage-WWHRS`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets:

Shower-Outlets
--------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets`>/

- Documentation2: *Shower outlets present in the dwelling. If there are more than 5 then only include the 5 with the highest flow rates used.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet:

Shower-Outlet
-------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet`>/

- Documentation2: *Various details for each shower outlet.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-Outlet-Type`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-WWHRS`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *5*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-Outlet-Type:

Shower-Outlet-Type
------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-Outlet-Type`>/

- Documentation: *Hot water type for this shower outlet.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet`>
- Has text value: *True*
- Codes:
    - **"0"** - *unknown - for backward compatibility only, do not use*
    - **"1"** - *non-electric shower(s) only*
    - **"2"** - *electric shower(s) only*
    - **"3"** - *both electric and non-electric showers*
    - **"4"** - *no shower*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-WWHRS:

Shower-WWHRS
------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet/Shower-WWHRS`>/

- Documentation: *The WWHRS with which the shower is connected. If shower outlet type is instantaneous electric shower then only a storage WWHRS can be selected or none.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Shower-Outlets/Shower-Outlet`>
- Has text value: *True*
- Codes:
    - **"1"** - *none*
    - **"2"** - *Instantaneous WWHRS 1*
    - **"3"** - *Instantaneous WWHRS 2*
    - **"4"** - *Storage WWHRS*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Number-Baths:

Number-Baths
------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Number-Baths`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Number-Baths-WWHRS:

Number-Baths-WWHRS
------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Number-Baths-WWHRS`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Community-DHW-Network-Index-Number:

Community-DHW-Network-Index-Number
----------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Community-DHW-Network-Index-Number`>/

- Documentation: *index number of heat network, if applicable, community water heating only.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Community-DHW-Sub-Network-Name:

Community-DHW-Sub-Network-Name
------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Community-DHW-Sub-Network-Name`>/

- Documentation: *only if hot water only heat network from pcdb. The name by which the sub community heat network is known.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Community-DHW-Distribution-Type:

Community-DHW-Distribution-Type
-------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Community-DHW-Distribution-Type`>/

- Documentation: *only if hot water only heat network.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>
- Has text value: *True*
- Codes:
    - **"5"** - *calculated*
    - **"6"** - *unknown*
    - **"9"** - *Two adjoining dwellings*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Community-DHW-CHP-Electricity-Generation:

Community-DHW-CHP-Electricity-Generation
----------------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating/Community-DHW-CHP-Electricity-Generation`>/

- Documentation: *Only if community heating not from pcdb and a heat source with CHP. CHP Electricity generation options from table 12f.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Heating`>
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

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source:

SAP-Energy-Source
-----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>/

- Documentation: *Details of energy sources available to the property.*
- Documentation2: *Details of the main Electricity supply to the Property.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Meter-Type`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Mains-Gas`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Electricity-Smart-Meter-Present`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Gas-Smart-Meter-Present`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Is-Dwelling-Export-Capable`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines-Count`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines-Terrain-Type`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbine-Details`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/PV-Connection`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/PV-Diverter`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/PV-Battery-Count`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/PV-Batteries`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Is-Hydro-Output-Connected-To-Dwelling-Meter`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Meter-Type:

Meter-Type
----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Meter-Type`>/

- Documentation: *The type of Electricity Meter - taken from a pre-defined list of values.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>
- Has text value: *True*
- Codes:
    - **"1"** - *dual*
    - **"2"** - *Single*
    - **"3"** - *Unknown*
    - **"4"** - *dual (24 hour)*
    - **"5"** - *off-peak 18 hour*
    - **"6"** - *off-peak 10 hour*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Mains-Gas:

Mains-Gas
---------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Mains-Gas`>/

- Documentation: *Whether mains gas is available in the property.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>
- Has text value: *True*
- Codes:
    - **"Y"** - *mains gas available in the property*
    - **"N"** - *mains gas not available in the property*
    - **"NR"** - *not recorded; for backwards compatibility only, do not use*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Electricity-Smart-Meter-Present:

Electricity-Smart-Meter-Present
-------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Electricity-Smart-Meter-Present`>/

- Documentation: *Is an electricity Smart Meter present?*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Gas-Smart-Meter-Present:

Gas-Smart-Meter-Present
-----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Gas-Smart-Meter-Present`>/

- Documentation: *Is a gas Smart Meter present?*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Is-Dwelling-Export-Capable:

Is-Dwelling-Export-Capable
--------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Is-Dwelling-Export-Capable`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines-Count:

Wind-Turbines-Count
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines-Count`>/

- Documentation: *Number of wind turbines; 0 if none.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines-Terrain-Type:

Wind-Turbines-Terrain-Type
--------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbines-Terrain-Type`>/

- Documentation: *Terrain type*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>
- Has text value: *True*
- Codes:
    - **"1"** - *urban*
    - **"2"** - *suburban*
    - **"3"** - *rural*
    - **"4"** - *not recorded*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbine-Details:

Wind-Turbine-Details
--------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbine-Details`>/

- Documentation: *Included when details are known*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbine-Details/Rotor-Diameter`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbine-Details/Hub-Height`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbine-Details/Rotor-Diameter:

Rotor-Diameter
--------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbine-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbine-Details/Rotor-Diameter`>/

- Documentation: *Diameter of rotor of wind turbine*
- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbine-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbine-Details/Hub-Height:

Hub-Height
----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbine-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbine-Details/Hub-Height`>/

- Documentation: *Height of rotor hub above ridge of roof*
- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Wind-Turbine-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply:

Photovoltaic-Supply
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/PV-Arrays`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/None-Or-No-Details`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/PV-Arrays:

PV-Arrays
---------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/PV-Arrays`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/PV-Arrays/PV-Array`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *3*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/PV-Arrays/PV-Array:

PV-Array
--------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/PV-Arrays`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/PV-Arrays/PV-Array`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/PV-Arrays`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/PV-Arrays/PV-Array/Peak-Power`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/PV-Arrays/PV-Array/Orientation`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/PV-Arrays/PV-Array/Pitch`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/PV-Arrays/PV-Array/Overshading`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/PV-Arrays/PV-Array/Peak-Power:

Peak-Power
----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/PV-Arrays`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/PV-Arrays/PV-Array`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/PV-Arrays/PV-Array/Peak-Power`>/

- Documentation: *Peak kW of photovoltaics (PVs) (kWp). If the total peak power has been apportioned between different dwellings within the same building, this is the kWp ascribed to the dwelling being assessed.*
- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/PV-Arrays/PV-Array`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/PV-Arrays/PV-Array/Orientation:

Orientation
-----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/PV-Arrays`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/PV-Arrays/PV-Array`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/PV-Arrays/PV-Array/Orientation`>/

- Documentation: *PV orientation; only if peak kWp > 0.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/PV-Arrays/PV-Array`>
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
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/PV-Arrays/PV-Array/Pitch:

Pitch
-----

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/PV-Arrays`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/PV-Arrays/PV-Array`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/PV-Arrays/PV-Array/Pitch`>/

- Documentation: *PV pitch; only if peak kWp > 0.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/PV-Arrays/PV-Array`>
- Has text value: *True*
- Codes:
    - **"1"** - *horizontal*
    - **"2"** - *30 degrees*
    - **"3"** - *45 degrees*
    - **"4"** - *60 degrees*
    - **"5"** - *vertical*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/PV-Arrays/PV-Array/Overshading:

Overshading
-----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/PV-Arrays`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/PV-Arrays/PV-Array`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/PV-Arrays/PV-Array/Overshading`>/

- Documentation: *PV overshading; only if peak kWp > 0.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/PV-Arrays/PV-Array`>
- Has text value: *True*
- Codes:
    - **"1"** - *none or very little*
    - **"2"** - *modest*
    - **"3"** - *significant*
    - **"4"** - *heavy*
    - **"5"** - *severe*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/None-Or-No-Details:

None-Or-No-Details
------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/None-Or-No-Details`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/None-Or-No-Details/Percent-Roof-Area`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/None-Or-No-Details/Percent-Roof-Area:

Percent-Roof-Area
-----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/None-Or-No-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/None-Or-No-Details/Percent-Roof-Area`>/

- Documentation: *Photovoltaic area as percentage of total roof area. 0% indicates that a photovoltaic supply is not present in the property.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Photovoltaic-Supply/None-Or-No-Details`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/PV-Connection:

PV-Connection
-------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/PV-Connection`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>
- Has text value: *True*
- Codes:
    - **"0"** - *not applicable (FGHRS or no PV)*
    - **"1"** - *not connected to dwelling's electricity meter*
    - **"2"** - *connected to dwelling's electricity meter*
    - **"NR"** - *not recorded; for backwards compatibility only, do not use*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/PV-Diverter:

PV-Diverter
-----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/PV-Diverter`>/

- Documentation: *Diverter present.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/PV-Battery-Count:

PV-Battery-Count
----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/PV-Battery-Count`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/PV-Batteries:

PV-Batteries
------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/PV-Batteries`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/PV-Batteries/PV-Battery`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/PV-Batteries/PV-Battery:

PV-Battery
----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/PV-Batteries`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/PV-Batteries/PV-Battery`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/PV-Batteries`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/PV-Batteries/PV-Battery/Battery-Capacity`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *20*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/PV-Batteries/PV-Battery/Battery-Capacity:

Battery-Capacity
----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/PV-Batteries`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/PV-Batteries/PV-Battery`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/PV-Batteries/PV-Battery/Battery-Capacity`>/

- Documentation: *Battery capacity in kWh. defaults to 5kW in unknown.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/PV-Batteries/PV-Battery`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation:

Hydro-Electric-Generation
-------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Hydro-Electric-Generation`>/

- Documentation: *Electricity generated by hydro-electric generator, in kWh/year. To be provided if Hydro-Electric-Generation-Month is not provided.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Is-Hydro-Output-Connected-To-Dwelling-Meter:

Is-Hydro-Output-Connected-To-Dwelling-Meter
-------------------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source/Is-Hydro-Output-Connected-To-Dwelling-Meter`>/

- Documentation: *Whether the hydro-electric station is connected to dwelling's electricity meter*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Energy-Source`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts:

SAP-Building-Parts
------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/

- Documentation2: *Details of the significant building parts that comprise the main habitable building in the property. The main habitable area generally consists of a single main building but can over time be extended to include extensions such as new wings and additional storeys. For the purpose of calculating the overall Energy Assessment for the property details of each distinct Building Part, such as its construction, have to be gathered because different materials have different insulation ratings (obviously) which affects the overall rating.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Integral-Conservatory`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Integral-Conservatory:

SAP-Integral-Conservatory
-------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Integral-Conservatory`>/

- Documentation2: *A conservatory intergrated into the property that is within the heat-loss perimeter and forms part of the habitable area.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Integral-Conservatory/Double-Glazed`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Integral-Conservatory/Floor-Area`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Integral-Conservatory/Glazed-Perimeter`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Integral-Conservatory/Room-Height`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Integral-Conservatory/Double-Glazed:

Double-Glazed
-------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Integral-Conservatory`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Integral-Conservatory/Double-Glazed`>/

- Documentation: *Indicates whether the conservatory is double glazed*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Integral-Conservatory`>
- Has text value: *True*
- Codes:
    - **"Y"** - *Yes*
    - **"N"** - *No*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Integral-Conservatory/Floor-Area:

Floor-Area
----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Integral-Conservatory`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Integral-Conservatory/Floor-Area`>/

- Documentation: *The gross floor area of the conservatory*
- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Integral-Conservatory`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Integral-Conservatory/Glazed-Perimeter:

Glazed-Perimeter
----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Integral-Conservatory`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Integral-Conservatory/Glazed-Perimeter`>/

- Documentation: *The length of the glazed area*
- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Integral-Conservatory`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Integral-Conservatory/Room-Height:

Room-Height
-----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Integral-Conservatory`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Integral-Conservatory/Room-Height`>/

- Documentation: *The average height of the conservatory*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Integral-Conservatory`>
- Has text value: *True*
- Codes:
    - **"1"** - *1 storey*
    - **"1.5"** - *1.5 storey*
    - **"2"** - *2 storey*
    - **"2.5"** - *2.5 storey*
    - **"3"** - *3 storey*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part:

SAP-Building-Part
-----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/

- Documentation2: *A permanent structure that forms part of the Property and is built primarily for human habitation. A Building is usually made up of one or more Storey's and may contain a number of Internal Structural Features. An extension would be a Building Part.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Building-Part-Number`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Identifier`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Construction-Age-Band`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Floor-U-Value`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Floor-Insulation-Thickness`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Floor-Heat-Loss`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Roof-Construction`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Roof-Insulation-Location`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Roof-U-Value`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Roof-Insulation-Thickness`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Rafter-Insulation-Thickness`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Flat-Roof-Insulation-Thickness`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Sloping-Ceiling-Insulation-Thickness`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Wall-Construction`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Wall-Insulation-Type`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Wall-Thickness-Measured`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Wall-Thickness`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Wall-Dry-Lined`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Wall-U-Value`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Wall-Insulation-Thickness`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Wall-Insulation-Thickness-Measured`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Wall-Insulation-Thermal-Conductivity`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Party-Wall-Construction`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *unbounded*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Building-Part-Number:

Building-Part-Number
--------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Building-Part-Number`>/

- Documentation: *An integer value which uniquely identifies the building part in the property. The value "1" must be assigned to the main dwelling.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Identifier:

Identifier
----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Identifier`>/

- Documentation: *Identifier for the Building part - generally only required if there are more that one Building Parts of the same type e.g. "West Wing" and "East Wing" Extensions*
- Documentation2: *A string containing a unique identifier for something. The underlying assumption is that each instance of a class or entity will have a unique identifier assigned to it which can then be assigned to any referencing entity as a reference to the entity instance. This is a very similar concept to XML ID datatype but is locally defined because of the need to extend the datatype with domain specific attributes.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Construction-Age-Band:

Construction-Age-Band
---------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Construction-Age-Band`>/

- Documentation: *The age band when this building part was constructed.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
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
    - **"L"** - *England and Wales: 2012-2021; Scotland: 2012-2022; Northern Ireland: 2014 onwards*
    - **"M"** - *England and Wales: 2022 onwards; Scotland: 2023 onwards (TBA); Northern Ireland: 2014 onwards (TBA)*
    - **"0"** - *Not applicable*
    - **"NR"** - *Not recorded*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions:

SAP-Floor-Dimensions
--------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension:

SAP-Floor-Dimension
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>/

- Documentation2: *Various measurements for each floor that makes up a particular Build-Part.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Heat-Loss-Perimeter`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Room-Height`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Total-Floor-Area`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Floor`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Floor-Construction`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Floor-Insulation`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Party-Wall-Length`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *unbounded*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Heat-Loss-Perimeter:

Heat-Loss-Perimeter
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Heat-Loss-Perimeter`>/

- Documentation: *The estimate total heat loss perimeter for the Storey. The heat loss perimeter is any part of the storey that is exposed to the outside world through which heat may escape.*
- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Room-Height:

Room-Height
-----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Room-Height`>/

- Documentation: *Average height of the Storey*
- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Total-Floor-Area:

Total-Floor-Area
----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Total-Floor-Area`>/

- Documentation: *The total floor area of the storey*
- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Floor:

Floor
-----

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Floor`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>
- Has text value: *True*
- Codes:
    - **"0"** - *lowest occupied*
    - **"1"** - *lowest+1*
    - **"2"** - *lowest+2*
    - **"3"** - *lowest+3*
    - **"4"** - *lowest+4*
    - **"5"** - *lowest+5*
    - **"6"** - *lowest+6*
    - **"99"** - *roof rooms*
    - **"NR"** - *not recorded*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Floor-Construction:

Floor-Construction
------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Floor-Construction`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>
- Has text value: *True*
- Codes:
    - **"0"** - *unknown*
    - **"1"** - *solid*
    - **"2"** - *suspended timber*
    - **"3"** - *suspended (not timber)*
    - **"4"** - *basement floor*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Floor-Insulation:

Floor-Insulation
----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Floor-Insulation`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>
- Has text value: *True*
- Codes:
    - **"0"** - *unknown*
    - **"1"** - *as built*
    - **"2"** - *retro-fitted*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Party-Wall-Length:

Party-Wall-Length
-----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension/Party-Wall-Length`>/

- Documentation: *set to zero if no party wall*
- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Floor-Dimensions/SAP-Floor-Dimension`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Floor-U-Value:

Floor-U-Value
-------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Floor-U-Value`>/

- Documentation: *Only one of Floor-Insulation-Thickness and Floor-U-Value is included*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Floor-Insulation-Thickness:

Floor-Insulation-Thickness
--------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Floor-Insulation-Thickness`>/

- Documentation: *Only one of Floor-Insulation-Thickness and Floor-U-Value is included*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Has text value: *True*
- Codes:
    - **"NI"** - *unknown*
    - **"25mm"** - *25mm*
    - **"50mm"** - *50mm*
    - **"75mm"** - *75mm*
    - **"100mm"** - *100mm*
    - **"125mm"** - *125mm*
    - **"150mm"** - *150mm*
    - **"175mm"** - *175mm*
    - **"200mm"** - *200mm*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Floor-Heat-Loss:

Floor-Heat-Loss
---------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Floor-Heat-Loss`>/

- Documentation: *Identifies the type of foor through which heat loss occurs.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Has text value: *True*
- Codes:
    - **"1"** - *exposed floor*
    - **"2"** - *semi-exposed upper floor to unheated space*
    - **"3"** - *semi-exposed upper floor to partially heated space*
    - **"6"** - *Other flat below*
    - **"7"** - *Ground floor*
    - **"8"** - *same dwelling below*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Roof-Construction:

Roof-Construction
-----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Roof-Construction`>/

- Documentation: *Describes the material that the roof of the Building Part is constructed from e.g. Tile, Slate etc.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Has text value: *True*
- Codes:
    - **"0"** - *None*
    - **"1"** - *Flat*
    - **"2"** - *Pitched. This is retained for backwards compatibility only and should not be used. A pitched roof should be 4, 5, 6 or 8*
    - **"3"** - *Another dwelling above*
    - **"4"** - *Pitched (slates or tiles), access to loft*
    - **"5"** - *Pitched (slates or tiles), no access to loft*
    - **"6"** - *Pitched (thatch)*
    - **"7"** - *Same dwelling above*
    - **"8"** - *Pitched roof with sloping ceiling*
    - **"9"** - *Non residential/unheated space*
    - **"NR"** - *Not recorded*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Roof-Insulation-Location:

Roof-Insulation-Location
------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Roof-Insulation-Location`>/

- Documentation: *The location of the insulation in the roof e.g. between joists, in rafters etc.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Has text value: *True*
- Codes:
    - **"1"** - *Rafters*
    - **"2"** - *Joists*
    - **"3"** - *No access.. This is retained for backwards compatibility only and should not be used. No access is covered by enum 5 of RoofTypeCode*
    - **"4"** - *Unknown*
    - **"5"** - *None; applicable only when Roof-Construction is 4, 5 or 6*
    - **"6"** - *Flat roof insulation*
    - **"7"** - *Sloping ceiling insulation*
    - **"ND"** - *Not Defined*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Roof-U-Value:

Roof-U-Value
------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Roof-U-Value`>/

- Documentation: *Include one of Roof-U-Value, Roof-Insulation-Thickness, Rafter-Insulation-Thickness, Flat-Roof-Insulation-Thickness, Sloping-Ceiling-Insulation-Thickness*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Roof-Insulation-Thickness:

Roof-Insulation-Thickness
-------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Roof-Insulation-Thickness`>/

- Documentation: *See Roof-U-Value*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Has text value: *True*
- Codes:
    - **"NI"** - *unknown*
    - **"0"** - *None*
    - **"12mm"** - *12mm*
    - **"25mm"** - *25mm*
    - **"50mm"** - *50mm*
    - **"75mm"** - *75mm*
    - **"100mm"** - *100mm*
    - **"125mm"** - *125mm*
    - **"150mm"** - *150mm*
    - **"175mm"** - *175mm*
    - **"200mm"** - *200mm*
    - **"225mm"** - *225mm*
    - **"250mm"** - *250mm*
    - **"270mm"** - *270mm*
    - **"300mm"** - *300mm*
    - **"350mm"** - *350mm*
    - **"400mm+"** - *400mm or more*
    - **"ND"** - *Not Defined*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Rafter-Insulation-Thickness:

Rafter-Insulation-Thickness
---------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Rafter-Insulation-Thickness`>/

- Documentation: *See Roof-U-Value*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Has text value: *True*
- Codes:
    - **"NI"** - *insulation thickness unknown*
    - **"AB"** - *as built*
    - **"12mm"** - *12mm*
    - **"25mm"** - *25mm*
    - **"50mm"** - *50mm*
    - **"75mm"** - *75mm*
    - **"100mm"** - *100mm*
    - **"125mm"** - *125mm*
    - **"150mm"** - *150mm*
    - **"175mm"** - *175mm*
    - **"200mm"** - *200mm*
    - **"225mm"** - *225mm*
    - **"250mm"** - *250mm*
    - **"270mm"** - *270mm*
    - **"300mm"** - *300mm*
    - **"350mm"** - *350mm*
    - **"400+mm"** - *400+mm*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Flat-Roof-Insulation-Thickness:

Flat-Roof-Insulation-Thickness
------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Flat-Roof-Insulation-Thickness`>/

- Documentation: *See Roof-U-Value*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Has text value: *True*
- Codes:
    - **"NI"** - *insulation thickness unknown*
    - **"AB"** - *as built*
    - **"12mm"** - *12mm*
    - **"25mm"** - *25mm*
    - **"50mm"** - *50mm*
    - **"75mm"** - *75mm*
    - **"100mm"** - *100mm*
    - **"125mm"** - *125mm*
    - **"150mm"** - *150mm*
    - **"175mm"** - *175mm*
    - **"200mm"** - *200mm*
    - **"225mm"** - *225mm*
    - **"250mm"** - *250mm*
    - **"270mm"** - *270mm*
    - **"300mm"** - *300mm*
    - **"350mm"** - *350mm*
    - **"400+mm"** - *400+mm*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Sloping-Ceiling-Insulation-Thickness:

Sloping-Ceiling-Insulation-Thickness
------------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Sloping-Ceiling-Insulation-Thickness`>/

- Documentation: *See Roof-U-Value*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Has text value: *True*
- Codes:
    - **"NI"** - *insulation thickness unknown*
    - **"AB"** - *as built*
    - **"12mm"** - *12mm*
    - **"25mm"** - *25mm*
    - **"50mm"** - *50mm*
    - **"75mm"** - *75mm*
    - **"100mm"** - *100mm*
    - **"125mm"** - *125mm*
    - **"150mm"** - *150mm*
    - **"175mm"** - *175mm*
    - **"200mm"** - *200mm*
    - **"225mm"** - *225mm*
    - **"250mm"** - *250mm*
    - **"270mm"** - *270mm*
    - **"300mm"** - *300mm*
    - **"350mm"** - *350mm*
    - **"400+mm"** - *400+mm*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Wall-Construction:

Wall-Construction
-----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Wall-Construction`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Has text value: *True*
- Codes:
    - **"1"** - *stone (granite or whinstone)*
    - **"2"** - *stone (sandstone or limestone)*
    - **"3"** - *solid brick*
    - **"4"** - *cavity*
    - **"5"** - *timber frame*
    - **"6"** - *basement wall*
    - **"7"** - *curtain wall*
    - **"8"** - *system built*
    - **"9"** - *cob wall*
    - **"10"** - *park home wall*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Wall-Insulation-Type:

Wall-Insulation-Type
--------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Wall-Insulation-Type`>/

- Documentation: *Describes the type of insulation present in the wall if any.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Has text value: *True*
- Codes:
    - **"1"** - *external*
    - **"2"** - *filled cavity*
    - **"3"** - *internal*
    - **"4"** - *as built*
    - **"5"** - *unknown*
    - **"6"** - *filled cavity + external*
    - **"7"** - *filled cavity + internal*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Wall-Thickness-Measured:

Wall-Thickness-Measured
-----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Wall-Thickness-Measured`>/

- Documentation: *Whether wall thickness was measured*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Has text value: *True*
- Codes:
    - **"Y"** - *Yes*
    - **"N"** - *No*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Wall-Thickness:

Wall-Thickness
--------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Wall-Thickness`>/

- Documentation: *Wall thickness in mm. Omitted if Wall-Thickness-Measured is false*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Wall-Dry-Lined:

Wall-Dry-Lined
--------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Wall-Dry-Lined`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Has text value: *True*
- Codes:
    - **"Y"** - *Yes*
    - **"N"** - *No*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Wall-U-Value:

Wall-U-Value
------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Wall-U-Value`>/

- Documentation: *Only one of Wall-Insulation-Thickness and Wall-U-Value is included*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Wall-Insulation-Thickness:

Wall-Insulation-Thickness
-------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Wall-Insulation-Thickness`>/

- Documentation: *Only one of Wall-Insulation-Thickness and Wall-U-Value is included*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Has text value: *True*
- Codes:
    - **"NI"** - *unknown*
    - **"10mm"** - *10 mm*
    - **"25mm"** - *25 mm*
    - **"50mm"** - *50 mm*
    - **"75mm"** - *75 mm*
    - **"100mm"** - *100 mm*
    - **"125mm"** - *125 mm*
    - **"150mm"** - *150 mm*
    - **"175mm"** - *175 mm*
    - **"200mm"** - *200mm*
    - **"measured"** - *if wall insulation thickness is provided with precise measurement*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Wall-Insulation-Thickness-Measured:

Wall-Insulation-Thickness-Measured
----------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Wall-Insulation-Thickness-Measured`>/

- Documentation: *Only one of Wall-Insulation-Thickness is measured and Wall-U-Value is included*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Wall-Insulation-Thermal-Conductivity:

Wall-Insulation-Thermal-Conductivity
------------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Wall-Insulation-Thermal-Conductivity`>/

- Documentation: *Only if documentary evidence is available*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Has text value: *True*
- Codes:
    - **"1"** - *0.04*
    - **"2"** - *0.03*
    - **"3"** - *0.025*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof:

SAP-Room-In-Roof
----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Floor-Area`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Construction-Age-Band`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-1`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Floor-Area:

Floor-Area
----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Floor-Area`>/

- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Construction-Age-Band:

Construction-Age-Band
---------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Construction-Age-Band`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>
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
    - **"L"** - *England and Wales: 2012-2021; Scotland: 2012-2022; Northern Ireland: 2014 onwards*
    - **"M"** - *England and Wales: 2022 onwards; Scotland: 2023 onwards (TBA); Northern Ireland: 2014 onwards (TBA)*
    - **"0"** - *Not applicable*
    - **"NR"** - *Not recorded*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details:

Room-In-Roof-Details
--------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/

- Documentation: *Omit when Room-In-Roof details not included*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Flat-Ceiling-Length-1`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Flat-Ceiling-Height-1`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Flat-Ceiling-U-Value-1`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Flat-Ceiling-Insulation-Thickness-1`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Flat-Ceiling-Insulation-Type-1`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Flat-Ceiling-Insulation-Location-1`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Flat-Ceiling-Length-2`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Flat-Ceiling-Height-2`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Flat-Ceiling-U-Value-2`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Flat-Ceiling-Insulation-Thickness-2`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Flat-Ceiling-Insulation-Type-2`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Flat-Ceiling-Insulation-Location-2`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Stud-Wall-Length-1`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Stud-Wall-Height-1`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Stud-Wall-U-Value-1`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Stud-Wall-Insulation-Thickness-1`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Stud-Wall-Insulation-Type-1`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Stud-Wall-Length-2`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Stud-Wall-Height-2`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Stud-Wall-U-Value-2`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Stud-Wall-Insulation-Thickness-2`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Stud-Wall-Insulation-Type-2`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Slope-Length-1`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Slope-Height-1`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Slope-U-Value-1`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Slope-Insulation-Thickness-1`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Slope-Insulation-Type-1`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Slope-Length-2`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Slope-Height-2`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Slope-U-Value-2`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Slope-Insulation-Thickness-2`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Slope-Insulation-Type-2`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Gable-Wall-Length-1`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Gable-Wall-Height-1`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Gable-Wall-U-Value-1`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Gable-Wall-Type-1`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Gable-Wall-Length-2`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Gable-Wall-Height-2`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Gable-Wall-U-Value-2`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Gable-Wall-Type-2`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Common-Wall-Length-1`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Common-Wall-Height-1`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Common-Wall-U-Value-1`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Common-Wall-Length-2`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Common-Wall-Height-2`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Common-Wall-U-Value-2`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Flat-Ceiling-Length-1:

Flat-Ceiling-Length-1
---------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Flat-Ceiling-Length-1`>/

- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Flat-Ceiling-Height-1:

Flat-Ceiling-Height-1
---------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Flat-Ceiling-Height-1`>/

- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Flat-Ceiling-U-Value-1:

Flat-Ceiling-U-Value-1
----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Flat-Ceiling-U-Value-1`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Flat-Ceiling-Insulation-Thickness-1:

Flat-Ceiling-Insulation-Thickness-1
-----------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Flat-Ceiling-Insulation-Thickness-1`>/

- Documentation: *Mutually exclusive with U-value. Either U-value provided, or thickness.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Codes:
    - **"NI"** - *unknown*
    - **"0"** - *None*
    - **"12mm"** - *12mm*
    - **"25mm"** - *25mm*
    - **"50mm"** - *50mm*
    - **"75mm"** - *75mm*
    - **"100mm"** - *100mm*
    - **"125mm"** - *125mm*
    - **"150mm"** - *150mm*
    - **"175mm"** - *175mm*
    - **"200mm"** - *200mm*
    - **"225mm"** - *225mm*
    - **"250mm"** - *250mm*
    - **"270mm"** - *270mm*
    - **"300mm"** - *300mm*
    - **"350mm"** - *350mm*
    - **"400mm+"** - *400mm or more*
    - **"ND"** - *Not Defined*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Flat-Ceiling-Insulation-Type-1:

Flat-Ceiling-Insulation-Type-1
------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Flat-Ceiling-Insulation-Type-1`>/

- Documentation: *Mutually exclusive with U-value. Either U-value provided, or thickness.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Codes:
    - **"0"** - *mineral wool or EPS slab*
    - **"1"** - *PUR or PIR*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Flat-Ceiling-Insulation-Location-1:

Flat-Ceiling-Insulation-Location-1
----------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Flat-Ceiling-Insulation-Location-1`>/

- Documentation: *Mutually exclusive with U-value and insulation type. Either U-value provided, or insulation type or location. To enable using table 16.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Codes:
    - **"1"** - *Rafters*
    - **"2"** - *Joists*
    - **"3"** - *No access.. This is retained for backwards compatibility only and should not be used. No access is covered by enum 5 of RoofTypeCode*
    - **"4"** - *Unknown*
    - **"5"** - *None; applicable only when Roof-Construction is 4, 5 or 6*
    - **"6"** - *Flat roof insulation*
    - **"7"** - *Sloping ceiling insulation*
    - **"ND"** - *Not Defined*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Flat-Ceiling-Length-2:

Flat-Ceiling-Length-2
---------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Flat-Ceiling-Length-2`>/

- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Flat-Ceiling-Height-2:

Flat-Ceiling-Height-2
---------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Flat-Ceiling-Height-2`>/

- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Flat-Ceiling-U-Value-2:

Flat-Ceiling-U-Value-2
----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Flat-Ceiling-U-Value-2`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Flat-Ceiling-Insulation-Thickness-2:

Flat-Ceiling-Insulation-Thickness-2
-----------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Flat-Ceiling-Insulation-Thickness-2`>/

- Documentation: *Mutually exclusive with U-value. Either U-value provided, or thickness.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Codes:
    - **"NI"** - *unknown*
    - **"0"** - *None*
    - **"12mm"** - *12mm*
    - **"25mm"** - *25mm*
    - **"50mm"** - *50mm*
    - **"75mm"** - *75mm*
    - **"100mm"** - *100mm*
    - **"125mm"** - *125mm*
    - **"150mm"** - *150mm*
    - **"175mm"** - *175mm*
    - **"200mm"** - *200mm*
    - **"225mm"** - *225mm*
    - **"250mm"** - *250mm*
    - **"270mm"** - *270mm*
    - **"300mm"** - *300mm*
    - **"350mm"** - *350mm*
    - **"400mm+"** - *400mm or more*
    - **"ND"** - *Not Defined*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Flat-Ceiling-Insulation-Type-2:

Flat-Ceiling-Insulation-Type-2
------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Flat-Ceiling-Insulation-Type-2`>/

- Documentation: *Mutually exclusive with U-value. Either U-value provided, or thickness.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Codes:
    - **"0"** - *mineral wool or EPS slab*
    - **"1"** - *PUR or PIR*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Flat-Ceiling-Insulation-Location-2:

Flat-Ceiling-Insulation-Location-2
----------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Flat-Ceiling-Insulation-Location-2`>/

- Documentation: *Mutually exclusive with U-value and insulation type. Either U-value provided, or insulation type or location. To enable using table 16.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Codes:
    - **"1"** - *Rafters*
    - **"2"** - *Joists*
    - **"3"** - *No access.. This is retained for backwards compatibility only and should not be used. No access is covered by enum 5 of RoofTypeCode*
    - **"4"** - *Unknown*
    - **"5"** - *None; applicable only when Roof-Construction is 4, 5 or 6*
    - **"6"** - *Flat roof insulation*
    - **"7"** - *Sloping ceiling insulation*
    - **"ND"** - *Not Defined*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Stud-Wall-Length-1:

Stud-Wall-Length-1
------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Stud-Wall-Length-1`>/

- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Stud-Wall-Height-1:

Stud-Wall-Height-1
------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Stud-Wall-Height-1`>/

- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Stud-Wall-U-Value-1:

Stud-Wall-U-Value-1
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Stud-Wall-U-Value-1`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Stud-Wall-Insulation-Thickness-1:

Stud-Wall-Insulation-Thickness-1
--------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Stud-Wall-Insulation-Thickness-1`>/

- Documentation: *Mutually exclusive with U-value. Either U-value provided, or thickness.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Codes:
    - **"NI"** - *unknown*
    - **"0"** - *None*
    - **"12mm"** - *12mm*
    - **"25mm"** - *25mm*
    - **"50mm"** - *50mm*
    - **"75mm"** - *75mm*
    - **"100mm"** - *100mm*
    - **"125mm"** - *125mm*
    - **"150mm"** - *150mm*
    - **"175mm"** - *175mm*
    - **"200mm"** - *200mm*
    - **"225mm"** - *225mm*
    - **"250mm"** - *250mm*
    - **"270mm"** - *270mm*
    - **"300mm"** - *300mm*
    - **"350mm"** - *350mm*
    - **"400mm+"** - *400mm or more*
    - **"ND"** - *Not Defined*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Stud-Wall-Insulation-Type-1:

Stud-Wall-Insulation-Type-1
---------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Stud-Wall-Insulation-Type-1`>/

- Documentation: *Mutually exclusive with U-value. Either U-value provided, or thickness.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Codes:
    - **"0"** - *mineral wool or EPS slab*
    - **"1"** - *PUR or PIR*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Stud-Wall-Length-2:

Stud-Wall-Length-2
------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Stud-Wall-Length-2`>/

- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Stud-Wall-Height-2:

Stud-Wall-Height-2
------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Stud-Wall-Height-2`>/

- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Stud-Wall-U-Value-2:

Stud-Wall-U-Value-2
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Stud-Wall-U-Value-2`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Stud-Wall-Insulation-Thickness-2:

Stud-Wall-Insulation-Thickness-2
--------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Stud-Wall-Insulation-Thickness-2`>/

- Documentation: *Mutually exclusive with U-value. Either U-value provided, or thickness.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Codes:
    - **"NI"** - *unknown*
    - **"0"** - *None*
    - **"12mm"** - *12mm*
    - **"25mm"** - *25mm*
    - **"50mm"** - *50mm*
    - **"75mm"** - *75mm*
    - **"100mm"** - *100mm*
    - **"125mm"** - *125mm*
    - **"150mm"** - *150mm*
    - **"175mm"** - *175mm*
    - **"200mm"** - *200mm*
    - **"225mm"** - *225mm*
    - **"250mm"** - *250mm*
    - **"270mm"** - *270mm*
    - **"300mm"** - *300mm*
    - **"350mm"** - *350mm*
    - **"400mm+"** - *400mm or more*
    - **"ND"** - *Not Defined*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Stud-Wall-Insulation-Type-2:

Stud-Wall-Insulation-Type-2
---------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Stud-Wall-Insulation-Type-2`>/

- Documentation: *Mutually exclusive with U-value. Either U-value provided, or thickness.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Codes:
    - **"0"** - *mineral wool or EPS slab*
    - **"1"** - *PUR or PIR*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Slope-Length-1:

Slope-Length-1
--------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Slope-Length-1`>/

- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Slope-Height-1:

Slope-Height-1
--------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Slope-Height-1`>/

- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Slope-U-Value-1:

Slope-U-Value-1
---------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Slope-U-Value-1`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Slope-Insulation-Thickness-1:

Slope-Insulation-Thickness-1
----------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Slope-Insulation-Thickness-1`>/

- Documentation: *Mutually exclusive with U-value. Either U-value provided, or thickness.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Codes:
    - **"NI"** - *unknown*
    - **"0"** - *None*
    - **"12mm"** - *12mm*
    - **"25mm"** - *25mm*
    - **"50mm"** - *50mm*
    - **"75mm"** - *75mm*
    - **"100mm"** - *100mm*
    - **"125mm"** - *125mm*
    - **"150mm"** - *150mm*
    - **"175mm"** - *175mm*
    - **"200mm"** - *200mm*
    - **"225mm"** - *225mm*
    - **"250mm"** - *250mm*
    - **"270mm"** - *270mm*
    - **"300mm"** - *300mm*
    - **"350mm"** - *350mm*
    - **"400mm+"** - *400mm or more*
    - **"ND"** - *Not Defined*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Slope-Insulation-Type-1:

Slope-Insulation-Type-1
-----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Slope-Insulation-Type-1`>/

- Documentation: *Mutually exclusive with U-value. Either U-value provided, or thickness.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Codes:
    - **"0"** - *mineral wool or EPS slab*
    - **"1"** - *PUR or PIR*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Slope-Length-2:

Slope-Length-2
--------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Slope-Length-2`>/

- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Slope-Height-2:

Slope-Height-2
--------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Slope-Height-2`>/

- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Slope-U-Value-2:

Slope-U-Value-2
---------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Slope-U-Value-2`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Slope-Insulation-Thickness-2:

Slope-Insulation-Thickness-2
----------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Slope-Insulation-Thickness-2`>/

- Documentation: *Mutually exclusive with U-value. Either U-value provided, or thickness.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Codes:
    - **"NI"** - *unknown*
    - **"0"** - *None*
    - **"12mm"** - *12mm*
    - **"25mm"** - *25mm*
    - **"50mm"** - *50mm*
    - **"75mm"** - *75mm*
    - **"100mm"** - *100mm*
    - **"125mm"** - *125mm*
    - **"150mm"** - *150mm*
    - **"175mm"** - *175mm*
    - **"200mm"** - *200mm*
    - **"225mm"** - *225mm*
    - **"250mm"** - *250mm*
    - **"270mm"** - *270mm*
    - **"300mm"** - *300mm*
    - **"350mm"** - *350mm*
    - **"400mm+"** - *400mm or more*
    - **"ND"** - *Not Defined*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Slope-Insulation-Type-2:

Slope-Insulation-Type-2
-----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Slope-Insulation-Type-2`>/

- Documentation: *Mutually exclusive with U-value. Either U-value provided, or thickness.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Codes:
    - **"0"** - *mineral wool or EPS slab*
    - **"1"** - *PUR or PIR*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Gable-Wall-Length-1:

Gable-Wall-Length-1
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Gable-Wall-Length-1`>/

- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Gable-Wall-Height-1:

Gable-Wall-Height-1
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Gable-Wall-Height-1`>/

- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Gable-Wall-U-Value-1:

Gable-Wall-U-Value-1
--------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Gable-Wall-U-Value-1`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Gable-Wall-Type-1:

Gable-Wall-Type-1
-----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Gable-Wall-Type-1`>/

- Documentation: *Mutually exclusive with U-value. Either U-value provided, or gable type to use table 4.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Codes:
    - **"0"** - *exposed*
    - **"1"** - *party*
    - **"2"** - *Sheltered*
    - **"3"** - *connected or adjacent to heated space*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Gable-Wall-Length-2:

Gable-Wall-Length-2
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Gable-Wall-Length-2`>/

- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Gable-Wall-Height-2:

Gable-Wall-Height-2
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Gable-Wall-Height-2`>/

- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Gable-Wall-U-Value-2:

Gable-Wall-U-Value-2
--------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Gable-Wall-U-Value-2`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Gable-Wall-Type-2:

Gable-Wall-Type-2
-----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Gable-Wall-Type-2`>/

- Documentation: *Mutually exclusive with U-value. Either U-value provided, or gable type to use table 4.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Codes:
    - **"0"** - *exposed*
    - **"1"** - *party*
    - **"2"** - *Sheltered*
    - **"3"** - *connected or adjacent to heated space*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Common-Wall-Length-1:

Common-Wall-Length-1
--------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Common-Wall-Length-1`>/

- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Common-Wall-Height-1:

Common-Wall-Height-1
--------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Common-Wall-Height-1`>/

- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Common-Wall-U-Value-1:

Common-Wall-U-Value-1
---------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Common-Wall-U-Value-1`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Common-Wall-Length-2:

Common-Wall-Length-2
--------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Common-Wall-Length-2`>/

- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Common-Wall-Height-2:

Common-Wall-Height-2
--------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Common-Wall-Height-2`>/

- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Common-Wall-U-Value-2:

Common-Wall-U-Value-2
---------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details/Common-Wall-U-Value-2`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-1:

Room-In-Roof-Type-1
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-1`>/

- Documentation: *Required if detailed input not provided, and RR type 1*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-1/Gable-Wall-Length-1`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-1/Gable-Wall-Type-1`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-1/Gable-Wall-Length-2`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-1/Gable-Wall-Type-2`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-1/Gable-Wall-Length-1:

Gable-Wall-Length-1
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-1`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-1/Gable-Wall-Length-1`>/

- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-1`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-1/Gable-Wall-Type-1:

Gable-Wall-Type-1
-----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-1`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-1/Gable-Wall-Type-1`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-1`>
- Has text value: *True*
- Codes:
    - **"0"** - *exposed*
    - **"1"** - *party*
    - **"2"** - *Sheltered*
    - **"3"** - *connected or adjacent to heated space*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-1/Gable-Wall-Length-2:

Gable-Wall-Length-2
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-1`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-1/Gable-Wall-Length-2`>/

- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-1`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-1/Gable-Wall-Type-2:

Gable-Wall-Type-2
-----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-1`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-1/Gable-Wall-Type-2`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-1`>
- Has text value: *True*
- Codes:
    - **"0"** - *exposed*
    - **"1"** - *party*
    - **"2"** - *Sheltered*
    - **"3"** - *connected or adjacent to heated space*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2:

Room-In-Roof-Type-2
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2`>/

- Documentation: *Required if detailed input not provided, and RR type 2*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2/Gable-Wall-Length-1`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2/Gable-Wall-Height-1`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2/Gable-Wall-Type-1`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2/Gable-Wall-Length-2`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2/Gable-Wall-Height-2`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2/Gable-Wall-Type-2`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2/Common-Wall-Length-1`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2/Common-Wall-Height-1`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2/Common-Wall-Length-2`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2/Common-Wall-Height-2`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2/Gable-Wall-Length-1:

Gable-Wall-Length-1
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2/Gable-Wall-Length-1`>/

- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2/Gable-Wall-Height-1:

Gable-Wall-Height-1
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2/Gable-Wall-Height-1`>/

- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2/Gable-Wall-Type-1:

Gable-Wall-Type-1
-----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2/Gable-Wall-Type-1`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2`>
- Has text value: *True*
- Codes:
    - **"0"** - *exposed*
    - **"1"** - *party*
    - **"2"** - *Sheltered*
    - **"3"** - *connected or adjacent to heated space*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2/Gable-Wall-Length-2:

Gable-Wall-Length-2
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2/Gable-Wall-Length-2`>/

- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2/Gable-Wall-Height-2:

Gable-Wall-Height-2
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2/Gable-Wall-Height-2`>/

- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2/Gable-Wall-Type-2:

Gable-Wall-Type-2
-----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2/Gable-Wall-Type-2`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2`>
- Has text value: *True*
- Codes:
    - **"0"** - *exposed*
    - **"1"** - *party*
    - **"2"** - *Sheltered*
    - **"3"** - *connected or adjacent to heated space*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2/Common-Wall-Length-1:

Common-Wall-Length-1
--------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2/Common-Wall-Length-1`>/

- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2/Common-Wall-Height-1:

Common-Wall-Height-1
--------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2/Common-Wall-Height-1`>/

- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2/Common-Wall-Length-2:

Common-Wall-Length-2
--------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2/Common-Wall-Length-2`>/

- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2/Common-Wall-Height-2:

Common-Wall-Height-2
--------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2/Common-Wall-Height-2`>/

- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Room-In-Roof/Room-In-Roof-Type-2`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1:

SAP-Alternative-Wall-1
----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1`>/

- Documentation: *Included only for building parts that have an alternative wall*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1/Wall-Construction`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1/Wall-Insulation-Type`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1/Wall-Area`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1/Wall-Thickness-Measured`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1/Wall-Thickness`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1/Wall-U-Value`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1/Wall-Insulation-Thickness`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1/Wall-Insulation-Thickness-Measured`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1/Wall-Insulation-Thermal-Conductivity`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1/Wall-Dry-Lined`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1/Sheltered-Wall`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1/Wall-Construction:

Wall-Construction
-----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1/Wall-Construction`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1`>
- Has text value: *True*
- Codes:
    - **"1"** - *stone (granite or whinstone)*
    - **"2"** - *stone (sandstone or limestone)*
    - **"3"** - *solid brick*
    - **"4"** - *cavity*
    - **"5"** - *timber frame*
    - **"6"** - *basement wall*
    - **"7"** - *curtain wall*
    - **"8"** - *system built*
    - **"9"** - *cob wall*
    - **"10"** - *park home wall*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1/Wall-Insulation-Type:

Wall-Insulation-Type
--------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1/Wall-Insulation-Type`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1`>
- Has text value: *True*
- Codes:
    - **"1"** - *external*
    - **"2"** - *filled cavity*
    - **"3"** - *internal*
    - **"4"** - *as built*
    - **"5"** - *unknown*
    - **"6"** - *filled cavity + external*
    - **"7"** - *filled cavity + internal*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1/Wall-Area:

Wall-Area
---------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1/Wall-Area`>/

- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1/Wall-Thickness-Measured:

Wall-Thickness-Measured
-----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1/Wall-Thickness-Measured`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1`>
- Has text value: *True*
- Codes:
    - **"Y"** - *Yes*
    - **"N"** - *No*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1/Wall-Thickness:

Wall-Thickness
--------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1/Wall-Thickness`>/

- Documentation: *Wall thickness in mm*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1/Wall-U-Value:

Wall-U-Value
------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1/Wall-U-Value`>/

- Documentation: *Only one of Wall-Insulation-Thickness and Wall-U-Value is included*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1/Wall-Insulation-Thickness:

Wall-Insulation-Thickness
-------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1/Wall-Insulation-Thickness`>/

- Documentation: *Only one of Wall-Insulation-Thickness and Wall-U-Value is included*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1`>
- Has text value: *True*
- Codes:
    - **"NI"** - *unknown*
    - **"10mm"** - *10 mm*
    - **"25mm"** - *25 mm*
    - **"50mm"** - *50 mm*
    - **"75mm"** - *75 mm*
    - **"100mm"** - *100 mm*
    - **"125mm"** - *125 mm*
    - **"150mm"** - *150 mm*
    - **"175mm"** - *175 mm*
    - **"200mm"** - *200mm*
    - **"measured"** - *if wall insulation thickness is provided with precise measurement*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1/Wall-Insulation-Thickness-Measured:

Wall-Insulation-Thickness-Measured
----------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1/Wall-Insulation-Thickness-Measured`>/

- Documentation: *Only one of Wall-Insulation-Thickness is measured and Wall-U-Value is included*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1/Wall-Insulation-Thermal-Conductivity:

Wall-Insulation-Thermal-Conductivity
------------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1/Wall-Insulation-Thermal-Conductivity`>/

- Documentation: *Only if documentary evidence is available*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1`>
- Has text value: *True*
- Codes:
    - **"1"** - *0.04*
    - **"2"** - *0.03*
    - **"3"** - *0.025*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1/Wall-Dry-Lined:

Wall-Dry-Lined
--------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1/Wall-Dry-Lined`>/

- Documentation: *Value to be "N" for wall types where dry-lining is not applicable.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1`>
- Has text value: *True*
- Codes:
    - **"Y"** - *Yes*
    - **"N"** - *No*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1/Sheltered-Wall:

Sheltered-Wall
--------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1/Sheltered-Wall`>/

- Documentation: *Wall between dwelling and unheated corridor or stairwell*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-1`>
- Has text value: *True*
- Codes:
    - **"Y"** - *Yes*
    - **"N"** - *No*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2:

SAP-Alternative-Wall-2
----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2`>/

- Documentation: *Included only for building parts that have an alternative wall*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2/Wall-Construction`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2/Wall-Insulation-Type`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2/Wall-Area`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2/Wall-Thickness-Measured`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2/Wall-Thickness`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2/Wall-U-Value`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2/Wall-Insulation-Thickness`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2/Wall-Insulation-Thickness-Measured`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2/Wall-Insulation-Thermal-Conductivity`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2/Wall-Dry-Lined`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2/Sheltered-Wall`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2/Wall-Construction:

Wall-Construction
-----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2/Wall-Construction`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2`>
- Has text value: *True*
- Codes:
    - **"1"** - *stone (granite or whinstone)*
    - **"2"** - *stone (sandstone or limestone)*
    - **"3"** - *solid brick*
    - **"4"** - *cavity*
    - **"5"** - *timber frame*
    - **"6"** - *basement wall*
    - **"7"** - *curtain wall*
    - **"8"** - *system built*
    - **"9"** - *cob wall*
    - **"10"** - *park home wall*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2/Wall-Insulation-Type:

Wall-Insulation-Type
--------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2/Wall-Insulation-Type`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2`>
- Has text value: *True*
- Codes:
    - **"1"** - *external*
    - **"2"** - *filled cavity*
    - **"3"** - *internal*
    - **"4"** - *as built*
    - **"5"** - *unknown*
    - **"6"** - *filled cavity + external*
    - **"7"** - *filled cavity + internal*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2/Wall-Area:

Wall-Area
---------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2/Wall-Area`>/

- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2/Wall-Thickness-Measured:

Wall-Thickness-Measured
-----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2/Wall-Thickness-Measured`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2`>
- Has text value: *True*
- Codes:
    - **"Y"** - *Yes*
    - **"N"** - *No*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2/Wall-Thickness:

Wall-Thickness
--------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2/Wall-Thickness`>/

- Documentation: *Wall thickness in mm*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2/Wall-U-Value:

Wall-U-Value
------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2/Wall-U-Value`>/

- Documentation: *Only one of Wall-Insulation-Thickness and Wall-U-Value is included*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2/Wall-Insulation-Thickness:

Wall-Insulation-Thickness
-------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2/Wall-Insulation-Thickness`>/

- Documentation: *Only one of Wall-Insulation-Thickness and Wall-U-Value is included*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2`>
- Has text value: *True*
- Codes:
    - **"NI"** - *unknown*
    - **"10mm"** - *10 mm*
    - **"25mm"** - *25 mm*
    - **"50mm"** - *50 mm*
    - **"75mm"** - *75 mm*
    - **"100mm"** - *100 mm*
    - **"125mm"** - *125 mm*
    - **"150mm"** - *150 mm*
    - **"175mm"** - *175 mm*
    - **"200mm"** - *200mm*
    - **"measured"** - *if wall insulation thickness is provided with precise measurement*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2/Wall-Insulation-Thickness-Measured:

Wall-Insulation-Thickness-Measured
----------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2/Wall-Insulation-Thickness-Measured`>/

- Documentation: *Only one of Wall-Insulation-Thickness is measured and Wall-U-Value is included*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2/Wall-Insulation-Thermal-Conductivity:

Wall-Insulation-Thermal-Conductivity
------------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2/Wall-Insulation-Thermal-Conductivity`>/

- Documentation: *Only if documentary evidence is available*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2`>
- Has text value: *True*
- Codes:
    - **"1"** - *0.04*
    - **"2"** - *0.03*
    - **"3"** - *0.025*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2/Wall-Dry-Lined:

Wall-Dry-Lined
--------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2/Wall-Dry-Lined`>/

- Documentation: *Value to be "N" for wall types where dry-lining is not applicable.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2`>
- Has text value: *True*
- Codes:
    - **"Y"** - *Yes*
    - **"N"** - *No*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2/Sheltered-Wall:

Sheltered-Wall
--------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2/Sheltered-Wall`>/

- Documentation: *Wall between dwelling and unheated corridor or stairwell*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/SAP-Alternative-Wall-2`>
- Has text value: *True*
- Codes:
    - **"Y"** - *Yes*
    - **"N"** - *No*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Party-Wall-Construction:

Party-Wall-Construction
-----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part/Party-Wall-Construction`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Building-Parts/SAP-Building-Part`>
- Has text value: *True*
- Codes:
    - **"0"** - *unable to determine*
    - **"1"** - *solid masonry, timber frame or system built*
    - **"2"** - *cavity masonry, unfilled*
    - **"3"** - *cavity masonry, filled*
    - **"4"** - *cavity masonry, filled and sealed*
    - **"NA"** - *not applicable (detached property or no party wall in this building part)*
    - **"NI"** - *no information - pre-9.92 survey*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Flat-Details:

SAP-Flat-Details
----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Flat-Details`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Flat-Details/Flat-Location`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Flat-Details/Storey-Count`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Flat-Details/Level`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Flat-Details/Top-Storey`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Flat-Details/Heat-Loss-Corridor`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Flat-Details/Unheated-Corridor-Length`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Flat-Details/Flat-Location:

Flat-Location
-------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Flat-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Flat-Details/Flat-Location`>/

- Documentation: *Identifies the storey within the block that the entrance to the flat is located on*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Flat-Details`>
- Has text value: *True*
- Codes:
    - **"-1"** - *Basement*
    - **"00"** - *Ground*
    - **"01"** - *1st*
    - **"02"** - *2nd*
    - **"03"** - *3rd*
    - **"04"** - *4th*
    - **"05"** - *5th*
    - **"06"** - *6th*
    - **"07"** - *7th*
    - **"08"** - *8th*
    - **"09"** - *9th*
    - **"10"** - *10th*
    - **"11"** - *11th*
    - **"12"** - *12th*
    - **"13"** - *13th*
    - **"14"** - *14th*
    - **"15"** - *15th*
    - **"16"** - *16th*
    - **"17"** - *17th*
    - **"18"** - *18th*
    - **"19"** - *19th*
    - **"20"** - *20th*
    - **"20+"** - *21st or above*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Flat-Details/Storey-Count:

Storey-Count
------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Flat-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Flat-Details/Storey-Count`>/

- Documentation: *The number of Storeys in the Apartment Block.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Flat-Details`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Flat-Details/Level:

Level
-----

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Flat-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Flat-Details/Level`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Flat-Details`>
- Has text value: *True*
- Codes:
    - **"0"** - *basement*
    - **"1"** - *ground floor*
    - **"2"** - *mid floor*
    - **"3"** - *top floor*
    - **"99"** - *for backward compatibility only, do not use.*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Flat-Details/Top-Storey:

Top-Storey
----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Flat-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Flat-Details/Top-Storey`>/

- Documentation: *Indicates that the Apartment is located on the Top Storey of the Apartment Block.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Flat-Details`>
- Has text value: *True*
- Codes:
    - **"Y"** - *Yes*
    - **"N"** - *No*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Flat-Details/Heat-Loss-Corridor:

Heat-Loss-Corridor
------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Flat-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Flat-Details/Heat-Loss-Corridor`>/

- Documentation: *Indiocates that the flat contained a cossidor through which heat is lost.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Flat-Details`>
- Has text value: *True*
- Codes:
    - **"0"** - *no corridor*
    - **"1"** - *heated corridor*
    - **"2"** - *unheated corridor*
    - **"3"** - *stairwell*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Flat-Details/Unheated-Corridor-Length:

Unheated-Corridor-Length
------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Flat-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Flat-Details/Unheated-Corridor-Length`>/

- Documentation: *The tortal length of unheated corridor in the flat. Only popualted if Heat-Loss-Corridor = {Unheated Corridor}*
- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Flat-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows:

SAP-Windows
-----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows`>/

- Documentation: *To be used when all windows are measured.*
- Documentation2: *Details of the windows in the building*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window:

SAP-Window
----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Window-Location`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Window-Height`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Window-Width`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Draught-Proofed`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Glazing-Type`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Window-Type`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Orientation`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Window-Transmission-Details`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/PVC-Frame`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Glazing-Gap`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Frame-Factor`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Window-Wall-Type`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Permanent-Shutters-Present`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Permanent-Shutters-Insulated`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *unbounded*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Window-Location:

Window-Location
---------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Window-Location`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window`>
- Has text value: *True*
- Codes:
    - **"0"** - *Main Property*
    - **"1"** - *1st Extension*
    - **"2"** - *2nd Extension*
    - **"3"** - *3rd Extension*
    - **"4"** - *4th Extension*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Window-Height:

Window-Height
-------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Window-Height`>/

- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Window-Width:

Window-Width
------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Window-Width`>/

- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Draught-Proofed:

Draught-Proofed
---------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Draught-Proofed`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Glazing-Type:

Glazing-Type
------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Glazing-Type`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window`>
- Has text value: *True*
- Codes:
    - **"1"** - *double glazing installed before 2002 in EAW, 2003 in SCT, 2006 NI*
    - **"2"** - *double glazing installed between 2002-2022 in EAW, 2003-2023 in SCT, 2006-2022 NI*
    - **"3"** - *double glazing, unknown install date*
    - **"4"** - *secondary glazing, unknown data*
    - **"5"** - *single glazing*
    - **"6"** - *triple glazing, unknown install date*
    - **"7"** - *double, known data*
    - **"8"** - *triple, known data*
    - **"ND"** - *not defined*
    - **"9"** - *triple glazing, installed between 2002-2022 in EAW, 2003-2023 in SCT, 2006-2022 NI*
    - **"10"** - *triple glazing, installed before 2002 in EAW, 2003 in SCT, 2006 NI*
    - **"11"** - *secondary glazing, normal emissivity*
    - **"12"** - *secondary glazing, low emissivity*
    - **"13"** - *double glazing, installed during or after 2022 in EAW, 2023 in SCT, 2022 NI*
    - **"14"** - *triple glazing, installed during or after 2022 in EAW, 2023 in SCT, 2022 NI*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Window-Type:

Window-Type
-----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Window-Type`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window`>
- Has text value: *True*
- Codes:
    - **"1"** - *window*
    - **"2"** - *roof-window*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Orientation:

Orientation
-----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Orientation`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window`>
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

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Window-Transmission-Details:

Window-Transmission-Details
---------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Window-Transmission-Details`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Window-Transmission-Details/Data-Source`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Window-Transmission-Details/U-Value`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Window-Transmission-Details/Solar-Transmittance`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Window-Transmission-Details/Data-Source:

Data-Source
-----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Window-Transmission-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Window-Transmission-Details/Data-Source`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Window-Transmission-Details`>
- Has text value: *True*
- Codes:
    - **"2"** - *manufacturer data*
    - **"4"** - *BFRC data*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Window-Transmission-Details/U-Value:

U-Value
-------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Window-Transmission-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Window-Transmission-Details/U-Value`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Window-Transmission-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Window-Transmission-Details/Solar-Transmittance:

Solar-Transmittance
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Window-Transmission-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Window-Transmission-Details/Solar-Transmittance`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Window-Transmission-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/PVC-Frame:

PVC-Frame
---------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/PVC-Frame`>/

- Documentation: *include when Glazing-Type is 1 or 3. If true: wood or PVC, if false: metal.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window`>
- Has text value: *True*
- Codes:
    - **"true"** - *True*
    - **"1"** - *True*
    - **"false"** - *False*
    - **"0"** - *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Glazing-Gap:

Glazing-Gap
-----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Glazing-Gap`>/

- Documentation: *include when Glazing-Type is 1 or 3 and PVC-Frame is true.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window`>
- Has text value: *True*
- Codes:
    - **"6"** - *6mm*
    - **"12"** - *12mm*
    - **"16+"** - *16mm or more*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Frame-Factor:

Frame-Factor
------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Frame-Factor`>/

- Documentation: *include when frame factor is known.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Window-Wall-Type:

Window-Wall-Type
----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Window-Wall-Type`>/

- Documentation: *Identifies the type of wall the window is located*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window`>
- Has text value: *True*
- Codes:
    - **"1"** - *External wall type 1*
    - **"2"** - *Alternative wall 1*
    - **"3"** - *Alternative wall 2*
    - **"4"** - *Roof of Room in Roof*
    - **"5"** - *gable wall 1.*
    - **"6"** - *gable wall 2.*
    - **"7"** - *common wall 1 Only include for RR Type 2.*
    - **"8"** - *common wall 2 Only include for RR Type 2.*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Permanent-Shutters-Present:

Permanent-Shutters-Present
--------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Permanent-Shutters-Present`>/

- Documentation: *Identifies if permanent shutters are present*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window`>
- Has text value: *True*
- Codes:
    - **"Y"** - *Yes*
    - **"N"** - *No*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Permanent-Shutters-Insulated:

Permanent-Shutters-Insulated
----------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window/Permanent-Shutters-Insulated`>/

- Documentation: *Identifies if permanent shutters are insulated. Include when permanent shutters are present*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Windows/SAP-Window`>
- Has text value: *True*
- Codes:
    - **"Y"** - *Yes*
    - **"N"** - *No*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Windows-Transmission-Details:

Windows-Transmission-Details
----------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Windows-Transmission-Details`>/

- Documentation: *To be used when windows are not measured.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Windows-Transmission-Details/Data-Source`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Windows-Transmission-Details/U-Value`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Windows-Transmission-Details/Solar-Transmittance`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Windows-Transmission-Details/Data-Source:

Data-Source
-----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Windows-Transmission-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Windows-Transmission-Details/Data-Source`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Windows-Transmission-Details`>
- Has text value: *True*
- Codes:
    - **"2"** - *manufacturer data*
    - **"4"** - *BFRC data*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Windows-Transmission-Details/U-Value:

U-Value
-------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Windows-Transmission-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Windows-Transmission-Details/U-Value`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Windows-Transmission-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Windows-Transmission-Details/Solar-Transmittance:

Solar-Transmittance
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Windows-Transmission-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Windows-Transmission-Details/Solar-Transmittance`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Windows-Transmission-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Deselected-Improvements:

SAP-Deselected-Improvements
---------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Deselected-Improvements`>/

- Documentation: *This must record any measures deselected by the DEA*
- Documentation2: *There are 22 possible improvement measures, designated from A to V. This must record measures deselected by DEA (A to V is the full set, only E, N, U and V are considered at the moment for new build).*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Deselected-Improvements/Deselected-Improvement-Measure`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Deselected-Improvements/Deselected-Improvement-Measure:

Deselected-Improvement-Measure
------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Deselected-Improvements`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Deselected-Improvements/Deselected-Improvement-Measure`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Deselected-Improvements`>
- Has text value: *True*
- Codes:
    - **"A"** - *Loft Insulation*
    - **"A2"** - *Flat roof insulation*
    - **"A3"** - *Room-in-roof insulation*
    - **"B"** - *Cavity wall insulation*
    - **"B4"** - *Party wall insulation*
    - **"C"** - *Hot water cylinder insulation*
    - **"D"** - *Draughtproofing*
    - **"E"** - *Low energy lights*
    - **"F"** - *Cylinder thermostat*
    - **"G"** - *Heating controls for wet central heating system*
    - **"G2"** - *Water heating controls*
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
    - **"U1"** - *PV Battery*
    - **"U2"** - *PV Diverter*
    - **"V"** - *Wind turbine (roof mounted)*
    - **"V2"** - *Wind turbine (on mast)*
    - **"W"** - *Floor insulation; for backwards compatibility only, do not use*
    - **"W1"** - *Insulation of suspended floor*
    - **"W2"** - *Insulation of solid ground floor*
    - **"X"** - *Insulated doors*
    - **"Y"** - *Instantaneous waste water heat recovery*
    - **"Y2"** - *Storage waste water heat recovery*
    - **"Z1"** - *Air or ground source heat pump*
    - **"Z2"** - *Air or ground source heat pump with underfloor heating*
    - **"Z3"** - *Micro-CHP*
    - **"NR"** - *Not recorded*
- Minimum occurrence: *1*
- Maximum occurrence: *unbounded*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Door-Count:

Door-Count
----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Door-Count`>/

- Documentation: *Number of external doors*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Insulated-Door-Count:

Insulated-Door-Count
--------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Insulated-Door-Count`>/

- Documentation: *Number of insulated external doors*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Draughtproofed-Door-Count:

Draughtproofed-Door-Count
-------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Draughtproofed-Door-Count`>/

- Documentation: *Number of draught proofed external doors*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Insulated-Door-U-Value:

Insulated-Door-U-Value
----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Insulated-Door-U-Value`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/Percent-Draughtproofed:

Percent-Draughtproofed
----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/Percent-Draughtproofed`>/

- Documentation: *Percentage of windows and doors with adequate draught proofing*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Has text value: *True*
- Data type: *<class 'int'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features:

SAP-Special-Features
--------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature:

SAP-Special-Feature
-------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Description`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *unbounded*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Description:

Description
-----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Description`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature:

Energy-Feature
--------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Energy-Saved-Or-Generated`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Saved-Or-Generated-Fuel`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Energy-Used`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Energy-Used-Fuel`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Energy-Saved-Or-Generated:

Energy-Saved-Or-Generated
-------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Energy-Saved-Or-Generated`>/

- Documentation: *Energy saved or generated in kWh/year.*
- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Saved-Or-Generated-Fuel:

Saved-Or-Generated-Fuel
-----------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Saved-Or-Generated-Fuel`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature`>
- Has text value: *True*
- Codes:
    - **"0"** - *To be used only when there is no heating/hot-water system or data is from a community network*
    - **"1"** - *mains gas - this is for backwards compatibility only and should not be used*
    - **"2"** - *LPG - this is for backwards compatibility only and should not be used*
    - **"3"** - *bottled LPG*
    - **"4"** - *oil - this is for backwards compatibility only and should not be used*
    - **"5"** - *anthracite*
    - **"6"** - *wood logs*
    - **"7"** - *bulk wood pellets*
    - **"8"** - *wood chips*
    - **"9"** - *dual fuel - mineral + wood*
    - **"10"** - *electricity - this is for backwards compatibility only and should not be used*
    - **"11"** - *waste combustion - this is for backwards compatibility only and should not be used*
    - **"12"** - *biomass - this is for backwards compatibility only and should not be used*
    - **"13"** - *biogas - landfill - this is for backwards compatibility only and should not be used*
    - **"14"** - *house coal - this is for backwards compatibility only and should not be used*
    - **"15"** - *smokeless coal*
    - **"16"** - *wood pellets in bags for secondary heating*
    - **"17"** - *LPG special condition*
    - **"18"** - *B30K (not community)*
    - **"19"** - *bioethanol*
    - **"20"** - *mains gas (community)*
    - **"21"** - *LPG (community)*
    - **"22"** - *oil (community)*
    - **"23"** - *B30D (community)*
    - **"24"** - *coal (community)*
    - **"25"** - *electricity (community)*
    - **"26"** - *mains gas (not community)*
    - **"27"** - *LPG (not community)*
    - **"28"** - *oil (not community)*
    - **"29"** - *electricity (not community)*
    - **"30"** - *waste combustion (community)*
    - **"31"** - *biomass (community)*
    - **"32"** - *biogas (community)*
    - **"33"** - *house coal (not community)*
    - **"34"** - *biodiesel from any biomass source*
    - **"35"** - *biodiesel from used cooking oil only*
    - **"36"** - *biodiesel from vegetable oil only (not community)*
    - **"37"** - *appliances able to use mineral oil or liquid biofuel*
    - **"51"** - *biogas (not community)*
    - **"56"** - *heat from boilers that can use mineral oil or biodiesel (community)*
    - **"57"** - *heat from boilers using biodiesel from any biomass source (community)*
    - **"58"** - *biodiesel from vegetable oil only (community)*
    - **"99"** - *from heat network data (community)*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Energy-Used:

Energy-Used
-----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Energy-Used`>/

- Documentation: *Energy used in kWh/year.*
- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Energy-Used-Fuel:

Energy-Used-Fuel
----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Energy-Used-Fuel`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature`>
- Has text value: *True*
- Codes:
    - **"0"** - *To be used only when there is no heating/hot-water system or data is from a community network*
    - **"1"** - *mains gas - this is for backwards compatibility only and should not be used*
    - **"2"** - *LPG - this is for backwards compatibility only and should not be used*
    - **"3"** - *bottled LPG*
    - **"4"** - *oil - this is for backwards compatibility only and should not be used*
    - **"5"** - *anthracite*
    - **"6"** - *wood logs*
    - **"7"** - *bulk wood pellets*
    - **"8"** - *wood chips*
    - **"9"** - *dual fuel - mineral + wood*
    - **"10"** - *electricity - this is for backwards compatibility only and should not be used*
    - **"11"** - *waste combustion - this is for backwards compatibility only and should not be used*
    - **"12"** - *biomass - this is for backwards compatibility only and should not be used*
    - **"13"** - *biogas - landfill - this is for backwards compatibility only and should not be used*
    - **"14"** - *house coal - this is for backwards compatibility only and should not be used*
    - **"15"** - *smokeless coal*
    - **"16"** - *wood pellets in bags for secondary heating*
    - **"17"** - *LPG special condition*
    - **"18"** - *B30K (not community)*
    - **"19"** - *bioethanol*
    - **"20"** - *mains gas (community)*
    - **"21"** - *LPG (community)*
    - **"22"** - *oil (community)*
    - **"23"** - *B30D (community)*
    - **"24"** - *coal (community)*
    - **"25"** - *electricity (community)*
    - **"26"** - *mains gas (not community)*
    - **"27"** - *LPG (not community)*
    - **"28"** - *oil (not community)*
    - **"29"** - *electricity (not community)*
    - **"30"** - *waste combustion (community)*
    - **"31"** - *biomass (community)*
    - **"32"** - *biogas (community)*
    - **"33"** - *house coal (not community)*
    - **"34"** - *biodiesel from any biomass source*
    - **"35"** - *biodiesel from used cooking oil only*
    - **"36"** - *biodiesel from vegetable oil only (not community)*
    - **"37"** - *appliances able to use mineral oil or liquid biofuel*
    - **"51"** - *biogas (not community)*
    - **"56"** - *heat from boilers that can use mineral oil or biodiesel (community)*
    - **"57"** - *heat from boilers using biodiesel from any biomass source (community)*
    - **"58"** - *biodiesel from vegetable oil only (community)*
    - **"99"** - *from heat network data (community)*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates:

Air-Change-Rates
----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates`>/

- Documentation: *For Appendix Q procedure that provides air change rates. Only one Special Feature can have data on air change rates.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate`>
- Has text value: *False*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate:

Air-Change-Rate
---------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate/Air-Change-Rate-Month`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate/Air-Change-Rate-Value`>
- Has text value: *False*
- Minimum occurrence: *12*
- Maximum occurrence: *12*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate/Air-Change-Rate-Month:

Air-Change-Rate-Month
---------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate/Air-Change-Rate-Month`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate`>
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

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate/Air-Change-Rate-Value:

Air-Change-Rate-Value
---------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate/Air-Change-Rate-Value`>/

- Documentation: *Air change rate in month.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Energy-Feature/Air-Change-Rates/Air-Change-Rate`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature:

Emissions-Feature
-----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature`>/

- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`>
- Child elements: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature/Emissions-Saved`> <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature/Emissions-Created`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature/Emissions-Saved:

Emissions-Saved
---------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature/Emissions-Saved`>/

- Documentation: *Emissions saved in kg/year.*
- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature/Emissions-Created:

Emissions-Created
-----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/SAP-Data`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature`>/<:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature/Emissions-Created`>/

- Documentation: *Additional emissions in kg/year.*
- Documentation2: *A measurement of something such as a length or area. All measurements are to 2 decimal places and must be positive.*
- Parent element: <:ref:`RdSAP-Report/SAP-Data/SAP-Property-Details/SAP-Special-Features/SAP-Special-Feature/Emissions-Feature`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header:

Report-Header
-------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/

- Documentation2: *Report Header contains all the identification and searchable details for the Report.*
- Parent element: <:ref:`RdSAP-Report`>
- Child elements: <:ref:`RdSAP-Report/Report-Header/RRN`> <:ref:`RdSAP-Report/Report-Header/Inspection-Date`> <:ref:`RdSAP-Report/Report-Header/Report-Type`> <:ref:`RdSAP-Report/Report-Header/Completion-Date`> <:ref:`RdSAP-Report/Report-Header/Registration-Date`> <:ref:`RdSAP-Report/Report-Header/Status`> <:ref:`RdSAP-Report/Report-Header/Language-Code`> <:ref:`RdSAP-Report/Report-Header/Property-Type`> <:ref:`RdSAP-Report/Report-Header/Region-Code`> <:ref:`RdSAP-Report/Report-Header/Country-Code`> <:ref:`RdSAP-Report/Report-Header/Transaction-Type`> <:ref:`RdSAP-Report/Report-Header/Tenure`> <:ref:`RdSAP-Report/Report-Header/Energy-Assessor`> <:ref:`RdSAP-Report/Report-Header/Property`> <:ref:`RdSAP-Report/Report-Header/Related-Party-Disclosure`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/RRN:

RRN
---

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/RRN`>/

- Documentation: *Report Reference Number is the unique report Identifier shown on the EPC.*
- Parent element: <:ref:`RdSAP-Report/Report-Header`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Inspection-Date:

Inspection-Date
---------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Inspection-Date`>/

- Documentation: *Date of site visit.*
- Parent element: <:ref:`RdSAP-Report/Report-Header`>
- Has text value: *True*
- Data type: *Date string (ISO format)*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Report-Type:

Report-Type
-----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Report-Type`>/

- Documentation: *The type of assessment that was carried out.*
- Parent element: <:ref:`RdSAP-Report/Report-Header`>
- Has text value: *True*
- Codes:
    - **"2"** - *RdSAP Energy Performance Certificate*
    - **"3"** - *Full SAP Energy Performance Certificate*
    - **"4"** - *Interim RdSAP Energy Performance Certificate (to be superseded by SAP EPC)*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Completion-Date:

Completion-Date
---------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Completion-Date`>/

- Documentation: *Date of completion of report. Equal to or later than Inspection-Date and before or equal to Registration-Date.*
- Parent element: <:ref:`RdSAP-Report/Report-Header`>
- Has text value: *True*
- Data type: *Date string (ISO format)*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Registration-Date:

Registration-Date
-----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Registration-Date`>/

- Documentation: *Date when report submitted to register.*
- Parent element: <:ref:`RdSAP-Report/Report-Header`>
- Has text value: *True*
- Data type: *Date string (ISO format)*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Status:

Status
------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Status`>/

- Parent element: <:ref:`RdSAP-Report/Report-Header`>
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

.. _RdSAP-Report/Report-Header/Language-Code:

Language-Code
-------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Language-Code`>/

- Documentation: *The language that the report is written in.*
- Parent element: <:ref:`RdSAP-Report/Report-Header`>
- Has text value: *True*
- Codes:
    - **"1"** - *English*
    - **"2"** - *Welsh*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Property-Type:

Property-Type
-------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Property-Type`>/

- Documentation: *The type of property that is being assessed. This should be the same as the Property-Type recorded in the Property-Details section.*
- Parent element: <:ref:`RdSAP-Report/Report-Header`>
- Has text value: *True*
- Codes:
    - **"0"** - *House*
    - **"1"** - *Bungalow*
    - **"2"** - *Flat*
    - **"3"** - *Maisonette*
    - **"4"** - *Park home*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Region-Code:

Region-Code
-----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Region-Code`>/

- Documentation: *Region within the UK.*
- Parent element: <:ref:`RdSAP-Report/Report-Header`>
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
    - **"NR"** - *for backwards compatibility only - do not use*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Country-Code:

Country-Code
------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Country-Code`>/

- Documentation: *Country within the UK.*
- Parent element: <:ref:`RdSAP-Report/Report-Header`>
- Has text value: *True*
- Codes:
    - **"ENG"** - *England*
    - **"WLS"** - *Wales*
    - **"SCT"** - *Scotland*
    - **"NIR"** - *Northern Ireland*
    - **"IOM"** - *Isle of Man*
    - **"NR"** - *for backwards compatibility only - do not use*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Transaction-Type:

Transaction-Type
----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Transaction-Type`>/

- Parent element: <:ref:`RdSAP-Report/Report-Header`>
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
    - **"9"** - *assessment for green deal - this is for backwards compatibility only and should not be used*
    - **"10"** - *following green deal - this is for backwards compatibility only and should not be used*
    - **"11"** - *FiT application - this is for backwards compatibility only and should not be used*
    - **"12"** - *RHI application - this is for backwards compatibility only and should not be used*
    - **"13"** - *ECO assessment - this is for backwards compatibility only and should not be used*
    - **"14"** - *Stock condition survey*
    - **"15"** - *Grant scheme (ECO, RHI, etc.)*
    - **"16"** - *Non-grant scheme (e.g. MEES)*
    - **"17"** - *re-mortgaging*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Tenure:

Tenure
------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Tenure`>/

- Parent element: <:ref:`RdSAP-Report/Report-Header`>
- Has text value: *True*
- Codes:
    - **"1"** - *owner-occupied*
    - **"2"** - *rented (social)*
    - **"3"** - *rented (private)*
    - **"ND"** - *unknown*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Energy-Assessor:

Energy-Assessor
---------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor`>/

- Documentation2: *An Energy Assessor is certified by a Certification Scheme as being qualified to carry out a SAP assessment and/or an RdSAP assessment.*
- Parent element: <:ref:`RdSAP-Report/Report-Header`>
- Child elements: <:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Name`> <:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Notify-Lodgement`> <:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Contact-Address`> <:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Web-Site`> <:ref:`RdSAP-Report/Report-Header/Energy-Assessor/E-Mail`> <:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Fax`> <:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Telephone`> <:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Company-Name`> <:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Scheme-Name`> <:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Scheme-Web-Site`> <:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Identification-Number`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Energy-Assessor/Name:

Name
----

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Name`>/

- Documentation: *The name by which the Home Inspector is registered. This is a structured name containing prefix, first name + surname.*
- Parent element: <:ref:`RdSAP-Report/Report-Header/Energy-Assessor`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Energy-Assessor/Notify-Lodgement:

Notify-Lodgement
----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Notify-Lodgement`>/

- Documentation: *Indicates whether the assessor wants to be notified that a the report has been lodged in the register*
- Parent element: <:ref:`RdSAP-Report/Report-Header/Energy-Assessor`>
- Has text value: *True*
- Codes:
    - **"Y"** - *Yes*
    - **"N"** - *No*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Energy-Assessor/Contact-Address:

Contact-Address
---------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Contact-Address`>/

- Documentation: *The address that any written correspondence can be sent to. This is not the same as the Registered Address because it may, of course, be a Post Office Box.*
- Documentation2: *An address is composed of a number of structured elements such as Postcode, Post-Town, Street etc.*
- Parent element: <:ref:`RdSAP-Report/Report-Header/Energy-Assessor`>
- Child elements: <:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Contact-Address/Address-Line-1`> <:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Contact-Address/Address-Line-2`> <:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Contact-Address/Address-Line-3`> <:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Contact-Address/Post-Town`> <:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Contact-Address/Postcode`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Energy-Assessor/Contact-Address/Address-Line-1:

Address-Line-1
--------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Contact-Address`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Contact-Address/Address-Line-1`>/

- Parent element: <:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Contact-Address`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Energy-Assessor/Contact-Address/Address-Line-2:

Address-Line-2
--------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Contact-Address`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Contact-Address/Address-Line-2`>/

- Documentation: *The District part of the Address. A District is an optional sub-part of the Post Town e.g. "Kings Heath" in "Birmingham" or "Ellington" in London.*
- Parent element: <:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Contact-Address`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Energy-Assessor/Contact-Address/Address-Line-3:

Address-Line-3
--------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Contact-Address`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Contact-Address/Address-Line-3`>/

- Parent element: <:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Contact-Address`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Energy-Assessor/Contact-Address/Post-Town:

Post-Town
---------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Contact-Address`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Contact-Address/Post-Town`>/

- Parent element: <:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Contact-Address`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Energy-Assessor/Contact-Address/Postcode:

Postcode
--------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Contact-Address`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Contact-Address/Postcode`>/

- Documentation: *The Postcode for the Address*
- Parent element: <:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Contact-Address`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Energy-Assessor/Web-Site:

Web-Site
--------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Web-Site`>/

- Parent element: <:ref:`RdSAP-Report/Report-Header/Energy-Assessor`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Energy-Assessor/E-Mail:

E-Mail
------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor/E-Mail`>/

- Documentation: *the E-Mail address that the Authorised User can be contacted at.*
- Parent element: <:ref:`RdSAP-Report/Report-Header/Energy-Assessor`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Energy-Assessor/Fax:

Fax
---

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Fax`>/

- Parent element: <:ref:`RdSAP-Report/Report-Header/Energy-Assessor`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Energy-Assessor/Telephone:

Telephone
---------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Telephone`>/

- Parent element: <:ref:`RdSAP-Report/Report-Header/Energy-Assessor`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Energy-Assessor/Company-Name:

Company-Name
------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Company-Name`>/

- Documentation: *The Name of the Company that the assessor is employed by.*
- Parent element: <:ref:`RdSAP-Report/Report-Header/Energy-Assessor`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Energy-Assessor/Scheme-Name:

Scheme-Name
-----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Scheme-Name`>/

- Parent element: <:ref:`RdSAP-Report/Report-Header/Energy-Assessor`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Energy-Assessor/Scheme-Web-Site:

Scheme-Web-Site
---------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Scheme-Web-Site`>/

- Parent element: <:ref:`RdSAP-Report/Report-Header/Energy-Assessor`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Energy-Assessor/Identification-Number:

Identification-Number
---------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Identification-Number`>/

- Parent element: <:ref:`RdSAP-Report/Report-Header/Energy-Assessor`>
- Child elements: <:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Identification-Number/Certificate-Number`> <:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Identification-Number/Membership-Number`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Energy-Assessor/Identification-Number/Certificate-Number:

Certificate-Number
------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Identification-Number`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Identification-Number/Certificate-Number`>/

- Documentation: *The unique identifier assigned to the assessor by the scheme by which they can be identified throughout their membership of the scheme.*
- Parent element: <:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Identification-Number`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Energy-Assessor/Identification-Number/Membership-Number:

Membership-Number
-----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Identification-Number`>/<:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Identification-Number/Membership-Number`>/

- Documentation: *For Scottish DEAs only*
- Parent element: <:ref:`RdSAP-Report/Report-Header/Energy-Assessor/Identification-Number`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Property:

Property
--------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Property`>/

- Documentation2: *A discrete identifiable possession, such as a piece of real-estate, to which its owner has legal title. For the Home Information Pack legislation the types of property are restricted to residential properties. It should be observed that "a property is a property is a property" and all real-estate properties, whether residential or commercial or whether being sold for the first or the nth time will have a very similar conceptual structure and similar rules and constraints. As such the broad description of a Property can be regarded as a framework, containing a set of extension points, that can be expanded as necessary to cover additional detail.*
- Parent element: <:ref:`RdSAP-Report/Report-Header`>
- Child elements: <:ref:`RdSAP-Report/Report-Header/Property/Address`> <:ref:`RdSAP-Report/Report-Header/Property/UPRN`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Property/Address:

Address
-------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Property`>/<:ref:`RdSAP-Report/Report-Header/Property/Address`>/

- Documentation2: *An address is composed of a number of structured elements such as Postcode, Post-Town, Street etc.*
- Parent element: <:ref:`RdSAP-Report/Report-Header/Property`>
- Child elements: <:ref:`RdSAP-Report/Report-Header/Property/Address/Address-Line-1`> <:ref:`RdSAP-Report/Report-Header/Property/Address/Address-Line-2`> <:ref:`RdSAP-Report/Report-Header/Property/Address/Address-Line-3`> <:ref:`RdSAP-Report/Report-Header/Property/Address/Post-Town`> <:ref:`RdSAP-Report/Report-Header/Property/Address/Postcode`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Property/Address/Address-Line-1:

Address-Line-1
--------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Property`>/<:ref:`RdSAP-Report/Report-Header/Property/Address`>/<:ref:`RdSAP-Report/Report-Header/Property/Address/Address-Line-1`>/

- Parent element: <:ref:`RdSAP-Report/Report-Header/Property/Address`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Property/Address/Address-Line-2:

Address-Line-2
--------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Property`>/<:ref:`RdSAP-Report/Report-Header/Property/Address`>/<:ref:`RdSAP-Report/Report-Header/Property/Address/Address-Line-2`>/

- Documentation: *The District part of the Address. A District is an optional sub-part of the Post Town e.g. "Kings Heath" in "Birmingham" or "Ellington" in London.*
- Parent element: <:ref:`RdSAP-Report/Report-Header/Property/Address`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Property/Address/Address-Line-3:

Address-Line-3
--------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Property`>/<:ref:`RdSAP-Report/Report-Header/Property/Address`>/<:ref:`RdSAP-Report/Report-Header/Property/Address/Address-Line-3`>/

- Parent element: <:ref:`RdSAP-Report/Report-Header/Property/Address`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Property/Address/Post-Town:

Post-Town
---------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Property`>/<:ref:`RdSAP-Report/Report-Header/Property/Address`>/<:ref:`RdSAP-Report/Report-Header/Property/Address/Post-Town`>/

- Parent element: <:ref:`RdSAP-Report/Report-Header/Property/Address`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Property/Address/Postcode:

Postcode
--------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Property`>/<:ref:`RdSAP-Report/Report-Header/Property/Address`>/<:ref:`RdSAP-Report/Report-Header/Property/Address/Postcode`>/

- Documentation: *The Postcode for the Address*
- Parent element: <:ref:`RdSAP-Report/Report-Header/Property/Address`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Property/UPRN:

UPRN
----

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Property`>/<:ref:`RdSAP-Report/Report-Header/Property/UPRN`>/

- Documentation: *Unique Property Reference Number*
- Parent element: <:ref:`RdSAP-Report/Report-Header/Property`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *0*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Related-Party-Disclosure:

Related-Party-Disclosure
------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Related-Party-Disclosure`>/

- Parent element: <:ref:`RdSAP-Report/Report-Header`>
- Child elements: <:ref:`RdSAP-Report/Report-Header/Related-Party-Disclosure/Related-Party-Disclosure-Number`> <:ref:`RdSAP-Report/Report-Header/Related-Party-Disclosure/Related-Party-Disclosure-Text`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Report-Header/Related-Party-Disclosure/Related-Party-Disclosure-Number:

Related-Party-Disclosure-Number
-------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Related-Party-Disclosure`>/<:ref:`RdSAP-Report/Report-Header/Related-Party-Disclosure/Related-Party-Disclosure-Number`>/

- Documentation: *Code indicating any potential conflicts of interest or commercial relationships with other parties.*
- Parent element: <:ref:`RdSAP-Report/Report-Header/Related-Party-Disclosure`>
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

.. _RdSAP-Report/Report-Header/Related-Party-Disclosure/Related-Party-Disclosure-Text:

Related-Party-Disclosure-Text
-----------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Report-Header`>/<:ref:`RdSAP-Report/Report-Header/Related-Party-Disclosure`>/<:ref:`RdSAP-Report/Report-Header/Related-Party-Disclosure/Related-Party-Disclosure-Text`>/

- Documentation: *For backward compatibility only*
- Parent element: <:ref:`RdSAP-Report/Report-Header/Related-Party-Disclosure`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Insurance-Details:

Insurance-Details
-----------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Insurance-Details`>/

- Documentation2: *Details of the Professional Indemnity Insurance policy used to provide cover against a compensation claim against any particular Home Condition Report. A particular Home Condition Report may be covered by an Professional Indemnity Insurance policy in one of three different ways: * The Home Inspector has personal Professional Indemnity Insurance and the Home Condition Report is covered by this. * The Home Condition Report is covered by an umbrella Professional Indemnity Insurance policy held by the Home Condition Report Supplier that assigned the inspection to the Home Inspector. * An individual insurance policy is taken out to cover the individual report such as the case where the property is unusual and falls outside the Home Inspectors normal Professional Indemnity Insurance policy. A Home Inspector may use any or all of these methods to providing Professional Indemnity Insurance for a Report on a case-by-case basis.*
- Parent element: <:ref:`RdSAP-Report`>
- Child elements: <:ref:`RdSAP-Report/Insurance-Details/Insurer`> <:ref:`RdSAP-Report/Insurance-Details/Policy-No`> <:ref:`RdSAP-Report/Insurance-Details/Effective-Date`> <:ref:`RdSAP-Report/Insurance-Details/Expiry-Date`> <:ref:`RdSAP-Report/Insurance-Details/PI-Limit`>
- Has text value: *False*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Insurance-Details/Insurer:

Insurer
-------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Insurance-Details`>/<:ref:`RdSAP-Report/Insurance-Details/Insurer`>/

- Documentation: *The name of the insurance company that underwrites / issued the insurance policy*
- Parent element: <:ref:`RdSAP-Report/Insurance-Details`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Insurance-Details/Policy-No:

Policy-No
---------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Insurance-Details`>/<:ref:`RdSAP-Report/Insurance-Details/Policy-No`>/

- Documentation: *The policy number of the insurance policy*
- Parent element: <:ref:`RdSAP-Report/Insurance-Details`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Insurance-Details/Effective-Date:

Effective-Date
--------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Insurance-Details`>/<:ref:`RdSAP-Report/Insurance-Details/Effective-Date`>/

- Documentation: *The date that the insurance policy becomes effective (commences cover)*
- Parent element: <:ref:`RdSAP-Report/Insurance-Details`>
- Has text value: *True*
- Data type: *Date string (ISO format)*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Insurance-Details/Expiry-Date:

Expiry-Date
-----------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Insurance-Details`>/<:ref:`RdSAP-Report/Insurance-Details/Expiry-Date`>/

- Documentation: *The date that the insurance policy is supposed to expire.*
- Parent element: <:ref:`RdSAP-Report/Insurance-Details`>
- Has text value: *True*
- Data type: *Date string (ISO format)*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/Insurance-Details/PI-Limit:

PI-Limit
--------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/Insurance-Details`>/<:ref:`RdSAP-Report/Insurance-Details/PI-Limit`>/

- Documentation: *The upper limit of the Professional Indemnity cover provided by the insurance policy.*
- Documentation2: *Extension of a Decimal value for use with monetary values where a currency code needs to be specified. The currency code is actually metadata about the value so, in line with good XML practice, the Currency Code is declared as an XML-Attribute of the Money datatype rather than as a separate XML-Element. The currency attribute should then include a list of valid currencies codes that are supported.*
- Parent element: <:ref:`RdSAP-Report/Insurance-Details`>
- Has text value: *True*
- Data type: *<class 'float'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

.. _RdSAP-Report/ExternalDefinitions-Revision-Number:

ExternalDefinitions-Revision-Number
-----------------------------------

<:ref:`RdSAP-Report`>/<:ref:`RdSAP-Report/ExternalDefinitions-Revision-Number`>/

- Documentation: *A number indicating the version of related ExternalDefinitions.xsd*
- Parent element: <:ref:`RdSAP-Report`>
- Has text value: *True*
- Data type: *<class 'str'>*
- Minimum occurrence: *1*
- Maximum occurrence: *1*

