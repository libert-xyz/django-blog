from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from models import *
from forms import *

# Create your views here.

def post_create(request):

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print form.cleaned_data.get('title')
        instance.save()
        ## message success
        messages.success(request, 'Successfully created')
        return HttpResponseRedirect(instance.get_absolute_url())

    #if request.method == 'POST':
        #title = request.POST.get('title')
        #Post.objects.create(title = title)
    context = {
            'form':form,
            }

    return render(request,'post_form.html',context)

def post_detail(request,slug=None):
    #instance = Post.objects.get(id=3)
    instance = get_object_or_404(Post,slug=slug)
    context = {'title':instance.title, 'instance':instance}

    return render(request,'post_detail.html',context)


def post_list(request):

    query_list = Post.objects.all() #.order_by("-timestamp")
    paginator = Paginator(query_list, 4) # Show 4 posts per page

    page = request.GET.get('page')
    try:
        query = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        query = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        query = paginator.page(paginator.num_pages)

    if request.user.is_authenticated():
        context = {'user': 'User', 'query':query}
    else:
        context = {'user':'Anonymous'}

    return render(request,'post_list.html',context)


def post_update(request,slug=None):

    instance = get_object_or_404(Post,slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        print form.cleaned_data.get('title')
        instance.save()
        messages.success(request, 'Successfully Updated',extra_tags='navbar')

        ## message success
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {'title':instance.title, 'instance':instance, 'form':form}

    return render(request,'post_form.html',context)

def post_delete(request,slug=None):

    instance = get_object_or_404(Post,slug=slug)
    instance.delete()
    messages.success(request, 'Successfully Deleted')
    return redirect('posts:list')
