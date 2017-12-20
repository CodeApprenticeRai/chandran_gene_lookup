from django.shortcuts import render
from django.http import HttpResponse
from django.db import connections
from django.db.models import Count
from django.http import JsonResponse
from . import db_interface

def index(request):
	context = {'':''}
	return render(request, 'visualize/index.html')

def visualize(request):
	gene_symbol = str(request.GET)

	context = { "gene_symbol": gene_symbol }
	return render(request, 'visualize/graph.html', context)


def jdata(request):
	gene_symbol = request.GET
	data = db_interface.get_data_json('0610005C13Rik')
	return JsonResponse(data, safe=False)
