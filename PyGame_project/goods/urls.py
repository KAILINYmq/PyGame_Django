from django.conf.urls import url
from rest_framework.routers import DefaultRouter

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
    # 游戏详情页
    url(r'^Category/(?P<id>\d+)/sks/$', views.Category_page_list.as_view()),
]

