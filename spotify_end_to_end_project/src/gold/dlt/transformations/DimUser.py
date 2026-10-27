# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
from pyspark import pipelines as dp

expectations = {
    "rule_1": "user_id IS NOT NULL"
}

# 1. Streaming staging table with expectations
@dp.expect_all_or_drop(expectations)
@dp.table(name="dimuser_stg")
def dimuser_stg():
    return spark.readStream.table("spotify_cata.silver.dimuser")


# 2. Gold streaming target with expectations
dp.create_streaming_table(
    name="dimuser",
    expect_all_or_drop=expectations
)


# 3. CDC with SCD Type 2
dp.create_auto_cdc_flow(
    target="dimuser",
    source="dimuser_stg",
    keys=["user_id"],
    sequence_by="updated_at",
    stored_as_scd_type=2
)