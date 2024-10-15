# TIS

## Installation
### Step1. Install Gstreamer with the following command or the method specified by the system.
  ```bash
  sudo apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio
  sudo apt install libcairo2-dev libxt-dev libgirepository1.0-dev
  ```

### Step2. Download Tcam-capture from [HERE](https://www.theimagingsource.com/zh-hant-tw/product/software/tiscamera/) and install it.
  ```bash
  sudo dpkg -i <tiscamera_driver>.deb
  ```

### Step4. Add this path to `~/.bashrc`
  ```bash
  sudo vim ~/.bashrc    # Add this to last line: export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libffi.so.8
  source ~/.bashrc
  ```

### Step5. Verify the connection and adjusting the camera configuration
  ```
  tcam-capture
  ```
