# 导入表单基础类库
from flask_wtf import FlaskForm
# 导入表单字段类型
from wtforms import StringField, PasswordField, BooleanField, SubmitField
# 导入字段验证器
from wtforms.validators import DataRequired, Email, EqualTo, Length
# 导入字段有效性异常类
from wtforms import ValidationError
# 导入User的模型类
from app.models import User


# 用户注册表单
class RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(6,30, message='用户名必须在6~30个字符之间')])
    password = PasswordField('密码', validators=[DataRequired(), Length(6,20, message='密码长度不在6~20之间')])
    confirm = PasswordField('确认密码', validators=[EqualTo('password', message='两次密码不一致')])
    email = StringField('邮箱', validators=[Email(message='邮箱格式不正确')])
    submit = SubmitField('立即注册')

    # 自定义表单验证：validate_字段名
    @staticmethod
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            return ValidationError('该用户已存在，请选用其它名称')

    @staticmethod
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            return ValidationError('该邮箱已使用，请更换其它邮箱')


# 登录表单
class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    remember_me = BooleanField('记住我')
    submit = SubmitField('立即登录')


# 修改密码表单
class PasswordForm(FlaskForm):
    old_pwd = PasswordField('原密码', validators=[DataRequired()])
    new_pwd = PasswordField('新密码', validators=[DataRequired(), Length(6, 20, message='密码长度不在6~20之间')])
    confirm = PasswordField('确认密码', validators=[EqualTo('new_pwd', message='两次密码不一致')])
    submit = SubmitField('确认修改')
