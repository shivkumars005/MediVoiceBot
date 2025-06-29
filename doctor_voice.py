# Step 1a: Set up Text-to-Speech TTS Model with gTTS 

import os
from gtts import gTTS
from elevenlabs.client import ElevenLabs
from elevenlabs import save
import subprocess
import platform

def gtts_text_to_speech_old(input_text, output_file_path):
    language = 'en'  
    audio_obj = gTTS(
        text=input_text,
        lang=language, 
        slow=False)
    audio_obj.save(output_file_path)

input_text = "Hello, this is a test for the text-to-speech conversion using gTTS."
#gtts_text_to_speech_old(input_text, output_file_path = "doctor_voice_gtts.mp3")

# Step 1b: Set up Text-to-Speech TTS Model with Elevenlabs

ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")
client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

def elevenlabs_text_to_speech_old(input_text, output_file_path):
    audio = client.text_to_speech.convert(
        text = input_text,
        output_format = "mp3_22050_32",
        voice_id="21m00Tcm4TlvDq8ikWAM"
    )
    save(audio, output_file_path)

input_text = "Hello, this is a test for the text-to-speech conversion using Eleven Labs."
#elevenlabs_text_to_speech_old(input_text, output_file_path = "doctor_voice_elevenlabs.mp3")

# Step 2: use model to convert text to speech


def gtts_text_to_speech(input_text, output_file_path):
    language = 'en'  
    audio_obj = gTTS(
        text=input_text,
        lang=language, 
        slow=False)
    audio_obj.save(output_file_path)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_file_path])
        elif os_name == "Windows":
            subprocess.run(['ffplay', '-nodisp', '-autoexit', '-loglevel', 'quiet', output_file_path])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_file_path])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


input_text = "Hello, this is a Auto play test for the text-to-speech conversion using gTTS."
#gtts_text_to_speech(input_text, output_file_path = "doctor_voice_gtts_autoplay.mp3")


def elevenlabs_text_to_speech(input_text, output_file_path):
    audio = client.text_to_speech.convert(
        text = input_text,
        output_format = "mp3_22050_32",
        voice_id="21m00Tcm4TlvDq8ikWAM"
    )
    save(audio, output_file_path)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_file_path])
        elif os_name == "Windows":
            subprocess.run(['ffplay', '-nodisp', '-autoexit', '-loglevel', 'quiet', output_file_path])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_file_path])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")
    
    return output_file_path

input_text = "Hello, this is a Auto play test for the text-to-speech conversion using Eleven Labs."
#elevenlabs_text_to_speech(input_text, output_file_path = "doctor_voice_elevenlabs_autoplay.mp3")
