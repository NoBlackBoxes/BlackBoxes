# systems : NBBOS

A no black box operating system (for the Rapsberry Pi 4b)

Based on work here: https://github.com/isometimes/rpi4-osdev/tree/master

## Prerequsites

- Download cross-compile toolchain: https://developer.arm.com/downloads/-/gnu-a
- Extract it to a temporary folder within the LBB repo (boxes/systems/NBBOS) tree

```bash
mkdir _tmp
cd _tmp
tar -xhf gcc-arm*
```

- Clone and build usbboot (to write to eMMC on CM4)
```bash
git clone --depth=1 https://github.com/raspberrypi/usbboot
cd usbboot
make
```

- Use rpiboot to mount boot partition and copy a new kernel image

## Basic

- UART

- connect as follows
```bash
minicom -D /dev/ttyUSB0 -b 115200
```
