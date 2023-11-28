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

## Basic

- UART

- connect as follows
```bash
minicom -D /dev/ttyUSB0 -b 115200
```
