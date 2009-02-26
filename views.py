from django.http import HttpResponse

def hello(request):
	return HttpResonse("Hello world")
