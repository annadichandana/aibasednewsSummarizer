import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from newspaper import Article
from transformers import pipeline

summarizer = None

def get_summarizer():
    global summarizer
    if summarizer is None:
        print("Loading summarization model... (this may take a minute on first run)")
        summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    return summarizer

@csrf_exempt  
def index(request):
    if request.method == "POST":
        input_type = request.POST.get('input_type', '')
        text_to_summarize = ""
        
        try:
            if input_type == 'text':
                text_to_summarize = request.POST.get('raw_text', '').strip()
            elif input_type == 'url':
                url = request.POST.get('url', '').strip()
                if url:
                    article = Article(url)
                    article.download()
                    article.parse()
                    text_to_summarize = article.text
            elif input_type == 'file':
                if 'file' in request.FILES:
                    uploaded_file = request.FILES['file']
                    if uploaded_file.name.endswith('.txt'):
                        text_to_summarize = uploaded_file.read().decode('utf-8')
                    else:
                        return JsonResponse({'error': 'Only .txt files are supported.'}, status=400)
            
            if not text_to_summarize:
                return JsonResponse({'error': 'Please provide some text to summarize.'}, status=400)
                
            ai_summarizer = get_summarizer()
            
            max_input_length = 3500
            if len(text_to_summarize) > max_input_length:
                short_text = text_to_summarize[:max_input_length]
                last_period = short_text.rfind('.')
                if last_period > 0:
                    short_text = short_text[:last_period+1]
            else:
                short_text = text_to_summarize
                
            summary_result = ai_summarizer(short_text, max_length=150, min_length=40, do_sample=False)
            summary = summary_result[0]['summary_text']
            
            return JsonResponse({
                'success': True,
                'summary': summary,
                'original_text_preview': text_to_summarize[:300] + "..." if len(text_to_summarize) > 300 else text_to_summarize
            })
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return render(request, 'index.html')
