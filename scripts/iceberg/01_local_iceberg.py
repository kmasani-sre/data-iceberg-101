from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("JSON_To_Iceberg") \
    .config("spark.jars.packages", "org.apache.iceberg:iceberg-spark-runtime-4.0_2.13:1.10.0,org.apache.iceberg:iceberg-gcp-bundle:1.10.0") \
    .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
    .config("spark.sql.catalog.local", "org.apache.iceberg.spark.SparkCatalog") \
    .config("spark.sql.catalog.local.type", "hadoop") \
    .config("spark.sql.catalog.local.warehouse", "/Users/kmasani/ml-learning/dw") \
    .getOrCreate()

df = spark.read.option("multiLine", True).json("/Users/kmasani/ml-learning/movies.json")

df.printSchema()

df.writeTo("local.db.movies_iceberg_table").createOrReplace()
