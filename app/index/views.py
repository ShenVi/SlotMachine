__author__ = 'Ran'
from app import Flask, cache
from ..index import index
from flask import render_template, request, session, redirect
from flask_login import current_user

#首页
@index.route('/')
def home():
    if current_user.is_authenticated:
        return render_template('game.html')
    else:
        return render_template('index.html')