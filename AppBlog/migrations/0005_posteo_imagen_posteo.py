# Generated by Django 4.1 on 2022-10-09 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0004_remove_posteo_imagen_posteo'),
    ]

    operations = [
        migrations.AddField(
            model_name='posteo',
            name='imagen_posteo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
