# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import User,Artical
from django.core.paginator import *

from django.shortcuts import render

def index(request,pagenum):
    user = User.objects.all()
    user1 = User.objects.get(name='yin')
    artical = user1.artical_set.get(pk=1)
    pagenator = Paginator(user,7)
    page = pagenator.page(int(pagenum))
    context = {'data':page,'artical':artical}
    return render(request,'myblog/index.html',context)

def text(request):
    return render(request,'myblog/text.html')

def about(request):
    return render(request,'myblog/about.html')

def show_artical(request,id):
    artical = Artical.objects.get(id=id)
    context = {'artical':artical}
    return render(request,'myblog/text.html',context)

def lunbo(request):
    return render(request,'myblog/lunbo.html')