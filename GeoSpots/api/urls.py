from django.urls import path

from . import views

urlpatterns = [
    path('api/posts', views.get_posts),
    path('api/posts/create', views.create_post),
    path('api/posts/<str:pk>', views.get_post),
    path('api/posts/<str:pk>/update', views.update_post),
    
]