#Step 1: Set up AUDIO recorder (ffmpeg & portaudio) 
import os
import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO
from groq import Groq


# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def record_audio(file_path, timeout=20, phrase_time_limit=None):
    """
    Simplified function to record audio from the microphone and save it as a MP3 file.

    Args:
    file_path (str): The path where the recorded audio will be saved.
    timeout (int): The maximum time to wait for audio input to start (seconds).
    phrase_time_limit (int): The maximum time to record audio (seconds).
    """

    # Initialize the audio recorder
    recogniser = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            recogniser.adjust_for_ambient_noise(source, duration=1)
            logging.info("Start speaking now. Recording audio...")

            # Record audio until the user stops speaking
            audio_data = recogniser.listen(source, timeout = timeout, phrase_time_limit = phrase_time_limit)
            logging.info("Audio recording complete.")

            # Convert the audio data recorded to MP3 file format
            wave_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wave_data))
            audio_segment.export( file_path, format="mp3", bitrate="128k")

            logging.info(f"Audio saved to {file_path}")

    except Exception as e:
        logging.error(f"An error occured: {e}")
audio_file_path = "patient_voice.mp3"
#record_audio(audio_file_path)

#Step 2: Set up Speech-to-Text STT Model for transcription

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
stt_model = "whisper-large-v3"

def transcibe_with_groq(stt_model, audio_file_path, GROQ_API_KEY):
    client = Groq(api_key=GROQ_API_KEY)
    audio_file = open(audio_file_path, "rb")

    transcription = client.audio.transcriptions.create(
        model = stt_model,
        file = audio_file,
        language = "en"
    )
    # Print the transcription result
    return transcription.text

