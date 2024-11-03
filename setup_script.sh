#!/bin/bash
# Use bash instead of sh

set -e  # Exit immediately if any command fails
CURRENT=$(pwd)

echo "Starting script execution..."

# Check CUDA_VERSION
echo "Checking CUDA version..."
export CUDA_VERSION=$(nvcc --version | grep -Po "(\d+\.)+\d+" | head -1) || { echo "Failed to check CUDA version"; exit 1; }
echo "CUDA Version: $CUDA_VERSION"

# Update system and install dependencies
echo "Updating package lists..."
sudo apt-get update || { echo "Failed at: sudo apt-get update"; exit 1; }

echo "Installing system dependencies..."
sudo apt-get install -y --allow-downgrades --allow-change-held-packages --no-install-recommends \
    build-essential \
    git \
    curl \
    vim \
    tmux \
    wget \
    bzip2 \
    unzip \
    g++ \
    ca-certificates \
    ffmpeg \
    libx264-dev \
    imagemagick || { echo "Failed to install system dependencies"; exit 1; }

echo "System dependencies installed successfully."

# Check if pip is available
echo "Checking for pip installation..."
PIP_PATH=$(which pip3)
if [ -z "$PIP_PATH" ]; then
    echo "Error: pip3 is not installed or not found in PATH"
    exit 1
else
    echo "Pip found at: $PIP_PATH"
fi

# Install Python dependencies and check versions
echo "Installing Python dependencies individually and checking versions..."

packages=(
    "cmake"
    "pynvml"
    "Pillow>=8.3.2"
    "scipy>=1.7.0"
    "scikit-image"
    "tqdm>=4.62.0"
    "wget"
    "cython"
    "lmdb"
    "av"
    "opencv-python"
    "opencv-contrib-python"
    "imutils"
    "imageio-ffmpeg"
    "qimage2ndarray"
    "albumentations"
    "requests>=2.26.0"
    "nvidia-ml-py3==7.352.0"
    "pyglet"
    "timm"
    "diskcache"
    "rsa==4.8"
    "boto3"
    "awscli_plugin_endpoint"
    "awscli"
    "wandb"
    "tensorboard"
    "lpips"
    "face-alignment"
    "dlib"
    "clean-fid"
)

# Loop through each package for installation and version check
for package in "${packages[@]}"; do
    echo "Installing $package..."
    $PIP_PATH install --upgrade "$package" || { echo "Error: Failed to install $package"; exit 1; }
    echo "Checking version for $package..."
    $PIP_PATH show "${package%%==*}" | grep Version || echo "Version check failed for $package"
    echo "$package installed and checked successfully."
done

echo "All Python dependencies installed successfully."
