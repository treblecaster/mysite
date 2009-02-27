from django.http import HttpResponse
import datetime

def my_homepage_view(request):
	return HttpResponse("Top level")

def hello(request):
	return HttpResponse("Hello world")

def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)
