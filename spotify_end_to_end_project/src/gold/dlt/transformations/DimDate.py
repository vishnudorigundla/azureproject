# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
from pyspark import pipelines as dp

@dp.table(name="dimdate_stg")
def dimdate_stg():
    return spark.readStream.table("spotify_cata.silver.dimdate")


dp.create_streaming_table(name="dimdate")

dp.create_auto_cdc_flow(
    target="dimdate",
    source="dimdate_stg",
    keys=["date_key"],
    sequence_by="date",
    stored_as_scd_type=2
)