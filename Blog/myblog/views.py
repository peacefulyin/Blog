# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt

from models import User,Artical,Comment
from django.core.paginator import *
from django.http import JsonResponse

from django.shortcuts import render

"""
def index(request,pagenum):
    user = User.objects.all()
    user1 = User.objects.get(name='yin')
    artical = user1.artical_set.get(pk=1)
    pagenator = Paginator(user,6)
    page = pagenator.page(int(pagenum))
    context = {'data':page,'artical':artical}
    return render(request,'myblog/index.html',context)
"""

def index(request):
    user = User.objects.all()
    user1 = User.objects.get(name='yin')
    artical = user1.artical_set.get(pk=1)
    pagenator = Paginator(user,3)
    page = pagenator.page(int(1))
    context = {'data':page,'artical':artical}
    return render(request,'myblog/index.html',context)


def return_json(request,pagenum):
    user = User.objects.all()
    user1 = User.objects.get(name='yin')
    artical = user1.artical_set.get(pk=1)
    pagenator = Paginator(user, 3)
    page = pagenator.page(int(pagenum))
    context = {'data': page, 'artical': artical}
    list = []
    for i in page:
        list.append(i.name)
    dict = {'a':list,'b':artical.content}
    #dict = json.dumps(dict)
    return JsonResponse(dict)

def text(request):
    return render(request,'myblog/text.html')

def about(request):
    return render(request,'myblog/about.html')

def show_artical(request,id,pagenum=1):
    artical = Artical.objects.get(id=1)
    comments = artical.comment_set.all()
    pagenator = Paginator(comments, 5)
    page = pagenator.page(int(pagenum))
    context = {'artical':artical,'comments':page}
    return render(request,'myblog/text.html',context)

@csrf_exempt
def return_comments(request,pagenum):
    title = request.POST.get('atitle')
    artical = Artical.objects.get(title=title)
    comments = artical.comment_set.all()
    pagenator = Paginator(comments, 5)
    page = pagenator.page(int(pagenum))
    list = []
    for i in page:
        list.append({'name':i.name,'pub_time':i.pub_time,'text':i.text})
    context = {'comments':list}
    return JsonResponse(context)


def test(request):
    return render(request,'myblog/comment.html')

@csrf_exempt
def send_data(request):
    name = request.POST.get('name')
    text = request.POST.get('text')
    time = request.POST.get('time')
    aname = request.POST.get('aname')
    artical = Artical.objects.get(title=aname)
    Comment.objects.get_or_create(name=name, pub_time=time, text = text, artical = artical)

    return JsonResponse({'1':'1'})

