# Generated by Django 2.0 on 2021-10-18 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20211018_1355'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='users',
        ),
    ]