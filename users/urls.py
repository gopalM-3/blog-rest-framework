from django.urls import path
from .views import BlogUserLogout, BlogUserRegister

urlpatterns = [
    path('register/', BlogUserRegister.as_view()),
    path('logout/', BlogUserLogout.as_view()),
]
