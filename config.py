tenant_id = "edf874bb-35fe-478a-b528-490414122885"
client_id = "0ce30ac6-bd8b-4e13-8196-c7a9ece3e34c"
client_s = "NJU8Q~AiuftivkjZuD339HmiwWQC0Af3LzF6Ub55"
storage_account = "stdatabricksbasicdev1"


def configure_adls_access(spark):
    spark.conf.set(
        f"fs.azure.account.auth.type.{storage_account}.dfs.core.windows.net",
        "OAuth"
    )

    spark.conf.set(
        f"fs.azure.account.oauth.provider.type.{storage_account}.dfs.core.windows.net",
        "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider"
    )

    spark.conf.set(
        f"fs.azure.account.oauth2.client.id.{storage_account}.dfs.core.windows.net",
        client_id
    )

    spark.conf.set(
        f"fs.azure.account.oauth2.client.secret.{storage_account}.dfs.core.windows.net",
        client_s
    )

    spark.conf.set(
        f"fs.azure.account.oauth2.client.endpoint.{storage_account}.dfs.core.windows.net",
        f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"
    )


raw_file_path = f"abfss://raw@{storage_account}.dfs.core.windows.net/orders/sample_orders.csv"

bronze_output_path = f"abfss://bronze@{storage_account}.dfs.core.windows.net/orders_delta"

silver_output_path = f"abfss://silver@{storage_account}.dfs.core.windows.net/orders_cleaned_delta"

gold_output_path = f"abfss://gold@{storage_account}.dfs.core.windows.net/sales_by_country_delta"
