# Generated by Django 4.0.4 on 2022-07-26 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0021_alter_comment_publication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='publication',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.publication'),
        ),
    ]
