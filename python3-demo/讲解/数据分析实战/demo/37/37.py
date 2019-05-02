#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/16 15:19 
# @Author : 韧桂 
# @Site :  
# @File : 37.py 
# @Software: PyCharm
from selenium import webdriver
import time

browser = webdriver.Chrome()

# 登录微博
def weibo_login(username, password):
     # 打开微博登录页
     browser.get('https://passport.weibo.cn/signin/login')
     browser.implicitly_wait(5)
     time.sleep(1)
     # 填写登录信息：用户名、密码
     browser.find_element_by_id("loginName").send_keys(username)
     browser.find_element_by_id("loginPassword").send_keys(password)
     time.sleep(1)
     # 点击登录
     browser.find_element_by_id("loginAction").click()
     time.sleep(1)
# 设置用户名、密码
username = '16607730939'
password = "ljwb7313520"
weibo_login(username, password)


# # 添加指定的用户
# def add_follow(uid):
#      browser.get('https://m.weibo.com/u/'+str(uid))
#      time.sleep(1)
#      #browser.find_element_by_id("follow").click()
#
#      follow_button = browser.find_element_by_xpath('//div[@class="m-add-box m-followBtn"]')
#      follow_button.click()
#      time.sleep(1)
#      # 选择分组
#
#      group_button = browser.find_element_by_xpath('//div/a[@class="m-btn m-btn-white m-btn-text-black"]')
#      group_button.click()
#      time.sleep(1)
# # 每天学点心理学 UID
# uid = '1890826225'
# add_follow(uid)
#
#
# # 给指定某条微博添加内容
# def add_comment(weibo_url, content):
#      browser.get(weibo_url)
#      browser.implicitly_wait(5)
#      content_textarea = browser.find_element_by_css_selector("textarea.W_input").clear()
#      content_textarea = browser.find_element_by_css_selector("textarea.W_input").send_keys(content)
#      time.sleep(2)
#      # comment_button = browser.find_element_by_css_selector("a.W_btn_a").click()
#      comment_button = browser.find_element_by_xpath('//*[@id="Pl_Official_WeiboDetail__73"]/div/div/div/div[4]/div/div[2]/div[2]/div[2]/div[1]/a/em').click()
#      time.sleep(1)
# content = '每天学点心理学'
# weibo_url = 'https://weibo.com/1890826225/HjjqSahwl'
# add_comment(weibo_url, content)

# 发文字微博
def post_weibo(content):
     # 跳转到用户的首页
     browser.get('https://weibo.com')
     browser.implicitly_wait(5)
     # 点击右上角的发布按钮
     post_button = browser.find_element_by_css_selector("[node-type='publish']").click()
     # 在弹出的文本框中输入内容
     content_textarea = browser.find_element_by_css_selector("textarea.W_input").send_keys(content)
     time.sleep(2)
     # 点击发布按钮
     post_button = browser.find_element_by_css_selector("[node-type='submit']").click()
     time.sleep(1)


# 给指定的微博写评论
uid = '6493662154'
content = 'Gook Luck! 好运已上路！'
# 自动发微博
post_weibo(content)

