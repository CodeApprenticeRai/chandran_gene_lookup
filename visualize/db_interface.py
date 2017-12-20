import MySQLdb
# import plotly.plotly as ply
# import plotly.graph_objs as go

def get_row(gene_symbol):
	conn = MySQLdb.connect(host="uf-gene-comp.cfkwbxqw8ftv.us-east-2.rds.amazonaws.com", user="TareG", password="iloveyou", db="uf_gene_comp")

	cursor = conn.cursor()
	
	#these can be made dynamic (as in fed from a web form)
	table = "`barreslab_rnaseq_raw_data`"
	gen_sym = "'{}'".format(gene_symbol)

	request_row = "SELECT * FROM {0} WHERE `gene_symbol` = {1} LIMIT 10".format(table, gen_sym)

	request_row_range = "SELECT * FROM `barreslab_rnaseq_raw_data` LIMIT 10"

	cursor.execute(request_row)

	return cursor.fetchall()[0]

def get_col_names():
	conn = MySQLdb.connect(host="uf-gene-comp.cfkwbxqw8ftv.us-east-2.rds.amazonaws.com", user="TareG", password="iloveyou", db="uf_gene_comp")

	cursor = conn.cursor()
	
	request_column_names = "SHOW columns FROM {}".format(table)
	cursor.execute(request_column_names)
	return [desc[0] for desc in cursor.fetchall()]
	
def get_ply_plot(x,y):
	data = [go.Bar(x,y)]
	return py.iplot(data, filename="gene_graph")
	
def json(gene_symbol):
	raw_freq = get_row(gene_symbol)
	raw_names = get_col_names()
	
	
	jdata = json.dumps(raw_names,raw_freq)
	return jdata

#Remember to add conditional functionality
def process_data(x,y):
	x = raw_x[2:]
	y = raw_y[2:]
	y = [float(f) for f in y ]

	json_ready_data = []

	for i in range(len(x)):
		data = {}
		data["name"] = x[i]
		data["freq"] = y[i]
		json_ready_data.append(data)
	
	return json_ready_data
	
