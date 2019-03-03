# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CatColorsInfo(models.Model):
    color = models.TextField(unique=True, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'cat_colors_info'


class Cats(models.Model):
    name = models.CharField(primary_key=True, max_length=80)
    color = models.TextField(blank=True, null=True)  
    tail_length = models.IntegerField(blank=True, null=True)
    whiskers_length = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'cats'


class CatsStat(models.Model):
    tail_length_mean = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tail_length_median = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tail_length_mode = models.TextField(blank=True, null=True)
    whiskers_length_mean = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    whiskers_length_median = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    whiskers_length_mode = models.TextField(blank=True, null=True) 

    class Meta:
        db_table = 'cats_stat'
