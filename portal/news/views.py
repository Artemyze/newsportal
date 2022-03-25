from django.shortcuts import render
from .forms import PostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView  # импортируем уже знакомый generic
from django.core.paginator import Paginator  # импортируем класс, позволяющий удобно осуществлять постраничный вывод

from .models import Post


class PostList(ListView):
    model = Post
    template_name = 'news/postlist.html'
    context_object_name = 'postlist'
    queryset = Post.objects.filter(categoryType='NW').order_by('dateCreate')
    paginate_by = 10


# создаём представление, в котором будут детали конкретного отдельного товара
class PostDetail(DetailView):
    model = Post  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'news/postdetail.html'  # название шаблона будет postlist.html
    context_object_name = 'postdetail'


class PostCreate(CreateView):
    template_name = 'news/post_create.html'
    form_class = PostForm


class PostUpdate(UpdateView):
    template_name = 'news/post_create.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDelete(DeleteView):
    template_name = 'news/post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'