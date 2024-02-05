import os

import redis
from rq import Worker, Queue, Connection
from dotenv import load_dotenv
from utils import get_settings

load_dotenv()

settings = get_settings()
redis_conn = redis.from_url(settings.REDIS_URL)
task_queue = Queue('chat_queue', connection=redis_conn)
worker = Worker([task_queue], connection=redis_conn)
listen = ['default', 'low', 'high', 'chat_queue']

if __name__=='__main__':
        with Connection(redis_conn):
                worker = Worker(list(map(Queue, listen)))
                worker.work()