# Generated by Django 4.0.4 on 2022-07-06 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_remove_publication_tags_publication_tag1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='photo4',
            field=models.ImageField(blank=True, upload_to='firstapp/static/img'),
        ),
        migrations.AddField(
            model_name='publication',
            name='photo5',
            field=models.ImageField(blank=True, upload_to='firstapp/static/img'),
        ),
        migrations.AddField(
            model_name='publication',
            name='tag5',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
