# Generated by Django 3.1 on 2021-07-01 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seller',
            old_name='user_name',
            new_name='root_user',
        ),
    ]
