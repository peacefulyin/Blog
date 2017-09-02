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
    tag = models.CharField(max_length=15)
    user = models.ForeignKey(User)
    #content_url = models.CharField(max_length=30)
    img_url = models.CharField(max_length=100)
    def __str__(self):
        return self.title.encode('utf-8')

class Comment(models.Model):
    name = models.CharField(max_length=100)
    pub_time = models.DateTimeField()
    text = models.CharField(max_length=300)
    artical = models.ForeignKey(Artical)
    def __str__(self):
        return self.artical.encode('utf-8')