cyanberry-config
===============

A utility based on [fedberry-config](https://github.com/fedberry/fedberry-config/)
for making common Raspberry Pi configuration changes via a simple
menu-driven interface. The majority of the configuration changes result in
automated modifications to `/boot/config.txt` and/or other standard
AOSC OS configuration files. Many options will require a reboot to take effect.

Dependencies
------------

While being noted as an AOSC OS tool, `cyanberry-config` really isn't
distro-specific to AOSC OS. As long as you are able to obtain the following
for your distro (on an ARM device), you are good to go:

- BlueZ (bluetooth stack for Linux)
- Newt (providing the whiptail command)
- Systemd (whole-sale inclusion of util-linux and everything below...)
- pv (for progress reporting)
