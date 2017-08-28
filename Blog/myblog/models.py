# -*- coding: utf-8 -*-
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20,unique=True)
    email = models.EmailField()
    #phone = models.CharField(max_length=11)
    gender = models.BooleanField(default=True)
    def __str__(self):
        return self.name.encode('utf-8')

class Artical(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    pub_time = models.DateTimeField()
    user = models.ForeignKey(User)
    #content_url = models.CharField(max_length=30)
    img_url = models.CharField(max_length=100)
    def __str__(self):
        return self.title.encode('utf-8')
