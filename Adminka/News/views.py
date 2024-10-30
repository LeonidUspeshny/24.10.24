from lib2to3.fixes.fix_input import context
from django.shortcuts import render
from .models import News, Category


def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    contexts = {
        'news': news,
        'title': 'Список новостей',
        'categories': categories,
    }
    return render(request, 'News/index.html', context=contexts)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'categories': categories,
        'category': category

    }
    return render(request, 'News/category.html', context=context)


