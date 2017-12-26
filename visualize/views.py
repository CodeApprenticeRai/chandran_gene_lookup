from django.shortcuts import render
from django.http import HttpResponse
from django.db import connections
from django.db.models import Count
from django.http import JsonResponse
from . import db_interface
import sys


def index(request):
	context = {'':''}
	return render(request, 'visualize/index.html')

def visualize(request):
	gene_symbol = request.GET['gene_symbol']

	print("\n\n{}\n\n".format(gene_symbol),file=sys.stderr)

	context = { "gene_symbol": gene_symbol }
	return render(request, 'visualize/graph.html', context)


def jdata(request):
	gene_symbol = request.GET['gene_symbol']

	print("\n\n{}\n\n".format(gene_symbol),file=sys.stderr)

	data = db_interface.get_data(gene_symbol)

	print("\n\n{}\n\n".format(type(data[0])),file=sys.stderr)

	return JsonResponse(data, encoder=None, safe=False)
