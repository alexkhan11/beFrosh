# Generated by Django 3.1 on 2021-07-11 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20210711_1138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='imgage',
            new_name='image',
        ),
    ]
