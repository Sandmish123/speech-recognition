
# import streamlit as st
# from audio_recorder_streamlit import audio_recorder
# import soundfile as sf
# import numpy as np

# st.title("🎙️ Audio Recorder and Playback")

# # Record Audio
# audio_bytes = audio_recorder(
#     text="Record your audio",
#     recording_color="#e63946",
#     neutral_color="#457b9d",
#     icon_name="microphone",
#     icon_size="4x",
#     pause_threshold=2.0,
#     sample_rate=41000
# )

# # Save and Playback Audio
# if audio_bytes:
#     audio_path = "recorded_audio.wav"
#     with open(audio_path, "wb") as f:
#         f.write(audio_bytes)
    
#     st.success("✅ Audio Recorded Successfully!")
#     st.audio(audio_bytes, format="audio/wav")

#     if st.button("▶️ Play Recorded Audio"):
#         try:
#             data, samplerate = sf.read(audio_path)
#             st.write(f"Playing at {samplerate} Hz")
#             sf.write('temp_audio.wav', data, samplerate)
#             st.audio('temp_audio.wav', format='audio/wav')
#             st.success("Playback completed.")
#         except Exception as e:
#             st.error(f"Error during playback: {e}")













import streamlit as st
from audio_recorder_streamlit import audio_recorder
import soundfile as sf
import numpy as np
import speech_recognition as sr
import os

def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_path) as source:
            st.write("Transcribing audio...")
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
            st.success("Transcription: " + text)
            return text
    except sr.UnknownValueError:
        st.error("Speech recognition could not understand the audio.")
    except sr.RequestError as e:
        st.error(f"Could not request results; {e}")

st.title("🎙️ Audio Recorder and Playback")

# Record Audio
audio_bytes = audio_recorder(
    text="Record your audio",
    recording_color="#e63946",
    neutral_color="#457b9d",
    icon_name="microphone",
    icon_size="4x",
    pause_threshold=2.0,
    sample_rate=41000
)

# Save and Playback Audio
if audio_bytes:
    audio_path = "/home/sandeep-cc/mediapipe/speech-input/recorded_audio.wav"
    with open(audio_path, "wb") as f:
        f.write(audio_bytes)
    
    st.success("✅ Audio Recorded Successfully!")
    st.audio(audio_bytes, format="audio/wav")

    if st.button("▶️ Play Recorded Audio"):
        try:
            data, samplerate = sf.read(audio_path)
            st.write(f"Playing at {samplerate} Hz")
            sf.write('temp_audio.wav', data, samplerate)
            st.audio('temp_audio.wav', format='audio/wav')
            st.success("Playback completed.")
        except Exception as e:
            st.error(f"Error during playback: {e}")

if st.button("Start Transcription"): 
    transcribe_audio(audio_path)
    # Check if audio exists before transcription
    if os.path.exists(audio_path) and os.path.getsize(audio_path) > 0:
        st.write("got the file")
    else:
        st.error("No valid audio file found at the specified path. Please record audio first.")
