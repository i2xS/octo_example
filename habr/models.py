from django.db import models


class User(models.Model):
    name = models.CharField(primary_key=True, max_length=128)


class Category(models.Model):
    name = models.CharField(primary_key=True, max_length=128)


class Article(models.Model):
    creator = models.ForeignKey(User)
    pub_date = models.DateTimeField()
    link = models.URLField()

    title = models.CharField(max_length=512, default='')
    description = models.TextField(default='')
    categories = models.ManyToManyField(Category)
