from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
from .serializers import CreateUserSerializer, Chage_Password
from .models import User

class UsernameCountView(APIView):
    """判断用户名是否已存在"""
    def get(self, request, nickname):
        # 用nickname去User模型中查询此用户名的数据
        # count:查到数据了会返回条数，没有查询到则会返回0
        count = User.objects.filter(nickname=nickname).count()
        data = {
            'nickname': nickname,
            'count': count
        }
        # 响应
        return Response(data)

class MobileCountView(APIView):
    """判断手机号是否已存在"""
    def get(self, request, mobile):
        # 用username去User模型中查询此用户名的数据
        count = User.objects.filter(mobile=mobile).count()
        data = {
            'mobile': mobile,
            'count': count
        }
        # 响应
        return Response(data)

class EmailCountView(APIView):
    """判断邮箱是否已存在"""
    def get(self, request, email):
        # 用Email去User模型中查询此用户名的数据
        count = User.objects.filter(email=email).count()
        data = {
            'email': email,
            'count': count
        }
        # 响应
        return Response(data)

class UserView(CreateAPIView):
    """
    注册
    """
    # 指定序列化器
    print("注册")
    serializer_class = CreateUserSerializer


class UserAuthorizationView(ObtainJSONWebToken):
    """
    用户登陆
    """
    # TODO PASS
    def post(self, request):
        response = super().post(request)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # 表示用户登陆成功
            user = serializer.validated_data.get("user")

        return response


class Changepassword(CreateAPIView):
    """
    修改密码
    """
    # TODO 修改密码
    # def post(self, request):
    #     # 调用jwt父类的扩展方法，对用户登录的数据进行验证
    #     response = super().post(request)
    #
    #     serializer = self.get_serializer(data=request.data)
    #     if serializer.is_valid():
    #         # 如果用户登陆则修改密码
    #         serializer_class = Chage_Password  # 序列化器