from .main import main
from .user import user
from .posts import posts


# 默认蓝本配置
DEFAULT_BLUEPRINT = (
    # (蓝本名称，URL前缀)
    (main, ''),
    (user, '/user'),
    (posts, '/posts')
)
