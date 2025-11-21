# Wifi_Hack

A powerful WPS (Wi-Fi Protected Setup) penetration testing tool for security research and network auditing. This tool helps security professionals test the vulnerability of WPS-enabled routers using Pixie Dust attacks and online brute-force methods.



## ⚠️ Legal Disclaimer

**FOR EDUCATIONAL AND AUTHORIZED TESTING PURPOSES ONLY**

This tool is designed for security research and penetration testing on networks you own or have explicit written permission to test. Unauthorized access to computer networks is illegal and punishable by law. The developers assume no liability and are not responsible for any misuse or damage caused by this program.

## ✨ Features

- 🎯 **Pixie Dust Attack** - Exploits weak WPS implementations
- 🔓 **Smart Brute Force** - Intelligent PIN guessing with session management
- 📡 **Network Scanner** - Detects WPS-enabled networks with vulnerability indicators
- 🔐 **30+ PIN Algorithms** - Supports vendor-specific PIN generation (D-Link, ASUS, TP-Link, etc.)
- 💾 **Session Recovery** - Resume interrupted brute-force attacks
- 📊 **Result Storage** - Saves credentials in CSV/TXT format
- 🔍 **Vulnerability Database** - Built-in list of 142+ vulnerable router models

## 📋 Requirements

### Hardware
- Rooted Android device with Termux **OR** Linux system
- Compatible wireless adapter supporting monitor mode

### Software
- Python 3.6 or higher
- Root access (`su` or `tsu`)
- Required packages: `wpa-supplicant`, `pixiewps`, `iw`

## 🚀 Installation

### Step 1: Automated Installation All Needed files

```bash
# Update packages
pkg update && pkg upgrade

# Install basic dependencies
pkg install git python

# Clone the installer
git clone https://github.com/rianhasansiam/wifi_hack_rian.git
cd wifi_hack_rian

# Run installer
python rianIntaller.py
```

### step 2: Now Start main step

```bash
# Update system
apt update && apt upgrade

# Install root repository
pkg install -y root-repo

# Install all dependencies
pkg install -y git tsu python wpa-supplicant pixiewps iw

# Set permissions
chmod +x rianHack.py

# Verify installation
sudo python rianHack.py --help
```

## 📖 Usage

### After Installation Use this Basic Commands which one you need...

**Scan networks and launch Pixie Dust attack:**
```bash
sudo python rianHack.py -i wlan0 -K
```

**Attack specific BSSID with Pixie Dust:**
```bash
sudo python rianHack.py -i wlan0 -b 00:91:4C:C3:AC:28 -K
```

**Online brute-force attack:**
```bash
sudo python rianHack.py -i wlan0 -b 00:90:4C:C1:AC:21 -B
```

**Brute-force with known first half of PIN:**
```bash
sudo python rianHack.py -i wlan0 -b 00:90:4C:C1:AC:21 -B -p 1234
```

**Test specific PIN:**
```bash
sudo python rianHack.py -i wlan0 -b 00:90:4C:C1:AC:21 -p 12345670
```

## 🔧 Troubleshooting

### Common Issues

**"Device or resource busy (-16)"**
```bash
# Solution: Toggle WiFi
# 1. Turn WiFi ON
# 2. Turn WiFi OFF
# 3. Run the script again
```

**"wpa_supplicant: command not found"**
```bash
pkg install -y wpa-supplicant
```

**"Permission denied"**
```bash
# Ensure you have root access
su
# OR
tsu
```

**Interface not found**
```bash
# List available interfaces
ip link show
# OR
iw dev
```


## 🎯 Attack Modes Explained

### Pixie Dust Attack (`-K`)
- **Speed**: Fast (seconds to minutes)
- **Success Rate**: High on vulnerable devices
- **Method**: Exploits weak random number generation in WPS
- **Best For**: Quick testing of known vulnerable routers

### Brute Force Attack (`-B`)
- **Speed**: Slow (hours to days)
- **Success Rate**: Depends on rate limiting
- **Method**: Systematically tries all possible PINs
- **Best For**: Targets without Pixie Dust vulnerability

## 🛡️ Supported Vendors

The tool includes PIN generation algorithms for:
- TP-Link
- D-Link
- ASUS
- Netgear
- Belkin
- Cisco
- Broadcom
- Realtek
- Huawei
- Edimax
- And many more...



## 📜 License

This project is open source and available for educational purposes.


**Note**: Always turn OFF your WiFi before running the script to avoid interface conflicts.
