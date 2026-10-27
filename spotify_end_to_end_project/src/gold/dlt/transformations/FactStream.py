# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
from pyspark import pipelines as dp

# 1. Create the staging dataset from the Silver table
@dp.table(name="factstream_stg")
def factstream_stg():
    return spark.readStream.table("spotify_cata.silver.factstream")


# 2. Create the Gold target streaming table
dp.create_streaming_table(name="factstream")


# 3. Apply CDC to the Gold target
dp.create_auto_cdc_flow(
    target="factstream",
    source="factstream_stg",
    keys=["stream_id"],
    sequence_by="stream_timestamp",
    stored_as_scd_type=1
)