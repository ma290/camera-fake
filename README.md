# Cam Emulator

Cam Emulator is a Python-based virtual camera application that streams video files to a virtual camera device. It allows users to select a video, play it, and broadcast it via a virtual webcam.

## Features
- Stream video files to a virtual camera.
- Easy-to-use graphical user interface (GUI).
- Integrated donation option with UPI ID: `credmemishra@fam`.
- Creator information with a link to the GitHub profile.

---

## Prerequisites

Make sure the following are installed:

- Python 3.7 or later
- `pip` (Python package manager)

---

## Installation Guide

### Step 1: Clone the Repository
```bash
git clone https://github.com/ma290/cam-emulator.git
cd cam-emulator
```

### Step 2: Create a Virtual Environment
#### On **Windows**:
```bash
python -m venv venv
venv\Scripts\activate
```

#### On **Kali Linux**:
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Step 3: Install Dependencies
Install all required Python packages from `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

## Running the Application

Run the application with:
```bash
python main.py
```

---

## Virtual Camera Setup

The script uses `pyvirtualcam`, which requires a virtual camera driver. Ensure a virtual camera is set up as follows:

#### On **Windows**:
- Install a virtual webcam driver if not already available (e.g., pre-installed drivers or OBS Virtual Camera).

#### On **Kali Linux**:
1. Install the `v4l2loopback` kernel module:
   ```bash
   sudo apt install v4l2loopback-dkms
   sudo modprobe v4l2loopback devices=1
   ```
2. Verify the virtual camera device is active:
   ```bash
   ls /dev/video*
   ```

---

## Features in Detail

- **Donate to Support**:
  - Access the "Donate" option from the GUI to support the creator via UPI:
    ```
    UPI ID: credmemishra@fam
    ```

- **About the Creator**:
  - Learn about the creator and access their GitHub profile:
    [GitHub Profile](https://github.com/ma290)

---

## License
This project is open-source and available under the MIT License.

---

## Contact
- **Creator**: [@ma290](https://github.com/ma290)
