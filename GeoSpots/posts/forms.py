from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from .models import Comment, LatLon, Map, Post, Profile


class PostForm(forms.ModelForm):
    template_name = 'post_form.html'

    class Meta:
        model = Post
        fields = ('title', 'text', 'group', 'image', 'lat', 'lon')
        labels = {
            'title': 'Name',
            'text': _('Text'),
            'group': _('Category'),
            'Coor': 'К какому посту относится',
            'image': 'Photo',
            'lat': 'Latitude',
            'lon': 'Longitude',
        }
        widgets = {'image': forms.ClearableFileInput(attrs={'class': 'custom-file-input'})}


class ExampleForm(forms.ModelForm):
    title = forms.CharField(label='Title', max_length=100)
    text = forms.CharField(label='Text', widget=forms.Textarea)

    latitude = forms.DecimalField(label='Latitude', required=False)
    longitude = forms.DecimalField(label='Longitude', required=False)
    photo = forms.ImageField(label='Photo', required=False)

    def __init__(self, *args, **kwargs):
        super(ExampleForm, self).__init__(*args, **kwargs)
        self.fields['latitude'].widget = forms.HiddenInput()
        self.fields['longitude'].widget = forms.HiddenInput()
        self.fields['photo'].widget = forms.HiddenInput()

    def add_place(self):
        self.fields['latitude'].widget = forms.TextInput()
        self.fields['longitude'].widget = forms.TextInput()

    def add_photo(self):
        self.fields['photo'].widget = forms.ClearableFileInput()

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


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {
            'text': 'Текст',
        }


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar',)
        labels = {
            'avatar': 'ava',
        }
