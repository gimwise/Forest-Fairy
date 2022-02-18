# from asyncio.windows_events import NULL
from pyexpat.errors import messages
# from ssl import AlertDescription
from django.shortcuts import redirect, render, get_object_or_404
# from django.contrib.auth import get_user_model
from .models import ToiletInfo, Comment, Bookmarks
from users.models import User
from .forms import ToiletForm, CommentForm
from django.db.models import Avg
# from django.core import serializers
from django.http import HttpResponse, JsonResponse
import json
from django.contrib import messages

# Create your views here.


def getJson(request):
    toilet_list = ToiletInfo.objects.all()
    toilets = []
    for toilet in toilet_list:
        dict = {
            'pk': toilet.id,
            'tname': toilet.tname,
            'tlocation': toilet.tlocation,
            'tlat': toilet.tlat,
            'tlong': toilet.tlong,
            'tnumber': toilet.tnumber,
            'topen': toilet.topen,
            'tbidget': toilet.tbidget,
            'tpaper': toilet.tpaper,
            'tpassword': toilet.tpassword,
            'tpublic': toilet.tpublic,
            'ttype': toilet.ttype,
            'avg': toilet.comment_set.aggregate(avg=Avg('score'))
        }
        # toilet_json.append(json.dumps(dict, ensure_ascii=False))
        toilets.append(dict)
    toilet_json = json.dumps(toilets)
    return HttpResponse(toilet_json, content_type="text/json-comment-filtered; charset=utf-8")


def getScore(request):
    toilet_list = ToiletInfo.objects.all()
    toilet_score_avg = []
    for toilet in toilet_list:
        dict = {'tname': toilet.tname,
                'avg': toilet.comment_set.aggregate(avg=Avg('score'))}
        toilet_score_avg.append(json.dumps(dict, ensure_ascii=False))
    return HttpResponse(content=toilet_score_avg, content_type="text/json-comment-filtered; charset=utf-8")

def myComments(req):
    commented_user = get_object_or_404(User,pk=req.user.id)
    return render(req, 'toilet/myComments.html', {'commented_user':commented_user})

def home(request):
    toilet_list = ToiletInfo.objects.all()
    toilets = []
    for toilet in toilet_list:
        dict = {
            'pk': toilet.id,
            'tname': toilet.tname,
            'tlocation': toilet.tlocation,
            'tlat': toilet.tlat,
            'tlong': toilet.tlong,
            'tnumber': toilet.tnumber,
            'topen': toilet.topen,
            'tbidget': toilet.tbidget,
            'tpaper': toilet.tpaper,
            'tpassword': toilet.tpassword,
            'tpublic': toilet.tpublic,
            'ttype': toilet.ttype,
            'avg': toilet.comment_set.aggregate(avg=Avg('score'))
        }

        toilets.append(dict)
    toilet_json = json.dumps(toilets)
    context = {'toilet_list': toilet_json}
    return render(request, 'home.html', context)

def toptions(answer):
    if(answer == 'true'):
        return True
    elif(answer == 'false'):
        return False
    else:
        return None
            

def add(request):
    if request.method == "POST":
        try:
            toilet_exist = ToiletInfo.objects.get(tlat=request.POST["tlat"], tlong=request.POST["tlong"])
        except:
            toilet_exist = None
        if(toilet_exist == None):
            form = ToiletForm(request.POST)
            if form.is_valid():
                toilet = form.save(commit=False)
                toilet.tlat = request.POST["tlat"]
                toilet.tlong = request.POST["tlong"]
                toilet.tlocation = request.POST["tlocation"]
                # if request.POST.get('ttype') != None:
                #     toilet.ttype = request.POST.get('ttype')
                toilet.tpublic = toptions(request.POST.get('tpublic'))
                toilet.tpassword = toptions(request.POST.get('tpassword'))
                toilet.tpaper = toptions(request.POST.get('tpaper'))
                toilet.tbidget = toptions(request.POST.get('tbidget'))
                toilet.save()
                return redirect('toilet:info',toilet.id)
        else:
            messages.warning(request, "위치 중복 경고")
            return render(request,'toilet/info.html',{'toilet':toilet_exist})
    else:
        form = ToiletForm()
        context = {'form': form}
        return render(request, 'toilet/add.html', context)


def edit(request, id):
    post = ToiletInfo.objects.get(id=id)
    if request.method == "POST":
        form = ToiletForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            post.tpublic = form.cleaned_data['tpublic']
            post.tpassword = form.cleaned_data['tpassword']
            post.tpaper = form.cleaned_data['tpaper']
            post.ttype = form.cleaned_data['ttype']
            post.tbidget = form.cleaned_data['tbidget']
            post.save()
            return redirect('/'+str(post.pk))
    else:
        form = ToiletForm()
        context = {'form': form}
        return render(request, 'toilet/edit.html', context)


def info(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            registForm = CommentForm(request.POST)
            if registForm.is_valid():
                rating = registForm.save(commit=False)
                uid = request.user.id
                print(uid)
                tid = request.POST.get('tid')
                rating.score = request.POST.get('score')
                rating.author = get_object_or_404(User, pk=uid)
                rating.toilet = get_object_or_404(ToiletInfo, pk=tid)
                rating.save()
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                return JsonResponse({'success': 'true', 'score': rating.score}, safe=False)
            else:
                print(registForm.errors)
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                print(registForm.non_field_errors)
        else:
            toilet = get_object_or_404(ToiletInfo, pk=id)
            uid = request.user.id
            user = get_object_or_404(User, pk=uid)
            try:
                comment_exist = Comment.objects.get(author=user, toilet=toilet)
            except:
                comment_exist = None
            try:
                bookmark_exist = Bookmarks.objects.get(user=user, toilet=toilet)
            except:
                bookmark_exist = None
            # print(comment_exist, bookmark_exist)
            context = {'toilet': toilet, 'comment_exist':comment_exist,'bookmark_exist': bookmark_exist}
            return render(request, 'toilet/info.html', context)
    else :
        toilet = get_object_or_404(ToiletInfo, pk=id)
        avg = toilet.comment_set.aggregate(avg=Avg('score'))
        context = {'toilet': toilet, 'comment_exist':avg}
        return render(request, 'toilet/info.html', context)




def intro(req):
    return render(req, 'toilet/intro.html')


def bookmarks(request, id):
    bookmarks = Bookmarks.objects.filter(user=id)

    context = {
        'bookmarks': bookmarks
    }
    return render(request, 'toilet/bookmarks.html', context)


def addBookmark(request, toilet_id):
    toilet = ToiletInfo.objects.get(pk=toilet_id)
    uid = request.user.id
    user = get_object_or_404(User, pk=uid)

    if request.method == 'POST':
        try:
            mark = Bookmarks.objects.get(user=user, toilet=toilet)
            mark.delete()
        except:
            mark = Bookmarks()
            mark.toilet = toilet
            mark.user = user
            mark.save()
    return redirect('toilet:info', toilet_id)


def delBookmark(request, toilet_id):
    toilet = ToiletInfo.objects.get(pk=toilet_id)
    uid = request.user.id
    user = get_object_or_404(User, pk=uid)

    if request.method == 'POST':
        mark = Bookmarks.objects.get(user=user, toilet=toilet)
        mark.delete()
        return redirect('toilet:bookmarks', uid)


