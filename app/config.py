from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DEBUG = True

# Flask Sqlalchemy Setting

# 数据库地址设置 mysql://root:@localhost:3307/niputv?charset=utf8
SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost:3306/slotmachine?charset=utf8'

SQLALCHEMY_TRACK_MODIFICATIONS = True

# Flask Bcrypt Setting
BCRYPT_LOG_ROUNDS = 1