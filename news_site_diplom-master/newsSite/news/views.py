from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import ArticlesForm
from .models import Articles, Category


def index(request):
    today = timezone.now().date()
    news = Articles.objects.filter(date__gte=today)
    return render(request, 'news/index.html', {'news': news})


def news_home(request):
    news = Articles.objects.all()
    categories = Category.objects.all()
    selected_category = request.GET.get('category')
    if selected_category:
        news = news.filter(category_id=selected_category)

    return render(request, 'news/news_home.html', {'news': news, 'categories': categories})


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
