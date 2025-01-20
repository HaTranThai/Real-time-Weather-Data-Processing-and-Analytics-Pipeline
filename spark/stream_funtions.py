from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, month, hour, dayofmonth, col, year, udf, to_timestamp
from pyspark.sql.functions import col, from_unixtime, date_format

from selector import current_select, airpollution_select 

def create_spark_session(app_name):
    spark = SparkSession.builder \
                        .appName(app_name) \
                        .getOrCreate()

    return spark

def create_kafka_read_stream(spark, kafka_address, kafka_port, topic, starting_offset="earliest"):
    read_stream = (spark
                   .readStream
                   .format("kafka")
                   .option("kafka.bootstrap.servers", f"{kafka_address}:{kafka_port}")
                   .option("failOnDataLoss", False)
                   .option("startingOffsets", starting_offset)
                   .option("subscribe", topic)
                   .load())

    return read_stream

def process_stream(stream, stream_schema, topic):
    stream = stream.selectExpr("CAST(value AS STRING)")
    stream = stream.select(from_json(col("value"), stream_schema).alias("data"))
    stream = stream.select("data.*")

    if topic == "Current_data":
        stream = current_select(stream)
        stream = stream.withColumn("dt", from_unixtime(col("dt")).cast("timestamp"))
        stream = stream.withColumn("sunrise", from_unixtime(col("sunrise")).cast("timestamp"))
        stream = stream.withColumn("sunset", from_unixtime(col("sunset")).cast("timestamp"))
    else:
        stream = airpollution_select(stream)
        stream = stream.withColumn("dt", from_unixtime(col("dt")).cast("timestamp"))

    return stream

def create_file_write_stream(stream, output_path, checkpoint_path, trigger_time="120 seconds"):
    write_stream = (stream
                    .writeStream
                    .format("parquet")
                    .option("path", output_path)
                    .option("checkpointLocation", checkpoint_path)
                    .trigger(processingTime=trigger_time)
                    .start())

    return write_stream
