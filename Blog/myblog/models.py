# -*- coding: utf-8 -*-
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20,unique=True)
    email = models.EmailField(unique=True)
    phone = models.IntegerField(max_length=11)
    gender = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Artical(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    pub_time = models.DateTimeField()
    user = models.ForeignKey(User)
    def __str__(self):
        return self.title
