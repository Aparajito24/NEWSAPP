from django.shortcuts import render
import requests

API_KEY = 'cfff528b915d4bbc8ef789472fe7041d'


def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')

    if country:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
    else:
        url = f'https://newsapi.org/v2/everything?q={category}&from=2021-06-23&sortBy=popularity&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()

    articles = data['articles']
    context = {
        'articles': articles
    }

    return render(request, 'news_api/home.html', context)

# Create your views here.
