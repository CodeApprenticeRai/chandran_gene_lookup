from django.shortcuts import render, render_to_response
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
	# context = {'gene_symbol': request.GET['gene_symbol']}
	gene_symbol = request.GET['gene_symbol']
	# print("Gene Symbol from /visualize:\n{}\n".format(gene_symbol),file=sys.stderr)

	xdata, ydata = db_interface.get_data(gene_symbol, plot=True)

	# print(xdata,ydata,file=sys.stderr, sep="\n\n")


	extra_serie1 = {"tooltip": {"y_start": "", "y_end": " cal"}}
	chartdata = {'x': xdata, 'name1': '', 'y1': ydata, 'extra1': extra_serie1 }
	charttype = "discreteBarChart"
	chartcontainer = 'discretebarchart_container'  # container name
	data = {
		'gene_symbol': gene_symbol,
		'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': True,
			 },
			}


	return render_to_response('visualize/graph.html', data)
	# return render(request,'visualize/nvd3_graph.html', context)

def jdata(request):
	gene_symbol = request.GET['gene_symbol']

	print("//Gene Symbol\n\n{}\n\n//Gene Symbol".format(gene_symbol),file=sys.stderr)

	data = db_interface.get_data(gene_symbol, d3=True)



	return JsonResponse(data, encoder=None, safe=False)
