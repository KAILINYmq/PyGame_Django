from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework_jwt.views import ObtainJSONWebToken

# Create your views here.
from .serializers import CreateUserSerializer


class UserView(CreateAPIView):
    """
    注册
    """
    # 指定序列化器
    print("注册")
    serializer_class = CreateUserSerializer


class UserAuthorizationView(ObtainJSONWebToken):
    """用户登陆"""
    def post(self, request):
        response = super().post(request)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # TODO 有bug "无法使用提供的认证信息登录。"
            # 表示用户登陆成功
            user = serializer.validated_data.get("user")

        return response