from __future__ import unicode_literals
from django.contrib import admin
from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	email = models.EmailField()

class UserAdmin(admin.ModelAdmin):
	list_display = ('username','password','email')
	
admin.site.register(User,UserAdmin)

class Recourse(models.Model):
	recoursename = models.CharField(max_length=50)
	recoursetime = models.CharField(max_length=8)
	recourseprice = models.FloatField();