# Setup kakfa EC2

- Clone project từ git về máy local:
```bash
git clone https://github.com/HaTranThai/WeatherFlow-with-Dagster.git
```

- Tạo máy EC2 trên AWS:
  - Chọn AMI: Ubuntu Server 20.04 LTS (HVM), SSD Volume Type
  - Chọn Instance Type: t3.large
  - Chọn Security Group: 
    - Add Rule: Type: SSH, Protocol: TCP, Port Range: 22, Source: Anywhere
    - Add Rule: Type: HTTP, Protocol: TCP, Port Range: 80, Source: Anywhere
    - Add Rule: Type: Custom TCP, Protocol: TCP, Port Range: 3000, Source: Anywhere
    - Add Rule: Type: Custom TCP, Protocol: TCP, Port Range: 9021, Source: Anywhere
    - Add Rule: Type: Custom TCP, Protocol: TCP, Port Range: 9092, Source: Anywhere
  - Tạo key pair và download file .pem về máy local
  - Khởi chạy instance

- Copy folder kafka và script vào EC2 (đảm bảo file .pem có quyền đọc):
```bash
scp -i /path/to/key.pem -r /path/to/kafka ubuntu@<Public IPv4 address>:~/
scp -i /path/to/key.pem /path/to/setup_docker.sh ubuntu@<Public IPv4 address>:~/
```

- Kết nối vào máy EC2:
```bash
ssh -i /path/to/key.pem ubuntu@<Public IPv4 address>
```

- Thêm biến môi trường Kafka vào EC2:
```bash
export KAFKA_ADDRESS=your_kafka_address
```

- Cài đặt Docker:
```bash
sudo chmod +x setup_docker.sh
./setup_docker.sh
newgrp docker
```

- Chạy Docker:
```bash
cd kafka
docker-compose up -d
```

- Kiểm tra trạng thái của các container:
```bash
docker ps
```

- Truy cập vào trang web control center của Kafka:
```
http://<Public IPv4 address>:9021
```

