from django.forms import ModelForm
from news.models import Subscriber


class SubscribeForm(ModelForm):  # добавляем галочку, или же true-false поле
    class Meta:
        model = Subscriber
        fields = ['categorySub', 'userSub']