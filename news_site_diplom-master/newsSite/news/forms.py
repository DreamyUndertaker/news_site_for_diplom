from .models import Articles, Category
from django.forms import DateInput, ModelForm, TextInput, Textarea, FileInput, Select


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date', 'image', 'category']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'дд.мм.гггг'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
            "image": FileInput(attrs={
                'class': 'form-control',
            }),
            "category": Select(attrs={
                'class': 'form-control',
            }),
        }
