import mysql.connector
 
mydb = mysql.connector.connect(
  host="localhost",       # 数据库主机地址
  user="root",    # 数据库用户名
  passwd="xuujii123456",   # 数据库密码
  database="vmovie"
)
 
mycursor = mydb.cursor()

#print(mydb)
mycursor.execute("CREATE TABLE vmovie (name VARCHAR(255), url VARCHAR(255))")