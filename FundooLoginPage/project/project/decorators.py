from functools import wraps
from project.settings import SECRET_KEY
from project.redis_class import Redis
rdb=Redis()
from snippets.token import decode

def redirect_if_wrong_boardname(func):
    def wrapper(request,user_id=None):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            token = request.headers.get('token')
            if token is not None:
                mytoken=jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
                user_id=mytoken.get('username')
                rdb.exists(user.username)
                return func(request,user_id)))
            else:
                return func("token not found")
        except:
            return Http404('Board not found')
    return wrapper

