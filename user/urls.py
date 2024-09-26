from django.urls import path
from .views import UserCreateView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('create/', UserCreateView.as_view(), name='user-create'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),
]
