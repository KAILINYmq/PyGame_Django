from django.conf.urls import url
from . import views

urlpatterns = [
    # 注册
    url(r'^users/$', views.UserView.as_view()),
]