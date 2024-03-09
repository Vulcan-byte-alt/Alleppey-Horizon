from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from register import views as v


app_name = 'socialaccount'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("allauth.urls")),
    path('register/', v.register, name='register'),
    path('', include('main.urls')),  # Adjust this line based on your app's URL configuration
    path('', include('django.contrib.auth.urls')),
    path('main/', include('django.contrib.auth.urls')),
    
]
