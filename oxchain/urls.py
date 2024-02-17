from django.urls import path
from .views import register_user, user_login, CryptoDataSet, Users

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('data/', CryptoDataSet.as_view({'get': 'list'}), name='data'),
    path('data/<int:pk>/', CryptoDataSet.as_view({'delete': 'destroy', 'put': 'update'}), name='data-detail'),
    path('users/', Users.as_view({'get': 'list'}), name='user')
    # path('logout/', user_logout, name='logout'),
]