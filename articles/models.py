from tabnanny import verbose
from django.db import models
# 1 from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class Article(models.Model):
    author = models.ForeignKey(get_user_model(), verbose_name="작성자", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return str(self.title)