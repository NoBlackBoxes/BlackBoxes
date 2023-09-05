import os

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

# List available sound devices
sound.list_devices()

# Initialize microphone thread
microphone = sound.microphone(4, 2, 44100, 4410, 441000)
microphone.start()

# Wait to start recording
input("Press Enter to save recording...")

# Start recording
microphone.save_wav(wav_path, 44100*3)

# Shutdown microphone
microphone.stop()

# FIN