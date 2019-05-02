#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/2/20 13:38 
# @Author : 韧桂 
# @Site :  r
# @File : 0220.py 
# @Software: PyCharm
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()  #声明一个浏览器对象，.Chrome声明浏览器驱动对象也可是Firefox,Edge,PhantomJS,Safari。需下载ChromeDriver，并配置环境变量。
try:
    browser.get('https://www.baidu.com')
    input = browser.find_element_by_id('kw')
    input.send_keys('Python')  #send_keys，敲入一些键/元素
    input.send_keys(Keys.ENTER)  #回车
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID,'content_left')))
    print(browser.current_url)
    print (browser.get_cookies())
    print (browser.page_source)  #网页源代码
finally:
    browser.close()  #关掉浏览器

'''
'''
#访问页面
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
print (browser.page_source)
browser.close()
'''
'''
#查找元素
#单个元素
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_first = browser.find_element_by_id('J_SearchTab')   #find_element_by_id方法，用id来寻找一个元素  id名称是J_SearchTab。导航栏id
#input_first = browser.find_element(By.ID, 'banner-slider')  #利用find_element通用的方式。第一个参数传入By，后面跟它的类型，类型所有字母需大写。第二个参数传要查找的元素。
input_second = browser.find_element_by_css_selector('#J_SearchTab')  #find_element_by_css_selector方法。 用css选择器来选择一个元素
input_third = browser.find_element_by_xpath('//*[@id="J_SearchTab"]')  #三次选择内容相同。属WebElement类型。
print (input_first, input_second, input_third)
browser.close()

#find_element_by_css_selector
#find_element_by_xpath
#find_element_by_name   通过name方法查找
#find_element_by_link_text
#find_element_by_partial_link_text
#find_element_by_tag_name
#find_element_by_class_name
'''
'''
#多个元素查找
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
#lis = browser.find_elements_by_css_selector('.content div')  #elements多了一个s。
lis = browser.find_elements(By.CSS_SELECTOR,'.content div')
print(lis)
browser.close()
'''
'''
#元素交互操作
#对获取的元素调用交互方法

from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input = browser.find_element_by_id('q')   #搜索输入框id
input.send_keys('iPone')   #send_keys方法输入iPone
time.sleep(1)   #延时1s
input.clear()  #clear清空输入框
input.send_keys('iPad')
button = browser.find_element_by_class_name('btn-search')  #点击搜索
button.click()  #调用click转到搜索页面
#跳不到产品搜索页面了，现在必须登录后才能搜索。
#更多操作 https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.remote.webelement
'''
'''
#交互动作
#将动作附加到动作链中串行执行。调用相应的API即可。
from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()  #模拟拖拽
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')  #选择拖拽目标。选择 frame标签，id为iframeResult
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')
actions = ActionChains(browser)   #声明一个动作链
actions.drag_and_drop(source, target)  #把source拖拽到target
actions.perform()  #提醒动作
#更多操作  https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains
'''

'''
#执行JavaScript
#有一些操作没有API,如进度条下拉等，或者交互动作API难以实现，都可以用这种方法。
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')  #execute_script()  API 传一些 JavaScript语句。完成js的执行，通过js对浏览器的操作。这里是下拉到网页的最下端。
browser.execute_script('alert("To Bottom")')   #提示一个alert，
'''


'''
#获取元素信息
#获取属性，获取文本值；和获取ID、位置、标签名、大小。

from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')

logo = browser.find_element_by_id('zh-top-link-logo')  #获取知乎logo信息，
print (logo)
print (logo.get_attribute('class'))  #再把属性值打印出来。
input = browser.find_element_by_class_name('zu-top-add-question')  #匹配提问按钮。
print (input.text)  #把文本值打印出来。
print (input.id)    #获取ID
print (input.location)   #获取位置
print (input.tag_name)  #获取标签名
print (input.size)  #大小
'''

'''
#Frame
#Frame在网页出现比较频繁，但是，如果出现Frame，我们在做元素筛选的时候，有可能会导入一些不太方便的问题。
# 比如说，这个Frame相当于一个独立的网页。我们在父级的Frame里面查找这个子元素的Frame，实际上必须切换到Frame才可以查找，否则是不能完成这个元素的查找的。
#这里我们演示切换父元素的Frame以及子元素的Frame。
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')  #切换子元素的Frame。
source = browser.find_element_by_css_selector('#draggable')
print (source)
try:
    logo = browser.find_element_by_class_name('logo')
