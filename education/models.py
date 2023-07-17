from django.db import models

from users.models import NULLABLE


class Course(models.Model):

    name = models.CharField(max_length=150, verbose_name='Название курса')
    preview = models.ImageField(upload_to='course_preview/', verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание курса')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):

    name = models.CharField(max_length=150, verbose_name='Название урока')
    description = models.TextField(verbose_name='Описание урока')
    preview = models.ImageField(upload_to='lesson_preview/', verbose_name='Превью', **NULLABLE)
    link = models.CharField(max_length=255, verbose_name='Ссылка на видео', **NULLABLE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'