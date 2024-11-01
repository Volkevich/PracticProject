from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import NewsForm
from .models import News, Category


# Create your views here.

class HomeNews(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'all_news'
    paginate_by = 5 #добавил погинацию

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список новостей'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class NewsByCategory(HomeNews):
    model = News
    template_name = "news/index.html"
    context_object_name = 'all_news'

    def get_queryset(self):
        return News.objects.filter(is_published=True, category_id=self.kwargs['category_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context


class ViewNews(DetailView):
    model = News
    # pk_url_kwarg = 'news_id'
    template_name = 'news/view_news.html'
    context_object_name = 'news_item'


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    # success_url = reverse_lazy('home')

#
# def index(request):
#     news = News.objects.all()
#     context = {
#         'all_news': news,
#         'title': 'Список новостей'
#     }
#     return render(request, 'news/index.html', context)
#
#
# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     # category = Category.objects.get(pk=category_id)
#     category = get_object_or_404(Category, pk=category_id)
#     context = {
#         'news': news,
#         'category': category
#     }
#     return render(request, 'news/category.html', context)
#
#
# def view_news(request, news_id):
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     return render(request, 'news/view_news.html', context={'news_item': news_item})
# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             #news = News.objects.create(**form.cleaned_data)
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#     return render(request, 'news/add_news.html', context={'form': form})
