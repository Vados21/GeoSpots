from django.forms import ModelForm
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Post, Map, LatLon


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group')
        labels = {
            'text': _('Текст'),
            'group': _('Группа')
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
        fields = ('lat', 'lon')
        labels = {
            'lat': 'Lat',
            'lon': 'Lon'
        }
