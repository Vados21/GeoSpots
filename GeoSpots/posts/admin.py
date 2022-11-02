from django.contrib import admin

from .models import Comment, Follow, Group, LatLon, Map, Post


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
        'post',
        'author'
    )


class LatLonAdmin(admin.ModelAdmin):
    list_display = (
        'lat',
        'lon',

    )


admin.site.register(Post, PostAdmin)
admin.site.register(Group)
admin.site.register(Comment)
admin.site.register(Follow)
admin.site.register(Map)
admin.site.register(LatLon)
