import pyaudio
import numpy as np
import webrtcvad

# Initialize variables
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1024

# Initialize PyAudio
audio = pyaudio.PyAudio()
vad = webrtcvad.Vad(3)  # Aggressiveness: 0-3 (higher = more suppression)

# Start the audio stream
stream = audio.open(format=FORMAT,
                     channels=CHANNELS,
                     rate=RATE,
                     input=True,
                     frames_per_buffer=CHUNK)

print("Listening with Noise Suppression... Press Ctrl+C to stop.")

try:
    while True:
        data = stream.read(CHUNK)
        is_speech = vad.is_speech(data, RATE)

        if is_speech:
            print("Speech detected!")
        else:
            print("No speech detected. Suppressing noise.")
except KeyboardInterrupt:
    print("Stopping...")
finally:
    stream.stop_stream()
    stream.close()
    audio.terminate()
