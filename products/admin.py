from django.contrib import admin
from models import product
# Register your models here.
class productAdmin(admin.ModelAdmin):
    list_display=('id','product_id','product_description','product_type','price','discount','points','gst')
admin.site.register(product,productAdmin)
