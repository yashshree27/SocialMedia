# Generated by Django 3.2 on 2021-10-21 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users_new',
            name='acc_created',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]