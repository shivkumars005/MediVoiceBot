# 🩺 MediVoiceBOT - AI Doctor Chatbot with Voice & Vision

MediVoiceBOT is an AI-powered medical assistant that allows users to:

* User can tell symptoms via microphone
* Upload a skin image * (Required)
* Receive a concise, doctor-like diagnosis & advice
* Hear the response in a natural voice via ElevenLabs TTS or gTTS

This is a **learning project** that showcases multimodal capabilities (audio, vision, text) using open-source tools and AI APIs.

---

## 🚀 Features

* 🎤 Voice-to-text with Whisper (via Groq API)
* 🖼️ Image analysis with LLaMA (Groq vision models)
* 🧠 Intelligent diagnosis prompt engineering
* 🗣️ Natural-sounding voice replies using ElevenLabs or gTTS
* 🎛️ Gradio UI for seamless web interaction

---

## Hosted at [MediVoiceBot](https://huggingface.co/spaces/shivakumars57/MediVoiceBot)

---

## 🛠️ Tech Stack

* Python 3.12
* Gradio
* Groq API (Whisper, LLaMA-4 Vision)
* ElevenLabs TTS
* gTTS (Google TTS fallback)
* FFmpeg (for audio playback)
* pydub, speech\_recognition
* Huggingface spaces (To deploy)

---

## ⚙️ Installation

### 1. Clone Repo

```bash
git clone https://github.com/shivkumars005/MediVoiceBOT
cd MediVoiceBOT
```

### 2. Set up virtual environment

```bash
python -m venv venv
venv\Scripts\activate    # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install FFmpeg (Windows)

* Download from: [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)
* Extract and add `bin/` to your Environment PATH
* Confirm via: `ffmpeg -version`

### 5. Also install portaudio .whl files and pyaudio

---

## 🔑 API Keys

Create a `.env` file in the root:

```env
GROQ_API_KEY=your_groq_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
```

You can sign up for:

* Groq: [https://console.groq.com](https://console.groq.com)
* ElevenLabs: [https://www.elevenlabs.io](https://www.elevenlabs.io)

---

## 🧪 Run the App

```bash
python gradio_app.py
```

Visit: `http://127.0.0.1:7860`

---

## 📝 Example Use

1. Speak: "I have a burning rash near my cheek."
2. Upload a skin photo * (Required)
3. App transcribes, analyzes, and responds:

   > "With what I see, I think you have contact dermatitis. You can apply a mild steroid cream and avoid irritants."
4. Audio plays back in doctor's voice

---

## 📁 Project Structure

```
MediVoiceBOT/
├── gradio_app.py           # Main UI and logic
├── brain.py                # Groq image analysis helpers
├── patient_voice.py        # Audio recording & transcription
├── doctor_voice.py         # Text-to-speech generation
├──images                   # Sample images folder
├── .env                    # API keys
├── requirements.txt
└── README.md
```

---

## ❗ Disclaimer

This project is for educational use only and does **not** provide real medical advice.

---

## 📬 Contact

Feel free to reach out for collaboration or questions:

* GitHub: [Shiva Kumar Souta](https://github.com/yourusername)
* Email: [shivakumarsouta18@gmail.com](mailto:shivakumarsouta18@gmail.com)
* LinkedIn: [Shiva Kumar Souta](https://www.linkedin.com/in/shivakumarsouta/)
* Portfolio: [My portfolio site](https://shivakumarsouta-portfolio.vercel.app/)
---


