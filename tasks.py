from celery_fun.my_worker import app
import time

@app.task
def gitclone(self, giturl):
	print('sleeping')
	self.update_state(state='sleeping')
	time.sleep(5)
	print('cloning %s' % giturl)

@app.task
def run_command(self, cmd):
	print('running %s' %cmd)
