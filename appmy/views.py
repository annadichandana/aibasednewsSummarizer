import requests
import re
import ast 
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

API_KEY = 'AIzaSyCInUwrK2Gns2MZR4SbmIP0rU3fQcFPbds'  
CSE_ID = '53bf6ac9a3cd54403'

@csrf_exempt  
def index(request):
    if request.method == "POST":
        query = request.POST.get('query', '')

        if is_math_expression(query):
            answer = solve_math_expression(query)
            return HttpResponse(f"Answer: {answer}")

        
        search_results = search_google(query)
        return HttpResponse(f"Search results: {search_results}")

    
    return render(request, 'index.html')

def is_math_expression(query):
    """Check if the query is a mathematical expression."""
    return bool(re.match(r'^[0-9+\-*/^().\s]+$', query))

def solve_math_expression(query):
    """Safely solve a simple mathematical expression."""
    try:
        result = ast.literal_eval(query)  
        return result
    except Exception as e:
        return f"Error solving expression: {str(e)}"

def search_google(query):
    """Function to search using Google Custom Search API."""
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={CSE_ID}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if 'items' in data:
            results = data['items']
            search_results = ""
            for result in results:
                title = result.get('title', 'No title available')
                snippet = result.get('snippet', 'No description available.')
                link = result.get('link', '#')
                image_url = result.get('pagemap', {}).get('cse_image', [{}])[0].get('src', None)
                
                search_results += f"""
                <div class="result">
                    <h3><a href="{link}">{title}</a></h3>
                    <p>{snippet}</p>
                    {f'<img src="{image_url}" alt="{title}" width="500" height="auto" />' if image_url else ''}
                    <p><a href="{link}">More info</a></p>
                </div><br><br>
                """
            return search_results
        else:
            return "No results found."
    except Exception as e:
        return f"Error: {str(e)}"
