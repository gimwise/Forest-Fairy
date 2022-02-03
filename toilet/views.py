from django.shortcuts import render, get_object_or_404
from .models import ToiletInfo
from django.core import serializers
from django.http import HttpResponse

# Create your views here.

def getJson(request):
    toilet_list = ToiletInfo.objects.all()
    toilet_json = serializers.serialize('json', toilet_list)
    return HttpResponse(toilet_json, content_type="text/json-comment-filtered")

def home(request):
    toilet_list = ToiletInfo.objects.all()
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
