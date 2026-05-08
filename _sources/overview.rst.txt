What is sap10calcs?
===================

`sap10calcs` is a Python package for running Standard Assessment Procedure energy calculations.

What is SAP10?
--------------

SAP10 is the Standard Assessment Procedure version 10, the UK Government's energy calculation method used for building regulations for new dwellings and as the calculation process behind Energy Performance Certificates (EPCs) for existing dwellings. SAP10 is developed and published by the Building Research Establishment: https://bregroup.com/expertise/energy/sap/sap10.

What is RdSAP10?
----------------

RdSAP10 is the Reduced-data Standard Assessment Procedure version 10, the UK Government's energy calculation method for Energy Performance Certificates for existing dwellings. RdSAP10 is developed and published by the Building Research Establishment: https://bregroup.com/expertise/energy/sap/sap10.

How does sap10calcs work?
-------------------------

`sap10calcs` runs SAP10 and RdSAP10 calculations by:

- taking an XML input file (or creating one from scratch)
- running a SAP calculation (this is done using a remote API service)
- returning the results of the calculation to the user (this is a file with all the intemediate and final calculation values)

What can sap10calcs be used for?
--------------------------------

`sap10calcs` can be used for:

- rerunning EPC calculations to experiment with different energy-efficiency recommendations (using the initial RdSAP XML file from the EPC assessment as the starting point).
- exploring new building designs to meet the latest building regulations, either for Part L or the Future Homes Standard.
- comparing SAP calculations to those from other models, such as the Home Energy Model or EnergyPlus.

Is the SAP calculation accredited?
----------------------------------

No, the SAP calculation used here is not accredited.

I would like to take this through the accrediation process but so far have not been able to find out how this works. If you can help with this please let me know.

Why does sap10calcs use a remote API service?
---------------------------------------------

The calculation engine for `sap10calcs` uses a remote API service which is hosted here: https://netzeroapis.com/

This is done for the following reasons:

- The remote API allows users to work with SAP10 calculations in languages other than Python, by calling the remote API directly rather than using the `sap10calcs` package.
- The SAP calculations rely on the `PCDB database <https://www.ncm-pcdb.org.uk/sap/index.jsp>`__, which is often being updated. Using the remote API, these updates will take place immediately for all calculation runs.
- The SAP calculation method is complex and not clearly described in the existing documentation, so many updates and fine-tuning is expected. Using a remote API these updates will take effect immediately.

How do I find out more?
-----------------------

Please contact me: 

- Email: s.k.firth@lboro.ac.uk
- Website: https://www.stevenfirth.com/
- University profile: https://www.lboro.ac.uk/departments/abce/staff/steven-firth/


