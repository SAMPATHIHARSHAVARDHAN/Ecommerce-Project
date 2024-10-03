from django.db import models

# Create your models here.
class product(models.Models):
    product_id=models.IntegerField(max_length=150)
    product_name=models.CharFieldField(max_length=150)
    product_description=models.CharFieldField(max_length=150)
    product_type=models.CharField(max_length=150)
    price=models.IntegerField(max_length=50)
    discount=models.IntegerField(max_length=50)
    gst=models.IntegerField(max_length=50)
    
class Meta:
    verbose_nmae="product"
    verbose_name_plural="products"
    
    



