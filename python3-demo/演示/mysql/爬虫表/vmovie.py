import pymysql

db = pymysql.connect(host='localhost', user='root', password='xuujii123456', port=3306, db='spiders')
cursor = db.cursor()
sql = 'CREATE TABLE IF NOT EXISTS vmovie (cover VARCHAR(255) NOT NULL, title VARCHAR(255) NOT NULL, playUrl VARCHAR(255) NOT NULL,  dec INT NOT NULL, PRIMARY KEY (title))'
cursor.execute(sql)
db.close()