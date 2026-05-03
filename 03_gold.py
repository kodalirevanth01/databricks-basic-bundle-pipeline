from pyspark.sql import SparkSession
from pyspark.sql.functions import sum as spark_sum, count
from config import configure_adls_access, silver_output_path, gold_output_path

spark = SparkSession.builder.getOrCreate()

configure_adls_access(spark)

df_silver = spark.read.format("delta").load(silver_output_path)

df_gold = (
    df_silver
    .groupBy("country")
    .agg(
        count("order_id").alias("total_orders"),
        spark_sum("quantity").alias("total_quantity"),
        spark_sum("total_amount").alias("total_sales_amount")
    )
)

df_gold.write.format("delta").mode("overwrite").save(gold_output_path)

print("Gold layer completed successfully")
print(f"Gold path: {gold_output_path}")
