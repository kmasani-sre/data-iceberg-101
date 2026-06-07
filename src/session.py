import os
from pyspark.sql import SparkSession

def get_spark_session(env="local"):
    """
    Returns a configured SparkSession.
    Options for env: 'local', 'iceberg-local', 'iceberg-aws'
    """
    builder = SparkSession.builder.appName(f"PySpark-Exploration-{env}")

    if env == "local":
        # Standard session for basic JSON/DataFrame tasks
        return builder.getOrCreate()

    elif env == "iceberg-local":
        # Configured for Local Iceberg Tables
        return (builder
                .config("spark.jars.packages", "org.apache.iceberg:iceberg-spark-runtime-4.0_2.13:1.10.0,org.apache.iceberg:iceberg-gcp-bundle:1.10.0")
                .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions")
                .config("spark.sql.catalog.local", "org.apache.iceberg.spark.SparkCatalog")
                .config("spark.sql.catalog.local.type", "hadoop")
                .config("spark.sql.catalog.local.warehouse", os.path.abspath("./data/warehouse"))
                .getOrCreate())

    elif env == "iceberg-aws":
        # Configured for AWS S3 and AWS Glue Catalog
        return (builder
                .config("spark.jars.packages", "org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.5.0,org.apache.hadoop:hadoop-aws:3.3.4")
                .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions")
                .config("spark.sql.catalog.aws_catalog", "org.apache.iceberg.spark.SparkCatalog")
                .config("spark.sql.catalog.aws_catalog.type", "glue")
                .config("spark.sql.catalog.aws_catalog.warehouse", "s3a://your-bucket-name/iceberg-warehouse/")
                .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
                # Note: ALWAYS use IAM Roles/DefaultAWSCredentialsProviderChain AND DO NOT USE ANY hardcoded keys
                .getOrCreate())

    else:
        raise ValueError(f"Unknown environment: {env}")