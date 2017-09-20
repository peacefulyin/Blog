# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import *
from django.http import JsonResponse,HttpResponse
from django.views.decorators.cache import cache_page
from django.shortcuts import render

from models import User, Artical, Comment, STag

import random



def index(request,classi):
    articals = Artical.objects.order_by('-id')
    pagenator = Paginator(articals,3)
    page = pagenator.page(int(1))

    populars = Artical.objects.order_by('-like_num')
    randpopular = random.sample(populars,4)
    relate = random.sample(populars,3)

    tags = STag.objects.all()
    randtags = random.sample(tags, 15)
    context = {'articals':page,'populars':randpopular,'relate':relate,'tags':randtags}
    return render(request,'myblog/index.html',context)


def return_articals(request,pagenum):
    Articals = Artical.objects.order_by('-id')
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
            'id':i.id,
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
    related = Artical.objects.order_by('-pub_time')[:3]

    populars = Artical.objects.order_by('-like_num')
    randpopular = random.sample(populars, 4)

    tags = STag.objects.all()
    randtags = random.sample(tags, 15)

    comments = artical.comment_set.all().order_by('pub_time')
    pagenator = Paginator(comments,10)
    page = pagenator.page(1)

    context = {'artical':artical,'populars':randpopular,'tags':randtags,'comments':page, 'related':related}

    return render(request,'myblog/text.html',context)

@csrf_exempt
def receive_comment(request):
    post_list = request.POST
    artical_id = post_list.get('artical_id')
    artical = Artical.objects.get(pk=artical_id)

    c = Comment()
    c.name = post_list.get('name')
    c.pub_time = post_list.get('pub_time')
    c.text = post_list.get('text')
    c.artical = artical
    c.save()
    return JsonResponse({'response':'ok'})



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


def base(request):
    return render(request,'myblog/base.html')
