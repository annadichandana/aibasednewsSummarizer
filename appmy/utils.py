from transformers import pipeline

# Load a pre-trained summarization model
summarizer = pipeline("summarization")

def summarize_text(text):
    if len(text) < 100:
        return "Text too short for summarization."
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return summary[0]['summary_text']
