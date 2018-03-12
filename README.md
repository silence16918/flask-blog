# flask-blog
### A small flask blog
###### 1、简介: flask+python3.6+sqllite+pycharm
###### 2、项目目录结构：
+--app  
|      +--config.py  
|      +--email.py  
|      +--extensions.py
|      +--forms
|      |      +--user.py
|      |      +--__init__.py
|      +--models
|      |      +--posts.py
|      |      +--user.py
|      |      +--__init__.py
|      +--static
|      +--templates
|      |      +--common
|      |      |      +--base.html
|      |      +--email
|      |      |      +--account_activate.html
|      |      +--errors
|      |      |      +--404.html
|      |      +--main
|      |      |      +--index.html
|      |      +--user
|      |      |      +--change_password.html
|      |      |      +--login.html
|      |      |      +--profile.html
|      |      |      +--register.html
|      +--views
|      |      +--main.py
|      |      +--posts.py
|      |      +--user.py
|      |      +--__init__.py
|      +--__init__.py
+--manage.py
+--migrations
+--test.py


###### 3、蓝本
###### 4、自定义模板
###### 5、自定义错误页面
###### 6、异步发邮件，发送激活邮件，重发激活邮件
###### 7、sqlite数据库
###### 8、用户注册，
###### 9、用户登录 flask_login， 记住账号下次免登录(UserMixin)
###### 10、自定义表单字段验证
###### 11、显示用户资料
###### 12、修改密码
###### 13、修改邮箱
###### 14、重设密码
###### 15、发博客
###### 16、分页（paginate）显示博客
###### 17、博客回复功能
