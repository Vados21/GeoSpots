from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('my_page', views.my_page, name='my_page'),
    path('follow', views.follow, name='follow'),
    path('favourites', views.favourites, name='favourites'),
    path('create', views.post_create, name='create_post'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('profile/<str:username>/', views.profile, name='profile'),
]
