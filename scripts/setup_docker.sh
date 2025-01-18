#!/bin/bash

# Update hệ thống
sudo apt update

# Cài đặt Docker
sudo apt install docker.io -y

# Khởi động và kích hoạt Docker
sudo systemctl start docker
sudo systemctl enable docker

# Thêm user hiện tại vào group Docker
sudo usermod -aG docker $USER

# Cài đặt Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Kiểm tra phiên bản Docker Compose
docker-compose --version

echo "Setup hoàn tất. Bạn có thể cần logout và login lại để sử dụng Docker mà không cần sudo."
