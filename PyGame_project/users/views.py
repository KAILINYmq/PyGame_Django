from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from . import serializers
from .serializers import CreateUserSerializer
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
    # 补充通过认证才能访问接口的权限
    # permission_classes = [IsAuthenticated]
    serializer_class = serializers.Chage_Password


class AddData(CreateAPIView):
    """添加或修改信息"""
    # 补充通过认证才能访问接口的权限
    # permission_classes = [IsAuthenticated]
    serializer_class = serializers.UserAddData


class Emailbd(UpdateAPIView):
    """
    保存邮箱
    """
    serializer_class = serializers.EmailSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class EmailYZ(APIView):
    """验证邮箱"""
    def get(self, request):
        # 获取token
        token = request.query_params.get('token')
        if not token:
            return Response({'缺少token'}, status=status.HTTP_400_BAD_REQUEST)

        # 校验 保存
        result = User.check_email_veerify_token(token)

        if result:
            return Response({"message": "OK"}, status=status.HTTP_200_OK)
        else:
            return Response({"非法的token"}, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(RetrieveAPIView):
    """
    用户详情信息
    """
    serializer_class = serializers.UserDetailSerializer
    # 补充通过认证才能访问接口的权限
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """
        返回请求的用户对象
        :return: user
        """
        return self.request.user
