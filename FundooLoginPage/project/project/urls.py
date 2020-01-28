
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token
from snippets import views
from snippets.views import login, Login,home, Registrations, activate, ForgotPassword, Logout, reset_password,ResetPassword,session
from django_short_url.views import get_surl
from django_short_url.models import ShortURL
from rest_framework import routers
from note.note_api import NoteViewSet
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_jwt_token), 
    path('api/token/', obtain_jwt_token), 
    path('login/', views.Login.as_view(), name='login'),
    path('activate/<slug:surl>/', views.activate, name='activate'),
    path('registration/', views.Registrations.as_view(), name="registration"),

    path('forgotpassword/', views.ForgotPassword.as_view(),name="forgotPassword"),
    # path('activate/<surl>/', views.activate, name="activate"),
    # path('reset_password/<slug:surl>/', views.reset_password, name="reset_password"),
    # path('resetpassword/<user_reset>', views.ResetPassword.as_view(), name="resetpassword"),
    path('logout/', views.Logout.as_view() ,name="logout"),
    # path('session/', views.session),
    path('reset_password/<surl>/', views.reset_password, name="reset_password"),
    path('resetpassword/<user_reset>/',
         views.ResetPassword.as_view(), name="resetpassword"),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path("", views.home, name="home"),

    url(r'^', include('note.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
    
    

]

