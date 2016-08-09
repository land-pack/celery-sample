import requests
from celery import Celery

#Have celery instance declare 
app = Celery('celery_http_client', broker='redis://localhost:6379/1')

#Have a task declare
@app.task
def fetch_url(url):
	response = requests.get(url)
	print response.status_code

def main(*urls):
	for url in urls:
		#fetch_url(url)		#: No use the celery to load the task
		fetch_url.delay(url)	#: Celery worker will do actully work!

if __name__ == '__main__':
	urls = ['http://oneapm.com','https://baidu.com','http://www.cug2313.com']
	main(*urls)
