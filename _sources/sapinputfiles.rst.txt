What are SAP XML files?
=======================

SAP10 and RdSAP10 use XML files for the inputs to the SAP calculations. These files also store some of the outputs of the calculations.

What is an XML file?
--------------------

An XML file is a text file which can be stored on the local computer. These text files store information using a specific `set of rules <https://www.w3.org/TR/xml/>`__ which allow them to be read, edited and queried. XML files are used to transfer information between software programmes and can be read by most programming languages. In Python I uses the `lxml package <https://lxml.de/>`__ to work with XML.

XML files have three main constructs:

- Elements, such as ``<SAP10-Data>``. The elements are in a tree-like structure with a root (start) element and parent/child elements.
- Element text, such as ``<Postcode>LE11 3TU</Postcode>``. Here the "Postcode" element has the text "LE11 3TU".
- Element attributes, such as ``<SAP-Report xmlns="https://epbr.digital.communities.gov.uk/xsd/sap">``. Here the "SAP-Report" element has a "xmlns" attribute.

What does a SAP10 XML file look like?
-------------------------------------

A SAP10 XML file looks like this (note this in a shortened version):

.. code-block:: xml

   <?xml version='1.0' encoding='UTF-8'?>
   <SAP-Report xmlns="https://epbr.digital.communities.gov.uk/xsd/sap">
      <Schema-Version-Original>SAP-Schema-19.1.0</Schema-Version-Original>
      <SAP-Version>10.2</SAP-Version>
      <Report-Header>
         <Property>
         <Address>
            <Postcode>LE11 3TU</Postcode>
         </Address>
         </Property>
      </Report-Header>
      <SAP10-Data>
         <Data-Type>1</Data-Type>
         <SAP-Property-Details>
         <Cold-Water-Source>1</Cold-Water-Source>
         <Living-Area>30</Living-Area>
         <Windows-Overshading>2</Windows-Overshading>
         <SAP-Building-Parts>
            ...
         </SAP-Building-Parts>
      </SAP10-Data>
   </SAP-Report>

This is a text file and this is how it would look if opened in, say, Notepad.

There are three questions here:

- What is the meaning of the different elements (``SAP-Report``, ``Schema-Version-Original`` etc.)?
- How should the different elements be structured (which should come first, what are the child elements of ``SAP-Report`` etc.)?
- What is the meaning of the text being used (i.e. what does ``Cold-Water-Source`` = "1" refer to)?

These questions are answered by the use of an XML Schema.

What is an XML schema?
----------------------

An `XML schema <https://www.w3.org/TR/xmlschema-1/>`__ is an additional set of rules for an XML document. Schemas are designed to work with a particular application and define the elements and structure of XML files for that application. For example, an XML schema for a building energy application might define the elements ``<Building>``, ``<Room>``, ``<SolarPanel>`` etc.

What is the the format of SAP XML files?
------------------------------------------------

SAP10 XML files use the schema given on the GitHub page for the Ministry of Housing, Communities and Local Government here: https://github.com/communitiesuk/epb-register-api/tree/master/api/schemas/xml/SAP-Schema-19.1.0/SAP

An example of a SAP10 XML input file which follows this schema can be seen here: :ref:`an_example_input_file`.

RdSAP10 XML files use the schema given on the GitHub page for the Ministry of Housing, Communities and Local Government here: 
https://github.com/communitiesuk/epb-register-api/tree/master/api/schemas/xml/RdSAP-Schema-21.0.0/RdSAP

OK, how do I read these XML schemas?
------------------------------------

If you look at these XML schemas on GitHub you will see that they are difficult to understand. This is because:

- The XML schema language itself isn't easy to read.
- The SAP10 and RdSAP10 schemas are actually multiple files with links between them.
- The SAP10 and RdSAP10 schemas use numerical codes (such as the code "1" for the value "detached") which makes them difficult to visually inspect.

So how do I work with SAP10 and RdSAP10 input files?
--------------------------------------------------------

Here is my guide to the SAP10 and RdSAP10 XML files:

- Use the online references to the XML schemas which I have created here (this is much easier than working with the XML schemas directly): 

   - :ref:`sap_xml_reference`
   - :ref:`rdsap_xml_reference`

- SAP10 XML files always start with either a :ref:`SAP-Compliance-Report` or a :ref:`SAP-Compliance-Report/SAP-Report` element.
- RdSAP10 XML files always start with the :ref:`RdSAP-Report` element.
- For manual editing:

   - Use `Visual Studio Code <https://code.visualstudio.com/>`__ (or similar) for manual editing of the XML files.
- For editing with Python:

   - Use the :py:func:`sap10calcs.parse_xml` or :py:func:`sap10calcs.parse_rdsap_xml` methods to read in the XML files using Python. Then use the `display` method on one of the XML elements (such as :py:meth:`sap10calcs.classes_SAP_Schema_19_1_0.SAP_Report.display`) to display the XML files in an easier-to-read format.
   - Use the :ref:`sap10calcs XML classes <classes>` to work with and edit the XML files.

What do I do if there is an error?
----------------------------------

It is very easy to create a SAP XML file that isn't correctly structured and will cause an error if used in a SAP calculation.

This is because the original SAP and RdSAP XML schemas are not particularly well structured and it is difficult to tell what information is required.

For example, changing the heating system from a gas boiler to a heat pump requires some XML elements to be removed and additional XML elements to be created.

`sap10calcs` should provide a useful error message to say when an XML element is missing or if an incorrect code has been used in an XML element. If instead there is a general error, then please contact me and I will fix this.











