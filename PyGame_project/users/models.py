from django.contrib.auth.models import AbstractUser
from django.db import models
from itsdangerous import TimedJSONWebSignatureSerializer as TJWSSerializer, BadData
from django.conf import settings

# Create your models here.
# 昵称	    手机号	邮箱	密码	    性别	头像     注册开发者	真实姓名 邮箱验证状态
# nickname	mobile	email	password	gender	avatar  developer	username email_active

class User(AbstractUser):
    """
    用户模型
    """
    GENDER_CHOICES = (
        (0, '女'),
        (1, '男')
    )
    nickname = models.CharField(max_length=20, blank=True, null=True, verbose_name='昵称')
    avatar = models.FileField(upload_to='avatar/',  null=True, verbose_name='头像')
    mobile = models.CharField(max_length=13, blank=True, null=True, verbose_name='手机号')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, blank=True, null=True, verbose_name='性别')
    developer = models.BooleanField(default=False, verbose_name='是否为开发者')
    email_active = models.BooleanField(default=False, verbose_name='邮箱验证状态')

    class Meta:
        db_table = "tb_users"
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    @staticmethod
    def check_send_sms_code_token(token):
        """
        找回密码时检验access token
        :param token: access token
        :return: mobile None
        """
        # 创建itsdangerous模型的转换工具
        serialize = TJWSSerializer(settings.SECRET_KEY, 300)
        try:
            data = serialize.loads(token)
        except BadData:
            return None
        else:
            mobile = data.get('mobile')
            return mobile

    def generate_set_password_token(self):
        """
        生成修改密码的token
        """
        serializer = TJWSSerializer(settings.SECRET_KEY, expires_in=300)
        data = {'user_id': self.id}
        token = serializer.dumps(data)
        return token.decode()


    def generate_smail_vereify_url(self):
        """
        生成邮箱验证链接
        """
        serializer = TJWSSerializer(settings.SECRET_KEY, expires_in=60 * 60 * 24)
        data = {'user_id': self.id, 'email': self.email}
        token = serializer.dumps(data)
        verify_url = 'http://127.0.0.1:7999/success_verify_email.html?token=' + token.decode()
        return verify_url


    @staticmethod
    def check_email_veerify_token(token):
        """检验token"""
        # 修改密码token有效期300
        serializer = TJWSSerializer(settings.SECRET_KEY, expires_in=300)
        try:
            data = serializer.loads(token)
        except BadData:
            return False
        else:
            email = data.get('email')
            user_id = data.get('user_id')
            # user = User.objects.get(id=user_id, email=email)
            # user.email_active = True
            # user.save()
            # 查询的同时，进行更新保存
            User.objects.filter(id=user_id, email=email).update(email_active=True)
            return True
