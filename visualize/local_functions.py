import re, string

# if genes not in proper form: return Error page (Index with Error Blimp)

def validate_symbols():
	pass

# Input: Single String with All Gene Symbols; Output: List of Gene Symbol Strings, with no spaces in each string;
def process_raw_symbols(raw_symbols): # raw_symbols is string
	check_symbols = [ ",", "\n", "\r", " ",  ]

	gene_symbols = raw_symbols
	if (type(gene_symbols) != str):
		for check_symbol in check_symbols:
			if check_symbol in raw_symbols:
				gene_symbols = raw_symbols.split(check_symbol)
				break

	for i in range( len( gene_symbols ) ):
		for check_symbol in check_symbols:
			gene_symbols[i] = gene_symbols[i].replace(check_symbol, "")


	pattern = re.compile('[\W_]+')

	if len(gene_symbols) > 0:
		if (type(gene_symbols) == str):
			gene_symbols = pattern.sub('', gene_symbols)
		else:
			for i in range(len(gene_symbols)):
				gene_symbols[i] = pattern.sub('', gene_symbols[i])

	processed_symbols = gene_symbols

	return processed_symbols
