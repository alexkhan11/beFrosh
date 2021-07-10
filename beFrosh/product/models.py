import uuid

from django.db import models
from django.db.models.deletion import CASCADE

from seller.models import Seller

class Product (models.Model):
    p_pk = models.UUIDField(primary_key = True, default = uuid.uuid4)
    title = models.CharField(null=False, max_length=128)
    desc =models.CharField(null=False, max_length=512)
    price = models.FloatField()
    quality = models.CharField(max_length=128)
    catagory = models.CharField(max_length=128)
    sold_status=models.BooleanField(default=False)
    
    # location = models.ForeignKey(Location, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller,related_name='product' , on_delete=CASCADE)

    def __str__(self) -> str:
        return self.title
    

class ProductImage(models.Model):
    img = models.ImageField(upload_to='product-images', blank=True, null=True)
    product = models.ForeignKey(Product, related_name='productImage', on_delete=CASCADE)
