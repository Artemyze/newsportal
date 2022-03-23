from django.shortcuts import render
from django.views.generic import ListView, DetailView  # импортируем уже знакомый generic
from django.core.paginator import Paginator  # импортируем класс, позволяющий удобно осуществлять постраничный вывод

from .models import Post
from .filters import PostFilter


class PostList(ListView):
    model = Post
    template_name = 'flatpages/postlist.html'
    context_object_name = 'postlist'
    queryset = Post.objects.filter(categoryType='NW').order_by('dateCreate')
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


# создаём представление, в котором будут детали конкретного отдельного товара
class PostDetail(DetailView):
    model = Post  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'flatpages/postdetail.html'  # название шаблона будет postlist.html
    context_object_name = 'postdetail'
