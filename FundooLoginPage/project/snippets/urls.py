from django.urls import path
from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token
from snippets import views
from snippets.views import login, Login,CreateProfile,AllUserList, Registrations, activate, ForgotPassword, Logout, reset_password,ResetPassword,session
from django_short_url.views import get_surl
from django_short_url.models import ShortURL
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   
    path('api-token-auth/', obtain_jwt_token), 
    path('api/token/', obtain_jwt_token), 
    path('login/', views.Login.as_view(), name='login'),
    path('activate/<slug:surl>/', views.activate, name='activate'),
    path('registration/', views.Registrations.as_view(), name="registration"),
    path('forgotpassword/', views.ForgotPassword.as_view(),name="forgotpassword"),
    path('logout/', views.Logout.as_view() ,name="logout"),
    path('reset_password/<surl>/', views.reset_password, name="reset_password"),
    path('resetpassword/<user_reset>',
         views.ResetPassword.as_view(), name="resetpassword"),
    path('session/', views.session),
    path('allusers/',views.AllUserList.as_view(),name="allusers"),
    path('profile/',CreateProfile.as_view(), name='profile'),
    #path('upload/',UploadView.as_view(), name ='file_upload'),

]

# if settings.DEBUG:
#   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)