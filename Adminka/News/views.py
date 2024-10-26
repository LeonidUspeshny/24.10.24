from lib2to3.fixes.fix_input import context

from django.shortcuts import render
# from django.shortcuts import HttpResponse

from .models import News


def index(request):
    news = News.objects.all()
    contexts = {
        'news': news,
        'title': 'Список новостей'
    }
    return render(request, 'index.html', context=contexts)
    # res = '<h1>Список новостей</h1>'
    # for i in news:
    #     res += f'<div>\n<p>{i.title}</p>\n<p>{i.content}</p>\n</div>\n<hr>\n'
    # return HttpResponse(res)


