import redis
from redis import StrictRedis

# class RedisOperation:
#     red = redis.StrictRedis(host='localhost', port=6379, db=0)

class Redis:
    """Open connection on Redis DataBase"""
    def __init__(self, redis_host='localhost', redis_port=6379, redis_db=0):
        self.host = redis_host 
        self.port = redis_port
        self.db = redis_db
        self.con = self.connect()
    def connect(self):
        try:
            con= self.con = redis.StrictRedis(
                host=self.host,
                port=self.port,
                db=self.db,)
            if con:
                print('Redis got connected : ', con)
            return con
                
        except Exception as e:
            print(e)
            print("RedisUtil Connection Error")
            con=self.con = None
            
    def set(self, redis_key, redis_value, exp_s=None, exp_ms=None):
        
        self.con.set(redis_key, redis_value, exp_s, exp_ms)
        return 'key:value is set in-memory cache'
    
    def delete(self, *names):
        print(names)
        self.con.delete(*names)

    def exists(self, redis_key):
        print(redis_key)
        return self.con.exists(redis_key)

    def get(self, redis_key):
        
        print(redis_key)
        return self.con.get(redis_key)
    
    # def get(self, value):
    #     print(value)
    #     return self.connection.get(value)


    def mget(self, *redis_key):
        return self.con.mget(*redis_key)

# import redis

# redis_object = redis.Redis("localhost")


# def Set(username, token):
#     """

#     :param username: saving token
#     :param token:this our actual token
#     :return:in this function we save token in redis
#     """
#     try:
#         redis_object.set(username, token)
#     except Exception:
#         return False


# def Get(username):
#     """

#     :param username: key for get token
#     :return:this function used for get token from redis

#     """
#     try:
#         return redis_object.get(username)
#     except Exception:
#         return False


# def Del(username):
#     """

#     :param username: kye for delete token
#     :return: this function used for delete token from redis

#     """
#     try:

#         redis_object.delete(username)

#     except Exception:
#         return False


# def All_Delete():
#     """

#     :return: this function used for delete all token from redis

#     """
#     try:
#         redis_object.flushall()
#     except Exception:
#         return False

