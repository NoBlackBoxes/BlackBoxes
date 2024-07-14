# Systems : Connecting

Strategies for connecting to a (remote) system.

## General Approach

In order to talk to another computer, we must be able to find it on our network. The following requirements must be met:

1. The *remote* computer (e.g. your NB3's Raspberry Pi) must be connected to your local area network (LAN)
2. Your *host* computer (your development laptop/desktop) must be connected to the same network
3. The remote computer must **ALLOW** external connections (e.g. enable an SSH server)
4. You must know the remote computer's **IP address** (or, in some cases, just the "hostname")

We will address each of these required steps below.

### NB3: Raspberry Pi

The following assumes you have used the [RPi Imager](https://www.raspberrypi.com/software/) to create an SD card containing the Raspbery Pi Operating System (RPiOS) ***AND*** configured a hostname, user account (with password), WiFi network name+passkey+country (if available), and **enabled SSH** to use password login. If you have not done so, then please follow the instructions [here](../rpios/README.md)!

#### 1. Connecting the NB3 to your LAN

- Wired Connection: If you have access to your router and an ethernet cable, then simply connect the cable between your router's spare jacks and the NB3's jack. A new device will automatically appear on your network with an assigned IP address.

- Wireless (WiFi) Connection (own router):