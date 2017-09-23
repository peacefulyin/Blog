# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.contrib import admin

class ArticalAdmin(admin.ModelAdmin):
    model = Artical
    filter_horizontal = ('name',)

admin.site.register(User)
admin.site.register(Artical)
admin.site.register(Comment)
admin.site.register(STag)
