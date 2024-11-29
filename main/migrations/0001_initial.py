# Generated by Django 5.0.1 on 2024-04-16 09:30

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
import main.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=64, unique=True)),
                ('username', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=128)),
                ('number', models.CharField(max_length=64)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AyurvedaBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treatment', models.CharField(max_length=255)),
                ('booking_date', models.DateField()),
                ('persons', models.IntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('booking_placed_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('payment_completed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(default=main.models.AyurvedaBooking.get_default_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AyurvedaPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_type', models.CharField(max_length=10)),
                ('card_number', models.CharField(max_length=16)),
                ('expiry_date', models.CharField(max_length=5)),
                ('cvv', models.CharField(max_length=3)),
                ('cardholder_name', models.CharField(max_length=255)),
                ('booking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.ayurvedabooking')),
                ('user', models.ForeignKey(default=main.models.AyurvedaPayment.get_default_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.TextField()),
                ('message', models.TextField()),
                ('user', models.ForeignKey(default=main.models.contact.get_default_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DeluxeBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_rooms', models.IntegerField()),
                ('no_person', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('booking_placed_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('payment_completed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(default=main.models.DeluxeBooking.get_default_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DeluxePayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_type', models.CharField(max_length=10)),
                ('card_number', models.CharField(max_length=16)),
                ('expiry_date', models.CharField(max_length=5)),
                ('cvv', models.CharField(max_length=3)),
                ('cardholder_name', models.CharField(max_length=255)),
                ('booking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.deluxebooking')),
                ('user', models.ForeignKey(default=main.models.DeluxePayment.get_default_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HotelBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hotel', models.CharField(max_length=20)),
                ('rooms', models.CharField(max_length=30, null=True)),
                ('price', models.CharField(max_length=255)),
                ('CheckIn', models.CharField(max_length=255)),
                ('payment_completed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(default=main.models.HotelBooking.get_default_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HotelPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_type', models.CharField(max_length=10)),
                ('card_number', models.CharField(max_length=16)),
                ('expiry_date', models.CharField(max_length=5)),
                ('cvv', models.CharField(max_length=3)),
                ('cardholder_name', models.CharField(max_length=255)),
                ('booking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.hotelbooking')),
                ('user', models.ForeignKey(default=main.models.HotelPayment.get_default_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LuxuryBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_rooms', models.IntegerField()),
                ('no_person', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('booking_placed_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('payment_completed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(default=main.models.LuxuryBooking.get_default_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LuxuryPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_type', models.CharField(max_length=10)),
                ('card_number', models.CharField(max_length=16)),
                ('expiry_date', models.CharField(max_length=5)),
                ('cvv', models.CharField(max_length=3)),
                ('cardholder_name', models.CharField(max_length=255)),
                ('booking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.luxurybooking')),
                ('user', models.ForeignKey(default=main.models.LuxuryPayment.get_default_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PremiumBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_rooms', models.IntegerField()),
                ('no_person', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('booking_placed_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('payment_completed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(default=main.models.PremiumBooking.get_default_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PremiumPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_type', models.CharField(max_length=10)),
                ('card_number', models.CharField(max_length=16)),
                ('expiry_date', models.CharField(max_length=5)),
                ('cvv', models.CharField(max_length=3)),
                ('cardholder_name', models.CharField(max_length=255)),
                ('booking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.premiumbooking')),
                ('user', models.ForeignKey(default=main.models.PremiumPayment.get_default_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResortBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Resort', models.CharField(max_length=20)),
                ('rooms', models.CharField(max_length=30, null=True)),
                ('price', models.CharField(max_length=255)),
                ('CheckIn', models.CharField(max_length=255)),
                ('payment_completed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(default=main.models.ResortBooking.get_default_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResortPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_type', models.CharField(max_length=10)),
                ('card_number', models.CharField(max_length=16)),
                ('expiry_date', models.CharField(max_length=5)),
                ('cvv', models.CharField(max_length=3)),
                ('cardholder_name', models.CharField(max_length=255)),
                ('booking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.resortbooking')),
                ('user', models.ForeignKey(default=main.models.ResortPayment.get_default_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShikaraBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shikara_ride', models.CharField(max_length=25)),
                ('booking_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('booking_placed_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('payment_completed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(default=main.models.ShikaraBooking.get_default_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShikaraPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_type', models.CharField(max_length=10)),
                ('card_number', models.CharField(max_length=16)),
                ('expiry_date', models.CharField(max_length=5)),
                ('cvv', models.CharField(max_length=3)),
                ('cardholder_name', models.CharField(max_length=255)),
                ('booking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.shikarabooking')),
                ('user', models.ForeignKey(default=main.models.ShikaraPayment.get_default_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
