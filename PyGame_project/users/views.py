from django.shortcuts import render
from rest_framework.generics import CreateAPIView

# Create your views here.
from .serializers import CreateUserSerializer


class UserView(CreateAPIView):
    """
    注册
    """
    # 指定序列化器
    print("注册")
    serializer_class = CreateUserSerializer