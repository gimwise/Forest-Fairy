from operator import truediv
from tkinter.tix import TixSubWidget
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToiletInfo(models.Model):
    tname=models.CharField(max_length=200,null=True)
    tlocation=models.CharField(max_length=300,null=True)
    tnumber=models.CharField(max_length=200,null=True)
    topen=models.CharField(max_length=200,null=True)
    tbidget=models.BooleanField(null=True)
    tpaper=models.BooleanField(null=True)
    tpassword=models.BooleanField(null=True)
    tpublic=models.BooleanField(null=True)
    ttype=models.BooleanField(null=True)


class Comment(models.Model):
    score=models.IntegerField()
    author =  models.ForeignKey(User, on_delete=models.CASCADE)