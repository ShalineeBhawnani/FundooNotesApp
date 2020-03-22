from functools import wraps
from project import settings
from .settings import SECRET_KEY
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
# from redis_class import Redis
# rdb=Redis()
from snippets import token
import jwt 
#User = get_user_model()
from datetime import timedelta
import datetime
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, get_user_model
def login_required_token(func=None):
    
    @wraps(func)
    def wrapper(request,user_id=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            token = request.headers.get('token')

            if token is None or token == '':
                raise ValueError("Token not received")

            mytoken=jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            user_id=mytoken.get('username')
            if rdb.exists(user_id):
                return function(request, user_id)
            return Response(status=status.HTTP_400_BAD_REQUEST)

        except ValueError:
            return JsonResponse(smd, status=status.HTTP_401_UNAUTHORIZED)
    return wrapper