from rest_framework import serializers
from .models import ToiletInfo

class ToiletSerializer(serializers.ModelSerializer):
    class Meta :
        model = ToiletInfo
        fields = ('id','tname', 'tlocation', 'tlat', 'tlong')
