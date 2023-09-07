# Audio : i2s : python

```bash
pip install --upgrade pip setuptools wheel
sudo apt install python3-dev build-essential
sudo apt install portaudio19-dev # required for 64-bit pyaudio build
pip install pyaudio
```

## Profiling

Input callback, 48000 rate, 4800 buffer, int16/PC, 1 channel, Float32 internal conversion, local buffers: 1:  0.00012125495735925573, 2: 9.963364727729189e-05

Input callback, 48000 rate, 4800 buffer, int16/PC, 1 channel, Float32 internal conversion, gloabl buffers: 1: 0.00011000594472497459, 2: 0.00010834503173828125

Input callback, 44100 rate, 4410 buffer, int16/PC, 2 channel, Float32 internal conversion, gloabl buffers: 1: 5.742907524108887e-05
