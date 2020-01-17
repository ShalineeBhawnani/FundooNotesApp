import datetime
import pdb
import jwt
import requests
from LoginFundoo.settings import SECRET_KEY, AUTH_ENDPOINT


def token_activation(username, password):
    """
    :param username: takes user name as parameter
    :param password: takes password
    :return: will return token
    """

    data = {
        'username': username,
        'password': password,
        'exp': datetime.datetime.now()+datetime.timedelta(days=1)
    }
    token = jwt.encode(data, SECRET_KEY, algorithm="HS256").decode('utf-8')
    return token


def token_validation(username, password):
    """
    :param username: takes user name as parameter
    :param password: takes password
    :return: will return token
    """

    data = {
        'username': username,
        'password': password
    }
    token1 = requests.post(AUTH_ENDPOINT, data=data)
    token = token1.json()['access']
    return token