from celery_fun.my_worker import app
import time

@app.task
def gitclone(giturl):
	print('sleeping')
	time.sleep(5)
	print('cloning %s' % giturl)

@app.task
def run_command(cmd):
	print('running %s' %cmd)
