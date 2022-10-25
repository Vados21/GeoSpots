from django.forms import ModelForm
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Post, Map, LatLon


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'group', 'image', 'lat', 'lon')
        labels = {
            'title': 'Name',
            'text': _('Текст'),
            'group': _('Группа'),
            'Coor': 'К какому посту относится',
            'image': 'Photo',
            'lat': 'Latitude',
            'lon': 'Longitude',
        }


class MapForm(ModelForm):
    class Meta:
        model = Map
        fields = ('destination',)
        labels = {
            'destination': 'destination',
        }


class LatLonForm(ModelForm):
    class Meta:
        model = LatLon
        fields = ('title', 'lat', 'lon')
        labels = {
            'title': 'Point name',
            'lat': 'Latitude',
            'lon': 'Longitude',
        }
