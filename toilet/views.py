from django.shortcuts import redirect, render, get_object_or_404
from .models import ToiletInfo
from django.db.models import Avg
from django.core import serializers
from django.http import HttpResponse, JsonResponse
import json

# Create your views here.
def getJson(request):
    toilet_list = ToiletInfo.objects.all()
    toilets = []
    for toilet in toilet_list :
        dict = {
                'pk' : toilet.id,
                'tname': toilet.tname,
                'tlocation' : toilet.tlocation,
                'tlat' : toilet.tlat,
                'tlong' : toilet.tlong,
                'tnumber' : toilet.tnumber,
                'topen' : toilet.topen,
                'tbidget' : toilet.tbidget,
                'tpaper' : toilet.tpaper,
                'tpassword' : toilet.tpassword,
                'tpublic' : toilet.tpublic,
                'ttype' : toilet.ttype,
                'avg': toilet.comment_set.aggregate(avg=Avg('score'))
                }
        # toilet_json.append(json.dumps(dict, ensure_ascii=False))
        toilets.append(dict)
    toilet_json = json.dumps(toilets)
    return HttpResponse(toilet_json, content_type="text/json-comment-filtered; charset=utf-8")

def getScore(request):
    toilet_list = ToiletInfo.objects.all()
    toilet_score_avg = []
    for toilet in toilet_list :
        dict = {'tname': toilet.tname, 'avg': toilet.comment_set.aggregate(avg=Avg('score'))}
        toilet_score_avg.append(json.dumps(dict, ensure_ascii=False))
    return HttpResponse(content=toilet_score_avg, content_type="text/json-comment-filtered; charset=utf-8")


def home(request):
    toilet_list = ToiletInfo.objects.all()

    context = {'toilet_list' : toilet_list}
    return render(request, 'home.html', context)

def add(req):
    if req.method=="POST":
        post= ToiletInfo()
        post.tlat = req.POST["tlat"]
        post.tlong = req.POST["tlong"]
        post.tlocation = req.POST["tlocation"]
        post.tpublic = True if req.POST.get('tpublic',False) else False 
        post.tpassword = True if req.POST.get('tpassword',False) else False
        post.tpaper = True if req.POST.get('tpaper',False) else False
        post.ttype = True if req.POST.get('ttype',False) else False
        post.tbidget = True if req.POST.get('tbidget',False) else False
        post.save()
        return redirect('/')
    else:                       
        return render(req, 'toilet/add.html')

def info(request, id):
    toilet = get_object_or_404(ToiletInfo, pk=id)
    context = {'toilet' : toilet}
    return render(request, 'toilet/info.html', context)

def intro(req):
    return render(req, 'toilet/intro.html')
