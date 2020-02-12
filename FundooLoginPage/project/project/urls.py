
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token
# from snippets import views
# from snippets.views import login, Login, Registrations, activate, ForgotPassword, Logout, reset_password,ResetPassword,session
from django_short_url.views import get_surl
from django_short_url.models import ShortURL
from rest_framework_jwt import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_jwt_token), 
    path('api/token/', obtain_jwt_token), 
    #path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    #path('social-auth/', include('social_django.urls', namespace="social")),
    # path("", views.home, name="home"),
    #path('api-auth/', include('rest_framework.urls')),
    path('', include('snippets.urls')),
    path('', include('note.urls')),
]

