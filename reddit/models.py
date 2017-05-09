from django.db import models


class User(models.Model):
    name = models.CharField(max_length=128, primary_key=True)
    uri = models.URLField()


class Category(models.Model):
    name = models.CharField(max_length=128, primary_key=True)


class Entry(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    updated = models.DateTimeField()
    title = models.CharField(max_length=512)
    author = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    content = models.TextField()
    link = models.URLField()
