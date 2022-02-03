from asyncio.windows_events import NULL
from email.policy import default
from tkinter import CASCADE
from django.db import models
from django.utils import timezone
from datetime import datetime




def place_global_symbol(instance, fileName):
    return 'global_symbols/{0}'.format(fileName)

def place_user_symbol(instance, fileName):
    date = datetime.now()
    return 'user_symbols/{0}/{1}/{2}/{3}'.format(date.year, date.month, date.day, fileName)




# Countries:
class Region(models.Model):
    region_self_str_id = models.CharField(max_length=4, unique=True)
    def __str__(self):
        return self.region_self_str_id

class RegionReferencePoint(models.Model):
    region_str_id = models.ForeignKey(Region, to_field='region_self_str_id', on_delete=models.CASCADE)
    name = models.CharField(max_length=81, unique=True)
    population = models.IntegerField()
    gdp = models.DecimalField(max_digits=25, decimal_places=5)
    prominent_religion = models.CharField(max_length=81, default='Not determined')
    def __str__(self):
        return self.name




# Global symbols:
class GlobalSymbol(models.Model):
    region_str_id = models.ForeignKey(Region, to_field='region_self_str_id', on_delete=models.CASCADE)
    region_int_id = models.IntegerField(null=True, default=None) # This is to be updated using triggers written into the database
    upload = models.ImageField(upload_to=place_global_symbol, default='was_not_associated.jpg')
    visibile = models.CharField(max_length=7, choices=(('visible','false'), ('visible','true')), default='false')
    def __str__(self):
        return str(self.upload)


class GlobalSymbolReferencePoint(models.Model):
    symbol_image_id = models.ForeignKey(GlobalSymbol, on_delete=models.CASCADE)
    location = models.CharField(max_length=81)
    upload_date = models.DateTimeField(default=timezone.now)
    english_reference = models.CharField(max_length=81, default='Not identified')
    def __str__(self):
        return self.english_reference




# User symbols:
class UserSymbol(models.Model):
    upload = models.ImageField(upload_to=place_user_symbol, default='was_not_associated.jpg')
    visibile = models.CharField(max_length=7, choices=(('visible','false'), ('visible','true')), default='false')
    def __str__(self):
        return str(self.upload)

class UserSymbolType(models.Model):
    symbol_type_self_unique_id = models.CharField(max_length=16, unique=True, null=True)
    def __str__(self):
        return self.symbol_type_self_unique_id

class UserSymbolReferencePoint(models.Model):
    symbol_image_id = models.ForeignKey(UserSymbol, related_name='symbol_image_id', on_delete=models.CASCADE)
    symbol_type_id = models.ForeignKey(UserSymbolType, to_field='symbol_type_self_unique_id', related_name='symbol_type_id', on_delete=models.PROTECT, null=True)
    upload_date = models.DateTimeField(default=timezone.now)
    english_reference = models.CharField(max_length=81, default='Not identified')
    # will contain user_name when in use
    def __str__(self):
        return self.english_reference