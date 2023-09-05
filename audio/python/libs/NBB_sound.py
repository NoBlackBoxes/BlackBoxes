import numpy as np
import pyaudio
import wave

#
# Utilities
#
def list_devices():
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')

    print("\n\nInput Devices\n-----------------\n")
    for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            print(" - Devices id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))
    print("\nOutput Devices\n-----------------\n")
    for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxOutputChannels')) > 0:
            print(" - Devices id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))
    p.terminate()
    print("-----------------\n\n")
    return

#
# Sound thread (microphone)
#
class microphone:
    def __init__(self, device, num_channels, sample_rate, buffer_size_samples, max_samples):        
        self.num_channels = num_channels
        self.sample_rate = sample_rate
        self.format = pyaudio.paInt16
        self.buffer_size_samples = buffer_size_samples
        self.max_samples = max_samples
        self.valid_samples = 0

        # Create rolling buffer (assumes 16-bit signed int samples)
        self.sound = np.zeros((self.max_samples, self.num_channels), dtype=np.int16)

        # Configure callback
        def callback(input_data, frame_count, time_info, status):
            output_data= np.zeros((0))

            # Seperate channel data
            channel_data = np.reshape(np.frombuffer(input_data, dtype=np.int16).transpose(), (-1,self.num_channels))

            # Fill buffer...and then concat
            if self.valid_samples < self.max_samples:
                self.sound[self.valid_samples:(self.valid_samples + self.buffer_size_samples), :] = channel_data
                self.valid_samples = self.valid_samples + self.buffer_size_samples
            else:
                self.sound = np.vstack([self.sound[self.buffer_size_samples:, :], channel_data])
                self.valid_samples = self.max_samples

            # Debug
            #print(np.mean(np.abs(channel_data), 0))

            return (output_data, pyaudio.paContinue)

        # Get pyaudio object
        self.pya = pyaudio.PyAudio()

        # Open audio input stream
        self.stream = self.pya.open(input_device_index=device, format=self.format, channels=num_channels, rate=sample_rate, input=True, output=False, frames_per_buffer=buffer_size_samples, start=False, stream_callback=callback)
        
    # Start streaming
    def start(self):
        self.stream.start_stream()

    # Stop streaming
    def stop(self):
        self.stream.stop_stream()
        self.stream.close()
        self.pya.terminate()

    # Reset sound input
    def reset(self):
        self.sound = np.zeros((self.max_samples, self.num_channels), dtype=np.int16)
        self.valid_samples = 0
        return

    # Start saving WAV
    def save_wav(self, wav_path, wav_max_samples):

        # Prepare WAV file
        wav_file = wave.open(wav_path, 'wb')
        wav_file.setnchannels(self.num_channels)
        wav_file.setsampwidth(2)
        wav_file.setframerate(self.sample_rate)

        # Determine WAV range (in samples)
        if wav_max_samples < self.valid_samples:
            wav_start_sample = self.valid_samples - wav_max_samples
            wav_stop_sample = self.valid_samples
        else:
            wav_start_sample = 0
            wav_stop_sample = self.valid_samples

        # Convert sound to frame data
        frames = np.reshape(self.sound[wav_start_sample:wav_stop_sample,:], -1)

        # Write to WAV
        wav_file.writeframes(frames)

        # Close WAV file
        wav_file.close()

        return

#
# Sound output thread (speaker)
#
class speaker:
    def __init__(self, device, num_channels, sample_rate, buffer_size_samples):        
        self.num_channels = num_channels
        self.sample_rate = sample_rate
        self.format = pyaudio.paInt16
        self.buffer_size_samples = buffer_size_samples
        self.current_sample = 0
        self.max_samples = 0

        # Create empty sound buffer
        self.empty = np.zeros((self.buffer_size_samples, self.num_channels), dtype=np.int16)
        self.sound = np.zeros((self.max_samples, self.num_channels), dtype=np.int16)

        # Configure callback
        def callback(input_data, frame_count, time_info, status):

            # Extract sound or silence from buffer and play frame_counts worth

            # Debug
            #print(np.mean(np.abs(channel_data), 0))

            return (output_data, pyaudio.paContinue)

        # Get pyaudio object
        self.pya = pyaudio.PyAudio()

        # Open audio output stream (from default device)
        self.stream = self.pya.open(output_device_index=device, format=self.format, channels=num_channels, rate=sample_rate, input=False, output=True, frames_per_buffer=buffer_size_samples, start=False, stream_callback=self.callback)
        
    # Start streaming
    def start(self):
        self.stream.start_stream()

    # Stop streaming
    def stop(self):
        self.stream.stop_stream()
        self.stream.close()
        self.pya.terminate()

    # Update thread method
    def update(self):
        empty_buffer = np.zeros((self.buffer_size_samples, self.num_channels), dtype=np.int16)
        while True :
            # End?
            if self.streaming is False :
                break
            
            # Playing?
            if self.current_sample < self.max_samples:
                # Write sound data buffer
                channel_data = np.copy(self.sound[self.current_sample:(self.current_sample + self.buffer_size_samples), :])
                raw_data = channel_data.flatten('C')
                self.stream.write(raw_data, self.buffer_size_samples, exception_on_underflow=False)

                # Increment buffer position
                self.current_sample = self.current_sample + self.buffer_size_samples
            else:
                self.stream.write(empty_buffer, self.buffer_size_samples, exception_on_underflow=False)
        
        # Shutdown thread
        self.stream.stop_stream()
        self.stream.close()
        self.pya.terminate()

    # Write sound method
    def write(self, sound):
        num_samples = np.shape(sound)[0]
        max_samples = num_samples - (num_samples % self.buffer_size_samples)
        self.sound = np.zeros((max_samples, self.num_channels), dtype=np.int16)
        self.sound = np.copy(sound[:max_samples,:])
        self.current_sample = 0
        self.max_samples = max_samples
        return

    # Reset sound output
    def reset(self):
        self.current_sample = 0
        return

    # Play WAV file
    def play_wav(self, wav_path):
        self.wav_path = wav_path

        # Read a WAV file
        wav_file = wave.open(wav_path, 'rb')
        wav_num_channels = wav_file.getnchannels()
        wav_sample_rate = wav_file.getframerate()
        wav_sample_width = wav_file.getsampwidth()
        wav_num_samples =  wav_file.getnframes()

        # Validate WAV file
        if wav_num_channels != self.num_channels:
            print("WAV file has inconsistent number of channels for output device.")
        if wav_sample_rate != self.sample_rate:
            print("WAV file has inconsistent sample rate for output device.")
        if wav_sample_width != 2:
            print("WAV file has inconsistent sample width for output device.")

        # Set number of frames
        wav_num_samples = wav_num_samples - (wav_num_samples % self.buffer_size_samples)

        # Read WAV file
        wav_data = wav_file.readframes(wav_num_samples)
        wav_file.close()

        # Seperate channel data
        channel_data = np.reshape(np.frombuffer(wav_data, dtype=np.int16).transpose(), (-1,self.num_channels))
        self.sound = channel_data

        # Start recording
        self.current_sample = 0
        self.max_samples = wav_num_samples

        return
    
    # Check if for sound output is finished
    def is_playing(self):
        if self.current_sample < self.max_samples:
            return True
        else:
            return False

    # Stop thread method
    def stop(self):
        self.streaming = False