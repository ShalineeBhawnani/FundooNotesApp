"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from snippets import views
from snippets.views import Login, Registrations, activate, ForgotPassword, reset_password,ResetPassword,session
from django_short_url.views import get_surl
from django_short_url.models import ShortURL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_jwt_token), 
    path('api/token/', obtain_jwt_token), 
    path('login/', views.Login.as_view(), name='login'),
    path('activate/<slug:surl>/', views.activate, name='activate'),
    path('registration/', views.Registrations.as_view(), name="registration"),

    path('forgot_password/', views.ForgotPassword.as_view(),name="forgot_Password"),
    # path('activate/<surl>/', views.activate, name="activate"),
    path('reset_password/<slug:surl>/', views.reset_password, name="reset_password"),
    path('resetpassword/<user_reset>', views.ResetPassword.as_view(), name="resetpassword"),
    # path('logout/', views.Logout.as_view() ,name="logout"),
    path('session/', views.session),   
]

