from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

from .models_resources.source import CatSource


class Author(models.Model):
    author_user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_rating = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.author_user}'

    def update_rating(self):
        postRat = self.post_set.all().aggregate(postRating=Sum('rating'))
        pRat = 0
        pRat += int(postRat.get('postRating'))

        comRat = self.author_user.comment_set.all().aggregate(commentRating=Sum('rating'))
        cRat = 0
        cRat += comRat.get('commentRating')

        self.author_rating = cRat + pRat * 3
        self.save()


class Category(models.Model):
    cat_model = models.CharField(max_length=64, unique=True)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categoryType = models.CharField(max_length=2, choices=CatSource.CATEGORY_CHOICES)
    dateCreate = models.DateTimeField(auto_now_add=True)
    postCategory = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=128)

    text = models.TextField()
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.author.objects.all().User.get_username()}{self.title}{self.dateCreate}'

    def preview(self):
        return f'{self.text[0:123]}...'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
