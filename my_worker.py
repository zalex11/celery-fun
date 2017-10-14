from celery_fun import celeryconfig
from celery import Celery

app = Celery('test')

#app.config_from_object('celery_fun.celeryconfig')
app.config_from_object(celeryconfig)
app.conf.task_routes = {
				'celery_fun.tasks.*':{'queue':'abcd'},
						}
#app.autodiscover_tasks()

if __name__ == '__main__':
	app.start()
