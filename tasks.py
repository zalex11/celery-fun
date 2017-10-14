from celery_fun.my_worker import app

@app.task
def gitclone(giturl):
	print('cloning %s' % giturl)

@app.task
def run_command(cmd):
	print('running %s' %cmd)
