import django, os, sys
from django.http import HttpResponse

# Dirty code that patches import errors
root_path = os.path.abspath( os.path.join( os.path.split(__file__)[0], "..") )
sys.path.insert(0, root_path)

# print(sys.path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'test.settings'
django.setup()
# -----------------------------

# Actual code starts here.

import matplotlib
matplotlib.use('Agg')

import numpy as np
import seaborn as sns


import matplotlib.pyplot as plt
import pandas as pd
from visualize.models import *

# f

def drop_dne(gene_symbols):
    new_symbols = []

    results = list(map((lambda x: len(CerebellumRankedGenes.objects.filter(ilmn_gene=x) ) > 0) , gene_symbols))
    for i in range(len(gene_symbols)):
        if results[i]:
           new_symbols.append(gene_symbols[i])
    return new_symbols

def create_heatmap(gene_symbols):
    # gene_symbols = ['FXN','1110032E23RIK','GMFG'] # RPP21,RHBDD1,RHOJ
    # catsShortened = ['Cerebellum','DRG','Heart']
    cats = ['Cerebellum','DRG','Heart']

    big_df = pd.DataFrame()

    for gene in gene_symbols:
        tg_dict = {}

        CRGs = CerebellumRankedGenes.objects.filter(ilmn_gene=gene)
        tg_doxs = CRGs.values( 't0_tg_dox_nd', 't1_tg_dox_nd', 't3_tg_dox_nd', 't4_tg_dox_nd', 't5_tg_dox_nd', 't4_tg_doxr_nd', 't5_tg_doxr_nd')[0]

        for key in tg_doxs:
            tg_dict[key] = [ float(tg_doxs[key]) ]

        g_index = gene + ' ' + cats[0]

        crg_df = pd.DataFrame(data=tg_dict, index = [g_index])

        tg_dict = {}
        DRGs = DrgRankedGenes.objects.filter(ilmn_gene=gene)
        tg_doxs = DRGs.values( 't0_tg_dox_nd', 't1_tg_dox_nd', 't3_tg_dox_nd', 't4_tg_dox_nd', 't5_tg_dox_nd', 't4_tg_doxr_nd', 't5_tg_doxr_nd')[0]
        for key in tg_doxs:
            tg_dict[key] = [ float(tg_doxs[key]) ]

        g_index = gene + ' ' + cats[1]
        drg_df = pd.DataFrame(data=tg_dict, index = [g_index])

        tg_dict = {}
        HRGs = HeartRankedGenes.objects.filter(ilmn_gene=gene)
        tg_doxs = HRGs.values( 't0_tg_dox_nd', 't1_tg_dox_nd', 't3_tg_dox_nd', 't4_tg_dox_nd', 't5_tg_dox_nd', 't4_tg_doxr_nd', 't5_tg_doxr_nd')[0]
        for key in tg_doxs:
            tg_dict[key] = [ float(tg_doxs[key]) ]

        g_index = gene + ' ' + cats[2]
        hrg_df = pd.DataFrame(data=tg_dict, index = [g_index])

        dfs = [crg_df, drg_df, hrg_df]

        df = pd.concat(dfs)
        big_df = big_df.append(df)

    plt.subplots(figsize=(12,9))
    ax = sns.heatmap(big_df)
    fig = ax.get_figure()
    img_path = "./visualize/heatmap.png"
    fig.savefig(img_path)
    return
