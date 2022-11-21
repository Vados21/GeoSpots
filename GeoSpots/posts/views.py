import logging

import folium

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentForm, LatLonForm, PostForm
from .models import Post, User

import urllib.request
import json


logging.basicConfig(level=logging.INFO)


def index(request):
    logging.info('index started')
    post_list = Post.objects.all().select_related('author')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def my_page(request):
    logging.info('map started')
    form = LatLonForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    map_folium = folium.Map(
        location=[61.171310, 28.766600],
        width=1200, height=700, zoom_start=4
    )
    point_list = Post.objects.all().values()

    map_folium.add_child(folium.LatLngPopup())

    for i in point_list:
        for_title = i.get('title')
        for_lat = i.get('lat')
        for_lon = i.get('lon')
        for_group = i.get('group_id')
        if for_group == 2:
            folium.Marker(
                location=[for_lat, for_lon],
                popup=for_title,
                icon=folium.Icon(
                    icon="glyphicon-tower", prefix='glyphicon', color='black')
                    ).add_to(map_folium)
        elif for_group == 3:
            folium.Marker(
                location=[for_lat, for_lon],
                popup=for_title, icon=folium.Icon(
                    icon="glyphicon-tree-conifer",
                    prefix='glyphicon', color='green')
                    ).add_to(map_folium)

        else:
            folium.Marker(
                location=[for_lat, for_lon],
                popup=for_title, icon=folium.Icon(
                    icon="glyphicon-tint",
                    prefix='glyphicon')
                    ).add_to(map_folium)
    map_folium = map_folium._repr_html_()

    context = {
        'form': form,
        'map_folium': map_folium,
    }

    return render(request, 'posts/map.html', context)


def follow(request):
    data = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?lat=60.1634&lon=23.5107&appid=446b6e8e3475d97c2504c6b27b11baa1&=446b6e8e3475d97c2504c6b27b11baa1&units=metric').read()
    list_of_data = json.loads(data)
    context = {
        'temp': str(list_of_data['main']['temp']) + ' °C',
    }
    print(data)
    return render(request, 'posts/follow.html', context)


def weather(request):
    logging.info('weather started')
    if request.method == 'POST':
        city = request.POST['city']

        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' +
            city +
            '&units=metric&appid=446b6e8e3475d97c2504c6b27b11baa1&=446b6e8e3475d97c2504c6b27b11baa1'
            ).read()
        list_of_data = json.loads(source)

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '
            + str(list_of_data['coord']['lat']),

            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }

    else:
        data = {}

    return render(request, "posts/weather.html", data)


def post_detail(request, post_id):
    logging.info('post_detail started')
    template = 'posts/post_detail.html'
    post = get_object_or_404(Post, id=post_id)
    post_lat = post.lat
    post_lon = post.lon
    post_title = post.text
    post_group = post.group.id
    map_folium = folium.Map(
        location=[post_lat, post_lon],
        width=800, height=500, zoom_start=8)
    if post_group == 2:
        folium.Marker(
            location=[post_lat, post_lon],
            popup=post_title, icon=folium.Icon(
                icon="glyphicon-tower", prefix='glyphicon', color='black')
                ).add_to(map_folium)
    elif post_group == 3:
        folium.Marker(
            location=[post_lat, post_lon],
            popup=post_title, icon=folium.Icon(
                icon="glyphicon-tree-conifer",
                prefix='glyphicon', color='green')
                ).add_to(map_folium)
    else:
        folium.Marker(
            location=[post_lat, post_lon],
            popup=post_title, icon=folium.Icon(
                icon="glyphicon-tint", prefix='glyphicon')
                ).add_to(map_folium)
    map_folium = map_folium._repr_html_()
    author_posts_count = post.author.posts.count()
    data = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?lat=' + str(post_lat) + '&lon=' + str(post_lon) + '&appid=446b6e8e3475d97c2504c6b27b11baa1&=446b6e8e3475d97c2504c6b27b11baa1&units=metric').read()
    list_of_data = json.loads(data)
    context = {
        'post': post,
        'author_posts_count': author_posts_count,
        'map_folium': map_folium,
        'temp': str(list_of_data['main']['temp']) + ' °C',
        'icon': list_of_data['weather'][0]['icon'],

    }
    return render(request, template, context)


@login_required
def post_create(request):
    logging.info('post create started')
    form = PostForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('posts:index')
    map_folium = folium.Map(
        location=[61.171310, 28.766600],
        width=800, height=500, zoom_start=4)
    point_list = Post.objects.all().values()
    map_folium.add_child(folium.LatLngPopup())

    for i in point_list:
        post_title = i.get('title')
        post_lat = i.get('lat')
        post_lon = i.get('lon')
        folium.Marker(
            location=[post_lat, post_lon],
            popup=post_title).add_to(map_folium)
    map_folium = map_folium._repr_html_()
    context = {'form': form}

    return render(request, 'posts/create_post.html', context)


def profile(request, username):
    logging.info('profile started')
    user = get_object_or_404(User, username=username)
    post_list = user.posts.all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    post_counter = paginator.count
    page_obj = paginator.get_page(page_number)
    context = {
        'username': user,
        'post_counter': post_counter,
        'page_obj': page_obj,
    }
    return render(request, 'posts/profile.html', context)


@login_required
def add_comment(request, post_id):
    logging.info('add comment started')
    post = get_object_or_404(Post, pk=post_id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
    return redirect('posts:post_detail', post_id=post_id)


def add_like(request, post_id):
    logging.info('add_like started')
    post = get_object_or_404(Post, id=post_id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        logging.info('removed')
    else:
        post.likes.add(request.user)
        logging.info('added')
    return redirect('posts:post_detail', post_id=post_id)
