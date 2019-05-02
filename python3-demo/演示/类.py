#C:\Program Files (x86)\Google\Chrome\Application
#coding:utf-8

#导入selenium
from selenium import webdriver

#我们用 class 创建一个类，后面接你要定义的类名，以冒号结束
class Qiubai:       #定义 Qiubai 这个类；class是python关键字。
    def __init__(self):  #def __init__() 这个函数比较特殊，我们叫它初始化方法或构造函数，
                          # 当这个类有实例被创建时，该方法就会被调用。
                          #还有一点，self 代表这个类的实例，它不是 Python 的关键字，
                          # 只是我们习惯于这样写，它是必须存在的。
        self.dr = webdriver.Chrome()  #打开Chrome浏览器
        self.dr.get('http://www.qiushibaike.com/')  #访问糗事百科主页

    #定义 print_content 函数
    def print_content(self):
        # 我们通过 find_element_by_id 方法获取了 id 为 content-left 的标签
        main_content = self.dr.find_element_by_id('content-left')
        # 我们对 main_content 使用 find_elements_by_class_name 方法获取了 class 为 content 的标签
        contents = main_content.find_elements_by_class_name('content')

        # 通过for循环输出获取到的内容
        i = 1
        for content in contents:
            print(str(i) + "." + content.text + '\n')
            i += 1
#我们定义了一个变量 i = 1，作为每个段子的编号，打印完一个就 +1，其中反斜杠 + n 表示换行

        self.quit()

    #定义 quit 函数
    def quit(self):
        # dr.quit()关闭浏览器
        self.dr.quit()

#最后通过 Qiubai().print_content() 来调用类中的方法
Qiubai().print_content()