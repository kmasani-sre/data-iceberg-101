## Data File Format - Types
Data file format is a standardized structure used to encode and organize data for storage, processing, and transfer.
Appropriate format for your use-case depends on system compatibility, and whether it is required for human readability or is for machine-optimized needs.

### XML - Extensible Markup Language
Markup langugage that defines a set of rules for encoding documents in this a format that is both human and machine readable.
Commonly used as configuration files and data exchange.
This is not as compact and not ideal for large datasets.

### JSON - JavaScript Object Notation
Data format easy for humans to read and for systems to work with.
Supports flexible data types - Strings, numbers, arrays and objects.

### Parquet - Columnar Storage Format
Column-oriented data file format that provides efficient data compression. Supports add/remove of columns easily.
Commonly used in large datasets in data warehouse, real time data processing.

### Avro - Row based Format
Avro is compact, binary data format that is commonly used with Apache Spark and Kafka.

## Open Table Format
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

#### Execution Output
![Screenshot of Iceberg table Storage View.](/scripts/iceberg/images/Iceberg_Execution_Output.png)
#### Storage View
![Screenshot of Iceberg table Storage View.](/scripts/iceberg/images/Iceberg_Local_Storage_Version_View.png)