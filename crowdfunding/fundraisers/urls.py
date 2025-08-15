from django.urls import path
from .views import FundraiserList, FundraiserDetail

urlpatterns = [
    path('', FundraiserList.as_view(), name='fundraiser-list'),
    path('<int:pk>/', FundraiserDetail.as_view(), name='fundraiser-detail'),
]
