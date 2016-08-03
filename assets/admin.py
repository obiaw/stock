from django.contrib import admin
from .models import Asset
# Register your models here.

class AssetAdmin(admin.ModelAdmin):
    #pass
    list_display=('asset_serial','asset_name','manufacturer'
        ,'model','category','short_description','holder',
        'location','price'
        )
    list_filter =['asset_name']

    search_fields =['asset_name','description','holder']

admin.site.register(Asset,AssetAdmin)
