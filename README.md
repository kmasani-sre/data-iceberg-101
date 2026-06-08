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

## Iceberg Tables
This was initially developed by Netflix and now an Apache project.
Iceberg is the table format, for huge analytics tables. It provides extreme high performance and supports ACID transactions.
It supports in-place schema evolution, that is entirely metadata-driven i.e. table structures can be modified without rewriting underlying data files.

## 
