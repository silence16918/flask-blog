from app.extensions import db
from datetime import datetime


class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    # 回复的博客id，默认为0，表示是发的博客
    rid = db.Column(db.Integer, index=True, default=0)
    # 博客内容
    content = db.Column(db.Text)
    # 发表时间
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # 关联的外键字段(表名.字段)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

