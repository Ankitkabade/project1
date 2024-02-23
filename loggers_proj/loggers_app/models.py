from django.db import models

class Product(models.Model):
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=30)
    product_category = models.CharField(max_length=30)
    product_price = models.IntegerField()
    product_manifacturing_date= models.DateField()
    product_manifactured_by = models.CharField(max_length=40)
    
