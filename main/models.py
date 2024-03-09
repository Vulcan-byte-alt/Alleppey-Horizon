from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=64, unique=True)
    username = models.CharField(max_length=150, unique=False)
    password = models.CharField(max_length=128)
    number = models.CharField(max_length=64)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class AyurvedaBooking(models.Model):
    def get_default_user():
        return CustomUser.objects.first()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=get_default_user)
    treatment = models.CharField(max_length=255)
    booking_date = models.DateField()
    persons = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    booking_placed_date = models.DateTimeField(auto_now_add=True,null=True)
    payment_completed = models.BooleanField(default=False)

    def __str__(self):
        ist_booking_placed_date = self.booking_placed_date.astimezone(timezone.get_current_timezone())
        return f"{self.treatment} - {self.user.username} - {self.booking_date} - {ist_booking_placed_date}"
    
    

class AyurvedaPayment(models.Model):
    def get_default_user():
        return CustomUser.objects.first()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=get_default_user)
    booking = models.ForeignKey(AyurvedaBooking, on_delete=models.CASCADE, null=True)
    card_type = models.CharField(max_length=10)
    card_number = models.CharField(max_length=16)
    expiry_date = models.CharField(max_length=5)
    cvv = models.CharField(max_length=3)
    cardholder_name = models.CharField(max_length=255)

    def __init__(self, *args, **kwargs):
        super(AyurvedaPayment, self).__init__(*args, **kwargs)
        # Your additional initialization logic can go here

class ShikaraBooking(models.Model):
    def get_default_user():
        return CustomUser.objects.first()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=get_default_user)
    shikara_ride = models.CharField(max_length=25)
    booking_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    booking_placed_date = models.DateTimeField(auto_now_add=True, null=True)
    payment_completed = models.BooleanField(default=False)

    def __str__(self):
        ist_booking_placed_date = self.booking_placed_date.astimezone(timezone.get_current_timezone())
        return f"{self.shikara_ride} - {self.user.username} - {self.booking_date} - {ist_booking_placed_date}"
    

class ShikaraPayment(models.Model):
    def get_default_user():
        return CustomUser.objects.first()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=get_default_user)
    booking = models.ForeignKey(ShikaraBooking, on_delete=models.CASCADE, null=True)
    card_type = models.CharField(max_length=10)
    card_number = models.CharField(max_length=16)
    expiry_date = models.CharField(max_length=5)
    cvv = models.CharField(max_length=3)
    cardholder_name = models.CharField(max_length=255)

    def __init__(self, *args, **kwargs):
        super(ShikaraPayment, self).__init__(*args, **kwargs)
        # Your additional initialization logic can go here


class DeluxeBooking(models.Model):
    def get_default_user():
        return CustomUser.objects.first()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=get_default_user)
    no_rooms = models.IntegerField()
    no_person = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    booking_placed_date = models.DateTimeField(auto_now_add=True, null=True)
    payment_completed = models.BooleanField(default=False)

    def __str__(self):
        ist_booking_placed_date = self.booking_placed_date.astimezone(timezone.get_current_timezone())
        return f"{self.user.username} - {self.no_rooms} rooms - {self.no_person} persons - {self.start_date} to {self.end_date} - {ist_booking_placed_date}"
    
class PremiumBooking(models.Model):
    def get_default_user():
        return CustomUser.objects.first()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=get_default_user)
    no_rooms = models.IntegerField()
    no_person = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    booking_placed_date = models.DateTimeField(auto_now_add=True, null=True)
    payment_completed = models.BooleanField(default=False)

    def __str__(self):
        ist_booking_placed_date = self.booking_placed_date.astimezone(timezone.get_current_timezone())
        return f"{self.user.username} - {self.no_rooms} rooms - {self.no_person} persons - {self.start_date} to {self.end_date} - {ist_booking_placed_date}"

