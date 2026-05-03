from pyspark.sql import SparkSession
from config import configure_adls_access, raw_file_path, bronze_output_path

spark = SparkSession.builder.getOrCreate()

configure_adls_access(spark)

df_raw = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv(raw_file_path)
)

df_raw.write.format("delta").mode("overwrite").save(bronze_output_path)

print("Bronze layer completed successfully")
print(f"Bronze path: {bronze_output_path}")
