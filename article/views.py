from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
# Create your views here.


def index(request):
    article_list = Article.objects.order_by('-pub_date')[:5]
    context = {'list_article': article_list}
    return render(request, 'article/index.html', context)


def detail(request, article_id):
    return HttpResponse("you are look at article %s" %article_id)

