# Generated by Django 3.1.7 on 2022-05-19 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_auto_20211206_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='image',
        ),
        migrations.AddField(
            model_name='pet',
            name='image_url',
            field=models.URLField(default='https://images.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500'),
            preserve_default=False,
        ),
    ]
