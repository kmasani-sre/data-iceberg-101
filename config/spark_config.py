import os
from pyspark.sql import SparkSession

def get_spark_iceberg_session(env="local"):
    """
    Configures and returns a Spark Session with Apache Iceberg support.
    Supports 'local' (Hadoop catalog on disk) and 's3' (AWS Glue/S3 setup).
    """
    # Required Iceberg Spark runtime package (Adjust versions according to your Spark/Scala stack)
    # Using Iceberg 1.5.0 with Spark 3.5 & Scala 2.12 as a stable baseline
    iceberg_spark_package = "org.apache.iceberg:iceberg-spark-runtime-4.0_2.13:1.10.0"
    gcp_bundle_package = "org.apache.iceberg:iceberg-gcp-bundle:1.10.0"
    aws_bundle_package = "org.apache.iceberg:iceberg-aws-bundle:1.5.0"

    builder = (SparkSession.builder
               .appName(f"Iceberg-Explorer-{env}")
               .config("spark.jars.packages", f"{iceberg_spark_package},{gcp_bundle_package}")
               # Enable Iceberg SQL extensions
               .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions")
               )

    if env == "local":
        warehouse_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../scripts/data/warehouse"))
        print(f"Warehouse Path: {warehouse_path}")
        builder = (builder
                   # Define a local catalog named 'demo'
                   .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions")
                   .config("spark.sql.catalog.local", "org.apache.iceberg.spark.SparkCatalog")
                   .config("spark.sql.catalog.local.type", "hadoop")
                   .config("spark.sql.sources.partitionOverwriteMode", "dynamic")
                   .config("spark.sql.catalog.local.warehouse", f"file://{warehouse_path}")
                   )
    elif env == "s3":
        # Assumes AWS environment variables (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY) are set
        s3_warehouse_path = os.getenv("AWS_S3_WAREHOUSE_PATH", "ICEBERG_WAREHOUSE_BUCKET_MISSING")

        builder = (builder
                   # Define an S3/Glue catalog named 'aws_catalog'
                   .config("spark.sql.catalog.aws_catalog", "org.apache.iceberg.spark.SparkCatalog")
                   .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions")
                   .config("spark.sql.catalog.aws_catalog.catalog-impl", "org.apache.iceberg.aws.glue.GlueCatalog")
                   .config("spark.sql.catalog.aws_catalog.warehouse", s3_warehouse_path)
                   .config("spark.sql.catalog.aws_catalog.io-impl", "org.apache.iceberg.aws.s3.S3FileIO")
                   # Hadoop AWS integration configs
                   .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
                   )

    return builder.getOrCreate()