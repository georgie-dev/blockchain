from django.urls import path
from .views import register_user, user_login, CryptoDataSet

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('data/', CryptoDataSet, name='data')
    # path('logout/', user_logout, name='logout'),
]