🎙️ Voice-to-Summary AI System
This project is an end-to-end pipeline that converts live voice input into a concise summary using state-of-the-art deep learning models. It combines:

🎤 Audio Recording (via microphone using sounddevice)

🧠 Speech-to-Text Transcription (using OpenAI’s Whisper ASR model)

📝 Text Summarization (with Hugging Face's distilBART transformer)

🔧 Features
Record real-time audio input

Automatically transcribe speech into text

Generate clean, readable summaries

GPU-accelerated summarization support

🚀 Tech Stack
Python

Whisper by OpenAI

Hugging Face Transformers (sshleifer/distilbart-cnn-12-6)

SoundDevice & Wavio for audio handling

📌 Use Case
Ideal for meeting note-taking, interview summarization, lecture capture, or voice memos.
