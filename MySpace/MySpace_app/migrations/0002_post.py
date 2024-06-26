# Generated by Django 5.0.4 on 2024-05-09 23:22

import datetime
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySpace_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=100)),
                ('caption', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='post_images')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('no_of_likes', models.IntegerField(default=0)),
            ],
        ),
    ]
