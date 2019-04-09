__author__ = 'Ran'
from app import Flask, cache
from ..game import game
from flask import render_template, request, session, redirect
from flask_login import current_user
from app.redis import establish_token
from app.DB_account import Account
from app.payment import purchase
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
                '''purchase() 账户-5元'''

                a = random.choice([1,2,3,4,5,6,7,8,9,10,11,12])
                b = random.choice([1,2,3,4,5,6,7,8,9,10,11,12])
                c = random.choice([1,2,3,4,5,6,7,8,9,10,11,12])
                return json.dumps({'code':1, 'a':a, 'b':b, 'c':c})

            else:
                return json.dumps({'code':0, 'text':'游戏币不足'})

        else:
            pass
    else:
        pass

#验证密匙
@game.route('/get-tokon')
def gettokon():
    if current_user.is_authenticated:
        
        token = establish_token()

        return json.dumps({'token':token, 'outtime':60})