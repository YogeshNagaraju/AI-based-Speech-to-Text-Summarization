from transformers import pipeline

# Use GPU if available (device=0), otherwise fallback to CPU
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", device=0)
