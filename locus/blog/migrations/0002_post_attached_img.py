# Generated by Django 3.0.7 on 2020-06-18 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='attached_img',
            field=models.ImageField(blank=True, upload_to='post_images'),
        ),
    ]
