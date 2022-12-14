# Generated by Django 4.1 on 2022-11-30 11:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0029_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likes_comment',
            field=models.ManyToManyField(blank=True, related_name='comment_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars', verbose_name='Avatar'),
        ),
    ]
