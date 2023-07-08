from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status, generics
from blog.models import Blog
from .serializers import BlogSerializer
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import viewsets, filters


class BlogUserWritePermission(BasePermission):
    message = 'Only author can edit/delete their blogs.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class BlogHome(generics.ListAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.blogobjects.all()


class BlogList(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = BlogSerializer

    def get_queryset(self):
        user = self.request.user
        return Blog.objects.filter(author=user)


class BlogDetail(generics.RetrieveAPIView):
    serializer_class = BlogSerializer

    def get_queryset(self):
        param = self.kwargs.get('pk')
        return Blog.objects.filter(id=param)


class BlogParamSearch(generics.ListAPIView):
    serializer_class = BlogSerializer

    def get_queryset(self):
        slug = self.request.query_params.get('slug', None)
        return Blog.objects.filter(slug=slug)


class BlogSearch(generics.ListAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['$hashtags']


class CreateBlog(generics.CreateAPIView):
    # permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()


class UpdateBlog(generics.UpdateAPIView):
    permission_classes = [BlogUserWritePermission]
    authentication_classes = [JWTAuthentication]
    serializer_class = BlogSerializer

    def get_queryset(self):
        param = self.kwargs.get('pk')
        return Blog.objects.filter(id=param)


class DeleteBlog(generics.DestroyAPIView):
    permission_classes = [BlogUserWritePermission]
    authentication_classes = [JWTAuthentication]
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
