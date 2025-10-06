The SAP calculation methodology
===============================

.. _sap_10_calculation_method:

SAP10 calculation method
------------------------

The SAP10 calculation method firstly takes a SAP10 XML file as an input file.

This XML file contains a mix of information including:

- The geometry of the building (floor area, room height, number of storeys, window area etc.)
- The U-values of the walls, roof, floor and windows.
- The space heating and cooling system (boiler type, efficiency, heat distribution system etc.)
- The water heating system (type, efficiency, cylinder or thermal store etc.)
- The ventilation system (air tightness, infiltration, natural or mechanical ventilation etc.)

This input data can be used to run different types of SAP calculations. In `sap10calcs` there are three SAP calculation options:

- **New dwelling as designed - dwelling emissions**: This is used to calculate the carbon emissions as a part of Building Regulations compliance. It uses the UK Average climate data.
- **Energy rating**: This is used to calculate the SAP rating (energy-efficiency band) as a part of an Energy Performance Certificate calculation. It uses the UK Average climate data and the fixed fuel costs in the `SAP10 specification <https://bregroup.com/documents/d/bre-group/sap-10-2-14-03-2025>`__.
- **EPC costs, emissions and primary energy**: This is used to calculate the energy and running costs as a part an Energy Performance Certificate calculation. This uses climate data based on the location of the building and the latest updates fuel prices from the PCDB (an online database).

Next, various lookups are employed to gather additional information to supplement the XML input data. This comes from:

- The SAP10 tables: These data tables are provided in the SAP10 document and include information such as regional climate data and heating system efficiency.
- The `Product Characterictic Database <https://www.ncm-pcdb.org.uk/sap/index.jsp>`__ (PCDB): This is an online database which contains detailed information on specific models of boilers and other heating systems, the latest updated fuel prices and climate data based on postcodes.

Next, the calculation process itself begins. This done by following the steps in the SAP Worksheet of the `SAP10 specification <https://bregroup.com/documents/d/bre-group/sap-10-2-14-03-2025>`__:

1. Overall dwelling dimensions.
2. Ventilation rate.
3. Heat loss and heat loss parameter.
4. Water heating energy requirements.
5. Internal gains.
6. Solar gains.
7. Mean internal temperature.
8. Space heating requirement.
9. Energy requirements.
10. Fuel costs.
11. SAP rating.
12. CO2 emissions.
13. Primary energy.

The outputs to a SAP calculation are the calculated values from the SAP worksheet, such as monthly energy requirements, annual fuel costs and the SAP rating.

RdSAP10 calculation method
--------------------------

The RdSAP10 calculation method firstly takes a RdSAP10 XML file as an input file.

This input file contains similar information to the SAP10 XML files, but in less detail.

The goal of the RdSAP10 calculation is to convert this less-detailed input data into a full set of SAP10 inputs (i.e. a SAP10 XML file), which can then be run thought a SAP10 calculation.

This process is described in the `RdSAP10 Specification <https://bregroup.com/documents/d/bre-group/rdsap-10-specification-10-06-2025>`__. This involves calculations of:

1. Areas and dimensions
2. Ventilation
3. Construction types and insulation (U-values)
4. Conservatories
5. Solar gains
6. Windows and doors
7. Room count and living area
8. Space and water heating
9. Additional items
10. Electricity tariff

This is done by using equations and lookup tables which are all located within the `RdSAP10 Specification <https://bregroup.com/documents/d/bre-group/rdsap-10-specification-10-06-2025>`__ document.

The output of the RdSAP10 calculation is a full SAP10 XML input file.

The EPC calculation method
--------------------------

The calculation method for Energy Performance Certificates actually involves several different calculations.

An EPC calculation will start with an RdSAP10 XML input file. The calculation then proceeds as:

1. The RdSAP10 XML file is converted to a full SAP10 XML file.
2. A SAP10 calculation is run using the **Energy rating** method, to calculate the SAP rating for the EPC.
3. A SAP10 calculation is run using the **EPC costs, emissions and primary energy** method, to calculate the current energy consumption and running costs for the EPC.
4. Energy-efficiency recommendations are then applied to the dwelling, using the logic in Section 21 of the `RdSAP10 Specification <https://bregroup.com/documents/d/bre-group/rdsap-10-specification-10-06-2025>`__. This might include additional insulation, replacement heating systems and renewable energy systems.
5. Steps 1, 2 and 3 are then rerun for each new RdSAP10 XML file that is created by applying the recommendations logic in Step 4.

So, an EPC with 4 energy-efficiency recommendations would have 5 RdSAP10 XML files, 5 SAP10 XML files and 10 SAP10 calculations.
