# fedberry-config
A utility for making common FedBerry configuration changes via a simple menu-driven interface or via command line switches. The majority of the configuration changes result in automated modifications to `/boot/config.txt`, `/boot/cmdline.txt` and/or other standard Fedora configuration files. Many options will require a reboot to take effect.

## Main Features:
* Enable / Disable Device Tree overlays
* Enable / Disable Device Tree parameters
* Enable / Disable hardware support / drivers including:
  * Mesa VC4 driver(s)
  * RPi Camera driver
  * Linux Infrared Remote Control (LIRC) support
  * Realtime Clock (RTC) support
  * Bluetooth support for RPi3
  * Sigma-Delta audio driver
* Expand (grow) root filesystem on SD card
* Select which kernel you want to use at boot 
* Add and enable swap files
* Set SELinux modes (enforcing, permissive, disabled)
* Enable / Disable plymouth graphical boot splash
* Show current system information

## Screen Shots
### Main Menu
![main_menu](https://cloud.githubusercontent.com/assets/16171842/26089234/b4f1b0a2-3a2e-11e7-8561-ba7f71e26d5a.png "Main Menu")

### Drivers Menu
![drivers_menu](https://cloud.githubusercontent.com/assets/16171842/26089288/1ce2f464-3a2f-11e7-80df-a5ad5f72389b.png "Drivers Menu")

### Command Line Options
![cmdline](https://cloud.githubusercontent.com/assets/16171842/26089163/26b20832-3a2e-11e7-8817-6099943bb2aa.png "Command Line Options")
