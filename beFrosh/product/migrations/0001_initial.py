# Generated by Django 3.2.3 on 2021-07-09 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('seller', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('desc', models.CharField(max_length=512)),
                ('image', models.ImageField(upload_to='product-images')),
                ('price', models.FloatField()),
                ('quality', models.CharField(max_length=128)),
                ('catagory', models.CharField(max_length=128)),
                ('sold_status', models.BooleanField(default=False)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.location')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.seller')),
            ],
        ),
    ]
