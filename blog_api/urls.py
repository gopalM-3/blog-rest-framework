from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BlogDetail, BlogHome, BlogList, BlogParamSearch, BlogSearch, CreateBlog, UpdateBlog, DeleteBlog

app_name = 'blog_api'

urlpatterns = [
    path('blogs/', BlogHome.as_view()),
    path('user/blogs/', BlogList.as_view()),
    path('<int:pk>/', BlogDetail.as_view()),
    path('blogs/slug/', BlogParamSearch.as_view()),
    path('blogs/hashtag/', BlogSearch.as_view()),
    path('blogs/create/', CreateBlog.as_view()),
    path('blogs/update/', UpdateBlog.as_view()),
    path('blogs/delete/', DeleteBlog.as_view()),
]
