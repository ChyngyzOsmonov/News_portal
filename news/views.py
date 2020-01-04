from django.shortcuts import render
from django.views.generic import ListView
from .models import News


class NewsListView(ListView):
    model = News
    template_name = 'blog.html'
    context_object_name = 'blog_object'
