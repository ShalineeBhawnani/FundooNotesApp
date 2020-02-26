from django.http import HttpResponseForbidden
from django.core.cache import cache
from rest_framework import status, exceptions
from django.http import HttpResponse
from rest_framework.authentication import get_authorization_header, BaseAuthentication
from rest_framework.response import Response
import jwt
import json
from project.settings import SECRET_KEY
from note import models
from django.shortcuts import HttpResponse, redirect, get_object_or_404
from project.redis_class import Redis
rdb=Redis()

def redirect_after_login(function):
    def wrapper(request, *args, **kwargs):
        user = request.user
        if user.id is not None:
            return redirect("/note")
        return function(request, *args, **kwargs)
    return wrapper