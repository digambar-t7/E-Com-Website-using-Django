# Generated by Django 3.2.6 on 2021-10-29 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20211029_1759'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogPosts',
            new_name='BlogPost',
        ),
    ]
