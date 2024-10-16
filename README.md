# TIS

## Requirement
* **OS**: Ubuntu

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
