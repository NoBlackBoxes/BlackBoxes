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
output_device = 1
num_input_channels = 1
num_output_channels = 1
sample_rate = 48000
buffer_size = int(sample_rate / 100)
max_samples = int(sample_rate * 10)

# List available sound devices
sound.list_devices()

# Initialize microphone
microphone = sound.microphone(input_device, num_input_channels, sample_rate, buffer_size, max_samples)
microphone.start()

# Initialize speaker
speaker = sound.speaker(output_device, num_output_channels, sample_rate, buffer_size)
speaker.start()

# Clear error ALSA/JACK messages from terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Live input/output (FEEDBACK!)
for i in range(1000):
    latest = microphone.latest(buffer_size)
    speaker.write(latest)
    time.sleep(0.01)

# Shutdown microphone
microphone.stop()

# Shutdown speaker
speaker.stop()


# FIN