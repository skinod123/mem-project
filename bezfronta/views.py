from django.shortcuts import render

# Create your views here.

from pickletools import read_unicodestring4
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404


from .models import Post, Question


def page_indeks(request):
    posts = Post.objects.all()
    for post in posts:
        print(post.id)
        print(post.title)

    context = {
        'posts': posts,
        'title': 'свежие посты'
        }
    return render(request, 'bezfronta/index.html', context)


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'templates/bezfronta/index.html', context)