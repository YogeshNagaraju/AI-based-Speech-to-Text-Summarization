import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.recorder import record_audio
from app.transcriber import transcribe_audio
from app.summarizer import summarize_text

TEMP_AUDIO = "temp_audio.wav"

if __name__ == "__main__":
    # 1. Record from mic
    recorded_file = record_audio(TEMP_AUDIO, duration=30)  # You can change duration

    # 2. Transcribe
    print("\n🔊 Transcribing...")
    transcript = transcribe_audio(recorded_file)
    print("\n📝 Transcribed Text:\n")
    print(transcript)

    # 3. Summarize
    print("\n🧠 Summarizing...")
    summary = summarize_text(transcript)
    print("\n📌 Summary:\n")
    print(summary)
