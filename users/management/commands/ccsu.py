from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='admin@mail.ru',
            first_name='Admin',
            last_name='AdminAdmin',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )

        user.set_password('1234567890')
        user.save()