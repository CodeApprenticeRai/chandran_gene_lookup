from django.db import models

# Create your models here.
class BarreslabRnaseqRawData(models.Model):
    gene_symbol = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    astrocytes = models.CharField(max_length=255, blank=True, null=True)
    neuron = models.CharField(max_length=255, blank=True, null=True)
    oligodendrocyte_precursor_cell = models.CharField(max_length=255, blank=True, null=True)
    newly_formed_oligodendrocyte = models.CharField(max_length=255, blank=True, null=True)
    myelinating_oligodendrocytes = models.CharField(max_length=255, blank=True, null=True)
    microglia = models.CharField(max_length=255, blank=True, null=True)
    endothelial_cells = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.gene_symbol

    class Meta:
        managed = False
        db_table = 'barreslab_rnaseq_raw_data'


class BarreslabRnaseqRawDataModules(models.Model):
    gene_symbol = models.CharField(primary_key=True, max_length=255)
    astrocytes = models.CharField(max_length=255, blank=True, null=True)
    neuron = models.CharField(max_length=255, blank=True, null=True)
    oligodendrocyte_precursor_cell = models.CharField(max_length=255, blank=True, null=True)
    newly_formed_oligodendrocyte = models.CharField(max_length=255, blank=True, null=True)
    myelinating_oligodendrocytes = models.CharField(max_length=255, blank=True, null=True)
    microglia = models.CharField(max_length=255, blank=True, null=True)
    endothelial_cells = models.CharField(max_length=255, blank=True, null=True)
    module = models.CharField(max_length=255, blank=True, null=True)
    merged_module = models.CharField(max_length=255, blank=True, null=True)
    module_merged_color = models.CharField(max_length=255, blank=True, null=True)
    meorangered3 = models.CharField(db_column='MEorangered3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    megreen = models.CharField(db_column='MEgreen', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mesienna3 = models.CharField(db_column='MEsienna3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    megreenyellow = models.CharField(db_column='MEgreenyellow', max_length=255, blank=True, null=True)  # Field name made lowercase.
    memaroon = models.CharField(db_column='MEmaroon', max_length=255, blank=True, null=True)  # Field name made lowercase.
    medarkslateblue = models.CharField(db_column='MEdarkslateblue', max_length=255, blank=True, null=True)  # Field name made lowercase.
    meskyblue1 = models.CharField(db_column='MEskyblue1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    memagenta = models.CharField(db_column='MEmagenta', max_length=255, blank=True, null=True)  # Field name made lowercase.
    meblue = models.CharField(db_column='MEblue', max_length=255, blank=True, null=True)  # Field name made lowercase.
    melightsteelblue = models.CharField(db_column='MElightsteelblue', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mebisque4 = models.CharField(db_column='MEbisque4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    meindianred4 = models.CharField(db_column='MEindianred4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    meivory = models.CharField(db_column='MEivory', max_length=255, blank=True, null=True)  # Field name made lowercase.
    meskyblue = models.CharField(db_column='MEskyblue', max_length=255, blank=True, null=True)  # Field name made lowercase.
    meturquoise = models.CharField(db_column='MEturquoise', max_length=255, blank=True, null=True)  # Field name made lowercase.
    meblack = models.CharField(db_column='MEblack', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mecoral2 = models.CharField(db_column='MEcoral2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mebrown = models.CharField(db_column='MEbrown', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mecoral1 = models.CharField(db_column='MEcoral1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    megrey = models.CharField(db_column='MEgrey', max_length=255, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.gene_symbol

    class Meta:
        managed = False
        db_table = 'barreslab_rnaseq_raw_data_modules'


class CerebellumRankedGenes(models.Model):
    cerebellum_ranked_genes_id = models.AutoField(primary_key=True)
    id = models.CharField(db_column='ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    ilmn_gene = models.CharField(db_column='ILMN_Gene', max_length=25, blank=True, null=True)  # Field name made lowercase.
    t0_tg_dox_nd = models.DecimalField(db_column='T0_TG_Dox_ND', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    t1_tg_dox_nd = models.DecimalField(db_column='T1_TG_Dox_ND', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    t3_tg_dox_nd = models.DecimalField(db_column='T3_TG_Dox_ND', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    t4_tg_dox_nd = models.DecimalField(db_column='T4_TG_Dox_ND', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    t5_tg_dox_nd = models.DecimalField(db_column='T5_TG_Dox_ND', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    t4_tg_doxr_nd = models.DecimalField(db_column='T4_TG_DoxR_ND', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    t5_tg_doxr_nd = models.DecimalField(db_column='T5_TG_DoxR_ND', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    aveexpr = models.DecimalField(db_column='AveExpr', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    f = models.DecimalField(db_column='F', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    p_value = models.DecimalField(db_column='P.Value', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    adj_p_val = models.DecimalField(db_column='adj.P.Val', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    species = models.CharField(db_column='Species', max_length=12, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=12, blank=True, null=True)  # Field name made lowercase.
    search_key = models.CharField(db_column='Search_Key', max_length=12, blank=True, null=True)  # Field name made lowercase.
    transcript = models.CharField(db_column='Transcript', max_length=12, blank=True, null=True)  # Field name made lowercase.
    ilmn_gene2 = models.CharField(db_column='ILMN_Gene2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    source_reference_id = models.CharField(db_column='Source_Reference_ID', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refseq_id = models.CharField(db_column='RefSeq_ID', max_length=25, blank=True, null=True)  # Field name made lowercase.
    unigene_id = models.CharField(db_column='Unigene_ID', max_length=5, blank=True, null=True)  # Field name made lowercase.
    entrez_gene_id = models.CharField(db_column='Entrez_Gene_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    gi = models.IntegerField(db_column='GI')  # Field name made lowercase.
    accession = models.CharField(db_column='Accession', max_length=25, blank=True, null=True)  # Field name made lowercase.
    symbol = models.CharField(db_column='Symbol', max_length=25, blank=True, null=True)  # Field name made lowercase.
    protein_product = models.CharField(db_column='Protein_Product', max_length=25, blank=True, null=True)  # Field name made lowercase.
    array_address_id = models.IntegerField(db_column='Array_Address_Id')  # Field name made lowercase.
    probe_type = models.CharField(db_column='Probe_Type', max_length=5, blank=True, null=True)  # Field name made lowercase.
    probe_start = models.IntegerField(db_column='Probe_Start')  # Field name made lowercase.
    probe_sequence = models.CharField(db_column='Probe_Sequence', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chromosome = models.CharField(db_column='Chromosome', max_length=25, blank=True, null=True)  # Field name made lowercase.
    probe_chr_orientation = models.CharField(db_column='Probe_Chr_Orientation', max_length=5, blank=True, null=True)  # Field name made lowercase.
    probe_coordinates = models.CharField(db_column='Probe_Coordinates', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cytoband = models.CharField(db_column='Cytoband', max_length=12, blank=True, null=True)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=255, blank=True, null=True)  # Field name made lowercase.
    synonyms = models.CharField(db_column='Synonyms', max_length=255, blank=True, null=True)  # Field name made lowercase.
    obsolete_probe_id = models.CharField(db_column='Obsolete_Probe_Id', max_length=255, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.symbol

    class Meta:
        managed = False
        db_table = 'cerebellum_ranked_genes'


class DrgRankedGenes(models.Model):
    drg_ranked_genes_id = models.AutoField(primary_key=True)
    id = models.CharField(db_column='ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    ilmn_gene = models.CharField(db_column='ILMN_Gene', max_length=25, blank=True, null=True)  # Field name made lowercase.
    t0_tg_dox_nd = models.DecimalField(db_column='T0_TG_Dox_ND', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    t1_tg_dox_nd = models.DecimalField(db_column='T1_TG_Dox_ND', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    t3_tg_dox_nd = models.DecimalField(db_column='T3_TG_Dox_ND', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    t4_tg_dox_nd = models.DecimalField(db_column='T4_TG_Dox_ND', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    t5_tg_dox_nd = models.DecimalField(db_column='T5_TG_Dox_ND', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    t4_tg_doxr_nd = models.DecimalField(db_column='T4_TG_DoxR_ND', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    t5_tg_doxr_nd = models.DecimalField(db_column='T5_TG_DoxR_ND', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    aveexpr = models.DecimalField(db_column='AveExpr', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    f = models.DecimalField(db_column='F', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    p_value = models.DecimalField(db_column='P.Value', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    adj_p_val = models.DecimalField(db_column='adj.P.Val', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    species = models.CharField(db_column='Species', max_length=12, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=12, blank=True, null=True)  # Field name made lowercase.
    search_key = models.CharField(db_column='Search_Key', max_length=12, blank=True, null=True)  # Field name made lowercase.
    transcript = models.CharField(db_column='Transcript', max_length=12, blank=True, null=True)  # Field name made lowercase.
    ilmn_gene2 = models.CharField(db_column='ILMN_Gene2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    source_reference_id = models.CharField(db_column='Source_Reference_ID', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refseq_id = models.CharField(db_column='RefSeq_ID', max_length=25, blank=True, null=True)  # Field name made lowercase.
    unigene_id = models.CharField(db_column='Unigene_ID', max_length=5, blank=True, null=True)  # Field name made lowercase.
    entrez_gene_id = models.CharField(db_column='Entrez_Gene_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    gi = models.IntegerField(db_column='GI')  # Field name made lowercase.
    accession = models.CharField(db_column='Accession', max_length=25, blank=True, null=True)  # Field name made lowercase.
    symbol = models.CharField(db_column='Symbol', max_length=25, blank=True, null=True)  # Field name made lowercase.
    protein_product = models.CharField(db_column='Protein_Product', max_length=25, blank=True, null=True)  # Field name made lowercase.
    array_address_id = models.IntegerField(db_column='Array_Address_Id')  # Field name made lowercase.
    probe_type = models.CharField(db_column='Probe_Type', max_length=5, blank=True, null=True)  # Field name made lowercase.
    probe_start = models.IntegerField(db_column='Probe_Start')  # Field name made lowercase.
    probe_sequence = models.CharField(db_column='Probe_Sequence', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chromosome = models.CharField(db_column='Chromosome', max_length=5, blank=True, null=True)  # Field name made lowercase.
    probe_chr_orientation = models.CharField(db_column='Probe_Chr_Orientation', max_length=5, blank=True, null=True)  # Field name made lowercase.
    probe_coordinates = models.CharField(db_column='Probe_Coordinates', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cytoband = models.CharField(db_column='Cytoband', max_length=12, blank=True, null=True)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=255, blank=True, null=True)  # Field name made lowercase.
    synonyms = models.CharField(db_column='Synonyms', max_length=255, blank=True, null=True)  # Field name made lowercase.
    obsolete_probe_id = models.CharField(db_column='Obsolete_Probe_Id', max_length=255, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.symbol

    class Meta:
        managed = False
        db_table = 'drg_ranked_genes'

class HeartRankedGenes(models.Model):
    heart_ranked_genes_id = models.AutoField(primary_key=True)
    id = models.CharField(db_column='ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    ilmn_gene = models.CharField(db_column='ILMN_Gene', max_length=25, blank=True, null=True)  # Field name made lowercase.
    t0_tg_dox_nd = models.DecimalField(db_column='T0_TG_Dox_ND', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    t1_tg_dox_nd = models.DecimalField(db_column='T1_TG_Dox_ND', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    t3_tg_dox_nd = models.DecimalField(db_column='T3_TG_Dox_ND', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    t4_tg_dox_nd = models.DecimalField(db_column='T4_TG_Dox_ND', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    t5_tg_dox_nd = models.DecimalField(db_column='T5_TG_Dox_ND', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    t4_tg_doxr_nd = models.DecimalField(db_column='T4_TG_DoxR_ND', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    t5_tg_doxr_nd = models.DecimalField(db_column='T5_TG_DoxR_ND', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    aveexpr = models.DecimalField(db_column='AveExpr', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    f = models.DecimalField(db_column='F', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    p_value = models.DecimalField(db_column='P.Value', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    adj_p_val = models.DecimalField(db_column='adj.P.Val', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    species = models.CharField(db_column='Species', max_length=12, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=12, blank=True, null=True)  # Field name made lowercase.
    search_key = models.CharField(db_column='Search_Key', max_length=12, blank=True, null=True)  # Field name made lowercase.
    transcript = models.CharField(db_column='Transcript', max_length=12, blank=True, null=True)  # Field name made lowercase.
    ilmn_gene2 = models.CharField(db_column='ILMN_Gene2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    source_reference_id = models.CharField(db_column='Source_Reference_ID', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refseq_id = models.CharField(db_column='RefSeq_ID', max_length=25, blank=True, null=True)  # Field name made lowercase.
    unigene_id = models.CharField(db_column='Unigene_ID', max_length=5, blank=True, null=True)  # Field name made lowercase.
    entrez_gene_id = models.CharField(db_column='Entrez_Gene_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    gi = models.IntegerField(db_column='GI')  # Field name made lowercase.
    accession = models.CharField(db_column='Accession', max_length=25, blank=True, null=True)  # Field name made lowercase.
    symbol = models.CharField(db_column='Symbol', max_length=25, blank=True, null=True)  # Field name made lowercase.
    protein_product = models.CharField(db_column='Protein_Product', max_length=25, blank=True, null=True)  # Field name made lowercase.
    array_address_id = models.IntegerField(db_column='Array_Address_Id')  # Field name made lowercase.
    probe_type = models.CharField(db_column='Probe_Type', max_length=5, blank=True, null=True)  # Field name made lowercase.
    probe_start = models.IntegerField(db_column='Probe_Start')  # Field name made lowercase.
    probe_sequence = models.CharField(db_column='Probe_Sequence', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chromosome = models.CharField(db_column='Chromosome', max_length=25, blank=True, null=True)  # Field name made lowercase.
    probe_chr_orientation = models.CharField(db_column='Probe_Chr_Orientation', max_length=5, blank=True, null=True)  # Field name made lowercase.
    probe_coordinates = models.CharField(db_column='Probe_Coordinates', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cytoband = models.CharField(db_column='Cytoband', max_length=12, blank=True, null=True)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=255, blank=True, null=True)  # Field name made lowercase.
    synonyms = models.CharField(db_column='Synonyms', max_length=255, blank=True, null=True)  # Field name made lowercase.
    obsolete_probe_id = models.CharField(db_column='Obsolete_Probe_Id', max_length=255, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.symbol

    class Meta:
        managed = False
        db_table = 'heart_ranked_genes'
