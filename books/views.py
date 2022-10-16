from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import News
from .models import Category
from datetime import datetime

def index(request):
    return render(request, 'books/index.html', {'age': '17'})

def home(request):
    return HttpResponse('<h1>My home</h1>')

def main_page(requests):
    Newss = News.objects.all()
    return render(requests, 'books/main page.html', {'news': Newss})

def news(requests):
    Newss = News.objects.all()
    cats = Category.objects.all()
    time = datetime.now()
    return render(requests, 'books/news.html', {'news': Newss, 'time_now': time, 'cats':cats})

def test(requests):
    posts = News.objects.all()
    return render(requests, 'books/test.html', {'news': posts})

def accidents(requests):
    Newss = News.objects.all()
    time = datetime.now()
    return render(requests, 'books/accidents.html', {'news': Newss, 'time_now': time})

def interview(requests):
    Newss = News.objects.all()
    time = datetime.now()
    return render(requests, 'books/interview.html', {'news': Newss, 'time_now': time})

def politics(requests):
    Newss = News.objects.all()
    time = datetime.now()
    return render(requests, 'books/politics.html', {'news': Newss, 'time_now': time})


def show_post(request, slug):
    post = get_object_or_404(News, slug=slug)

    context = {
        'post': post,
        'title': post.title,
        'content': post.content,
        'cat_selected': 1,
        'most_important': post.most_important,
        'photo': post.photo,
        'time_create': post.time_create
    }

    return render(request, 'books/post.html', context=context)


def economy(requests):
    Newss = News.objects.all()
    time = datetime.now()
    return render(requests, 'books/economy.html', {'news': Newss, 'time_now': time})


def about_tam_by(requests):
    Newss = News.objects.all()
    time = datetime.now()
    return render(requests, 'books/about_tam_by.html', {'news': Newss, 'time_now': time})

def tell(requests):
    Newss = News.objects.all()
    time = datetime.now()
    return render(requests, 'books/tell.html', {'news': Newss, 'time_now': time})


