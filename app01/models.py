from django.db import models

# Create your models here.

class GoodsInfo(models.Model):
    goodsName = models.CharField( max_length=200,null=True,db_index=True)
    goodsDesc = models.TextField(null=True)
    class Meta:
        db_table='GoodsInfo'


