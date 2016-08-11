from django.shortcuts import render
from blog.models import Article
# Create your views here.

def myview(request):
    posts = Article.objects.filter(published=True)

    return render(request, 'base.html', {'posts': posts})
