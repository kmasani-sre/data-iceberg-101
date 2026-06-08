### Iceberg Tables
This was initially developed by Netflix and now an Apache project.
Iceberg is the table format, for huge analytics tables. It provides extreme high performance and supports ACID transactions.
It supports in-place schema evolution, that is entirely metadata-driven i.e. table structures can be modified without rewriting underlying data files.

### Databricks
TBD

### POC Scope
1. Load the data from external source/file using PySpark  
2. Save this data as Iceberg tables on both local and Cloud (AWS S3) storage.  
3. Highlight the internal structure of the Iceberg storage.  
4. Load this dataset (S3 bucket / Iceberg tables) onto Databricks  
5. Use Databricks to analyze/query the data  


