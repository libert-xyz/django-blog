from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from models import *
from forms import *
# Create your views here.

def post_create(request):

    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print form.cleaned_data.get('title')
        instance.save()
        ## message success
        messages.success(request, 'Successfully created')
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request,'Not Successfully created')
    #if request.method == 'POST':
        #title = request.POST.get('title')
        #Post.objects.create(title = title)
    context = {
            'form':form,
            }

    return render(request,'post_form.html',context)

def post_detail(request,pk):
    #instance = Post.objects.get(id=3)
    instance = get_object_or_404(Post,id=pk)
    context = {'title':instance.title, 'instance':instance}

    return render(request,'post_detail.html',context)


def post_list(request):

    query = Post.objects.all()
    if request.user.is_authenticated():
        context = {'user': 'User', 'query':query}
    else:
        context = {'user':'Anonymous'}

    return render(request,'index.html',context)

def post_update(request,pk):

    instance = get_object_or_404(Post,id=pk)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        print form.cleaned_data.get('title')
        instance.save()
        messages.success(request, 'Successfully Updated',extra_tags='navbar')

        ## message success
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {'title':instance.title, 'instance':instance, 'form':form}

    return render(request,'post_form.html',context)

def post_delete(request,pk):

    instance = get_object_or_404(Post,id=pk)
    instance.delete()
    messages.success(request, 'Successfully Deleted')
    return redirect('posts:list')
