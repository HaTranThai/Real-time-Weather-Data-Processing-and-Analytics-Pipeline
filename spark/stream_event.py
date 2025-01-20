import os
import sys
from schema import schema
from stream_funtions import *

Current_data_topic = "Current_data"
Air_pollution_data_topic = "Air_pollution_data"

Kafka_broker = os.getenv("KAFKA_BROKER")
S3_bucket = os.getenv("S3_BUCKET")
S3_bucket_path = f's3://{S3_bucket}/output-data'

spark = create_spark_session('WeatherData')
spark.streams.resetTerminated()

Current_data = create_kafka_read_stream(spark, Kafka_broker, "9092", Current_data_topic)
Current_data = process_stream(Current_data, schema[Current_data_topic], Current_data_topic)

Air_pollution_data = create_kafka_read_stream(spark, Kafka_broker, "9092", Air_pollution_data_topic)
Air_pollution_data = process_stream(Air_pollution_data, schema[Air_pollution_data_topic], Air_pollution_data_topic)


current_data_stream = create_file_write_stream(Current_data
                                                  , f'{S3_bucket_path}/{Current_data_topic}'
                                                  , f'{S3_bucket_path}/checkpoint/{Current_data_topic}'
                                                  , "120 seconds")

air_pollution_data_stream = create_file_write_stream(Air_pollution_data
                                                    , f'{S3_bucket_path}/{Air_pollution_data_topic}'
                                                    , f'{S3_bucket_path}/checkpoint/{Air_pollution_data_topic}'
                                                    , "120 seconds")

current_data_stream.awaitTermination()
air_pollution_data_stream.awaitTermination()
