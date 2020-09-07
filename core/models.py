from django.db import models

# Create your models here.
class item(models.Model):
    itemname=models.CharField(max_length=50)
    price=models.FloatField(max_length=50)
    ite_id=models.IntegerField()


    def __str__(self):
        return self.itemname