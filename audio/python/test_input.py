import os
import time
import numpy as np

# Locals libs
import NBB_sound as sound

# Reimport
import importlib
importlib.reload(sound)

# Get user name
username = os.getlogin()

# Specify paths
repo_path = '/home/' + username + '/NoBlackBoxes/LastBlackBox'
box_path = repo_path + '/boxes/audio'
wav_path = box_path + '/_tmp/test.wav'

# Specify params
input_device = 1
num_channels = 2
sample_rate = 48000
buffer_size = int(sample_rate / 10)
max_samples = int(sample_rate * 10)

# List available sound devices
sound.list_devices()

# Initialize microphone
microphone = sound.microphone(input_device, num_channels, sample_rate, buffer_size, max_samples)
microphone.start()

# Clear error ALSA/JACK messages from terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Wait to save recording
input("Press Enter to save recording...")

# Save recording
microphone.save_wav(wav_path, sample_rate*3)

# Live processing
for i in range(10):
    latest = microphone.latest(buffer_size)
    print("{0:.2f}".format(np.mean(np.abs(latest[:,0]))))
    time.sleep(0.1)

# Shutdown microphone
microphone.stop()

# FIN