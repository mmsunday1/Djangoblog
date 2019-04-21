from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def posts_id(self):
        return self.id


class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    #posts = models.ForeignKey(Post, on_delete=models.CASCADE)
    posts = models.ManyToManyField(Post, blank=True,
    related_name='categories')
    #posts_id = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
