from operator import truediv
#from tkinter.tix import TixSubWidget
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# from django.contrib.auth.models import User
from users.models import User

# Create your models here.
class ToiletInfo(models.Model):
    squat = 0 # 좌변기
    toilet = 1 # 양변기
    unknown = 3
    TTYPE_CHOICE = [(squat, '좌변기'), (toilet, '양변기')]
    id = models.AutoField(primary_key=True)
    tname=models.CharField(max_length=200)
    tlocation=models.CharField(max_length=300)
    tlat = models.FloatField() #위도
    tlong = models.FloatField() #경도
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
    score=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    toilet = models.ForeignKey(ToiletInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.toilet.tname

class Bookmarks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    toilet = models.ForeignKey(ToiletInfo, on_delete=models.CASCADE)