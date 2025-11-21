# Wifi_Hack

A powerful WPS (Wi-Fi Protected Setup) penetration testing tool for security research and network auditing. This tool helps security professionals test the vulnerability of WPS-enabled routers using Pixie Dust attacks and online brute-force methods.

**Author:** Rian Hasan Siam  
**Contact:** [rianhasansiam](https://rianhasansiam.me)



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
- Rooted Android device with Termux **OR** Linux system (Kali Linux, Ubuntu, etc.)
- Compatible wireless adapter supporting monitor mode and packet injection

### Software
- Python 3.6 or higher
- Root access (`su`, `tsu`, or `sudo`)
- Required packages: `wpa-supplicant`, `pixiewps`, `iw`

## 🚀 Installation

### Method 1: Environment Installation

This method automatically installs all required dependencies and sets up the tool.

```bash
# Update packages
pkg update && pkg upgrade -y

# Install basic dependencies
pkg install -y git python

# Clone the repository
git clone https://github.com/rianhasansiam/wifi_hack_rian.git
cd wifi_hack_rian

# Run automated installer
python rianIntaller.py
```

### Step 1: Hack Setup

If you prefer manual installation or the automated installer fails:

```bash
# Update system
pkg update && pkg upgrade -y

# Install root repository
pkg install -y root-repo

# Install all dependencies
pkg install -y git tsu python wpa-supplicant pixiewps iw

# Set permissions
chmod +x rianHack.py

# Verify installation
sudo python rianHack.py --help
```

### Troubleshooting Installation

If you encounter issues:

1. **Permission Denied:** Ensure you have root access with `tsu` or `sudo`
2. **Package Not Found:** Try `pkg update` again or check your internet connection
3. **Python Version:** Verify you have Python 3.6+ with `python --version`
4. **Wireless Interface:** Check your interface name with `ip link show` or `ifconfig`

## 📖 Usage

### Basic Commands

**Quick scan and attack (recommended for beginners):**
```bash
cd ~
sudo python Wifi_Hack/rianHack.py -i wlan0 -K
```

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

**Save results to file:**
```bash
sudo python rianHack.py -i wlan0 -K -w
```

**Run in loop mode:**
```bash
sudo python rianHack.py -i wlan0 -K -l
```

### Command Line Options

```
Required:
  -i, --interface    Wireless interface name (e.g., wlan0, wlan1)


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

## 🛡️ Supported Vendors & Features

### PIN Generation Algorithms (30+)
- **D-Link**: Custom PIN algorithms for various models
- **ASUS**: Vendor-specific PIN generation
- **TP-Link**: Archer series and legacy models
- **Broadcom**: Multiple algorithm variants
- **Realtek**: Common chipset support
- **Cisco, Netgear, Linksys**: Static PINs and custom algorithms
- **And many more...**


## 🔬 Advanced Usage

### Pixie Dust with Force Mode
For stubborn targets that partially succeed:
```bash
sudo python rianHack.py -i wlan0 -b XX:XX:XX:XX:XX:XX -K -F
```

### Brute Force with Custom Delay
Avoid rate limiting:
```bash
sudo python rianHack.py -i wlan0 -b XX:XX:XX:XX:XX:XX -B -d 1.5
```

### Resume Interrupted Session
Sessions are automatically saved. Just run the same command again:
```bash
sudo python rianHack.py -i wlan0 -b XX:XX:XX:XX:XX:XX -B
# Will prompt to resume previous session
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Report Bugs**: Open an issue with detailed information
2. **Suggest Features**: Share your ideas for improvements
3. **Submit Pull Requests**: Fix bugs or add new features
4. **Update Vulnerability List**: Add newly discovered vulnerable models

## 📜 License

This project is licensed for educational and authorized testing purposes only. See the [Legal Disclaimer](#️-legal-disclaimer) section.

## 📞 Contact & Support

- **GitHub Issues**: [Report bugs or request features](https://github.com/rianhasansiam/wifi_hack_rian/issues)
- **Author**: Rian Hasan Siam
- **Repository**: [github.com/rianhasansiam/wifi_hack_rian](https://github.com/rianhasansiam/wifi_hack_rian)

## 🙏 Acknowledgments

This tool builds upon the excellent work of the security research community:
- Original OneShotPin concept and implementation
- WPS vulnerability research
- Open-source security tools community

## ⭐ Star History

If you find this tool useful, please consider giving it a star on GitHub!

---

**Version**: 1.0  
**Last Updated**: 2025  
**Status**: Active Development

Remember: **Always obtain proper authorization before testing any network!**

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
