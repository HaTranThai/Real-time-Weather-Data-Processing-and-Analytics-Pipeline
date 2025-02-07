# Setup Dagster EC2

- Clone project từ git về máy local:
```bash
git clone https://github.com/HaTranThai/WeatherFlow-with-Dagster.git
```

- Tạo máy EC2 trên AWS:
  - Chọn AMI: Ubuntu Server 20.04 LTS (HVM), SSD Volume Type
  - Chọn Instance Type: t2.small
  - Chọn Security Group: 
    - Add Rule: Type: SSH, Protocol: TCP, Port Range: 22, Source: Anywhere
    - Add Rule: Type: HTTP, Protocol: TCP, Port Range: 80, Source: Anywhere
    - Add Rule: Type: Custom TCP, Protocol: TCP, Port Range: 3000, Source: Anywhere
  - Tạo key pair và download file .pem về máy local
  - Khởi chạy instance

- Copy folder dagster và script vào EC2 (đảm bảo file .pem có quyền đọc):
```bash
scp -i /path/to/key.pem -r /path/to/dagster ubuntu@<Public IPv4 address>:~/
scp -i /path/to/key.pem /path/to/setup_docker.sh ubuntu@<Public IPv4 address>:~/
```

- Kết nối vào máy EC2:
```bash
ssh -i /path/to/key.pem ubuntu@<Public IPv4 address>
```

- Thêm biến môi trường Kafka và Redshift vào EC2:
```bash
export KAFKA_ADDRESS=your_kafka_address
export REDSHIFT_HOST=your_redshift_host
export AWS_ACCESS_KEY_ID=your_aws_access_key_id
export AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
```

- Cài đặt Docker:
```bash
sudo chmod +x setup_docker.sh
./setup_docker.sh
newgrp docker
```

- Chạy Docker:
```bash
cd dagster
docker-compose up -d
```

- Kiểm tra trạng thái của các container:
```bash
docker ps
```

- Truy cập vào trang web Dagster:
```
http://<Public IPv4 address>:3000
```



