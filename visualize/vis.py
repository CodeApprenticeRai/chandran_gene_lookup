from . import db_interface



def one_gene(gene_symbol):
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

    return data

def multiple_genes(gene_symbols):
    xdata = db_interface.get_data(gene_symbols[0], plot=True, just_x=True)
    ydata = []

    for gene in gene_symbols:
        y_i =  db_interface.get_data(gene, plot=True, just_y=True)
        ydata.append( y_i )

    extra_serie = {"tooltip": {"y_start": "", "y_end": ""}}

    chartdata = {
        'x': xdata,    }

    for i in range(len(gene_symbols)):
        chartdata[ "name{}".format(i+1) ] = "{}".format(gene_symbols[i])
        chartdata[ "y{}".format(i+1) ] = ydata[i]
        chartdata[ "extra{}".format(i+1) ] = extra_serie

    charttype = "multiBarChart"
    chartcontainer = "multibarchart_container"

    data = {
        'gene_symbols': gene_symbols,
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': True,
			 }
    }

    return data
