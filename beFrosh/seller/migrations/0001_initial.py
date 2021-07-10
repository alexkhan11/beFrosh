# Generated by Django 3.2.3 on 2021-07-09 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=128)),
                ('province', models.CharField(max_length=128)),
                ('district', models.CharField(max_length=128)),
                ('region', models.CharField(max_length=128)),
                ('street', models.CharField(max_length=128)),
                ('address_line', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(null=True, upload_to='')),
                ('phone_no', models.IntegerField()),
                ('whatsapp_no', models.IntegerField(null=True)),
                ('rating', models.FloatField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Location', to='seller.location')),
                ('user_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
