from django.shortcuts import render, get_object_or_404
from .models import ToiletInfo
from rest_framework import viewsets
from .serializers import ToiletSerializer

# Create your views here.

class ToiletViewSet(viewsets.ModelViewSet):
    queryset = ToiletInfo.objects.all()
    serializer_class = ToiletSerializer

def home(request):
    toilet_list = ToiletInfo.objects.all()
    # toilet_list = ToiletInfo.objects.order_by('-id')
    context = {'toilet_list' : toilet_list}
    return render(request, 'home.html', context)

def add(req):
    return render(req, 'toilet/add.html')

def info(request, id):
    toilet = get_object_or_404(ToiletInfo, pk=id)
    context = {'toilet' : toilet}
    return render(request, 'toilet/info.html', context)

def intro(req):
    return render(req, 'toilet/intro.html')
