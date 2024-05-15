from django.shortcuts import redirect, render
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required, user_passes_test

from .forms import ArticlesForm
from .models import Articles


def news_home(request):
    news = Articles.objects.all()
    return render(request, 'news/news_home.html', {'news': news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'

    form_class = ArticlesForm


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news-delete.html'


def create(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news_home')
    else:
        form = ArticlesForm()

    context = {
        'form': form,
    }

    return render(request, 'news/create.html', context)
