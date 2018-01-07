import MySQLdb
import json
import sys
# import plotly.plotly as ply
# import plotly.graph_objs as go

def get_row(gene_symbol):
	conn = MySQLdb.connect(host="uf-gene-comp.cfkwbxqw8ftv.us-east-2.rds.amazonaws.com", user="", password="", db="uf_gene_comp")

	cursor = conn.cursor()

	#these can be made dynamic (as in fed from a web form)
	table = "`barreslab_rnaseq_raw_data`"
	gen_sym = "'{}'".format(gene_symbol)

	request_row = "SELECT * FROM {0} WHERE `gene_symbol` = {1} LIMIT 10".format(table, gen_sym)

	request_row_range = "SELECT * FROM `barreslab_rnaseq_raw_data` LIMIT 10"

	cursor.execute(request_row)
	data = cursor.fetchall()

	# print("thing\n\n{}\n\nthing".format(cursor.fetchall()),file=sys.stderr)

	# cursor.nextset()
	cursor.close()
	print("Data from get_row call:\n{}\n\n".format(data),file=sys.stderr)
	cursor.close()
	return data[0]

def get_col_names():
	conn = MySQLdb.connect(host="uf-gene-comp.cfkwbxqw8ftv.us-east-2.rds.amazonaws.com", user="", password="", db="uf_gene_comp")

	cursor = conn.cursor()

	request_column_names = "SHOW columns FROM {}".format("`barreslab_rnaseq_raw_data`")
	cursor.execute(request_column_names)
	data = cursor.fetchall()
	cursor.close()
	return [desc[0] for desc in data]

def get_ply_plot(x,y):
	data = [go.Bar(x,y)]
	return py.iplot(data, filename="gene_graph")

def get_data_json(gene_symbol):
	raw_freq = get_row(gene_symbol)
	raw_names = get_col_names()
	data = process_data(raw_names,raw_freq)

	jdata = json.dumps(data)
	return jdata

def get_data(gene_symbol, plot=False, d3=False):
	raw_freq = get_row(gene_symbol)
	print("thing\n\n{}\n\nthing".format(raw_freq),file=sys.stderr)
	raw_names = get_col_names()
	data = process_data(raw_names,raw_freq, d3=d3)

	return data

#Remember to add conditional functionality
def process_data(x,y, d3=False):
	x = x[2:]
	y = y[2:]
	y = [float(f) for f in y ]


	if d3 == True:
		json_ready_data = []
		for i in range(len(x)):
			data = {}
			data["name"] = x[i]
			data["freq"] = y[i]
			json_ready_data.append(data)
		return json_ready_data
	else:
		return x,y
