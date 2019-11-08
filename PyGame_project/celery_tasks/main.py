"""celery服务启动文件"""
import os

from celery import Celery

if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PyGame_project.settings")

# 1.创建celery客户端对象
celery_app = Celery('meiduo')

# 2.加载配置信息(将来的任务存取的仓库)
celery_app.config_from_object('celery_tasks.config')

# 3.自动注册异步任务(将来那些异步任务可以仓库中存放)
celery_app.autodiscover_tasks(['celery_tasks.email'])

# 开启celery命令
# celery -A 应用路径(.包路经) worker -l info
# celery -A celery_tasks.main worker -l info
# win10上运行celery4.x就会出现这个问题(ValueError: not enough values to unpack (expected 3, got 0))
# 需要安装pip install eventlet后用以下命令执行
# celery -A celery_tasks.main worker -l info -P eventlet