# Generated by Django 4.1 on 2022-10-13 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_alter_latlon_lat_alter_latlon_lon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='latlon',
            name='lat',
            field=models.DecimalField(decimal_places=8, max_digits=8),
        ),
        migrations.AlterField(
            model_name='latlon',
            name='lon',
            field=models.DecimalField(decimal_places=8, max_digits=8),
        ),
    ]
