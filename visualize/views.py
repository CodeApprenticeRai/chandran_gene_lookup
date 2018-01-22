from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.db import connections
from django.db.models import Count
from django.http import JsonResponse
from . import db_interface, vis
import sys


def index(request):

	# try:
	# 	ng = request.GET["ng"]
	# 	context = {'num_of_genes': [i+1 for i in range(ng)] }
    #
	# except Exception:
	# 	ng=1
	# 	context = {'num_of_genes': [i+1 for i in range(ng)], }
    #

	#Forgive me Benevolent One for the poor coding :(

	ng = 1
	context = {'num_of_genes': [i+1 for i in range(ng)],
				'ng':ng}

	return render(request, 'visualize/index.html', context)

#really pathethic coding here : (
def index2(request):
	context = {'num_of_genes': [i+1 for i in range(2)],
				'ng': 2,}
	return render(request, 'visualize/index.html', context)

def index3(request):
	context = {'num_of_genes': [i+1 for i in range(3)],
	 			'ng': 3,}
	return render(request, 'visualize/index.html', context)


def visualize(request):
	# context = {'gene_symbol': request.GET['gene_symbol']}
	ng = request.GET['ng']
	gene_symbols = []

	for i in range( int(ng) ):
		ith_gene = request.GET[ 'gene_symbol{}'.format( i+1 ) ]
		gene_symbols.append( ith_gene  )

	one_gene = len( gene_symbols ) == 1
	# print("Gene Symbol from /visualize:\n{}\n".format(gene_symbol),file=sys.stderr)
	if one_gene:
		data = vis.one_gene(gene_symbols[0])
		return render_to_response('visualize/graph.html', data)

	two_genes = len( gene_symbols ) == 2
	if two_genes:
		data = vis.multiple_genes(gene_symbols)
		return render_to_response('visualize/graph.html', data)

	three_genes = len( gene_symbols ) == 3
	if three_genes:
		data = vis.multiple_genes(gene_symbols)
		return render_to_response('visualize/graph.html', data)
	# return render(request,'visualize/nvd3_graph.html', context)


def jdata(request):
	gene_symbol = request.GET['gene_symbol']

	print("//Gene Symbol\n\n{}\n\n//Gene Symbol".format(gene_symbol),file=sys.stderr)

	data = db_interface.get_data(gene_symbol, d3=True)



	return JsonResponse(data, encoder=None, safe=False)
