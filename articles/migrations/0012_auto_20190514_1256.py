# Generated by Django 2.1.8 on 2019-05-14 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_remove_articlepage_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlepage',
            old_name='writer',
            new_name='author',
        ),
    ]
