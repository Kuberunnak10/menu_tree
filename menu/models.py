from typing import Optional

from django.db import models
from django.urls import reverse


class MenuItem(models.Model):
    """Модель элемента меню."""
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    url_name = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=200, blank=True)
    menu_name = models.CharField(max_length=100, db_index=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        """Метод для получения абсолютного url."""
        if self.url_name:
            return reverse(self.url_name)
        return self.url
    