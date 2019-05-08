# Generated by Django 2.1.8 on 2019-05-07 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stories', '0005_auto_20190507_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storypage',
            name='available_authors',
        ),
        migrations.AddField(
            model_name='storypage',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
