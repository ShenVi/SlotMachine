from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DEBUG = True

# Flask Sqlalchemy Setting

# 数据库地址设置 mysql://root:@localhost:3307/niputv?charset=utf8
SQLALCHEMY_DATABASE_URI = ''

'''
    多数据设置 mysql://root:@localhost:3307/mahouo_account?charset=utf8

SQLALCHEMY_BINDS = {
    'account_userdata':        '',
}
'''

SQLALCHEMY_TRACK_MODIFICATIONS = True

# Flask Bcrypt Setting
BCRYPT_LOG_ROUNDS = 1