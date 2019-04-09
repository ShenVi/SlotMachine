__author__ = 'Ran'
from app import Flask, cache
from ..game import game
from flask import render_template, request, session, redirect
from flask_login import current_user

#首页
@game.route('/')
def home():
    return ''