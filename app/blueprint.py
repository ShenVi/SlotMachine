from app import app
from app.index import index
from app.account import account

'''
    设置访问后缀
    url_prefix='/watch'
'''

# 默认域名
#app.config['SERVER_NAME'] = 'myxxxxx.com'

# 注册蓝图
app.register_blueprint(index)
app.register_blueprint(account, url_prefix='/account')