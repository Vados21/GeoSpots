from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('map', views.my_page, name='map'),
    path('follow', views.follow, name='follow'),
    path('favourites', views.favourites, name='favourites'),
    path('create', views.post_create, name='create_post'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('posts/<int:post_id>/comment', views.add_comment, name='add_comment'),
    path('posts/<int:post_id>/like/', views.add_like, name='add_like'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
