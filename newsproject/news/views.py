from lib2to3.fixes.fix_input import context

from django.shortcuts import render

from .models import News, Category


# Create your views here.

def index(request):
    news = News.objects.all()
    context = {
        'all_news': news,
        'title': 'Список новостей'
    }
    return render(request, 'news/index.html', context)

def get_category(request, category_id):
    news = News.objects.filter(category_id = category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'category': category
    }
    return render(request, 'news/category.html', context)


def view_news(request, news_id):
    news_item = News.objects.get(pk=news_id)
    return render(request,'news/view_news.html', context={'news_item': news_item})
