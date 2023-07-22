from django.db import models

# Create your models here.
class food(models.Model):
    fname=models.CharField(max_length=50)
    fqty=models.IntegerField()
    fdetails=models.CharField(max_length=50)
    fimg=models.ImageField()

    # def __str__(self):
    #     return self.fname

