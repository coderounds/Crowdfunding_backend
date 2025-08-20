from django.urls import path
from .views import CustomUserList, CustomUserDetail

urlpatterns = [
    path('users/',Views.CustomUserList.as_view()),
    path('users/<int:pk>/', CustomUserDetail.as_view()),
]
