from flask import current_app
from app.extensions import db, login_manger
# 导入密码散列及校验函数
from werkzeug.security import generate_password_hash, check_password_hash
# 导入生成和校验token类库
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
# 导入Mixin类库
from flask_login import UserMixin


class User(UserMixin, db.Model):
    # 指定表名
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=False)
    email = db.Column(db.String(64), unique=True)
    # 在关联的另一模型中添加一个反向引用
    # 第一个参数：指定关联的另一模型名
    # backref：反向引用的字段名
    # lazy：指定加载方式，dynamic是不加载，但是提供记录查询
    # posts = db.relationship('Posts', backref='user', lazy='dynamic')

    # 生成账户激活时用的token
    def generate_activate_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        # 会将字典信息加密，变成一个加密后的字符串
        return s.dumps({'confirm_id': self.id})

    # 校验用户激活的token
    @staticmethod
    def check_activate_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            # 从用户提交过来的token中获取数据
            data = s.loads(token)
        except:
            return False
        # 根据主键查询数据，判断是否存在该用户
        user = User.query.get(data.get('confirm_id'))
        if user is None:
            # 用户不存在
            return False
        if not user.confirmed:
            # 如果没有激活
            user.confirmed = True
            db.session.add(user)
        return True


    # 保护密码属性，读取时抛出异常
    @property
    def password(self):
        raise AttributeError('密码是不可读属性')

    # 设置密码
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # 密码校验
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manger.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
