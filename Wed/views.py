from django.shortcuts import render
from .models import *
# Create your views here.
def homepage(request):
    context = {
        'homepage' : Intro.objects.all(),
        'story' : Story.objects.all(),
        'main_story' : Main_Story.objects.all(),
        'gallery' : Gallery.objects.all(),
        'prog_detail' : Prog_Detail.objects.all(),
    }
    return render(request, 'index.html', context)

def story(request):
    context = {
        'story' : Story.objects.all(),
        'main_story' : Main_Story.objects.all(),
        'gallery' : Gallery.objects.all(),
    }
    return render(request, 'story.html', context)

def gallery(request):
    context = {
        'gallery' : Gallery.objects.all(),
    }
    return render(request, 'gallery.html', context)

def blog(request):
    context = {
        'blog' : Blog.objects.all(),
    }
    return render(request, 'blog.html', context)

def single_blog(request):
    context = {
        'single_blog' : Single_blog.objects.all(),
    }
    return render(request, 'single_blog.html', context)

def accommodation(request):
    context = {
        'accommodation' : Accommodation.objects.all()
    }
    return render(request, 'accommodation.html', context)

def elements(request):
    return render(request, 'elements.html')

def contact(request):
    return render(request, 'contact.html')