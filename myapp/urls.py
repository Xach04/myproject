from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/auth/register/', views.UserRegisterAPIView.as_view(), name='user-register'),
    path('api/auth/login/', views.UserLoginAPIView.as_view(), name='user-login'),
]
