__author__ = 'Ran'
from app import Flask, cache, login_manager
from ..account import account
from flask import render_template, request, session, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from app.DB_account import Account
import json

@login_manager.user_loader
def load_user(user_id):
    return Account.query.filter_by(id=user_id).first()

#登录
@account.route('/auth', methods=["POST"])
def authaccount():
    if current_user.is_authenticated:
        return json.dumps({'code': 0, 'text': '你已登录过'})

    else:
        if request.method == 'POST':

            # 获取json数据
            jsondata = request.json
            print(request.json)

            # 判断用户输入的内容是否为空
            if jsondata['account'] == '':
                return json.dumps({'code': 0, 'text': '账户不能为空'})
            else:
                user = Account.query.filter_by(accounts = jsondata['account']).first()
                if(user):
                    session.permanent = True
                    login_user(user, remember=True)
                    return json.dumps({'code': 1, 'text': '登录成功'})
                else:
                    return json.dumps({'code': 0, 'text': '账户不存在'})

#注册
@account.route('/register', methods=["POST"])
def registeraccount():
    if current_user.is_authenticated:
        return json.dumps({'code': 0, 'text': '你已登录过'})

    else:
        if request.method == 'POST':
            print(request.json)

            # 获取json数据
            jsondata = request.json

            # 判断用户输入的内容是否为空
            if jsondata['account'] == '':
                return json.dumps({'code': 0, 'text': '账户不能为空'})
            else:
                Account(accounts = jsondata['account'])
                #自动提交数据库
                return json.dumps({'code': 1, 'text': '注册成功'})

#退出登录
@account.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index.home'))