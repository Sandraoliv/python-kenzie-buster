from django.urls import path
from users.views import UsersView

urlpatterns = [
    path('users/', UsersView.as_view()),
]
