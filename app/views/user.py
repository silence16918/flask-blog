from flask import Blueprint, render_template, flash, redirect, url_for, request
from app.forms import RegisterForm, LoginForm, PasswordForm
from app.email import send_mail
from app.models import User
from app.extensions import db
from flask_login import login_user, logout_user, login_required, current_user


user = Blueprint('user', __name__)


@user.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # 创建新用户
        u = User(username=form.username.data, password=form.password.data, email=form.email.data)
        # 添加到数据库
        db.session.add(u)
        # 此处需要手动提交，因为请求结束后才会执行SQL，才会生成 id
        # 而产出token时需要用到id
        db.session.commit()
        # 发送激活邮件
        token = u.generate_activate_token()
        send_mail(form.email.data, '账户激活', 'email/account_activate', token=token, user=u)
        # 给出flash消息
        flash('邮件已经发送至您的邮箱，请点击链接完成激活')
        return redirect(url_for('main.index'))
    return render_template('user/register.html', form=form)


@user.route('/activate/<token>')
def activate(token):
    if User.check_activate_token(token):
        flash('您的账户已激活，可以直接登录')
        return redirect(url_for('user.login'))
    else:
        flash('无效的链接')
        return redirect(url_for('main.index'))


@user.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        u = User.query.filter_by(username=form.username.data).first()
        if u is None:
            flash('无效的用户名')
        elif u.verify_password(form.password.data):
            # 用户登录，顺便完成了 '记住我' 的功能
            login_user(u, remember=form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        else:
            flash('无效的密码')
    return render_template('user/login.html', form=form)


@user.route('/logout/')
# 路由保护，需要登录才可访问
@login_required
def logout():
    logout_user()
    flash('您已退出登录')
    return redirect(url_for('main.index'))


@user.route('/profile/')
@login_required
def profile():
    return render_template('user/profile.html')


@user.route('/change_password/', methods=['GET', 'POST'])
@login_required
def change_password():
    form = PasswordForm()
    if form.validate_on_submit():
        if current_user.verify_password(form.old_pwd.data):
            current_user.password = form.new_pwd.data
            db.session.add(current_user)
            flash('密码修改成功，下次登录请使用新密码')
            return redirect(url_for('main.index'))
        else:
            flash('无效的原始密码')
            return redirect(url_for('user.change_password'))
    return render_template('user/change_password.html', form=form)