from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, User, Map, LatLon
from django.contrib.auth.decorators import login_required
from .forms import MapForm, PostForm, LatLonForm
from geopy.geocoders import Nominatim
#from .utils import get_geo
import folium


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def my_page(request):
    form = LatLonForm(request.POST or None)
    #post = get_object_or_404(Post, id=post_id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    map_folium = folium.Map(location=[61.171310, 28.766600], width=800, height=500, zoom_start = 4)
    point_list = LatLon.objects.all().values()
    map_folium.add_child(folium.LatLngPopup())

    for i in point_list:
        for_title = i.get('title')
        for_lat = i.get('lat')
        for_lon = i.get('lon')
        folium.Marker(location=[for_lat, for_lon], popup=for_title).add_to(map_folium)

#popup='', tooltip=''

    map_folium = map_folium._repr_html_()

    context = {
        'form': form,
        'map_folium': map_folium,
    }

    return render(request, 'posts/map.html', context)

#    #obj = get_object_or_404(Map, id=1)
#    form = MapForm(request.POST or None)
#    geolocator = Nominatim(user_agent='GeoSpots')
#    #ip = '84.248.157.53'
#    #counrty, city, lat, lon = get_geo(ip)
#    #print('country is', counrty)
#    #print('city is', city)
#    #print('lat is', lat)
#    #print('long is', lon)
#
#    map_folium = folium.Map(location=[61.171310, 28.766600], width=800, height=500, zoom_start = 7)
#    folium.Marker(location=[61.054993, 28.189663], popup='LPR', tooltip='click here').add_to(map_folium)
#
#    #сделать модель для координат, сохранять значения из формы и передаватьих на карту
#    #point_list = [[61.054993, 28.189663], [61.171310, 28.766600]]
#    
#    #перебор списка с координатами
#    #for i in index.point_list(len(point_list)):
#    #    print(range(point_list))
#    #folium.Marker(location=[i], popup='LPR', tooltip='click here').add_to(map_folium)
#
#    if form.is_valid():
#        instance = form.save(commit=False)
#        destination1 = form.cleaned_data.get('destination')
#        destination = geolocator.geocode(destination1)
#        print(destination)
#        d_lat = destination.latitude
#        d_long = destination.longitude
#        print(d_lat)
#        print(d_long)
#        instance.location = 'Lappeenranta'
#        instance.distance = 30.00
#        #instance.save()
#        folium.Marker(location=[d_lat, d_long], popup='LPR', tooltip='click here').add_to(map_folium)
#    map_folium = map_folium._repr_html_()
#    context = {
#        #'distance': obj,
#        'form': form,
#        'map': map_folium
#
#    }



def follow(request):
    return render(request, 'posts/follow.html')


def favourites(request):
    return render(request, 'posts/favorites.html')


def post_detail(request, post_id):
    template = 'posts/post_detail.html'
    post = get_object_or_404(Post, id=post_id)
    post_lat = post.Coor.lat
    post_lon = post.Coor.lon
    post_title = post.Coor.title
    map_folium = folium.Map(location=[post_lat, post_lon], width=800, height=500, zoom_start = 8)
    folium.Marker(location=[post_lat, post_lon], popup=post_title).add_to(map_folium)
    map_folium = map_folium._repr_html_()
    author_posts_count = post.author.posts.count()
    context = {
        'post': post,
        'author_posts_count': author_posts_count,
        'map_folium': map_folium,
    }
    return render(request, template, context)


@login_required
def post_create(request):
    form = PostForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('posts:index')
    context = {'form': form}

    return render(request, 'posts/create_post.html', context)


def profile(request, username):
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
