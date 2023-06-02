from django.urls import path
from .views import SignUp, SignOut

urlpatterns = [
    path('login', SignUp.as_view(), name='login'),
    ]
