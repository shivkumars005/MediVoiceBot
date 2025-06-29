import base64
from groq import Groq

# Step1: Set up GROQ API Key
import os
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Step2: Convert image to suitable format for the Multimodel LLM
#image_path = "acne.jpg"
def encode_image(image_path):  
    image_file = open(image_path, "rb")
    return base64.b64encode(image_file.read()).decode("utf-8")

# Step3: Set up the Multimodel LLM


query = "Is there something wrong with this skin? "
model = "meta-llama/llama-4-scout-17b-16e-instruct"

def analyze_image(query, model, encoded_image):
    client = Groq()
    messages = [
        {
            "role": "user", 
            "content": [{
                "type": "text",
                "text": query
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{encoded_image}"
                },
            },
        ],  
    }]

    chat_response = client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_response.choices[0].message.content