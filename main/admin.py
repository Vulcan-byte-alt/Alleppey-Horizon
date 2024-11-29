from django.contrib import admin
from django.contrib.auth.models import User
from .models import CustomUser
from .models import AyurvedaBooking
from django.utils.translation import gettext as _
from .models import AyurvedaPayment
from .models import ShikaraBooking
from .models import ShikaraPayment
from .models import DeluxeBooking
from .models import PremiumBooking
from .models import LuxuryBooking
from .models import DeluxePayment
from .models import PremiumPayment
from .models import LuxuryPayment
from .models import HotelBooking
from .models import ResortBooking
from .models import HotelPayment
from .models import ResortPayment
from .models import contact


# CustomUserAdmin
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'number')
    search_fields = ('username', 'email', 'number')

@admin.register(AyurvedaBooking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'treatment', 'booking_date', 'persons', 'total_price', 'booking_placed_date', 'payment_completed')
    search_fields = ('user__username', 'treatment', 'booking_date')
    list_filter = ('booking_placed_date', 'payment_completed')

@admin.register(ShikaraBooking)
class ShikaraBookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'shikara_ride', 'booking_date', 'price', 'booking_placed_date', 'payment_completed')
    search_fields = ('user__username', 'shikara_ride', 'booking_date')
    list_filter = ('shikara_ride', 'booking_placed_date', 'payment_completed')

@admin.register(DeluxeBooking)
class DeluxeBookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'no_rooms', 'no_person', 'start_date', 'end_date', 'price', 'booking_placed_date', 'payment_completed')
    search_fields = ('user__username', 'no_rooms', 'no_person', 'start_date')
    list_filter = ('booking_placed_date', 'payment_completed')

@admin.register(PremiumBooking)
class PremiumBookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'no_rooms', 'no_person', 'start_date', 'end_date', 'booking_placed_date', 'price', 'payment_completed')
    search_fields = ('user__username', 'no_rooms', 'no_person', 'start_date')
    list_filter = ('booking_placed_date', 'payment_completed')

@admin.register(LuxuryBooking)
class LuxuryBookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'no_rooms', 'no_person', 'start_date', 'end_date', 'price', 'booking_placed_date', 'payment_completed')
    search_fields = ('user__username', 'no_rooms', 'no_person', 'start_date')
    list_filter = ('booking_placed_date', 'payment_completed')

@admin.register(HotelBooking)
class HotelBooking(admin.ModelAdmin):
    list_display = ('user', 'Hotel','rooms', 'price', 'CheckIn','payment_completed')
    search_fields = ('user__username',)
    list_filter = ('CheckIn',)

@admin.register(ResortBooking)
class ResortBooking(admin.ModelAdmin):
    list_display = ('user', 'Resort','rooms', 'price', 'CheckIn','payment_completed')
    search_fields = ('user__username',)
    list_filter = ('CheckIn',)

@admin.register(contact)
class Contact(admin.ModelAdmin):
    list_display = ('user','name','email','subject','message')
    search_fields = ('user__username','email')

class BasePaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'card_type', 'card_number', 'expiry_date', 'cvv', 'cardholder_name']
    search_fields = ['user__username', 'cardholder_name', 'card_number']

@admin.register(DeluxePayment)
class DeluxePaymentAdmin(BasePaymentAdmin):
    pass

@admin.register(PremiumPayment)
class PremiumPaymentAdmin(BasePaymentAdmin):
    pass

@admin.register(LuxuryPayment)
class LuxuryPaymentAdmin(BasePaymentAdmin):
    pass

@admin.register(AyurvedaPayment)
class AyurvedaPaymentAdmin(BasePaymentAdmin):
    pass

@admin.register(ShikaraPayment)
class ShikaraPaymentAdmin(BasePaymentAdmin):
    pass

@admin.register(HotelPayment)
class HotelPaymentAdmin(BasePaymentAdmin):
    pass

@admin.register(ResortPayment)
class ResortPaymentAdmin(BasePaymentAdmin):
    pass