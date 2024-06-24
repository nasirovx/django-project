from .models import Article
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ["title", 'anons', 'full_text', 'date']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Название",
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Анонс",
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Статья",
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': "Дата публткации",
            }),
        }