# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
from pyspark import pipelines as dp

@dp.table(name="dimtrack_stg")
def dimtrack_stg():
    return spark.readStream.table("spotify_cata.silver.dimtrack")


dp.create_streaming_table(name="dimtrack")

dp.create_auto_cdc_flow(
    target="dimtrack",
    source="dimtrack_stg",
    keys=["track_id"],
    sequence_by="updated_at",
    stored_as_scd_type=2
)