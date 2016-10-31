from django.shortcuts import render, render_to_response
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse('<h1> Hello World !</h1>')


def auth(request):
    print(request.GET)

    username, password = request.GET['username'], request.GET['password']
    if username == 'admin' and password == 'admin':
        return HttpResponse('login success!!!!')
    else:
        # 返回数据
        return HttpResponse('login field')


def login(request):
    # 返回一个页面
    return render_to_response('index.html')
