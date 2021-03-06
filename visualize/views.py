from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.db import connections
from django.db.models import Count
from django.http import JsonResponse
from . import db_interface, vis, local_functions, seaborn_tests
import os, sys

def index(request):

    # try:
    # 	ng = request.GET["ng"]
    # 	context = {'num_of_genes': [i+1 for i in range(ng)] }
    #
    # except Exception:
    # 	ng=1
    # 	context = {'num_of_genes': [i+1 for i in range(ng)], }
    #

    ####Forgive me Benevolent One for the poor coding :(

    # ng = 1
    # context = {'num_of_genes': [i+1 for i in range(ng)],
    # 			'ng':ng}

    return render(request, 'visualize/index1_1.html') #, context)

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
    # ng = request.GET['ng']
    raw_gene_symbols = request.GET["gene_symbols"]  # comma separated, \n seperated or unformated string
    raw_genes_list = raw_gene_symbols.split()

    # print("//\n\nlength of RG:{}\n\n".format(len(raw_genes_list)),
    #   file=sys.stderr)


    processed_gene_symbols = local_functions.process_raw_symbols(raw_genes_list)

    print("//\n\nlength of PG:{}\n\n".format(len(processed_gene_symbols)),
      file=sys.stderr)

    if len(processed_gene_symbols) == 0:
        return render(request, 'visualize/index1_1.html') #, context)

    print("//Gene Symbols\n\n{}\n[{}]\n//Gene Symbols".format(processed_gene_symbols, type(processed_gene_symbols)),file=sys.stderr)




# for i in range( int(ng) ):
    # 	ith_gene = request.GET[ 'gene_symbol{}'.format( i+1 ) ]
    # 	gene_symbols.append( ith_gene  )

    # verification step: bad input: gene DNE, malformed input

    ## Create a function that drops all the genes that are invalid
    processed_gene_symbols = seaborn_tests.drop_dne(processed_gene_symbols)

    if len(processed_gene_symbols) > 0:
        seaborn_tests.create_heatmap(processed_gene_symbols)
        context = {'heatmap': 'heatmap'}
        return render(request, 'visualize/heatmap.html', context)

    else:
        error_message = "One of the gene's you entered was not found in our Database"
        context = { "error_message": error_message }
        return render(request, 'visualize/index1_1.html', context)


    # one_gene = len( processed_gene_symbols ) == 1
    # # print("Gene Symbol from /visualize:\n{}\n".format(gene_symbol),file=sys.stderr)
    # if one_gene:
    # 	data = vis.one_gene(processed_gene_symbols[0])
    # 	return render_to_response('visualize/graph.html', data)
    #
    # two_genes = len( processed_gene_symbols ) == 2
    # if two_genes:
    # 	data = vis.multiple_genes(processed_gene_symbols)
    # 	return render_to_response('visualize/graph.html', data)
    #
    # three_genes = len( processed_gene_symbols ) == 3
    # if three_genes:
    # 	data = vis.multiple_genes(processed_gene_symbols)
    # 	return render_to_response('visualize/graph.html', data)


    # return render(request,'visualize/nvd3_graph.html', context)


def jdata(request):
    gene_symbol = request.GET['gene_symbol']

    print("//Gene Symbol\n\n{}\n\n//Gene Symbol".format(gene_symbol),file=sys.stderr)

    data = db_interface.get_data(gene_symbol, d3=True)



    return JsonResponse(data, encoder=None, safe=False)

def heatmap(request):
    img_path = "./visualize/heatmap.png"
    # print("cwd\n\n{}\n\ncwd".format(os.getcwd()))
    with open(img_path, "rb") as f:
        return HttpResponse( f.read(), content_type="image/png")
