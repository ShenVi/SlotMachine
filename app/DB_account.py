# -*- coding: utf-8 -*-
from app import db
from flask_login import UserMixin, current_user
from flask_bcrypt import check_password_hash, generate_password_hash

# 账户表
class Account(db.Model, UserMixin):

    # 表的名字
    __tablename__ = 'account'

    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.Text)

    # 定义对象
    def __init__(self, key=None):
        self.key = key
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()