# automated-view-ddl-creation

> Creating automated Views for use in Aggregation Layer of any reporting tool(Power BI, Qlik, QuickSight) and to reduce manual effort of writing the views to nil. This activity has reduced resource focusing on writing SQL Queries by 100%. 
The Views are created from a CSV file as an input and the Output is the SQL View File and can be run in any Google BigQuery Instance.

# Structure to be created:

````CREATE VIEW `bt-us-nucl-tst-live.aggregation.F_SUBSCS_D_V` AS SELECT (COLUMNS) FROM `T_VNER2.F_SUBSCS_D`;````
 
# Installing
This Automated Framework was created on **Python 3.8.5** and uses some external libraries listed below:

### a) CSV
### b) Pandas
### c) Numpy

# Build/Run Command
Use following commands to build/Run the project from the project root. 
This script accepts 3 inputs and generates 2 YML Files
### CSV Sheet (Excel File which has the Table_Name and Columns row by row)
### Above CSV sheet can be found in input/View_Report001.csv (keep your own, but preserve headers of the original file)
````
python .\view_creation_main.py
````

### Authors
* Sourav Roy (souravroy7864@gmail.com)
