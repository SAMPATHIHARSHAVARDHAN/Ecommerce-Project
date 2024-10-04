from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=('product_id','product_description','product_type','price','discount','points','gst')
    search_fields=('title','content')


admin.site.register(Post , PostAdmin)
