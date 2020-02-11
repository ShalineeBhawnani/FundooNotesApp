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

#rdb = redis_class.Redis()

def requires_auth(function=None):
    def wraps(request, *args,**kwargs):
        token = jwt.decode(request.user.username,SECRET_KEY, algorithm="HS256")
        cache.get(request.user.username)
        print(request.user.username)
        print(token)
        return function(token)
    return wraps