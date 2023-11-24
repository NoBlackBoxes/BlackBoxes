# audio : i2s : driver_MAX98357A

***Important***: This driver installation only applies to *Revision 2* NB3_Mouth boards.

### Change OS Configuration 

The Raspberry Pi does not enable i2s by default. You can enable it by opening the file called "config.txt" in the /"boot" folder of your Raspberry Pi and changing a single line.

We also need to enable a driver for the NB£ Mouth board. The board uses an I2S codec + amplifier chip called the MAX98357A and driver is included in Linux. We only need to tell the OS that we want to use this driver by adding a "sevice tree overlay". This will require adding one more line to the configuration text file.

```bash
sudo nano /boot/config.txt
```

Then use the text editor to change and add the following lines:

```txt
#dtparam=i2s=on
```
...becomes

```txt
dtparam=i2s=on
dtoverlay=max98357a,sdmode-pin=16
```

### ADD DETAILS ABOUT BUILDING THE DRIVER! (?)


***After this, power down your NB3 and complete the hardware installation.***

## Testing

If the driver (module) is installed and loaded, then you should be able to record audio. Check that a device is available:

```bash
arecord -l
```

Should output something like this...

```txt
**** List of CAPTURE Hardware Devices ****
card 1: NB3audiocard [NB3_audio_card], device 0: simple-card_codec_link snd-soc-dummy-dai-0 [simple-card_codec_link snd-soc-dummy-dai-0]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```

To make a test recording.

```bash
arecord -D plughw:1 -c2 -r 48000 -f S32_LE -t wav -V stereo -v file_stereo.wav
```

To test playback.

```bash
aplay -D plughw:1 -c2 -r 48000 -f S32_LE -t wav -V stereo -v file_stereo.wav
```