from lib2to3.fixes.fix_input import context
from django.shortcuts import render
from .models import News


def index(request):
    news = News.objects.all()
    contexts = {
        'news': news,
        'title': 'Список новостей'
    }
    return render(request, 'index.html', context=contexts)



