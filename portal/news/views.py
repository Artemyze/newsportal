from django.shortcuts import render, redirect
from django.views import View

from .forms import PostForm, SubForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView  # импортируем уже знакомый generic
from django.core.paginator import Paginator  # импортируем класс, позволяющий удобно осуществлять постраничный вывод

from .models import Post, Subscriber
from django.contrib.auth.mixins import PermissionRequiredMixin


class ProtectedView(LoginRequiredMixin, TemplateView):
    template_name = 'login/index.html'


class PostList(LoginRequiredMixin, ListView):
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


class PostCreate(PermissionRequiredMixin, CreateView):
    template_name = 'news/post_create.html'
    form_class = PostForm
    permission_required = ('news.add_post',)


class PostUpdate(PermissionRequiredMixin, UpdateView):
    template_name = 'news/post_create.html'
    form_class = PostForm
    permission_required = ('news.change_post',)

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDelete(PermissionRequiredMixin, DeleteView):
    template_name = 'news/post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
    permission_required = ('news.delete_post',)


class Subscribe(UpdateView):
    pass



