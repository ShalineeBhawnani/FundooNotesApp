from django.contrib import admin
from django.urls import path
from .views import login, register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login', login),
    path('api/register', register)
]