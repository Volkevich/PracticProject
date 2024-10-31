
from django import forms

from news.models import Category


class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, label='Название')
    content = forms.CharField(label='Содержание', required=False)
    is_published = forms.BooleanField(label='Опубликовать?')
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Выберите категорию')