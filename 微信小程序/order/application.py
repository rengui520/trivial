#coding:utf-8
#封装
from flask import Flask  #封装APP变量
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy  #封装DB变量
import os

class Application( Flask ):
    def __init__(self,import_name,template_folder = None):
        super( Application,self ).__init__( import_name,template_folder = template_folder )
        self.config.from_pyfile( 'config/base_setting.py' )
        if "ops_config" in os.environ:
            self.config.from_pyfile( 'config/%_setting.py'%os.environ['ops_config'] )


        db.init_app( self )

db = SQLAlchemy()
app = Application( __name__,template_folder = os.getcwd() + "/web/templates/" )
manager = Manager( app )


'''
函数模板
'''
from common.libs.UrlManager import UrlManager
app.add_template_global( UrlManager.buildStaticUrl,'buildStaticUrl' )
app.add_template_global( UrlManager.buildUrl,'buildUrl' )