from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth import logout as django_logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from .models import AyurvedaBooking
from django.urls import reverse
from .models import Contact
from .models import CustomUser
from .models import HotelPayment
from .models import HotelBooking
from .models import ResortPayment
from .models import DeluxeBooking
from .models import LuxuryBooking
from .models import DeluxePayment
from .models import LuxuryPayment
from .models import ResortBooking
from .models import ShikaraBooking
from .models import ShikaraPayment
from .models import PremiumBooking
from .models import PremiumPayment
from .models import AyurvedaPayment
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic.edit import UpdateView, DeleteView


@never_cache
def home(request):
    form_submitted = request.session.pop('form_submitted', False)
    context = {'form_submitted': form_submitted}
    return render(request, "main/home.html",context )

def view(request):
    return render(request, "main/view.html", {})

from django.shortcuts import redirect

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, email=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                
                # Check if the user is a superuser
                if user.is_superuser:
                    # Redirect superusers to the Django admin
                    return redirect(reverse('admin:index'))
                
                # Redirect other users to the user view upon successful login
                return redirect('/')  # Assuming '/' is the URL name for the user view
            else:
                return render(request, 'main/signin.html', {'message': 'The account is not active'})
        else:
            return render(request, 'main/error.html', {'message': 'Email or password is incorrect'})

    return render(request, 'main/signin.html')



