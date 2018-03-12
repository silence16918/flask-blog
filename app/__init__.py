from flask import Flask, render_template
from app.config import config
from app.extensions import db, bootstrap, mail, moment, login_manger
from app.views import DEFAULT_BLUEPRINT


def create_app(config_name):
    # 创建Flask实例
    app = Flask(__name__)
    # 通过对象初始化配置
    app.config.from_object(config[config_name])
    # 调用初始化函数
    config[config_name].init_app(app)
    # 配置相关扩展
    config_extensions(app)
    # 配置各种蓝本
    config_blueprint(app)
    # 配置错误显示
    config_errorhandler(app)
    # 返回Flask实例
    return app


def config_extensions(app):
    db.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    login_manger.init_app(app)
    # 默认'basic'，另外None禁用，'strong'用户信息改的立即退出登录
    login_manger.session_protection = 'strong'
    # 设置登录页面的端点(视图函数)，访问选用登录才有权限的URL时自动跳转
    login_manger.login_view = 'user.login'
    # 需要登录时的提示信息，默认是英文字符串
    login_manger.login_message = '需要登录才可访问'


def config_blueprint(app):
    for blue_print, url_prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blue_print, url_prefix=url_prefix)


def config_errorhandler(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html')

