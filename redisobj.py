# -*- coding:utf-8 -*-

import redis

'''测试redis 队列'''
class RedisConPool(object):

    '''创建redis连接池'''
    def __init__(self,redisPool,taskKey='taskKey'):
        self.taskKey = taskKey
        self._redisPool = redisPool
        if self._redisPool == None:
           try:
               connectionPool = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True)
               self._redisPool = redis.Redis(connection_pool=connectionPool)
           except Exception as e:
                print(e)
                exit()

    '''添加队列消息'''
    def addTask(self,val):
        try:
            self._redisPool.lpush(self.taskKey, val)
        except Exception as e:
            print('something is error: ', e)
            exit()
        else:
            print('添加redis队列消息成功')
        finally:
            print('addTask 执行完毕')

    '''获取队列消息'''
    def readTask(self):
       return self._redisPool.rpop(self.taskKey)


# if __name__== '__main__':
#     rediss = RedisConPool(redisPool=None)
#     for x in range(10):
#         rediss.addTask(val=str(x))