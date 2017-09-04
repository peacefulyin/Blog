# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt
from models import User,Artical,Comment
from django.core.paginator import *
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render

import random


def test(request):
    return HttpResponse('hello,testing')

def index(request,classi):
    articals = Artical.objects.all()
    populars = Artical.objects.order_by('-like_num')
    result = random.sample(populars,4)
    pagenator = Paginator(articals,3)
    page = pagenator.page(int(1))
    context = {'articals':page,'populars':result}
    return render(request,'myblog/index.html',context)


def return_articals(request,pagenum):
    Articals = Artical.objects.all()
    pagenator = Paginator(Articals, 3)
    page = pagenator.page(int(pagenum))
    list = []
    for i in page:
        result = str(i.pub_time)[:10].split('-')
        pub_time = '{}年{}月{}日'.format(result[0],result[1],result[2])
        item = {
            'title': i.title,
            'content': i.content,
            'pub_time': pub_time,
            'tag': i.tag,
            'author': i.user.name,
        }
        list.append(item)
    dict = {'articals':list}
    return JsonResponse(dict)

def text(request,id):
    return render(request,'myblog/text.html')

def about(request):
    return render(request,'myblog/about.html')

def show_artical(request,id,pagenum=1):
    artical = Artical.objects.get(id=int(id))
    #comments = artical.comment_set.all()
    #pagenator = Paginator(comments, 5)
    #page = pagenator.page(int(pagenum))
    context = {'artical':artical}
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

