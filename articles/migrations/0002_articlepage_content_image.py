# Generated by Django 2.1.8 on 2019-04-24 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepage',
            name='content_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
