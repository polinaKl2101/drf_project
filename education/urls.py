from django.urls import path

from education.apps import EducationConfig
from rest_framework.routers import DefaultRouter

from education.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, PaymentsListAPIView, PaymentsCreateAPIView, PaymentsRetrieveAPIView, \
    PaymentsUpdateAPIView, PaymentsDestroyAPIView

app_name = EducationConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [

    path('lesson/create/', LessonCreateAPIView.as_view(), name='create_lesson'),
    path('lesson/', LessonListAPIView.as_view(), name='list_lesson'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='get_lesson'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='update_lesson'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='delete_lesson'),

    path('payment/', PaymentsListAPIView.as_view(), name='payment'),
    path('payment/create/', PaymentsCreateAPIView.as_view(), name='create_payment'),
    path('payment/<int:pk>/', PaymentsRetrieveAPIView.as_view(), name='get_payment'),
    path('payment/update/<int:pk>/', PaymentsUpdateAPIView.as_view(), name='update_payment'),
    path('payment/delete/<int:pk>/', PaymentsDestroyAPIView.as_view(), name='delete_payment'),

              ] + router.urls
