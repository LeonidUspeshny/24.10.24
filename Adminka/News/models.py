from django.db import models
from django.template.base import kwarg_re
from django.urls import reverse_lazy

class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='media/%Y/%m/%d')
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def get_absolute_url(self):
        return reverse_lazy('view_news', kwargs={'pk': self.pk})

    class Meta:
        verbose_name='Новость'
        verbose_name_plural='Новости'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True)

    def get_absolute_url(self):
        return reverse_lazy('Category', kwargs={'category_id':self.pk})

    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'
        ordering = ['title']