@login_required
def user(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        print(request.user.username)  # Check if the username is accessible
    else:
        print("User is not authenticated")  # Check if the user is not autheticated

    context = {
        'user' : request.user,
    }
    print(request.user.username)  # Check if the username is printed in the console for debugging purposes      
    return render(request, 'main/user.html', context)

User = get_user_model()

def is_common_password(password):
    common_passwords = ["password", "123456", "qwerty", "abc123"]  # Add more common passwords
    return password.lower() in common_passwords

def is_weak_password(password):
    return len(password) < 8 or password.isdigit()

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        number = request.POST.get('number')

        # Custom password validation
        if is_common_password(password):
            messages.error(request, 'Password is too common.')
        elif is_weak_password(password):
            messages.error(request, 'Password must be at least 8 characters and not all numeric.')
        else:
            # Create a CustomUser object but do not save it yet
            hashed_password = make_password(password)
            new_user = User.objects.create(username=username, email=email, password=hashed_password, number=number)

            # Log in the user
            request.session['user_id'] = new_user.id

            # Redirect to the service view after successful signup
            return redirect('user')

    return render(request, "main/signup.html")


def app_logout(request):
    django_logout(request)
    return redirect("home")  # Redirect users to the home page or any desired URL after logout


@login_required
def houseboat(request):
    return render(request, "main/houseboat.html", {})

@login_required
def deluxe(request):
    if request.method == "POST":
        user = request.user
        no_room = request.POST.get('numRooms')
        no_person = request.POST.get('numPersons')
        start_date = request.POST.get('startDate')
        end_date = request.POST.get('endDate')
        price = request.POST.get('hidden_total_price')

        deluxe = DeluxeBooking(user=user , no_rooms=no_room , no_person=no_person, start_date=start_date, end_date=end_date, price=price)
        deluxe.save()
        return redirect('payment',booking_id=deluxe.id)
    
    return render(request, "main/deluxe.html", {})

@login_required
def premium(request):
    if request.method == "POST":
        user = request.user
        no_room = request.POST.get('numRooms')
        no_person = request.POST.get('numPersons')
        start_date = request.POST.get('startDate')
        end_date = request.POST.get('endDate')
        price = request.POST.get('hiddenTotalPrice')

        premium = PremiumBooking(user=user , no_rooms=no_room , no_person=no_person, start_date=start_date, end_date=end_date, price=price)
        premium.save()
        return redirect('premium_payment',booking_id=premium.id)
    
    return render(request, "main/premium.html", {})

@login_required
def luxury(request):
    if request.method == "POST":
        user = request.user
        no_room = request.POST.get('numRooms')
        no_person = request.POST.get('numPersons')
        start_date = request.POST.get('startDate')
        end_date = request.POST.get('endDate')
        price = request.POST.get('hidden_total_price')

        luxury = LuxuryBooking(user=user , no_rooms=no_room , no_person=no_person, start_date=start_date, end_date=end_date, price=price)
        luxury.save()
        return redirect('luxury_payment',booking_id=luxury.id)
    
    return render(request, "main/luxury.html", {})

def details(request):
    return render(request,"main/details.html", {})

@login_required
def payment(request, booking_id):
    booking = get_object_or_404(DeluxeBooking, pk=booking_id)

    if request.method == 'POST':
        user = request.user
        card_type = request.POST.get("card-type")
        card_number = request.POST.get("card-number")
        expiry_date = request.POST.get("expiry-date")
        cvv = request.POST.get("cvv")
        cardholder_name = request.POST.get("cardholder-name")

        deluxe_payment_instance = DeluxePayment(user=user, booking=booking, card_type=card_type, card_number=card_number, expiry_date=expiry_date, cvv=cvv, cardholder_name=cardholder_name)
        deluxe_payment_instance.save()

        # Update the payment_completed field in the Booking model
        booking.payment_completed = True
        booking.save()

        return render(request, "main/home.html", {})

    return render(request, "main/payment.html", {'booking': booking})

@login_required
def premiumpayment(request, booking_id):
    booking = get_object_or_404(PremiumBooking, pk=booking_id)

    if request.method == 'POST':
        user = request.user
        card_type = request.POST.get("card-type")
        card_number = request.POST.get("card-number")
        expiry_date = request.POST.get("expiry-date")
        cvv = request.POST.get("cvv")
        cardholder_name = request.POST.get("cardholder-name")

        premium_payment_instance = PremiumPayment(user=user, booking=booking, card_type=card_type, card_number=card_number, expiry_date=expiry_date, cvv=cvv, cardholder_name=cardholder_name)
        premium_payment_instance.save()

        # Update the payment_completed field in the Booking model
        booking.payment_completed = True
        booking.save()

        return render(request, "main/home.html", {})

    return render(request, "main/premium_payment.html", {'booking': booking})

@login_required
def luxurypayment(request, booking_id):
    booking = get_object_or_404(LuxuryBooking, pk=booking_id)

    if request.method == 'POST':
        user = request.user
        card_type = request.POST.get("card-type")
        card_number = request.POST.get("card-number")
        expiry_date = request.POST.get("expiry-date")
        cvv = request.POST.get("cvv")
        cardholder_name = request.POST.get("cardholder-name")

        luxury_payment_instance = LuxuryPayment(user=user, booking=booking, card_type=card_type, card_number=card_number, expiry_date=expiry_date, cvv=cvv, cardholder_name=cardholder_name)
        luxury_payment_instance.save()

        # Update the payment_completed field in the Booking model
        booking.payment_completed = True
        booking.save()

        return render(request, "main/home.html", {})

    return render(request, "main/luxury_payment.html", {'booking': booking})


def ayurveda_home(request):
    return render(request,"main/ayurveda_home.html", {})

@login_required
def ayurveda_booking(request):
    if request.method == 'POST':
        user = request.user
        treatment = request.POST.get("treatment")
        booking_date = request.POST.get("booking_date")
        persons = request.POST.get("persons")
        total_price = request.POST.get("hidden_total_price")

        booking = AyurvedaBooking(user=user, treatment=treatment, booking_date=booking_date, persons=persons, total_price=total_price)
        booking.save()

        # Redirect to ayurveda_payment view with booking ID as a parameter
        return redirect('process_ayurveda_payment', booking_id=booking.id)

    return render(request, "main/ayurveda_booking.html", {})

@login_required
def process_ayurveda_payment(request, booking_id):
    booking = AyurvedaBooking.objects.get(pk=booking_id)

    if request.method == 'POST':
        user = request.user
        card_type = request.POST.get("card-type")
        card_number = request.POST.get("card-number")
        expiry_date = request.POST.get("expiry-date")
        cvv = request.POST.get("cvv")
        cardholder_name = request.POST.get("cardholder-name")

        ayurveda_payment_instance = AyurvedaPayment(user=user, booking=booking, card_type=card_type, card_number=card_number, expiry_date=expiry_date, cvv=cvv, cardholder_name=cardholder_name)
        ayurveda_payment_instance.save()

        # Update the payment_completed field in the Booking model
        booking.payment_completed = True
        booking.save()

        return render(request, "main/home.html", {})

    return render(request, "main/ayurveda_payment.html", {'booking': booking})


def ayurveda_details(request):
    return render(request,"main/ayurveda_details.html", {})


def shikara_home(request):
    return render(request,"main/shikara_home.html", {})


@login_required
def shikara(request):

    return render(request,"main/shikara.html", {})

@login_required
def shikara_booking(request):

    if request.method == "POST":
        user = request.user
        ride_Type = request.POST.get("rideType")
        bookingDate = request.POST.get("bookingDate")
        price = request.POST.get("hidden_total_price")
        shikara = ShikaraBooking(user=user, shikara_ride=ride_Type, booking_date=bookingDate, price=price)
        shikara.save()

        return redirect('shikara_payment', booking_id=shikara.id)  # Use shikara.id instead of booking.id

    return render(request, "main/shikara_booking.html", {})

@login_required
def shikara_payment(request, booking_id):  # Add booking_id as a parameter

    booking = ShikaraBooking.objects.get(pk=booking_id)

    if request.method == 'POST':
        user = request.user
        card_type = request.POST.get("card-type")
        card_number = request.POST.get("card-number")
        expiry_date = request.POST.get("expiry-date")
        cvv = request.POST.get("cvv")
        cardholder_name = request.POST.get("cardholder-name")

        shikara_payment = ShikaraPayment(
            user=user, booking=booking, card_type=card_type, card_number=card_number,
            expiry_date=expiry_date, cvv=cvv, cardholder_name=cardholder_name
        )
        shikara_payment.save()

        # Update the payment_completed field in the Booking model
        booking.payment_completed = True
        booking.save()

        return render(request, "main/home.html", {})

    return render(request, "main/shikara_payment.html", {'shikara': booking})


@login_required
def user_bookings(request):
    # Retrieve bookings for the logged-in user
    user_bookings = ShikaraBooking.objects.filter(user=request.user)
    return render(request, 'main/shikara_view.html', {'user_bookings': user_bookings})

@login_required
def ayurveda_bookings(request):
    # Retrieve Ayurveda bookings for the logged-in user
    user_bookings = AyurvedaBooking.objects.filter(user=request.user)
    return render(request, "main/ayurveda_view.html", {'user_bookings': user_bookings})

def houseboat_home(request):
    return render(request,"main/houseboat_home.html", {})

@login_required
def deluxe_bookings(request):
    # Retrieve Deluxe Houseboat bookings for the logged-in user
    user_deluxe_bookings = DeluxeBooking.objects.filter(user=request.user)
    
    # Pass the Deluxe Houseboat booking data to the template context
    context = {
        'user_deluxe_bookings': user_deluxe_bookings,
    }

    # Render the user homepage with the Deluxe Houseboat booking data
    return render(request, "main/deluxe_view.html", context)

@login_required
def premium_bookings(request):
    # Retrieve Deluxe Houseboat bookings for the logged-in user
    user_premium_bookings = PremiumBooking.objects.filter(user=request.user)
    
    # Pass the Deluxe Houseboat booking data to the template context
    context = {
        'user_premium_bookings': user_premium_bookings,
    }

    # Render the user homepage with the Deluxe Houseboat booking data
    return render(request, "main/premium_view.html", context)

@login_required
def luxury_bookings(request):
    # Retrieve Deluxe Houseboat bookings for the logged-in user
    user_luxury_bookings = LuxuryBooking.objects.filter(user=request.user)
    
    # Pass the Deluxe Houseboat booking data to the template context
    context = {
        'user_luxury_bookings': user_luxury_bookings,
    }

    # Render the user homepage with the Deluxe Houseboat booking data
    return render(request, "main/luxury_view.html", context)

@method_decorator(login_required, name='dispatch')
class UserDetailView(DetailView):
    model = CustomUser
    template_name = 'main/user_detail.html'

    def get_object(self):
        return self.request.user

@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = CustomUser
    fields = ('username', 'email', 'number')
    template_name = 'main/user_update.html'
    success_url = reverse_lazy('account')

    def get_object(self):
        return self.request.user

@method_decorator(login_required, name='dispatch')
class UserDeleteView(DeleteView):
    model = CustomUser
    template_name = 'main/user_delete.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


@login_required
def hotels(request):
    return render(request, 'main/hotels.html',{})

@login_required
def ramada(request):
    if request.method == 'POST':
        user = request.user
        Hotel = "Ramada"
        rooms = request.POST.get('numRooms')
        price = request.POST.get('hidden_total_price')
        CheckIn = request.POST.get('date')

        hotel = HotelBooking(user=user , Hotel=Hotel , rooms=rooms, price=price, CheckIn=CheckIn)
        hotel.save()
        return redirect('hotel_payment', booking_id=hotel.id)

    return render(request, 'main/ramada.html', {})


@login_required
def beach_resorts(request):
    if request.method == 'POST':
        user = request.user
        Resort = "Beach Resorts"
        rooms = request.POST.get('numRooms')
        price = request.POST.get('hidden_total_price')
        CheckIn = request.POST.get('date')

        resort = ResortBooking(user=user , Resort=Resort , rooms=rooms, price=price, CheckIn=CheckIn)
        resort.save()
        return redirect('resort_payment',booking_id=resort.id)
    
    return render(request,'main/beach_resorts.html',{})

@login_required
def turtle_resort(request):
    if request.method == 'POST':
        user = request.user
        Resort = "Abad  Turtle Resort"
        rooms = request.POST.get('numRooms')
        price = request.POST.get('hidden_total_price')
        CheckIn = request.POST.get('date')

        resort = ResortBooking(user=user , Resort=Resort , rooms=rooms, price=price, CheckIn=CheckIn)
        resort.save()
        return redirect('resort_payment',booking_id=resort.id)

    return render(request,'main/abad.html',{})

@login_required
def palace_resort(request): 
    if request.method == 'POST':
        user = request.user
        Resort = "Lake Palace"
        rooms = request.POST.get('numRooms')
        price = request.POST.get('hidden_total_price')
        CheckIn = request.POST.get('date')

        resort = ResortBooking(user=user , Resort=Resort , rooms=rooms, price=price, CheckIn=CheckIn)
        resort.save()
        return redirect('resort_payment',booking_id=resort.id)

    return render(request,'main/palace.html',{})

@login_required
def regency(request):
    if request.method == 'POST':
        user = request.user
        Hotel = "Classic Regency"
        rooms = request.POST.get('numRooms')
        price = request.POST.get('hidden_total_price')
        CheckIn = request.POST.get('date')

        hotel = HotelBooking(user=user , Hotel=Hotel , rooms=rooms, price=price, CheckIn=CheckIn)
        hotel.save()
        return redirect('hotel_payment',booking_id=hotel.id)

    return render(request,'main/regency.html',{})

@login_required
def raheem(request):
    if request.method == 'POST':
        user = request.user
        Resort = "Raheem Residency"
        rooms = request.POST.get('numRooms')
        price = request.POST.get('hidden_total_price')
        CheckIn = request.POST.get('date')

        resort = ResortBooking(user=user , Resort=Resort , rooms=rooms, price=price, CheckIn=CheckIn)
        resort.save()
        return redirect('resort_payment',booking_id=resort.id)

    return render(request,'main/raheem.html',{})

@login_required
def marari(request):
    if request.method == 'POST':
        user = request.user
        Resort = "Marari Village Beach Resort"
        rooms = request.POST.get('numRooms')
        price = request.POST.get('hidden_total_price')
        CheckIn = request.POST.get('date')

        resort = ResortBooking(user=user , Resort=Resort , rooms=rooms, price=price, CheckIn=CheckIn)
        resort.save()
        return redirect('resort_payment',booking_id=resort.id)

    return render(request,'main/marari.html',{})

@login_required
def zostel(request):
    if request.method == 'POST':
        user = request.user
        Resort = "Zostel Alleppey"
        rooms = request.POST.get('numRooms')
        price = request.POST.get('hidden_total_price')
        CheckIn = request.POST.get('date')

        resort = ResortBooking(user=user , Resort=Resort , rooms=rooms, price=price, CheckIn=CheckIn)
        resort.save()
        return redirect('resort_payment',booking_id=resort.id)

    return render(request,'main/zostel.html',{})

@login_required
def brooklands(request):
    if request.method == 'POST':
        user = request.user
        Hotel = "Brooklands"
        rooms = request.POST.get('numRooms')
        price = request.POST.get('hidden_total_price')
        CheckIn = request.POST.get('date')

        hotel = HotelBooking(user=user , Hotel=Hotel , rooms=rooms, price=price, CheckIn=CheckIn)
        hotel.save()
        return redirect('hotel_payment',booking_id=hotel.id)

    return render(request,'main/brooklands.html',{})

@login_required
def hotel_payment(request,booking_id):

    booking = HotelBooking.objects.get(pk=booking_id)

    if request.method == 'POST':
        user = request.user
        card_type = request.POST.get("card-type")
        card_number = request.POST.get("card-number")
        expiry_date = request.POST.get("expiry-date")
        cvv = request.POST.get("cvv")
        cardholder_name = request.POST.get("cardholder-name")

        hotel_payment = HotelPayment(
            user=user, booking=booking, card_type=card_type, card_number=card_number,
            expiry_date=expiry_date, cvv=cvv, cardholder_name=cardholder_name
        )
        hotel_payment.save()

        # Update the payment_completed field in the Booking model
        booking.payment_completed = True
        booking.save()

        return render(request, "main/home.html", {})

    return render(request, "main/hotel_payment.html", {'hotel': booking})

@login_required
def resort_payment(request, booking_id):

    booking = ResortBooking.objects.get(pk=booking_id)

    if request.method == 'POST':
        user = request.user
        card_type = request.POST.get("card-type")
        card_number = request.POST.get("card-number")
        expiry_date = request.POST.get("expiry-date")
        cvv = request.POST.get("cvv")
        cardholder_name = request.POST.get("cardholder-name")

        resort_payment = ResortPayment(
            user=user, booking=booking, card_type=card_type, card_number=card_number,
            expiry_date=expiry_date, cvv=cvv, cardholder_name=cardholder_name
        )
        resort_payment.save()

        # Update the payment_completed field in the Booking model
        booking.payment_completed = True
        booking.save()

        return render(request, "main/home.html", {})

    return render(request, "main/resort_payment.html", {'resort': booking})

def contact(request):
    if request.method == "POST":
        user = request.user
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        contact = Contact(user=user, name=name, email=email, subject=subject, message=message)
        contact.save()

        messages.success(request, 'Your message was submitted successfully.')
        request.session['form_submitted'] = True
        return redirect('home')
    

@login_required
def hotel_bookings(request):
    # Retrieve hotel bookings for the logged-in user
    user_hotel_bookings = HotelBooking.objects.filter(user=request.user)

    return render(request, "main/hotel_view.html", {'user_hotel_bookings': user_hotel_bookings})

@login_required
def resort_bookings(request):
    # Retrieve hotel bookings for the logged-in user
    user_resort_bookings = ResortBooking.objects.filter(user=request.user)

    return render(request, "main/resort_view.html", {'user_resort_bookings': user_resort_bookings})

def page_development(request):
    return render(request, "main/page_development.html")

def hotel_home(request):
    return render(request,'main/hotels_home.html',{})






