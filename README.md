# AI-Based News Summarizer

## Overview
The AI-Based News Summarizer is a smart web application that leverages advanced Natural Language Processing (NLP) to read long news articles and generate short, meaningful summaries. It helps users quickly understand the main points of news content without reading the entire article.

## Features
- **Multiple Input Methods:** Summarize text by pasting it directly, providing a news article URL, or uploading a `.txt` file.
- **Advanced AI Summarization:** Uses Hugging Face's `transformers` library (specifically the `sshleifer/distilbart-cnn-12-6` model) for high-quality abstractive summarization.
- **Modern User Interface:** A beautiful, responsive glassmorphism UI built with Bootstrap and custom CSS, featuring animated loading states.
- **Fast Local Inference:** Runs the AI model locally for privacy and speed, with model caching for instant subsequent requests.

## Tech Stack
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Machine Learning:** Hugging Face `transformers` (PyTorch)
- **Web Scraping:** `newspaper3k` for URL article extraction

## Installation

1. Clone the repository (if applicable) and navigate to the project directory:
   ```bash
   git clone https://github.com/yourusername/appmy.git
   cd aibasednewsSummarizer
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: The first time you run the application, it will download the NLP model which is around 1.2GB. This requires a stable internet connection.)*

4. Run the development server (No database migrations required!):
   ```bash
   python manage.py runserver
   ```

## Usage
1. Open a web browser and navigate to `http://127.0.0.1:8000/`.
2. Choose your preferred input method:
   - **Paste Text:** Copy and paste the raw text of a news article.
   - **News URL:** Provide a valid URL to a news article (the app will automatically extract the text).
   - **Upload .txt:** Upload a text file containing the article.
3. Click **"Generate Summary"**.
4. Wait for the AI to process the text (this takes longer on the very first run as the model loads into memory).
5. Read your concise, abstractive summary!


---
Developed By Chandana Annadi
