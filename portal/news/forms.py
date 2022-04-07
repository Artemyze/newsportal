from django.forms import ModelForm
from .models import Post, Subscriber


class PostForm(ModelForm):  # добавляем галочку, или же true-false поле
    class Meta:
        model = Post
        fields = ['author', 'postCategory', 'categoryType', 'title',
                  'text']


class SubForm(ModelForm):  # добавляем галочку, или же true-false поле
    class Meta:
        model = Subscriber
        fields = ['categorySub', 'userSub']
