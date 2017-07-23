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
![main_menu](https://user-images.githubusercontent.com/16171842/28496645-5568ede4-6fa3-11e7-9f1e-bec1445c2388.png "Main Menu")

### Command Line Options
![cmdline](https://user-images.githubusercontent.com/16171842/28496652-64153dca-6fa3-11e7-92e8-a72d5e49f7ec.png "Command Line Options")
