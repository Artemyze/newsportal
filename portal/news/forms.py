from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):  # добавляем галочку, или же true-false поле
    class Meta:
        model = Post
        fields = ['author', 'postCategory', 'categoryType', 'title',
                  'text']
