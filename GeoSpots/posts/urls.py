from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('map', views.map_page, name='map'),
    path('favorites/<str:username>/', views.favorites, name='favorites'),
    path('weather', views.weather, name='weather'),
    path('create', views.post_create, name='create_post'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('profile/<str:username>/settings', views.settings, name='settings'),
    path('posts/<int:post_id>/comment', views.add_comment, name='add_comment'),
    path('posts/<int:post_id>/like/', views.add_like, name='add_like'),
    path('posts/comment_like/<int:pk>',
         views.add_like_comment, name='add_like_comment'),
    path('follow/', views.follow_index, name='follow_index'),
    path('profile/<str:username>/follow/',
         views.profile_follow, name='profile_follow'),
    path(
        'profile/<str:username>/unfollow/',
        views.profile_unfollow,
        name='profile_unfollow'
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
