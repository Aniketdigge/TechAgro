from django.db import models

class Product(models.Model):
    Product_id = models.AutoField
    Product_name = models.CharField(max_length=50)
    Desc = models.CharField(max_length=300)
    Pub_date = models.DateField()
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)

   


