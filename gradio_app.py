#VoiceBot UI with Gradio

import os
import gradio as gr

from brain import encode_image, analyze_image
from patient_voice import record_audio, transcibe_with_groq
from doctor_voice import gtts_text_to_speech, elevenlabs_text_to_speech

from dotenv import load_dotenv
load_dotenv()


system_prompt = """
            You have to act as a professional doctor, i know you are not but this is for learning purpose. 
            What's in this image?. Do you find anything wrong with it medically? 
            If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
            your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
            Donot say 'In the image I see' but say 'With what I see, I think you have ....'
            Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
            Keep your answer concise (max 2 sentences). No preamble, start your answer right away please.
            """


def process_inputs(audio_file_path, image_filepath):
    speech_to_text_output = transcibe_with_groq(stt_model="whisper-large-v3",
                                                audio_file_path=audio_file_path,
                                                GROQ_API_KEY=os.environ.get("GROQ_API_KEY"))

    # Handle the image input
    if image_filepath:
        doctor_response = analyze_image(query=system_prompt+speech_to_text_output, 
                                                   encoded_image=encode_image(image_filepath), 
                                                   model="meta-llama/llama-4-scout-17b-16e-instruct") 
    else:
        doctor_response = "No image provided for me to analyze"

    voice_of_doctor = elevenlabs_text_to_speech(input_text=doctor_response, 
                                                output_file_path="final.mp3") 

    return speech_to_text_output, doctor_response, voice_of_doctor


# Create the interface
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath"),
        gr.Image(type="filepath")
    ],
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio(label="Doctor's voice", type="filepath")
    ],
    title="AI Doctor with Vision and Voice"
)

iface.launch(debug=True)

#http://127.0.0.1:7860