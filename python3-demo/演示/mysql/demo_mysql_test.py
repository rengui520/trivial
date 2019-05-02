import mysql.connector
 
mydb = mysql.connector.connect(
  host="localhost",       # 数据库主机地址
  user="root",    # 数据库用户名
  passwd="xuujii123456"   # 数据库密码
)
 
mycursor = mydb.cursor()

#print(mydb)
mycursor.execute("CREATE DATABASE vmovie")