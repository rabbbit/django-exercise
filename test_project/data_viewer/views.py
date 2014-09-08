from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello world, you are at the data viewer index")

def csv(request):
	return HttpResponse("CSV")

def prn(request):
	return HttpResponse("PRN")

# Create your views here.
