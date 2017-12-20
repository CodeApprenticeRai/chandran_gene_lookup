from django.db import models

# Create your models here.
class BarreslabRnaseqRawData(models.Model):
    gene_symbol = models.CharField(max_length=500, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    astrocytes = models.CharField(max_length=500, blank=True, null=True)
    neuron = models.CharField(max_length=500, blank=True, null=True)
    oligodendrocyte_precursor_cell = models.CharField(max_length=500, blank=True, null=True)
    newly_formed_oligodendrocyte = models.CharField(max_length=500, blank=True, null=True)
    myelinating_oligodendrocytes = models.CharField(max_length=500, blank=True, null=True)
    microglia = models.CharField(max_length=500, blank=True, null=True)
    endothelial_cells = models.CharField(max_length=500, blank=True, null=True)
	
class BarreslabRnaseqRawDataModules(models.Model):
    gene_symbol = models.CharField(primary_key=True, max_length=500)
    astrocytes = models.CharField(max_length=500, blank=True, null=True)
    neuron = models.CharField(max_length=500, blank=True, null=True)
    oligodendrocyte_precursor_cell = models.CharField(max_length=500, blank=True, null=True)
    newly_formed_oligodendrocyte = models.CharField(max_length=500, blank=True, null=True)
    myelinating_oligodendrocytes = models.CharField(max_length=500, blank=True, null=True)
    microglia = models.CharField(max_length=500, blank=True, null=True)
    endothelial_cells = models.CharField(max_length=500, blank=True, null=True)
    module = models.CharField(max_length=500, blank=True, null=True)
    merged_module = models.CharField(max_length=500, blank=True, null=True)
    module_merged_color = models.CharField(max_length=500, blank=True, null=True)
    meorangered3 = models.CharField(db_column='MEorangered3', max_length=500, blank=True, null=True)  # Field name made lowercase.
    megreen = models.CharField(db_column='MEgreen', max_length=500, blank=True, null=True)  # Field name made lowercase.
    mesienna3 = models.CharField(db_column='MEsienna3', max_length=500, blank=True, null=True)  # Field name made lowercase.
    megreenyellow = models.CharField(db_column='MEgreenyellow', max_length=500, blank=True, null=True)  # Field name made lowercase.
    memaroon = models.CharField(db_column='MEmaroon', max_length=500, blank=True, null=True)  # Field name made lowercase.
    medarkslateblue = models.CharField(db_column='MEdarkslateblue', max_length=500, blank=True, null=True)  # Field name made lowercase.
    meskyblue1 = models.CharField(db_column='MEskyblue1', max_length=500, blank=True, null=True)  # Field name made lowercase.
    memagenta = models.CharField(db_column='MEmagenta', max_length=500, blank=True, null=True)  # Field name made lowercase.
    meblue = models.CharField(db_column='MEblue', max_length=500, blank=True, null=True)  # Field name made lowercase.
    melightsteelblue = models.CharField(db_column='MElightsteelblue', max_length=500, blank=True, null=True)  # Field name made lowercase.
    mebisque4 = models.CharField(db_column='MEbisque4', max_length=500, blank=True, null=True)  # Field name made lowercase.
    meindianred4 = models.CharField(db_column='MEindianred4', max_length=500, blank=True, null=True)  # Field name made lowercase.
    meivory = models.CharField(db_column='MEivory', max_length=500, blank=True, null=True)  # Field name made lowercase.
    meskyblue = models.CharField(db_column='MEskyblue', max_length=500, blank=True, null=True)  # Field name made lowercase.
    meturquoise = models.CharField(db_column='MEturquoise', max_length=500, blank=True, null=True)  # Field name made lowercase.
    meblack = models.CharField(db_column='MEblack', max_length=500, blank=True, null=True)  # Field name made lowercase.
    mecoral2 = models.CharField(db_column='MEcoral2', max_length=500, blank=True, null=True)  # Field name made lowercase.
    mebrown = models.CharField(db_column='MEbrown', max_length=500, blank=True, null=True)  # Field name made lowercase.
    mecoral1 = models.CharField(db_column='MEcoral1', max_length=500, blank=True, null=True)  # Field name made lowercase.
    megrey = models.CharField(db_column='MEgrey', max_length=500, blank=True, null=True)  # Field name made lowercase.