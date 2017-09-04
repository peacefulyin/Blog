# -*- coding: utf-8 -*-
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20,unique=True)
    email = models.EmailField(default='')
    #phone = models.CharField(max_length=11)
    gender = models.BooleanField(default=True)
    def __str__(self):
        return self.name.encode('utf-8')

class Artical(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    pub_time = models.DateTimeField()
    tag = models.CharField(max_length=15,default='lifestyle')
    img_url = models.CharField(max_length=100,null=True,blank=True)
    read_num = models.IntegerField(default=0)
    like_num = models.IntegerField(default=0)
    user = models.ForeignKey(User)


    def __str__(self):
        return self.title.encode('utf-8')

class STag(models.Model):
    name = models.CharField(max_length=15)
    artical = models.ManyToManyField(Artical,null=True,blank=True)
    def __str__(self):
        return self.name.encode('utf-8')



class Comment(models.Model):
    name = models.CharField(max_length=100)
    pub_time = models.DateTimeField()
    text = models.CharField(max_length=300)
    artical = models.ForeignKey(Artical)
    def __str__(self):
        return self.name.encode('utf-8')