import sounddevice as sd
import wavio

def record_audio(output_path="temp_audio.wav", duration=10, sample_rate=44100):
    print(f" Recording for {duration} seconds...")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()  # Wait until recording is finished
    wavio.write(output_path, recording, sample_rate, sampwidth=2)
    print(f" Recording saved as {output_path}")
    return output_path
