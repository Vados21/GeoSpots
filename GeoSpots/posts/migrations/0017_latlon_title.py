# Generated by Django 4.1 on 2022-10-14 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0016_remove_latlon_post_post_coor'),
    ]

    operations = [
        migrations.AddField(
            model_name='latlon',
            name='title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
