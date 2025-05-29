# apiapp/views.py
import requests
from django.http import JsonResponse
from django.shortcuts import render
def fetch_api_data(request):
    api_url = "https://api.publicapis.org/entries"  # sample public API
    try:
        response = requests.get(api_url)
        data = response.json()
        return JsonResponse(data, safe=False)
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": str(e)}, status=500)


def index(request):
    return render(request, 'index.html')
