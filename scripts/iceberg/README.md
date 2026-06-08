## POC Scope
1. Load the data from external source/file using PySpark
2. Save this data as Iceberg tables on both local and Cloud (AWS S3) storage.
3. Highlight the internal structure of the Iceberg storage.
4. Load this dataset (S3 bucket / Iceberg tables) onto Databricks
5. Use Databricks to analyze/query the data

## Open Table Format
An *Open Table Format (OTF)* is an open-sourced metadata layer that sits on top of raw data files (like parquet) in Cloud storage.
It organizes these files into manageable database tables, providing features like
1. ACID transactions
2. Schema evolution
3. Time travel 

+- - - - - - - - - - - - - - - - - - - - - - - +  
| [Layer-3] Compute Engines - Spark/Python     |  
|- - - - - - - - - - - - - - - - - - - - - - - |  
| [Layer-2] OTF Metadata layer /  Iceberg      |  
|- - - - - - - - - - - - - - - - - - - - - - - |  
| [Layer-1] Object Storage - Parquet           |  
+- - - - - - - - - - - - - - - - - - - - - - - +  

In this pattern, there is a disintegration of compute and object storage. Layer-1 leveraging existing file formats like avro, parquet
takes care of handling the data, its compression and encoding.   
  
Layer-2, OTF then organizes this storage data into logical tables. OTF adds an abstraction layer
through metadata and thus providing database like features such as schemas, partitions, consistency, ACID transactions.  
  
Layer-3, compute engines like Spark, Trino interact with the OTF and process the data while being vendor-agnostic.

Three major standards are
1. Apache Iceberg
2. Delta Lake
3. Apache Hudi

### Apache Iceberg
Apache Iceberg uses a tree structure of metadata files that scales to massive tables with extensive snapshot history. The format separates metadata from data completely, enabling efficient operations at scale.

#### Execution Output
![Screenshot of Iceberg table Storage View.](/scripts/iceberg/images/Iceberg_Execution_Output.png)
#### Storage View
![Screenshot of Iceberg table Storage View.](/scripts/iceberg/images/Iceberg_Local_Storage_Version_View.png)