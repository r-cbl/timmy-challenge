# Generated by Django 4.1.5 on 2023-01-20 05:53

from django.db import migrations, models
import timmy_mountains.models


class Migration(migrations.Migration):

    dependencies = [
        ('timmy_mountains', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mountain',
            name='content',
            field=models.TextField(max_length=100000, validators=[timmy_mountains.models.is_mountain]),
        ),
        migrations.AlterField(
            model_name='mountainwithtunnels',
            name='content',
            field=models.TextField(max_length=1000, validators=[timmy_mountains.models.is_mountain_with_tunnels]),
        ),
    ]