except NoSuchElementException:   #找不到这个元素时报错。
    print ('NO LOGO')
browser.switch_to.parent_frame()   #切换父元素的Frame。
logo = browser.find_element_by_class_name('logo')
print (logo)
print (logo.text)
'''

#等待
#防止浏览器没有完全加载一些Ajax请求时，便进行下一步操作。
'''
#隐式等待
# 当使用了隐式等待执行测试的时候，如果WebDriver 没有在 DOM 中找到元素，将继续等待，超过设定时间后则抛出找不到元素的异常，换句话说，当查找元素或元素并没有立即出现大的时候，隐式等待将等待一段时间再查找DOM，默认的时间是0。
from selenium import webdriver

browser = webdriver.Chrome()
browser.implicitly_wait(10)  #传入一个等待时间
browser.get('https://www.zhihu.com/explore')
input = browser.find_element_by_class_name('zu-top-add-question')
print (input)
'''
'''
#显示等待
# 指定一个等待时间，再加一个等待条件。那么，它会在这个最长等待时间内判断这个条件是否成立。
# 如果成立，它就会立即返回，否则，它会一直等待，然后等待到这个最长的等待时间，如果还是不满足这个条件，它就会抛出异常，
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
browser.get('https://www.taobao.com/')
wait = WebDriverWait(browser, 10)  #声明WebDriverWait对象。第二个参数是最长等待时间
input = wait.until(EC.presence_of_element_located((By.ID,'q')))  #等待条件，判断搜索框是否出现。并赋值给input
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))  #判断是否是可点击
print (input, button)

#title_is 标题是某内容
#title_contains  标题包含某内容
#presence_of_element_located  元素加载出，传入定位元组，如(By,ID, 'p')
#visibility_of_element_located  元素可见，传入定位元组
#visibility_of   可见，传入元素对象
#presence_of_all_elements_located  所有元素加载出
#text_to_be_present_in_element 某个元素文本包含某文字
#text_to_be_present_in_element_value 某个元素值包含某文字
#frame_to_be_available_and_switch_to_it    frame加载并切换
#invisibility_of_element_located   元素不可见
#element_to_be_clickable   元素可点击
#staleness_of 判断一个元素是否仍在DOM,可判断页面是否已经刷新
#element_to_be_selected  元素可选择，传元素对象
#element_located_to_be_selected   元素可选择，传入定位元组
#element_selection_state_to_be   传入元素对象以及状态，相等返回True，否则返回False
#element_located_selection_state_to_be   传入定位元组以及状态，相等返回True，否则返回False
#alert_is_present   是否出现Alert

#更多操作https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions
'''
'''
#前进后退

import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com/')
browser.get('https://www.taobao.com/')
browser.get('https://www.python.org/')
browser.back()  #后退一步
time.sleep(1)   #睡眠一秒
browser.forward()    #前进一步
browser.close()   #关闭浏览器
'''
'''
#Cookies
#保持登录状态
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
print (browser.get_cookies())
browser.add_cookie({'name':'name','domain':'www.zhihu.com','value':'germey'})   #加一些信息进去
print (browser.get_cookies())
browser.delete_all_cookies()   #清空cookies
print (browser.get_cookies())
'''
'''
#选项卡管理
#管理多选项卡，通过执行一个js，执行window.open()。
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.execute_script('window.open()')
print (driver.window_handles)   #返回所有选项卡，所有窗口的引用
driver.switch_to.window(driver.window_handles[1])  #切换到第二个选项卡
driver.get('https://www.taobao.com')
time.sleep(1)
driver.switch_to.window(driver.window_handles[0])  #切换到第一个选项卡
driver.get('https://python.org')
'''
'''
#异常处理
#点击异常，加载异常
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
browser.find_element_by_id('hello')
'''
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException

browser = webdriver.Chrome()
try:
    browser.get('https://www.taobao.com')
except TimeoutException:   #超时异常
    print ('Time Out')
try:
    browser.find_element_by_id('hello')
except NoSuchElementException:   #元素不存在时异常
    print ('No Element')
finally:
    browser.close()

    #更多操作https://selenium-python.readthedocs.io/api.html#module-selenium.common.exceptions