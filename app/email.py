from flask import current_app, render_template
from flask_mail import Message
from threading import Thread
from app.extensions import mail


def send_async_mail(app, msg):
    # 邮件发送必须在线程上下文中，因此需要自己创建上下文
    with app.app_context():
        mail.send(msg)


# 封装异步发送邮件函数
def send_mail(to, subject, template, **kwargs):
    # 在任意文件中找到项目的app
    app = current_app._get_current_object()
    msg = Message(subject=subject,
                  sender=app.config['MAIL_USERNAME'],
                  recipients=[to])
    msg.body = render_template(template+'.txt', **kwargs)
    msg.html = render_template(template+'.html', **kwargs)

    thr = Thread(target=send_async_mail, args=[app, msg])
    thr.start()
    return thr
