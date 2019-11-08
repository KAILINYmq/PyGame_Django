from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from django.views.static import serve  # 上传文件处理函数

from PyGame_project.settings import MEDIA_ROOT  # 从配置中导入MEDIA_ROOT
from . import views

urlpatterns = [
    # 游戏index数据
    url(r'^index/$', views.GameListView.as_view()),
    # 游戏分类接口
    url(r'^Category/$', views.GameCategory.as_view()),
    # 游戏热门接口
    url(r'^GameHOT/$', views.GameZAN.as_view()),
    # 游戏详情页接口
    url(r'^categories/(?P<id>\d+)/page/$', views.GamePage.as_view()),
    # 游戏分类页面
    url(r'^categorys/(?P<category>\d+)/skus/$', views.Category_page_list.as_view()),
    # 个人收藏页面url
    url(r'^collect/$', views.UserCollect.as_view()),
    # 游戏待审核接口
    url(r'^userlaunched/$', views.UserLaunched.as_view()),
    # 发布游戏接口
    # url(r'^upgamefiles/$', views.upload_file),
    url(r'^upgamefiles/$', views.UpGameFiles.as_view()),
    # 上传文件
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
]

