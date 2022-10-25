# Generated by Django 4.1 on 2022-10-17 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0018_latlon_destination_alter_group_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='latlon',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='latlon',
            name='lon',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True),
        ),
    ]