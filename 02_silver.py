from pyspark.sql import SparkSession
from pyspark.sql.functions import col, trim, upper, to_date
from config import configure_adls_access, bronze_output_path, silver_output_path

spark = SparkSession.builder.getOrCreate()

configure_adls_access(spark)

df_bronze = spark.read.format("delta").load(bronze_output_path)

df_silver = (
    df_bronze
    .withColumn("customer_name", trim(col("customer_name")))
    .withColumn("country", upper(trim(col("country"))))
    .withColumn("order_date", to_date(col("order_date"), "yyyy-MM-dd"))
    .withColumn("quantity", col("quantity").cast("int"))
    .withColumn("unit_price", col("unit_price").cast("double"))
    .withColumn("total_amount", col("quantity") * col("unit_price"))
)

df_silver.write.format("delta").mode("overwrite").save(silver_output_path)

print("Silver layer completed successfully")
print(f"Silver path: {silver_output_path}")
