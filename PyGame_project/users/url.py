from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    # 注册
    url(r'^users/$', views.UserView.as_view()),
    # 判断用户名是否存在
    url(r'^usernames/(?P<nickname>\w{5,20})/count/$', views.UsernameCountView.as_view()),
    # 判断手机号是否存在
    url(r'^mobiles/(?P<mobile>1[3-9]\d{9})/count/$', views.MobileCountView.as_view()),
    # 判断邮箱是否存在
    url(r'^email/(?P<email>\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14})/count/$', views.EmailCountView.as_view()),
    # 登陆, 获取JWT token
    url(r'^authorizations/$', obtain_jwt_token),
    # url(r'^authorizations/$', views.UserAuthorizationView.as_view()),
    # 修改密码
    url(r'^changepassword/$', views.Changepassword.as_view())
]