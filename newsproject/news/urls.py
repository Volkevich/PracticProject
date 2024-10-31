from django.urls import path

from .views import add_news, HomeNews, NewsByCategory, ViewNews, CreateNews

urlpatterns = [
    # path('', index, name='home'),
    path('', HomeNews.as_view(), name='home'),
    path('<int:pk>/', ViewNews.as_view(), name='view_news'),
    # path('category/<int:category_id>/', get_category, name='category'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('add-news/', CreateNews.as_view(), name='add_news')
]
