#coding:utf-8

'''
每次发布都有个版本号：201812180900，201812182100

'''

from flask import Flask,url_for
from imooc import route_imooc  #蓝牙路由管理
from common.libs.UrlManager import UrlManager  #url_for链接管理
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.register_blueprint(route_imooc, url_prefix = "/imooc")    #(2)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:hh83ty?Gb3&4@127.0.0.1/mysql'
db = SQLAlchemy(app)

@app.route("/")  #网址
def hello_word():  #定义一个方法名

    url = url_for("index")

    url_1 = UrlManager.buildUrl("/api")
    url_2 = UrlManager.buildStaticUrl("/css/bootstrap.css")

    msg = 'Hello World,url:%s,url_1:%s,url_2:%s'%(url,url_1,url_2)  #日记记录

    app.logger.error(msg)
    app.logger.info(msg)
    app.logger.debug(msg)

    return msg


@app.route("/api")
def index():

    from sqlalchemy import text
    sql = text("SELECT * FROM `user`")
    result = db.engine.execute(sql)
    for row in result:  #循环
        app.logger.info(row)

    return 'Index page'

@app.route("/api/hello")
def hello():
    return 'Hello World'

@app.errorhandler(404) #引入404错误
def page_not_found(error):
    app.logger.error(error) #错误日记输出
    return 'This page does not exist', 404

if __name__ == "__main__":
    app.run(debug = True)

    #app.run(host='0.0.0.0')监控所有端口


