from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    text = models.TextField("Текст")
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="notes", verbose_name="Автор")
    created_at = models.DateTimeField("Создана", auto_now_add=True)

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
        ordering = ("-created_at",)

    def __str__(self):
        return self.title
