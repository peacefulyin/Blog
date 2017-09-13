# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.paginator import Paginator
from collections import defaultdict


from models import User,Sheet,Comment

def base(request):
    return render(request, 'piano/base.html')

def index(request):
    sheet = Sheet.objects.values('album').distinct().order_by('album')[0:42]
    paginator = Paginator(sheet,6)
    #pages = [{'page%s'%str(i):paginator.page(i)} for i in paginator.page_range]
    context = defaultdict()
    for i in paginator.page_range:
        context['sheet'+str(i)] = paginator.page(i)

    return render(request, 'piano/index.html' ,context)

@csrf_exempt
def list(request, title):
    sheets = Sheet.objects.filter(album=title)
    list = [{'music':x.music,'page_num':x.page_num} for x in sheets]

    return JsonResponse({'list':list})


def show_sheet(request, name):
    sheet = Sheet.objects.get(music=name)
    for_list = [x+1 for x in range(sheet.page_num)]
    print for_list
    context = {'sheet':sheet,'for_list':for_list}
    return render(request,'piano/sheet.html',context)

def category(request, name):
    sheets = Sheet.objects.values('album').distinct().order_by('album')
    len_sheet = len(sheets)
    quarter = len_sheet/4
    sheet = ''
    if name == 'new':
        sheet = sheets[:quarter]
    elif name == 'hot':
        sheet = sheets[quarter:quarter*2]
    elif name == 'treasure':
        sheet = sheets[quarter*2:quarter*3]
    elif name == 'like':
        sheet = sheets[quarter*3:]
    elif name == 'all':
        sheet = sheets
    context = {'sheet':sheet}
    return render(request, 'piano/list.html', context)
