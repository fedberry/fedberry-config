# fedberry-config
A utility for making common FedBerry configuration changes via a simple menu-driven interface or via command line switches. The majority of the configuration changes result in automated modifications to `/boot/config.txt`, `/boot/cmdline.txt` and/or other standard Fedora configuration files. Many options will require a reboot to take effect.

## Main Features:
* Configure Device Tree Overlays / Parameters
* Configure various system options & devices including:
  * Mesa VC4 driver
  * Sigma-Delta on-board audio driver
  * Various 3rd party audio drivers
  * RPi Camera driver
  * Linux Infrared Remote Control (LIRC) support
  * Realtime Clock (RTC) support
  * RPi3 Bluetooth & Wifi support
  * Sigma-Delta audio driver
  * GPU memory allocation support
  * Console framebuffer depth support
* Expand (grow) root filesystem on SD card
* Select kernel version to use for booting 
* Add and enable swap files
* Set SELinux modes
* Enable / Disable plymouth graphical boot splash
* Enable overclocking support for RPi2

## Screen Shots
### Main Menu
![main_menu](https://cloud.githubusercontent.com/assets/16171842/26089234/b4f1b0a2-3a2e-11e7-8561-ba7f71e26d5a.png "Main Menu")

### Drivers Menu
![drivers_menu](https://cloud.githubusercontent.com/assets/16171842/26089288/1ce2f464-3a2f-11e7-80df-a5ad5f72389b.png "Drivers Menu")

### Command Line Options
![cmdline](https://cloud.githubusercontent.com/assets/16171842/26089163/26b20832-3a2e-11e7-8817-6099943bb2aa.png "Command Line Options")
