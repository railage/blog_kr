from django.shortcuts import render, redirect, get_object_or_404
from .models import Article

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/list.html', {'articles': articles})

def article_create(request):
    if request.method == 'POST':
        Article.objects.create(
            title=request.POST['title'],
            content=request.POST['content']
        )
        return redirect('article_list')
    return render(request, 'articles/create.html')

def article_edit(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        article.title = request.POST['title']
        article.content = request.POST['content']
        article.save()
        return redirect('article_list')
    return render(request, 'articles/edit.html', {'article': article})

def article_delete(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    return redirect('article_list')