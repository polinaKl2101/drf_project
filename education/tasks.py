from datetime import date, timedelta
from celery import shared_task
from django.core.mail import send_mail

from config import settings
from education.models import Course
from users.models import User


@shared_task
def send_course_update_mail(course_id):

    course = Course.objects.get(pk=course_id)
    send_mail(subject=f"Курс {course.name} обновлен!",
              message=f"Курс, на который вы подписаны обновился! Проверьте обновление!",
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=['pklopunova@mail.ru'],
              fail_silently=False)


@shared_task
def block_inactive_users():
    month_ago = date.today() - timedelta(days=30)
    inactive_users = User.objects.filter(
        last_login__lt=month_ago
    )
    inactive_users.update(is_active=False)