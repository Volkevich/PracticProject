import re

from django import forms
from django.core.exceptions import ValidationError

from news.models import News


# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=150, label='Название', widget=forms.TextInput(
#         attrs={
#             'class': 'form-control'
#         }
#     ))
#     content = forms.CharField(label='Содержание', required=False, widget=forms.Textarea(
#         attrs={
#             'class': 'form-control',
#             'rows': 5
#         }
#     ))
#     is_published = forms.BooleanField(label='Опубликовать?', initial=True)
#     category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория',
#                                       empty_label='Выберите категорию', widget=forms.Select(
#             attrs={
#                 'class': 'form-control'
#             }
#         ))

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'category', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Выберите категорию"

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'^\d+$', title):
            raise ValidationError('Название не должно содержать только цифры')
        if re.match(r'^\d+', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title

    def clean_is_published(self):
        if self.cleaned_data['is_published']:
            return self.cleaned_data['is_published']
        raise ValidationError('Статус публикации должен быть подтверждён')
