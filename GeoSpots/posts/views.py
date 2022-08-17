from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'posts/index.html')

def my_page(request):
    return render(request, 'posts/my_page.html')

def follow(request):
    return render(request, 'posts/follow.html')

def favourites(request):
    return render(request, 'posts/favorites.html')