from operator import truediv
from tkinter.tix import TixSubWidget
from django.db import models
# from django.contrib.auth.models import User
from users.models import User

# Create your models here.
class ToiletInfo(models.Model):
    squat = 0 # 푸세식
    toilet = 1 # 좌변식
    unknown = 3
    TTYPE_CHOICE = [(squat, '푸세식'), (toilet, '좌변식')]
    tname=models.CharField(max_length=200,null=True)
    tlocation=models.CharField(max_length=300,null=True)
    tlat = models.FloatField(null=True)
    tlong = models.FloatField(null=True)
    tnumber=models.CharField(max_length=200,null=True)
    topen=models.CharField(max_length=200,null=True)
    tbidget=models.BooleanField(null=True)
    tpaper=models.BooleanField(null=True)
    tpassword=models.BooleanField(null=True)
    tpublic=models.BooleanField(null=True)
    ttype=models.IntegerField(choices=TTYPE_CHOICE,
                                blank=True,
                                null=True,
                                default=unknown)



class Comment(models.Model):
    score=models.IntegerField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    toilet = models.ForeignKey(ToiletInfo, related_name= 'comment_set', on_delete=models.CASCADE)

    def __str__(self):
        return self.toilet.tname