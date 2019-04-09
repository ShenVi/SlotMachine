# -*- coding: utf-8 -*-
from app import db
from flask_login import UserMixin, current_user
import time

# 账户表
class Bill(db.Model):

    # 表的名字
    __tablename__ = 'bill'

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Text)
    expendituremoney = db.Column(db.Integer) #支出
    income = db.Column(db.Integer) #收入
    money = db.Column(db.Integer) #收入
    date = db.Column(db.String(100))

    # 定义对象
    def __init__(self, userid=None, expendituremoney=None, income=None, money=None, date=None):
        self.userid = current_user.id
        self.expendituremoney = expendituremoney
        self.income = income
        self.money = money
        self.date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.update()  # 提交数据

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()

#db.create_all()