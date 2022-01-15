from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('' , include('accounts.urls')),
    path('home' , include('cart.urls')),
    path('admin/', admin.site.urls),
]