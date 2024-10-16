# TIS

## Compatible System
* **OS**: Ubuntu/ Raspbian

## Pre-built Resources
* [Camera Driver for Arm64 CPU](https://itriaihub.blob.core.windows.net/github-download-resources/repository/TIS/tiscamera_1.1.0.4139_arm64_ubuntu_1804.deb)
* [Camera Driver for for x86_64 CPU](https://itriaihub.blob.core.windows.net/github-download-resources/repository/TIS/tiscamera_1.1.0.4139_amd64_ubuntu_1804.deb)

## Installation
#### Step1. Download the camera driver and install it.
  ```bash
  git clone https://github.com/R300-AI/TIS.git && cd TIS
  bash build.sh && cd ..
  sudo dpkg -i <tiscamera_driver>.deb
  ```

#### Step2. Add library to `~/.bashrc`.
  ```bash
  sudo vim ~/.bashrc    # Add this to last line: export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libffi.so.8
  source ~/.bashrc
  ```

#### Step3. Verify the connection and adjusting the camera configuration
  ```
  tcam-capture
  ```

## Usage
```
python demo.py
```
