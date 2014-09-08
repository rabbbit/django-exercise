from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return render(request, 'data_viewer/index.html')

def csv(request):
	columns = ['123', '456']

	context = {'columns': columns}

	return render(request, 'data_viewer/table_view.html', context)

def prn(request):
	return HttpResponse("PRN")

# Create your views here.
