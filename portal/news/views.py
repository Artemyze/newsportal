# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post
    template_name = 'flatpages/postlist.html'
    context_object_name = 'postlist'
    queryset = Post.objects.filter(categoryType='NW').order_by('dateCreate')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# создаём представление, в котором будут детали конкретного отдельного товара
class PostDetail(DetailView):
    model = Post  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'flatpages/postdetail.html'  # название шаблона будет postlist.html
    context_object_name = 'postdetail'
