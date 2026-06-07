## Iceberg
An *Open Table Format (OTF)* is an open-sourced metadata layer that sits on top of raw data files (like parquet) in Cloud storage.
It organizes these files into manageable database tables, providing features like
1. ACID transactions
2. Schema evolution
3. time travel

+- - - - - - - - - - - - - - - - - - - - - - - +  
| [Layer-3] Compute Engines - Spark/Python     |  
|- - - - - - - - - - - - - - - - - - - - - - - |  
| [Layer-2] Metadata layer / OTF - Iceberg     |  
|- - - - - - - - - - - - - - - - - - - - - - - |  
| [Layer-1] Object Storage - Parquet           |  
+- - - - - - - - - - - - - - - - - - - - - - - +  

Three major standards are
1. Apache Iceberg
2. Delta Lake
3. Apache Hudi

### Apache Iceberg
Apache Iceberg uses a tree structure of metadata files that scales to massive tables with extensive snapshot history. The format separates metadata from data completely, enabling efficient operations at scale.