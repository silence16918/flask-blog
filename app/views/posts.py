from flask import Blueprint

posts = Blueprint('posts', __name__)


@posts.route('/send/')
def send():
    return '发表博客'
