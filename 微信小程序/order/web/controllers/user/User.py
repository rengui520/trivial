#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/12/24 22:36 
# @Author : Aries 
# @Site :  
# @File : User.py 
# @Software: PyCharm
from flask import Blueprint,render_template

route_user = Blueprint( 'user_page',__name__ )

@route_user.route("/login")
def login():
    return render_template( "user/login.html" )