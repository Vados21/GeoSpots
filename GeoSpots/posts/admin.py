from django.contrib import admin

from .models import Comment, Follow, Group, LatLon, Map, Post, Profile


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'
    filter_horizontal = ['likes']


class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description'
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class Comments(admin.ModelAdmin):
    list_display = (
        'pk',
        'post',
        'author',
    )
    filter_horizontal = ['likes_comment']


class LatLonAdmin(admin.ModelAdmin):
    list_display = (
        'lat',
        'lon',

    )


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'surname',
        'date_of_birth',
        'avatar'
    )

admin.site.register(Post, PostAdmin)
admin.site.register(Group)
admin.site.register(Comment)
admin.site.register(Follow)
admin.site.register(Map)
admin.site.register(LatLon)
admin.site.register(Profile)
