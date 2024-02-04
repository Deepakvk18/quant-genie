import redis
from rq import Queue
from utils import get_settings

settings = get_settings()
redis_conn = redis.from_url(settings.REDIS_URL)
task_queue = Queue(name='chat_queue', connection=redis_conn)