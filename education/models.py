from django.db import models
from django.conf import settings
from users.models import NULLABLE, User


class Course(models.Model):

    name = models.CharField(max_length=150, verbose_name='Название курса')
    preview = models.ImageField(upload_to='course_preview/', verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание курса')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

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
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons', verbose_name='Курс')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Payments(models.Model):

    PAYMENT_OPTIONS = (
        ('Cash', 'Наличные'),
        ('Bank payment', 'Перевод на счет'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', verbose_name='Пользователь')
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата оплаты')
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='paid_course', verbose_name='Оплаченный курс', **NULLABLE)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='paid_lesson', verbose_name='Оплаченный урок', **NULLABLE)
    payment_amount = models.IntegerField(verbose_name='Сумма оплаты')
    payment_method = models.CharField(max_length=50, choices=PAYMENT_OPTIONS, verbose_name='Способ оплаты')

    def __str__(self):
        return f'{self.user} - {self.paid_course if self.paid_course else self.paid_lesson}. Метод оплаты: {self.payment_method}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'


class CourseSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Название курса')
    is_subscribed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.email} - subscription {self.is_subscribed}'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
