# -*- coding: utf-8 -*-
from app import db
from flask_login import UserMixin, current_user

# 账户表
class Account(db.Model, UserMixin):

    # 表的名字
    __tablename__ = 'account'

    id = db.Column(db.Integer, primary_key=True)
    accounts = db.Column(db.Text)
    money = db.Column(db.Integer)

    # 定义对象
    def __init__(self, accounts=None, money=0):
        self.accounts = accounts
        self.money = money
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()