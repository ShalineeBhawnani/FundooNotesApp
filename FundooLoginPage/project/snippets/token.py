import datetime
import pdb
import jwt
import requests
from project.settings import SECRET_KEY, AUTH_ENDPOINT
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six


def token_activation(username, password):
   

    data = {
        'username': username,
        'password': password,
        'exp': datetime.datetime.now()+datetime.timedelta(days=2)
    }
    token = jwt.encode(data, SECRET_KEY, algorithm="HS256").decode('utf-8')
    return token


def token_validation(username, password):

    data = {
        'username': username,
        'password': password
    }
    tokson = requests.post(AUTH_ENDPOINT, data=data)
    token = tokson.json()['access']
    return token

# def decode(token):
#         """
#         Decode a JWT that was issued by us.

#         Throws an InvalidTokenError on decoding failure or token expiration.
#         """
#         print(jwt.decode(token, SECRET_KEY, algorithms=['HS256']))
    
# decode('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFudSIsInBhc3N3b3JkIjoiMTIzIiwiZXhwIjoxNTg0MjU2MjQ0fQ.WVnwqIaHKFIAH7naxZqYEPUF_g1iAIunYZdTH3sUz-4')
    
    

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )
account_activation_token = TokenGenerator()


