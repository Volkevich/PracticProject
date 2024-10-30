from django.urls import path

from .views import index, get_category, view_news

urlpatterns = [
    path('', index, name='home'),
    path('<int:news_id>/', view_news, name='view_news'),
    path('category/<int:category_id>/', get_category, name='category')
]