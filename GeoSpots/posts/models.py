from typing_extensions import Required
from unicodedata import decimal
from unittest.util import _MAX_LENGTH
from django.contrib.auth import get_user_model
from django.db import models
from numpy import require

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=40)
    description = models.TextField(null=True)

    class Meta:
        verbose_name = 'Заголовок группы'

    def __str__(self):
        return self.title


class LatLon(models.Model):
    title = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)

    lat = models.DecimalField(max_digits=10, decimal_places=8)
    lon = models.DecimalField(max_digits=10, decimal_places=8)

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group, blank=True, null=True,
        on_delete=models.SET_NULL,
        related_name='posts'
    )
    Coor = models.ForeignKey(
        LatLon, blank=True, null=True,
        on_delete=models.CASCADE,
        related_name='coordinates'
    )
    image = models.ImageField(
        'Картинка',
        upload_to='posts/',
        blank=True
    )
    #location = models.PointField()

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.text


class Comment(models.Model):
    post = models.ForeignKey(
        Post, blank=True, null=True,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following'
    )

    def __str__(self):
        return str(self.user.username)


class Map(models.Model):
    location = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(f' {self.distance} km')


