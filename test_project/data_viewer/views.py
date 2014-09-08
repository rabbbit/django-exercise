from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
	return HttpResponse("Hello world, you are at the data viewer index")

def csv(request):
	columns = ['123', '456']

	template = loader.get_template('data_viewer/table_view.html')
	context = RequestContext(request, { 
        'columns': columns,
	})
	return HttpResponse(template.render(context), content_type='text/html')

def prn(request):
	return HttpResponse("PRN")

# Create your views here.
