from django.urls import path
from users.views import UsersView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('users/', UsersView.as_view()),
    path("users/login/", TokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
]
