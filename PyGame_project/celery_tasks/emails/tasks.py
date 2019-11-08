from celery_tasks.main import celery_app
from django.core.mail import send_mail
from django.core.mail import settings

# 发送邮件使用celery_tasks异步任务防止序列化器阻塞
@celery_app.task(name="send_verify_email")
def send_verify_email(to_email, verify_url):
    """
    发送验证邮件
    :param to_email: 收件人
    :param verify_url: 激活链接
    :return: None
    """
    subject = "PyGame邮箱验证"
    html_message = '<p>尊敬的用户你好！</p>' \
                   '<p>您的邮箱为: %s 。请点击链接激活您的邮箱:</p>' \
                   '<p><a href="%s">%s<a></p>' % (to_email, verify_url, verify_url)
    # 发送邮件
    send_mail(subject, "", settings.EMAIL_FROM, [to_email], html_message=html_message)