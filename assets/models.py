from django.db import models
#import moneyed
from djmoney.models.fields import MoneyField
from django.template.defaultfilters import truncatechars
# Create your models here.

MANUFACTURER =(
    ('hp','HP'),
    ('dell','DELL'),
    ('apple','APPLE')
    )
CATEGORY =(
    ('it','IT EQUIPMENT'),
    ('leisure','LEISURE')
    )

class Asset(models.Model):
    # pass
    asset_serial = models.CharField('Asset Serial Number',max_length=100,null=True,blank=True)
    asset_name = models.CharField('Asset Name',max_length=100)
    manufacturer =models.CharField('Maunfacturer',choices=MANUFACTURER, default='hp',max_length=200)
    model = models.CharField('Asset Model', max_length=200)
    category = models.CharField(choices=CATEGORY,default='IT EQUIPMENT',max_length=100)
    description = models.TextField(blank=True,null=True)
    holder = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    price = MoneyField(max_digits=65, decimal_places=2, default_currency='USD')

    def __str__(self):
        return self.asset_name, self.price

    @property
    def short_description(self):
        return truncatechars(self.description,50)
    


