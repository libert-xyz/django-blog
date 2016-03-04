from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from models import *
# Create your views here.

def post_create(request):

    return HttpResponse('<h1>Create</h1>')


def post_detail(request):
    #instance = Post.objects.get(id=3)
    instance = get_object_or_404(Post,id=1)
    context = {'title':instance.title, 'instance':instance}

    return render(request,'post_detail.html',context)


def post_list(request):

    query = Post.objects.all()
    if request.user.is_authenticated():
        context = {'title': 'User', 'query':query}


    else:
        context = {'user':'Anonymous'}

    return render(request,'index.html',context)

def post_update(request):

    return HttpResponse('<h1>update</h1>')

def post_delete(request):

    return HttpResponse('<h1>delete</h1>')
