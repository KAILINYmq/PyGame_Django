from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# 昵称	    手机号	邮箱	密码	    性别	头像     注册开发者	真实姓名 邮箱验证状态
# nickname	mobile	email	password	gender	avatar  developer	username email_active

class User(AbstractUser):
    """
    用户模型
    """
    nickname = models.CharField(max_length=20, blank=True, null=True, verbose_name='昵称')
    avatar = models.FileField(upload_to='avatar/',  null=True, verbose_name='头像')
    mobile = models.CharField(max_length=13, blank=True, null=True, verbose_name='手机号')
    gender = models.CharField(max_length=1, blank=True, null=True, verbose_name='性别')
    developer = models.BooleanField(default=False, verbose_name='是否为开发者')
    email_active = models.BooleanField(default=False, verbose_name='邮箱验证状态')

    class Meta:
        db_table = "tb_users"
        verbose_name = '用户'
        verbose_name_plural = verbose_name

