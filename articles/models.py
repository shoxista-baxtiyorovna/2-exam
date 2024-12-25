from django.db import models
from django.shortcuts import reverse


class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    short_content = models.TextField(max_length=300)
    long_content = models.TextField(max_length=500)
    author = models.CharField(max_length=100)
    publish_time = models.DateTimeField(auto_now_add=True)


    def get_detail_url(self):
        return reverse('articles:detail', args=[self.pk])


