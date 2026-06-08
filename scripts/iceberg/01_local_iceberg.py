import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.spark_config import get_spark_iceberg_session

def run_pipeline():
    # Start the Session
    spark = get_spark_iceberg_session(env="local")

    # Define paths
    json_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/input/movies.local.json"))
    table_identifier = "local.default.movie_events"

    # Mocking a quick JSON file if it doesn't exist
    if not os.path.exists(json_path):
        import json
        mock_data = [
            {"user_id": 101, "event": "click", "timestamp": "2026-06-01 10:00:00"},
            {"user_id": 102, "event": "login", "timestamp": "2026-06-01 10:05:00"},
            {"user_id": 103, "event": "purchase", "timestamp": "2026-06-01 10:12:00"}
        ]
        print(f"Preparing the mock data .. ")
        os.makedirs(os.path.dirname(json_path), exist_ok=True)
        with open(json_path, 'w') as f:
            for item in mock_data:
                f.write(json.dumps(item) + "\n")

    # Read the JSON file into a Spark DataFrame
    print(f"Reading data from: {json_path}")
    df = spark.read.option("multiLine", True).json(json_path)

    print("Inferred Schema:")
    df.printSchema()

    # Write DataFrame to an Apache Iceberg Table
    print(f"Writing data to Iceberg table: {table_identifier}")
    # 'append' mode will create the table if it doesn't exist or append if it does
    df.write \
        .format("iceberg") \
        .mode("append") \
        .save(table_identifier)

    # df.writeTo(table_identifier).mode("append").createOrReplace()

    # Read back from the Iceberg table to prove success
    print("\nQuerying the newly written Iceberg Table:")
    iceberg_df = spark.read.format("iceberg").load(table_identifier)
    iceberg_df.show()

    # Querying Iceberg Metadata (Snapshots)
    print("Iceberg Table History/Snapshots:")
    spark.read.format("iceberg").load(f"{table_identifier}.snapshots").show(truncate=False)

    spark.stop()

if __name__ == "__main__":
    run_pipeline()