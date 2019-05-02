#coding:utf-8
#入口
from application import app,manager
from flask_script import Server
import www

##web server
manager.add_command( "runserver", Server( host='0.0.0.0',port=5000,use_debugger = True ,use_reloader = True) )
#manager.add_command( "runserver", Server( port=app.config['SERVER_PORT'],use_debugger = True ,use_reloader = True) )

def main():
    #app.run( host="0.0.0.0",debug = True )
    manager.run( )

if __name__ == '__main__':  #__main__是入口方法
    try:
        import sys
        sys.exit( main() )
    except Exception as e:
        traceback.print_exc()
