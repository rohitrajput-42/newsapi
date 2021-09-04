from django.shortcuts import render
import requests
API_KEY = '1470783081614b44a6011167b537c977'


def Index(request):

    country = request.GET.get('country')
    category = request.GET.get('category')

    if country:
        url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}"
        response = requests.get(url)
        data = response.json()
    elif category:
        url = f"https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}"
        response = requests.get(url)
        data = response.json()
    else:
        url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}"
        response = requests.get(url)
        data = response.json()
        
    articles = data['articles']

    return render(request, 'index.html', {'articles': articles})