class LuxuryBooking(models.Model):
    def get_default_user():
        return CustomUser.objects.first()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=get_default_user)
    no_rooms = models.IntegerField()
    no_person = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    booking_placed_date = models.DateTimeField(auto_now_add=True, null=True)
    payment_completed = models.BooleanField(default=False)

    def __str__(self):
        ist_booking_placed_date = self.booking_placed_date.astimezone(timezone.get_current_timezone())
        return f"{self.user.username} - {self.no_rooms} rooms - {self.no_person} persons - {self.start_date} to {self.end_date} - {ist_booking_placed_date}"

class DeluxePayment(models.Model):
    def get_default_user():
        return CustomUser.objects.first()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=get_default_user)
    booking = models.ForeignKey(DeluxeBooking, on_delete=models.CASCADE, null=True)
    card_type = models.CharField(max_length=10)
    card_number = models.CharField(max_length=16)
    expiry_date = models.CharField(max_length=5)
    cvv = models.CharField(max_length=3)
    cardholder_name = models.CharField(max_length=255)

    def __init__(self, *args, **kwargs):
        super(DeluxePayment, self).__init__(*args, **kwargs)

class PremiumPayment(models.Model):
    def get_default_user():
        return CustomUser.objects.first()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=get_default_user)
    booking = models.ForeignKey(PremiumBooking, on_delete=models.CASCADE, null=True)
    card_type = models.CharField(max_length=10)
    card_number = models.CharField(max_length=16)
    expiry_date = models.CharField(max_length=5)
    cvv = models.CharField(max_length=3)
    cardholder_name = models.CharField(max_length=255)

    def __init__(self, *args, **kwargs):
        super(PremiumPayment, self).__init__(*args, **kwargs)

class LuxuryPayment(models.Model):
    def get_default_user():
        return CustomUser.objects.first()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=get_default_user)
    booking = models.ForeignKey(LuxuryBooking, on_delete=models.CASCADE, null=True)
    card_type = models.CharField(max_length=10)
    card_number = models.CharField(max_length=16)
    expiry_date = models.CharField(max_length=5)
    cvv = models.CharField(max_length=3)
    cardholder_name = models.CharField(max_length=255)

    def __init__(self, *args, **kwargs):
        super(LuxuryPayment, self).__init__(*args, **kwargs)


class HotelBooking(models.Model):
    def get_default_user():
        return CustomUser.objects.first()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=get_default_user) 
    Hotel = models.CharField(max_length=20)
    rooms = models.CharField(max_length=30,null=True)
    price = models.CharField(max_length=255)
    CheckIn = models.CharField(max_length=255)
    payment_completed = models.BooleanField(default=False)
   
class ResortBooking(models.Model):
    def get_default_user():
        return CustomUser.objects.first()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=get_default_user) 
    Resort = models.CharField(max_length=20)
    rooms = models.CharField(max_length=30,null=True)
    price = models.CharField(max_length=255)
    CheckIn = models.CharField(max_length=255)
    payment_completed = models.BooleanField(default=False)

class HotelPayment(models.Model):
    def get_default_user():
        return CustomUser.objects.first()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=get_default_user)
    booking = models.ForeignKey(HotelBooking, on_delete=models.CASCADE, null=True)
    card_type = models.CharField(max_length=10)
    card_number = models.CharField(max_length=16)
    expiry_date = models.CharField(max_length=5)
    cvv = models.CharField(max_length=3)
    cardholder_name = models.CharField(max_length=255)

    def __init__(self, *args, **kwargs):
        super(HotelPayment, self).__init__(*args, **kwargs)

class ResortPayment(models.Model):
    def get_default_user():
        return CustomUser.objects.first()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=get_default_user)
    booking = models.ForeignKey(ResortBooking, on_delete=models.CASCADE, null=True)
    card_type = models.CharField(max_length=10)
    card_number = models.CharField(max_length=16)
    expiry_date = models.CharField(max_length=5)
    cvv = models.CharField(max_length=3)
    cardholder_name = models.CharField(max_length=255)

    def __init__(self, *args, **kwargs):
        super(ResortPayment, self).__init__(*args, **kwargs)

class Contact(models.Model):
    def get_default_user():
        return CustomUser.objects.first()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=get_default_user)
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=254)
    subject = models.TextField()
    message = models.TextField()
