BROKER_TRANSPORT = "redis"

BROKER_HOST = "debian-test1"  # Maps to redis host.
BROKER_PORT = 6379         # Maps to redis port.
BROKER_VHOST = "0"         # Maps to database number.

CELERY_RESULT_BACKEND = "redis"
CELERY_REDIS_HOST = "debian-test1"
CELERY_REDIS_PORT = 6379
CELERY_REDIS_DB = 0

CELERY_IMPORTS = {'celery_fun.tasks',}
