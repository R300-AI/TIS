# TIS

## Requirement
* **OS**: Ubuntu

## Pre-built Resources
* [Camera Driver for Arm64 CPU](https://yjec.blob.core.windows.net/download/tiscamera_1.1.0.4139_arm64_ubuntu_1804.deb)
* [Camera Driver for for x86_64 CPU](https://yjec.blob.core.windows.net/download/tiscamera_1.1.0.4139_amd64_ubuntu_1804.deb)

## Installation
#### Step1. Install Gstreamer with the following command or the method specified by the system.
  ```bash
  git clone https://github.com/R300-AI/TIS.git && cd TIS
  bash build.sh && cd ..
  ```

#### Step2. Download Tcam-capture and add library to `~/.bashrc`.
  ```bash
  sudo dpkg -i <tiscamera_driver>.deb

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
