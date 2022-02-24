from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Título')
    body = models.TextField(verbose_name='Cuerpo')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')
    author = models.ForeignKey(
        get_user_model(),                         # ó settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Autor'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])
