from django.http import HttpResponse

def my_homepage_view(request):
	return HttpResponse("Top level")

def hello(request):
	return HttpResponse("Hello world")
