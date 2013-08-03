from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render_to_response

def index_temp_file(request,color):
	return render_to_response('index_temp_file.html',{'color':color})
	
def hello(request):
	return HttpResponse("Hello world")

def index_temp(request, input_name):
	t= Template('My name is {{name}}.')
	c= Context({'name': input_name})
	return HttpResponse(t.render(c))


