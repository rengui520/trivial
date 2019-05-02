#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/2/28 10:43 
# @Author : 韧桂 
# @Site :  
# @File : 0228.py 
# @Software: PyCharm
# Selenium+Chrome&PhantomJS(无界面浏览器)爬取淘宝美食
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()  #webdeiver为浏览器驱动
wait = WebDriverWait(browser, 10)  #提取赋值，减少重复书写。#设置等待过程

#定义一个搜索方法
def search():
    browser.get('https://www.taobao.com')
    input = wait.until(
        EC.presence_of_element_located((By.ID, "q"))   #匹配搜索框。#EC是选择条件
    )
    submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))   #点击搜索
    input.send_keys('美食')
    submit.click()  #输入内容后，点击按钮提交

def main():
    search()

if __name__ == '__main__':
    main()





