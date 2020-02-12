import redis
from redis import StrictRedis


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

   