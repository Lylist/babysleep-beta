
# coding:utf-8

from django.shortcuts import render,render_to_response
from django import forms
from Model.models import User

from django.http import HttpResponse
# Create your views here.
class UserForm(forms.Form):
	username = forms.CharField(label='用户名',max_length=50)
	password = forms.CharField(label='密码',widget=forms.PasswordInput())
	email = forms.EmailField(label='邮箱')

def index(request):
    return render(request, 'login.html')

def login(request):
	if request.method == 'POST':
		userform = UserForm(request.POST)
		if userform.is_valid():
			username = userform.cleaned_data['username']
			password = userform.cleaned_data['password']

			user = User.objects.filter(username__exact=username,password__exact=password)

			if user:
				return render_to_response('login.html',{'userform':userform})
			else:
				return HttpResponse('用户名或密码错误,请重新登录')

	else:
		userform = UserForm()
	return render_to_response('login.html',{'userform':userform})
	
def children(request):
    return render(request, 'children.html')
	
def forgetpassword(request):
    return render(request, 'forgetpassword.html')
	
def registration(request):
	if request.method == 'POST':
		userform = UserForm(request.POST)
		if userform.is_valid():
			username = userform.cleaned_data['username']
			password = userform.cleaned_data['password']
			email = userform.cleaned_data['email']

			user = User.objects.create(username=username,password=password,email=email)
			user.save()

			return HttpResponse('registration success!!!')
	else:
		userform = UserForm()
	return render(request,'registration.html',{'userform':userform})
	
def about_me(request):
    return render(request, 'about-me.html')
	
def collection(request):
    return render(request, 'collection.html')
	
def main(request):
    return render(request, 'main.html')
	
def record(request):
    return render(request, 'record.html')
	
def recordadd(request):
    return render(request, 'recordadd.html')
	
def recordedit(request):
    return render(request, 'recordedit.html')
	
def setting(request):
    return render(request, 'setting.html')
	
def todayplay(request):
    return render(request, 'todayplay.html')
	
def update_resources(request):
    return render(request, 'update_resources.html')
	
def channel_user(request):
    return render(request, 'channel_user.html')
