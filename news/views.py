from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView

def news(request):
    data = Article.objects.order_by('-date')
    return render(request, 'main/news.html', {"data":data})

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Форма была неверной"

    form = ArticleForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/create.html', data)


class NewsDetailView(DetailView):
    model = Article
    template_name = 'main/detail_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Article
    template_name = 'main/create.html'
    form_class = ArticleForm

class NewsDeleteView(DeleteView):
    model = Article
    success_url = '/news/'
    template_name = 'main/news_delete.html'