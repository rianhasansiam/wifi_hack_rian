#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WPS PIN Recovery Tool - Installer Script
Author: Rian Hasan Siam
GitHub: rianhasansiam/wifi_hack_rian
"""

import os
import sys
import subprocess

def print_banner():
    """Display installation banner"""
    banner = '''
\033[1;36;40m╔═══════════════════════════════════════════════════════╗
║     WPS PIN Recovery Tool - Installer v1.0          ║
║     Developed by: Rian Hasan Siam                   ║
║     GitHub: rianhasansiam/wifi_hack_rian            ║
╚═══════════════════════════════════════════════════════╝\033[0m

\033[1;93m⚠️  Requirements:\033[0m
  • Rooted Android device with Termux OR Linux system
  • Active internet connection
  • Sufficient storage space

\033[1;92m[*] Starting installation...\033[0m
'''
    print(banner)

def run_command(cmd, description):
    """Execute shell command with error handling"""
    print(f"\n\033[1;36m[*] {description}...\033[0m")
    try:
        result = subprocess.run(cmd, shell=True, check=True, 
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                              text=True)
        print(f"\033[1;92m[✓] {description} completed successfully\033[0m")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\033[1;91m[✗] Failed: {description}\033[0m")
        print(f"Error: {e.stderr}")
        return False

def check_root():
    """Check if running with root privileges"""
    try:
        # Check if 'tsu' command exists (Termux root)
        result = subprocess.run("which tsu", shell=True, capture_output=True)
        if result.returncode == 0:
            return True
        # Check if running as root
        result = subprocess.run("id -u", shell=True, capture_output=True, text=True)
        return result.stdout.strip() == "0"
    except Exception:
        return False

def main():
    """Main installation function"""
    print_banner()
    
    # Check Python version
    if sys.version_info < (3, 6):
        print("\033[1;91m[✗] Error: Python 3.6 or higher is required\033[0m")
        sys.exit(1)
    
    # Inform about root requirement
    if not check_root():
        print("\033[1;93m[!] Warning: Root access not detected")
        print("    Some features may require root privileges (tsu/sudo)\033[0m")
    
    # Update package manager
    if not run_command("pkg update -y && pkg upgrade -y", "Updating packages"):
        print("\033[1;93m[!] Warning: Package update failed, continuing anyway...\033[0m")
    
    # Install root repository
    run_command("pkg install -y root-repo", "Installing root repository")
    
    # Install core dependencies
    packages = ["git", "tsu", "python", "wpa-supplicant", "pixiewps", "iw"]
    pkg_list = " ".join(packages)
    
    if not run_command(f"pkg install -y {pkg_list}", "Installing dependencies"):
        print("\033[1;91m[✗] Critical: Failed to install required packages\033[0m")
        sys.exit(1)
    
    # Clone repository
    print("\n\033[1;36m[*] Cloning repository...\033[0m")
    repo_exists = os.path.exists("../Wifi_Hack")
    
    if repo_exists:
        print("\033[1;93m[!] Repository directory already exists\033[0m")
        response = input("    Remove and re-clone? [y/N]: ").strip().lower()
        if response == 'y':
            run_command("rm -rf ../Wifi_Hack", "Removing old repository")
            repo_exists = False
    
    if not repo_exists:
        if not run_command("cd .. && git clone https://github.com/rianhasansiam/wifi_hack_rian Wifi_Hack", 
                          "Cloning repository"):
            print("\033[1;91m[✗] Failed to clone repository\033[0m")
            sys.exit(1)
    
    # Set executable permissions
    run_command("cd ../Wifi_Hack && chmod +x rianHack.py", "Setting permissions")
    
    # Installation complete
    print('''
\033[1;92m╔═══════════════════════════════════════════════════════╗
║           Installation Completed Successfully!        ║
╚═══════════════════════════════════════════════════════╝\033[0m

\033[1;36mUsage Instructions:\033[0m
  1. Navigate to home directory: \033[1;93mcd ~\033[0m
  2. Run the tool: \033[1;93msudo python Wifi_Hack/rianHack.py -i wlan0 -K\033[0m
  3. For help: \033[1;93mpython Wifi_Hack/rianHack.py --help\033[0m

\033[1;36mQuick Commands:\033[0m
  • Scan networks:     \033[1;93msudo python Wifi_Hack/rianHack.py -i wlan0 -K\033[0m
  • Target specific:   \033[1;93msudo python Wifi_Hack/rianHack.py -i wlan0 -b <BSSID> -K\033[0m
  • Brute force:       \033[1;93msudo python Wifi_Hack/rianHack.py -i wlan0 -b <BSSID> -B\033[0m

\033[1;93m⚠️  Remember: Only test on networks you own or have permission to test!\033[0m

\033[1;92mThank you for using WPS PIN Recovery Tool!\033[0m
GitHub: \033[1;94mhttps://github.com/rianhasansiam/wifi_hack_rian\033[0m
''')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n\033[1;91m[!] Installation cancelled by user\033[0m")
        sys.exit(1)
    except Exception as e:
        print(f"\n\033[1;91m[✗] Unexpected error: {e}\033[0m")
        sys.exit(1)
