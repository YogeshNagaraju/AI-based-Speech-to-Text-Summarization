from transformers import pipeline

# Use a smaller version of BART
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text):
    num_tokens = len(text.split())

    # Set max and min length depending on input size
    max_len = min(130, int(num_tokens * 0.7))
    min_len = min(30, int(num_tokens * 0.3))

    if num_tokens < 10:
        print("[!] Input too short to summarize.")
        return text

    summary = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
    return summary[0]['summary_text']