import os

import redis
from rq import Worker, Queue
from dotenv import load_dotenv

load_dotenv()
REDIS_URL = os.getenv('REDIS_URL')

redis_conn = redis.from_url(REDIS_URL)
task_queue = Queue('chat_queue', connection=redis_conn)
worker = Worker([task_queue], connection=redis_conn)

if __name__=='__main__':
        worker.work()