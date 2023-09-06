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
wav_path = box_path + '/_data/sounds/Bach_prelude_C_major.wav'

# Specify params
output_device = 20
num_channels = 2
sample_rate = 44100
buffer_size = int(sample_rate / 10)
max_samples = int(sample_rate * 10)

# List available sound devices
sound.list_devices()

# Initialize speaker
speaker = sound.speaker(output_device, num_channels, sample_rate, buffer_size)
speaker.start()

# Play WAV file
speaker.play_wav(wav_path)

# Wait for finish
while speaker.is_playing():
    time.sleep(0.01)

# Shutdown speaker
speaker.stop()

#FIN