# Generated by Django 2.0 on 2021-10-18 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20211018_1435'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='users',
            new_name='users_new',
        ),
    ]