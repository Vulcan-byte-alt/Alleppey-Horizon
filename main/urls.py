from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import UserDetailView, UserUpdateView, UserDeleteView


urlpatterns = [
    path("", views.home, name="home"),
    path("signin/", views.signin, name="signin"),
    path("signup/", views.signup, name="signup"),
    path("user/", views.user, name="user"),  # Update the URL path for the service view
    path("view/", views.view, name="view"),
    path("logout/",views.app_logout, name="app_logout"),
    path('password/', auth_views.PasswordChangeView.as_view(), name='password'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name = "main/password_reset.html"), name="reset_password"),
    path('main/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = "main/password_reset_sent.html"), name="password_reset_done"),
    path('main/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = "main/password_reset_form.html"), name="password_reset_confirm"),
    path('main/reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name = "main/password_reset_done.html"), name="password_reset_complete"),
    path('houseboat/',views.houseboat, name="houseboat"),
    path('deluxe/',views.deluxe,name="deluxe"),
    path('premium/',views.premium,name="premium"),
    path('luxury/',views.luxury,name="luxury"),
    path('details/',views.details,name="details"),
    path('payment/<int:booking_id>/',views.payment,name="payment"),
    path('premium_payment/<int:booking_id>/',views.premiumpayment,name="premium_payment"),
    path('luxury_payment/<int:booking_id>/',views.luxurypayment,name="luxury_payment"),
    path('ayurveda_booking/',views.ayurveda_booking,name="ayurvedabooking"),
    path('ayurveda_details/',views.ayurveda_details,name="ayurveda details"),
    path('ayurveda_payment/<int:booking_id>/', views.process_ayurveda_payment, name='process_ayurveda_payment'),
    path('shikara/',views.shikara,name="shikara"),
    path('shikara_booking/',views.shikara_booking,name="shikara booking"),
    path('shikara_payment/<int:booking_id>/',views.shikara_payment,name="shikara_payment"),
    path('ayurveda_home',views.ayurveda_home,name="ayurveda home"),
    path('houseboat_home',views.houseboat_home,name="houseboat home"),
    path('shikara_home/',views.shikara_home,name="shikara home"),   
    path('user_bookings/',views.user_bookings, name='user_bookings'),   
    path('ayurveda_bookings/',views.ayurveda_bookings, name='ayurveda_bookings'),
    path('deluxe_bookings/',views.deluxe_bookings, name='deluxe_bookings'),
    path('premium_bookings/',views.premium_bookings, name='premium_bookings'),
    path('luxury_bookings/',views.luxury_bookings, name='luxury_bookings'),
    path('hotels/',views.hotels, name='hotels'),
    path('hotel_home/',views.hotel_home, name='hotel_home'),
    path('ramada/',views.ramada, name='ramada'),
    path('beach_resorts/',views.beach_resorts,name='beach_resort'),
    path('abad_turtle_beach/',views.turtle_resort,name='abad_resort'),
    path('palace/',views.palace_resort,name='palace'),
    path('regency/',views.regency, name='regency'),
    path('raheem/',views.raheem, name='raheem'),
    path('marari/',views.marari, name='marari'),
    path('zostel/',views.zostel, name='zostel'),
    path('brooklands/',views.brooklands,name='brooklands'),
    path('hotel_bookings/',views.hotel_bookings,name='hotel_bookings'),
    path('resort_bookings/',views.resort_bookings,name='resort_bookings'),
    path('contact/',views.contact, name='contact'),
    path('hotel_payment/<int:booking_id>/',views.hotel_payment, name='hotel_payment'),
    path('resort_payment/<int:booking_id>/',views.resort_payment, name='resort_payment'),
    path('page_development',views.page_development, name='page_development'),
    path('account/', UserDetailView.as_view(), name='account'),
    path('account/edit/', UserUpdateView.as_view(), name='edit_account'),
    path('account/delete/', UserDeleteView.as_view(), name='delete_account'),
    
    
            # ... other paths ...
]



