# Setup EMR Cluster (Spark)

- Clone project từ git về máy local:
```bash
git clone https://github.com/HaTranThai/WeatherFlow-with-Dagster.git
```

- Cài đặt biến môi trường:
```bash
export KAFKA_BROKER=your_kafka_broker
export S3_BUCKET=your_s3_bucket
```

- Copy folder spark vào master node (đảm bảo file .pem có quyền đọc):
```bash
scp -i /path/to/key.pem -r /path/to/spark hadoop@<Master Public IPv4 address>:~/
```

- Kết nối vào master node:
```bash
ssh -i /path/to/key.pem hadoop@<Master Public IPv4 address>
```

- Chạy spark-submit (Chọn đúng phiên bản của packages):
```bash
cd spark
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.1 stream_event.py
```