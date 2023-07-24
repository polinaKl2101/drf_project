from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserListAPIView, UserUpdateAPIView, UserRetrieveAPIView, UserDeleteAPIView, \
    UserPaymentsAPIView

app_name = UsersConfig.name

urlpatterns = [

    path('user/', UserListAPIView.as_view(), name='user'),
    path('user/create/', UserCreateAPIView.as_view(), name='create_user'),
    path('user/update/<int:pk>/', UserUpdateAPIView.as_view(), name='update_user'),
    path('user/retrieve/<int:pk>/', UserRetrieveAPIView.as_view(), name='retrieve_user'),
    path('user/delete/<int:pk>/', UserDeleteAPIView.as_view(), name='delete_user'),

    path('user/payments/', UserPaymentsAPIView.as_view(), name='payments_user'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
