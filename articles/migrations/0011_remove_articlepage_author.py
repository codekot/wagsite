# Generated by Django 2.1.8 on 2019-05-14 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_articlepage_writer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlepage',
            name='author',
        ),
    ]