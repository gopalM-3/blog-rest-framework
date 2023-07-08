from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BlogDetail, BlogHome, BlogList, BlogParamSearch, BlogSearch, CreateBlog, UpdateBlog, DeleteBlog

app_name = 'blog_api'

urlpatterns = [
    path('blog/home/', BlogHome.as_view()),
    path('blog/list/', BlogList.as_view()),
    path('blog/<int:pk>/', BlogDetail.as_view()),
    path('blog/param_search/', BlogParamSearch.as_view()),
    path('blog/search/', BlogSearch.as_view()),
    path('blog/create/', CreateBlog.as_view()),
    path('blog/update/<int:pk>/', UpdateBlog.as_view()),
    path('blog/delete/<int:pk>/', DeleteBlog.as_view()),
]
