__author__ = 'Ran'
from app import Flask, cache
from ..game import game
from flask import render_template, request, session, redirect
from flask_login import current_user
from app.redis import establish_token
from app.DB_account import Account
from app.DB_module import Bill
from app.payment import purchase, gamereward
import random

import json

#获取游戏结果
@game.route('/get-result', methods=["POST"])
def result():
    if current_user.is_authenticated:
        if request.method == 'POST':
            #jsondata = request.json

            #token = jsondata['token']

            user = Account.query.filter_by(id=current_user.id).first()

            if user.money < 5:

                purchase()
                '''
                    purchase() 账户-5元 消费
                '''

                a = random.choice([1,2,3,4,5,6,7,8,9,10,11,12])
                b = random.choice([1,2,3,4,5,6,7,8,9,10,11,12])
                c = random.choice([1,2,3,4,5,6,7,8,9,10,11,12])

                reward, rewardtype, roc = result_reward(a, b, c)
                
                jsons = {
                    'code':1,
                    'a':a,
                    'b':b,
                    'c':c,
                    'reward':reward,
                    'type':rewardtype,
                    'money':Account.query.filter_by(id=current_user.id).first().money,
                    'roc_date':roc.date,
                    'roc_expendituremoney':roc.expendituremoney,
                    'roc_income':roc.income,
                    'roc_money':roc.money
                }

                print(jsons)

                return json.dumps(jsons)

            else:
                return json.dumps({'code':0, 'text':'游戏币不足'})

        else:
            pass
    else:
        pass

def result_reward(a, b, c):
    if a == b & a == c:
        gamereward(3)
        roc = Bill(expendituremoney=None, income=50, money=Account.query.filter_by(id=current_user.id).first().money)
        return 50, 3, roc

    elif a == b or b == c:
        gamereward(2)
        roc = Bill(expendituremoney=None, income=20, money=Account.query.filter_by(id=current_user.id).first().money)
        return 20, 2, roc

    elif a == c:
        gamereward(2)
        roc = Bill(expendituremoney=None, income=20, money=Account.query.filter_by(id=current_user.id).first().money)
        return 20, 31, roc

    else:
        roc = Bill(expendituremoney=5, income=0, money=Account.query.filter_by(id=current_user.id).first().money)
        return 0, 0, roc


#验证密匙
@game.route('/get-tokon')
def gettokon():
    if current_user.is_authenticated:
        
        token = establish_token()

        return json.dumps({'token':token, 'outtime':60})