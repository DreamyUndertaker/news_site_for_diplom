from .models import Articles
from django.forms import DateInput, ModelForm, TextInput, Textarea, FileInput

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date', 'image']

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
        }