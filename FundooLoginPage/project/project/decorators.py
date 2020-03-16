from functools import wraps
from project import settings
from .settings import SECRET_KEY
# from redis_class import Redis
# rdb=Redis()
from snippets import token
import jwt 
# User = get_user_model()
from datetime import timedelta
import datetime
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, get_user_model
def login_required(func=None):
    
    @wraps(func)
    def wrapper(request,user_id=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            token = request.headers.get('token')
            if token is not None:
                print("token")
                mytoken=jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
                user_id=mytoken.get('username')
                print(user_id)
                return func(request,user_id)
        except:
            return Http404('Board not found')
    return wrapper


