from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from education.models import Course, Lesson, CourseSubscription
from users.models import User


class EducationTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            email='testusermail@mail.ru',
            password='testuserpassword'
        )

        self.course = Course.objects.create(
            name='Test Course',
            description='Test Course Description'
        )

        self.subscription = CourseSubscription.objects.create(
            user=self.user,
            course=self.course,
            is_subscribed=True
        )

    def test_create_lesson(self):
        """Тест создания урока"""

        self.client.force_authenticate(user=self.user)

        data = {
            'name': 'Test Lesson',
            'description': 'Test Lesson Description',
            'link': 'https://www.youtube.com/watch?v=l36FuBLNZCA',
            'course': self.course.id
        }

        response = self.client.post(
            reverse('education:create_lesson'),
            data=data,
        )

        # print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_update_lesson(self):
        """Тест обновления урока"""

        self.client.force_authenticate(user=self.user)

        test_lesson = Lesson.objects.create(
            name='Test Lesson',
            description='Test Lesson Description',
            owner=self.user,
            course=self.course,
            link='https://www.youtube.com/watch?v=l36FuBLNZCA'
        )

        test_data_fixed = {
            'name': 'Test Lesson Fixed',
            'description': 'Test Lesson Description Fixed',
            'link': 'https://www.youtube.com/watch?v=l36FuBLNZCA',
            'course': self.course.pk
        }

        response = self.client.patch(
            reverse('education:update_lesson', kwargs={'pk': test_lesson.pk}),
            data=test_data_fixed,
        )
        # print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            Lesson.objects.get().name,
            'Test Lesson Fixed'
        )

    def test_delete_lesson(self):

        self.client.force_authenticate(user=self.user)

        test_lesson = Lesson.objects.create(
            name='Test Lesson 2',
            description='Test Lesson Description 2',
            owner=self.user,
            course=self.course,
            link='https://www.youtube.com/watch?v=l36FuBLNZCA'
        )

        response = self.client.delete(
            reverse('education:delete_lesson', kwargs={'pk': test_lesson.id}),
        )

        # print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_create_subscription(self):

        self.client.force_authenticate(user=self.user)

        data = {
            'course': self.course.id,
            'name': 'Test Subscription',
            'description': 'Test Subscription Description',
            'link': 'https://www.youtube.com/watch?v=l36FuBLNZCA',

        }

        response = self.client.post(
            reverse('education:subscribe'),
            data=data
        )

        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_delete_subscription(self):

        self.client.force_authenticate(user=self.user)
        subscription = CourseSubscription.objects.create(user=self.user, course=self.course, is_subscribed=True)

        response = self.client.delete(
            reverse('education:unsubscribe', kwargs={'pk': subscription.id})
        )

        # print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
