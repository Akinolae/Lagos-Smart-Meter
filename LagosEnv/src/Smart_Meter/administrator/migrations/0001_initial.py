# Generated by Django 3.0.5 on 2020-04-07 08:28

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', cloudinary.models.CloudinaryField(max_length=255, verbose_name='avatar')),
                ('about_me', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
