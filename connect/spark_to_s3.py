from pyspark.sql import SparkSession

# Tạo SparkSession
spark = SparkSession.builder \
    .appName("Spark S3 Example") \
    .getOrCreate()

# Tạo DataFrame mẫu
data = [
    ("Alice", 34, "New York"),
    ("Bob", 45, "San Francisco"),
    ("Cathy", 29, "Seattle")
]
columns = ["Name", "Age", "City"]

df = spark.createDataFrame(data, columns)

# Lưu DataFrame vào S3 bucket
output_path = "s3://weather-data-hatran/output-data/"
df.write \
    .mode("overwrite") \
    .parquet(output_path)

print(f"Data saved to {output_path}")

# Dừng SparkSession
spark.stop()
