from pyspark.sql import SparkSession

# Initialize a local Spark session
spark = SparkSession.builder \
    .appName("LocalMacTest") \
    .master("local[*]") \
    .getOrCreate()

# Create dummy data
data = [("Apple", 3), ("Banana", 2), ("Orange", 5)]
columns = ["Fruit", "Quantity"]

df = spark.createDataFrame(data, columns)
df.show()

# Stop the session
spark.stop()
