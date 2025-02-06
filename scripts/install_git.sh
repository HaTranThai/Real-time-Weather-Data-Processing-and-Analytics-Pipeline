#!/bin/bash

# Cập nhật danh sách gói và nâng cấp hệ thống
sudo apt update && sudo apt upgrade -y

# Cài đặt Git
sudo apt install git -y

# Kiểm tra phiên bản Git đã cài đặt
git --version

# Cấu hình thông tin người dùng cho Git (tùy chọn)
echo "Nhập tên người dùng Git:"
read git_name
git config --global user.name "$git_name"

echo "Nhập email Git:"
read git_email
git config --global user.email "$git_email"

# Kiểm tra cấu hình Git
git config --list

echo "Cài đặt Git thành công!"

sudo apt update

sudo apt install subversion -y


