from django.urls import path, include
from rest_framework_jwt import views
from rest_framework_jwt.views import obtain_jwt_token
from snippets.views import Login, Registration
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('api/auth/', obtain_jwt_token),
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Registration.as_view(), name='register'),
    path('activate/<surl>/', views.activate, name="activate"),
]