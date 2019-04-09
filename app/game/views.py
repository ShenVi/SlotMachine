__author__ = 'Ran'
from app import Flask, cache
from ..game import game
from flask import render_template, request, session, redirect
from flask_login import current_user
from app.redis import establish_token
from app.DB_account import Account
from app.payment import purchase, gamereward
import random

import json

#获取游戏结果
@game.route('/get-result')
def result():
    if current_user.is_authenticated:
        if request.method == 'POST':
            jsondata = request.json

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

                reward = result_reward(a, b, c)

                return json.dumps({'code':1, 'a':a, 'b':b, 'c':c, 'gamereward':reward['addmoney']})

            else:
                return json.dumps({'code':0, 'text':'游戏币不足'})

        else:
            pass
    else:
        pass

def result_reward(a, b, c):
    if a == b & c:
        gamereward(3)
        return {'type':3, 'addmoney':50}

    elif a == b or b == c:
        gamereward(2)
        return {'type':2, 'addmoney':5}

    else:
        return {'type':0, 'addmoney':0}


#验证密匙
@game.route('/get-tokon')
def gettokon():
    if current_user.is_authenticated:
        
        token = establish_token()

        return json.dumps({'token':token, 'outtime':60})