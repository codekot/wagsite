# Generated by Django 2.1.8 on 2019-04-26 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_newspagegalleryimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newspagegalleryimage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='newspagegalleryimage',
            name='page',
        ),
        migrations.DeleteModel(
            name='NewsPageGalleryImage',
        ),
    ]
