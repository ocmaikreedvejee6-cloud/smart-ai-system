#!/bin/bash

echo "Updating system..."
sudo apt update

echo "Installing OpenCV..."
sudo apt install python3-opencv -y

echo "Creating virtual environment..."
python3 -m venv venv --system-site-packages

source venv/bin/activate

echo "Installing Python packages..."
pip install --upgrade pip
pip install ultralytics --no-deps --no-cache-dir
pip install numpy pillow pyyaml requests

echo "Running system..."
python main.py
