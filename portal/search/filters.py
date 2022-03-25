from django_filters import FilterSet
from news.models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'dateCreate': ['gt'],
            'title': ['icontains'],
            'author__author_user__last_name': ['icontains']
        }
