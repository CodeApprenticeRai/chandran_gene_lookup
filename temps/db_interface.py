import MySQLdb

conn = MySQLdb.connect(host="uf-gene-comp.cfkwbxqw8ftv.us-east-2.rds.amazonaws.com", user="TareG", password="iloveyou", db="uf_gene_comp")

cursor = conn.cursor()

#these can be made dynamic (as in fed from a web form)
table = "barreslab_rnaseq_raw_data"
gen_sym = "0610005C13Rik"

request_row = "SELECT * FROM {0} WHERE `gene_symbol` = {1} LIMIT 10".format(table, gen_sym)

request_row_range = "SELECT * FROM `barreslab_rnaseq_raw_data` LIMIT 10"

cursor.execute(request_row_range)

query_result = cursor.fetchall()

print(query_result)