__author__ = 'Ran'
from app import Flask, cache
from ..account import account
from flask import render_template, request, session, redirect
from flask_login import login_user, login_required, logout_user, current_user
from app.DB_account import Account
import json

#登录
@account.route('/auth')
def authaccount():
    if current_user.is_authenticated:
        return json.dumps({'code': 0, 'text': '你已登录过'})

    else:
        if request.method == 'POST':

            # 获取json数据
            jsondata = request.json

            # 判断用户输入的内容是否为空
            if jsondata['account'] == '':
                return json.dumps({'code': 0, 'text': '账户不能为空'})
            else:
                user = Account.query.filter_by(key = jsondata['account']).first()
                if(user):
                    session.permanent = True
                    login_user(user, remember=True)
                    return json.dumps({'code': 1, 'text': '登录成功'})
                else:
                    return json.dumps({'code': 0, 'text': '账户不存在'})

#注册
@account.route('/register')
def registeraccount():
    if current_user.is_authenticated:
        return json.dumps({'code': 0, 'text': '你已登录过'})

    else:
        if request.method == 'POST':

            # 获取json数据
            jsondata = request.json

            # 判断用户输入的内容是否为空
            if jsondata['account'] == '':
                return json.dumps({'code': 0, 'text': '账户不能为空'})
            else:
                Account(key=jsondata['account'])
                #自动提交数据库
                return json.dumps({'code': 1, 'text': '注册成功'})
