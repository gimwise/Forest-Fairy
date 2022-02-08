from django.shortcuts import redirect, render, get_object_or_404
from .models import ToiletInfo
from users.models import User
from .forms import ToiletForm, CommentForm
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

def add(request):
    if request.method=="POST":
        form = ToiletForm(request.POST)
        if form.is_valid() :
            toilet = form.save(commit=False)
            toilet.tlat = request.POST["tlat"]
            toilet.tlong = request.POST["tlong"]
            toilet.tlocation = request.POST["tlocation"]
            toilet.tpublic = True if request.POST.get('tpublic',False) else False
            toilet.tpassword = True if request.POST.get('tpassword',False) else False
            toilet.tpaper = True if request.POST.get('tpaper',False) else False
            toilet.ttype = True if request.POST.get('ttype',False) else False
            toilet.tbidget = True if request.POST.get('tbidget',False) else False
            toilet.save()
            return redirect('/')
    else:
        form = ToiletForm()
        context = {'form' : form}
    return render(request, 'toilet/add.html', context)

def info(request, id):
    if request.method=="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            uid = request.user.id
            print(uid)
            tid = request.POST.get('tid')
            rating.score = request.POST.get('score')
            rating.author = get_object_or_404(User, pk=uid)
            rating.toilet = get_object_or_404(ToiletInfo, pk=tid)
            rating.save()
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            return JsonResponse({'success':'true', 'score':rating.score}, safe=False)
        else:
            print(form.errors)
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            print(form.non_field_errors)
    else :
        toilet = get_object_or_404(ToiletInfo, pk=id)
        context = {'toilet' : toilet}
        return render(request, 'toilet/info.html', context)
    return JsonResponse({'success':'false'})
    

def intro(req):
    return render(req, 'toilet/intro.html')

