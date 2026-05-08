API reference
=============

This is the API reference for the `sap10calcs` package.

Functions
---------

.. autofunction:: sap10calcs.calculate

.. autofunction:: sap10calcs.create_rdsap_report_xml

.. autofunction:: sap10calcs.create_sap_report_xml

.. autofunction:: sap10calcs.parse_rdsap_xml

.. autofunction:: sap10calcs.parse_xml

.. autofunction:: sap10calcs.rdsap


.. _classes:

Classes
-------

`sap10calcs` contains hundreds of classes, one for each of the XML elements described in the :ref:`rdsap_xml_reference` and :ref:`sap_xml_reference`.

Below are the three starting elements for RdSAP and SAP XML files. The remaining classes are not documented here but follow a similar pattern to the three elements described below.

All classes have the following methods and properties:

   .. py:method:: copy()

      :returns: A copy of the Element.      

   .. py:method:: display()

      :returns: A string of the XML document with the codes replaced by the codes and values.
      :rtype: str

   .. py:property:: sap_xml_properties
      :type: list

      :returns: A list of all SAP-related properties of the Element (read-only).

   .. py:property:: sap_xml_methods
      :type: list

      :returns: A list of all SAP-related methods of the Element (read-only).
   
   .. py:property:: sap_xml_codes
      :type: dict

      :returns: A dictionary of the SAP-related codes used by the Element (read-only).

Elements with text values also have the following methods and attributes.

   .. py:property:: code

      A setter and getter for the text of the Element. When setting the text, this will raise an error if the text does not one of the codes as specified in the schema.

   .. py:property:: value

      Similar to the `code` property but uses the values rather than codes. 

The remaining methods and properties of the classes are then used to either add or return the child Elements. An additional property is also present to return the parent Element.

.. _rdsap_report:

.. py:class:: sap10calcs.classes_RdSAP_Schema_21_0_0.RdSAP_Report

   Represents a :ref:`RdSAP-Report` element.

   This is a subclass of a lxml Element, providing additional properties and methods to the Element as listed below:

   .. py:method:: add_calculation_software_name()

   .. py:method:: add_calculation_software_version()

   .. py:method:: add_user_interface_name()

   .. py:method:: add_schema_version_original()

   .. py:method:: add_schema_version_current()

   .. py:method:: add_sap_version()

   .. py:method:: add_pcdf_revision_number()

   .. py:method:: add_energy_assessment()

   .. py:method:: add_previous_epc_check()

   .. py:method:: add_sap_data()

   .. py:method:: add_report_header()
   
   .. py:method:: add_insurance_details()

   .. py:method:: add_externaldefinitions_revision_number()

   .. py:property:: calculation_software_name

   .. py:property:: calculation_software_version

   .. py:property:: user_interface_name

   .. py:property:: schema_version_original

   .. py:property:: schema_version_current
   
   .. py:property:: sap_version

   .. py:property:: pcdf_revision_number

   .. py:property:: previous_epc_check

   .. py:property:: energy_assessment

   .. py:property:: sap_data

   .. py:property:: report_header

   .. py:property:: insurance_details

   .. py:property:: externaldefinitions_revision_number


.. py:class:: sap10calcs.classes_SAP_Schema_19_1_0.SAP_Report

   Represents a :ref:`SAP-Compliance-Report/SAP-Report` element.

   This is a subclass of a lxml Element, providing additional properties and methods to the Element as listed below:

   .. py:method:: add_schema_version_original()

   .. py:method:: add_schema_version_current()

   .. py:method:: add_sap_version()

   .. py:method:: add_sap_data_version()

   .. py:method:: add_pcdf_revision_number()

   .. py:method:: add_calculation_software_name()

   .. py:method:: add_calculation_software_version()

   .. py:method:: add_user_interface_name()

   .. py:method:: add_user_interface_version()

   .. py:method:: add_report_header()

   .. py:method:: add_energy_assessment()

   .. py:method:: add_sap10_data()

   .. py:method:: add_pdf()

   .. py:method:: add_insurance_details()

   .. py:method:: add_externaldefinitions_revision_number()

   .. py:property:: sap_compliance_report

   .. py:property:: schema_version_original

   .. py:property:: schema_version_current

   .. py:property:: sap_version

   .. py:property:: sap_data_version

   .. py:property:: pcdf_revision_number

   .. py:property:: calculation_software_name

   .. py:property:: calculation_software_version

   .. py:property:: user_interface_name

   .. py:property:: user_interface_version

   .. py:property:: report_header

   .. py:property:: energy_assessment

   .. py:property:: sap10_data

   .. py:property:: pdf

   .. py:property:: insurance_details 

   .. py:property:: externaldefinitions_revision_number


.. py:class:: sap10calcs.classes_SAP_Schema_19_1_0.SAP_Compliance_Report

   Represents a :ref:`SAP-Compliance-Report` element.

   This is a subclass of a lxml Element, providing additional properties and methods to the Element as listed below:

   .. py:method:: add_sap_report()

   .. py:method:: add_client_name()

   .. py:method:: add_client_company()

   .. py:method:: add_client_address()

   .. py:method:: add_is_multiple_compliance()

   .. py:property:: sap_report

   .. py:property:: client_name

   .. py:property:: client_company

   .. py:property:: client_address

   .. py:property:: is_multiple_compliance

