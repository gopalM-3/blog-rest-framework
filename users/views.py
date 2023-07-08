from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .serializers import BlogUserRegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class BlogUserRegister(APIView):
    # permission_classes = [AllowAny]

    def post(self, request):
        reg_serializer = BlogUserRegisterSerializer(data=request.data)
        if reg_serializer.is_valid():
            new_blog_user = reg_serializer.save()
            if new_blog_user:
                return Response("User successfully created!", status=status.HTTP_201_CREATED)
        return Response("User creation failed", reg_serializer.errors, status=status.HTTP_201_CREATED)


class BlogUserLogout(APIView):
    # permission_classes = [AllowAny]

    def post(self, request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            return Response("Logout failed. Error: " + str(error), status=status.HTTP_400_BAD_REQUEST)
