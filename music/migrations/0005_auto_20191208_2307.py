# Generated by Django 2.2.7 on 2019-12-08 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_pictures_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pictures',
            old_name='images',
            new_name='image',
        ),
    ]