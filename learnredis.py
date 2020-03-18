import redis

def main():
    client = redis.Redis(host='',port=6379,password='')
    
    client.set('username','hellokitty',ex=300)
    print(client.ttl('username'))
    print(client.get('username').decode())
    client.set('nike','300')
    client.incr('nike')
    client.incrby('nike',50)
    print(client.get('nike'))
    client.hset('stu1','id','1001')
    client.hget('stu1','id')
    client.lpush('list1',10,20,30,40)
    client.lrange('list1',0,-1)


if __name__ == "__main__":
    main()