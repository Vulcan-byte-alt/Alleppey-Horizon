# Generated by Django 5.0.1 on 2024-02-14 18:01

import django.db.models.deletion
import main.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_hotelbooking_rooms'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResortBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hotel', models.CharField(max_length=20)),
                ('rooms', models.CharField(max_length=30, null=True)),
                ('price', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('user', models.ForeignKey(default=main.models.ResortBooking.get_default_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]