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
