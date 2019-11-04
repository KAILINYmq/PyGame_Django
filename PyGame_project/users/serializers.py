from rest_framework import serializers
import re
from rest_framework_jwt.settings import api_settings

from .models import User


class CreateUserSerializer(serializers.ModelSerializer):
    """
    注册序列化器
    """
    print("注册序列化器OK")
    password2 = serializers.CharField(label='密码2', required=True, allow_null=False, allow_blank=False, write_only=True)
    allow = serializers.CharField(label='同意协议', required=True, allow_null=False, allow_blank=False, write_only=True)
    """
    序列化器中需要的所有字段: 'username', 'mobile', 'password', 'password2', 'allow'
    模型中已有字段:'username', 'mobile', 'password'
    需要进行反序列化的字段: 'username', 'mobile', 'password', 'password2', 'allow'
    需要进行序列化的字段:  'username', 'mobile'
    """

    def validate_mobile(self, value):
        """
        对手机号进行验证
        """
        if not re.match(r'1[3-9]\d{9}', value):
            raise serializers.ValidationError('手机号格式错误')
        return value

    def validate_allow(self, value):
        if value != 'true':
            raise serializers.ValidationError('请勾选同意协议')
        return value

    def validate(self, attrs):
        # 对两个密码进行判断
        if attrs.get('password') != attrs.get('password2'):
            raise serializers.ValidationError('两次密码不一致')
        return attrs

    def create(self, validated_data):
        """重写序列化器的保存方法把多余数据移除(创建用户)"""
        print("open保存")
        del validated_data['password2']
        del validated_data['allow']
        # user = User.objects.create(**validated_data)# user = User.objects.create(**validated_data)
        user = User(**validated_data)
        # 调用django的认证系统加密密码
        user.set_password(validated_data['password'])
        user.save()
        # 手动生成JWT token
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER  # 加载生成载荷函数
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER  # 加载生成token的函数
        payload = jwt_payload_handler(user)  # 通过传入user对象生成jwt 载荷部分
        token = jwt_encode_handler(payload)  # 传入payload 生成token
        # 将token保存到user对象中，随着返回值返回给前端
        user.token = token
        print("保存OK")
        return user

    class Meta:
        print("MetaOK")
        model = User
        fields = ['username', 'password', 'password2', 'mobile', 'allow']
        extra_kwargs = {  # 对序列化器中的字段进行额外配置
            'username': {
                # 'min_length': 5,
                # 'max_length': 20,
                'error_messages': {  # 自定义反序列化校验错误信息
                    # 'min_length': '仅允许5-20个字符的用户名',
                    'max_length': '仅允许5-20个字符的用户名',
                }
            },
            'password': {
                'write_only': True,  # 只做反序列化
                # 'min_length': 8,
                # 'max_length ': 20,
                'error_messages': {
                    # 'min_length': '仅允许8-20个字符的密码',
                    'max_length': '仅允许8-20个字符的密码',
                }
            }
        }


# class Chage_Password(serializers.ModelSerializer):
#     """
#     修改密码序列器
#     """
#     TODO 修改密码
#     oldpassword = serializers.CharField(label='密码old', required=True, allow_null=False, allow_blank=False, write_only=True)
#     password = serializers.CharField(label='密码new', required=True, allow_null=False, allow_blank=False, write_only=True)
#     password1 = serializers.CharField(label='密码new1', required=True, allow_null=False, allow_blank=False, write_only=True)
#
#     def validate_oldpassword(self, value):
#         """
#         对旧密码进行验证
#         """
#         if not re.match(r'1[3-9]\d{9}', value):
#             raise serializers.ValidationError('密码错误')
#         return value
#
#     def validate(self, attrs):
#         # 对两个密码进行判断
#         if attrs.get('password') != attrs.get('password1'):
#             raise serializers.ValidationError('两次密码不一致')
#         return attrs
#
#     def create(self, validated_data):
#         """重写序列化器的保存方法把多余数据移除(创建用户)"""
#         print("open保存")
#         del validated_data['password1']
#         del validated_data['oldpassword']
#         # user = User.objects.create(**validated_data)# user = User.objects.create(**validated_data)
#         user = User(**validated_data)
#         # 调用django的认证系统加密密码
#         user.set_password(validated_data['password'])
#         user.save()
#         # 手动生成JWT token
#         jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER  # 加载生成载荷函数
#         jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER  # 加载生成token的函数
#         payload = jwt_payload_handler(user)  # 通过传入user对象生成jwt 载荷部分
#         token = jwt_encode_handler(payload)  # 传入payload 生成token
#         # 将token保存到user对象中，随着返回值返回给前端
#         user.token = token
#         print("保存OK")
#         return user
#
#     class Meta:
#         model = User
#         fields = ['oldpassword', 'password', 'password1']