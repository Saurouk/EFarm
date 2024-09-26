# auth_app/urls.py
from django.urls import path
from .views import UserList, CustomAuthToken

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('token-auth/', CustomAuthToken.as_view(), name='token-auth'),
]
