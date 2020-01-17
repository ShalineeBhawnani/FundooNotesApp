from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache
from django.core.mail import EmailMessage
from django_short_url.models import ShortURL
from rest_framework.exceptions import ValidationError
from smtplib import SMTPAuthenticationError
from jwt import ExpiredSignatureError
from django_short_url.views import get_surl
from django_short_url.models import ShortURL
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.decorators.clickjacking import xframe_options_deny
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.core.validators import validate_email
from django.contrib import messages
from django.conf import settings
import django
from rest_framework.views import APIView
from django.shortcuts import render, redirect
from .models import Registration
import jwt
from rest_framework.authentication import authenticate
from rest_framework.response import Response
from django.contrib.auth import login, logout
from django.db.models import Q
from rest_framework.generics import api_settings
from rest_framework.generics import GenericAPIView
from .serializers import (
    RegistrationSerializers,
    LoginSerializers,

)
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth import authenticate, get_user_model
from django_short_url.views import get_surl
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from .token import token_activation
import json
from .utils import jwt_response_payload_handler
from rest_framework_jwt.settings import api_settings
User = get_user_model
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

ACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


User = get_user_model()


class Login(GenericAPIView):
    serializer_class = LoginSerializers

    def post(self, request):
        permission_classes = [permissions.AllowAny]
        if request.user.is_authenticated:
            return Response({'details': 'user is already authenticated'})
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        qs = User.objects.filter(
            Q(username__iexact=username) or
            Q(email__iexact=email)
        ).distinct()
        if qs.count() == 1:
            user_obj = qs.first()
            if user_obj.check_password(password):
                user = user_obj
                login(request, user)
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                response = jwt_response_payload_handler(token, user)
                cache.set(user.username, token)
                print(cache.get(user.username))
                return Response({'details': 'user succesfully loggedin,thakyou'})
            return Response("check password again")
        return Response("multipale users are present with this username")


class Registration(GenericAPIView):
    serializer_class = RegistrationSerializers

    def post(self, request):
        if request.user.is_authenticated:
            return Response("your are already registred,please do login")
        data = request.data
        username = data.get('username')
        email = data.get('email')
        password1 = data.get('password1')
        password2 = data.get('password2')
        if password1 != password2:
            return Response("passwords are not matching")
        qs_name = User.objects.filter(
            Q(username__iexact=username)
        )
        qs_email = User.objects.filter(
            Q(email__iexact=email)
        )
        if qs_name.exists():
            return Response("already user id present with this username ")
        elif qs_email.exists():
            return Response("already user id present with this  email")
        else:
            user = User.objects.create(username=username, email=email)
            user.set_password(password1)
            user.is_active = False
            user.save()
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            response = jwt_response_payload_handler(token, user)

            url = str(token)
            surl = get_surl(url)
            z = surl.split("/")
            mail_subject = "Activate your account by clicking below link"
            mail_message = render_to_string('email_validation.html', {
                'user': user.username,
                'domain': get_current_site(request).domain,
                'surl': z[2]
            })
            print(mail_message)
            recipient_email = user.email
            email = EmailMessage(
                mail_subject, mail_message, to=[recipient_email])
            email.send()
            return Response({"response": response,
                             "details": "verify through your email"})


def activate(request, surl):
    """
    :param request: request is made by the used
    :param token:  token is fetched from url
    :return: will register the account
    """
    try:
        tokenobject = ShortURL.objects.get(surl=surl)
        token = tokenobject.lurl
        decode = jwt.decode(token, settings.SECRET_KEY)
        username = decode['username']
        user = User.objects.get(username=username)
        # if user is not none then user account willed be activated
        if user is not None:
            user.is_active = True
            user.save()
            return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        else:
            return HttpResponse('not valid user')
    except KeyError as e:
        return HttpResponse(e)
    except Exception as f:
        return HttpResponse(f)
