# Generated by Django 4.1 on 2022-10-14 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_latlon_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='point',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Point_post', to='posts.group'),
        ),
    ]
