import MySQLdb
# 创建一个数据库连接对象
db = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    password='wxc7586637039',
    db='TESTDB',
    charset= 'utf8mb4' #'utf8'
)
# 获取连接的游标
cursor = db.cursor()
# 执行SQL语句
cursor.execute("SELECT VERSION()")
# 执行语句,展示所有数据库
cursor.execute('show databases')
# 遍历所有数据库 (多维元组)
for i in cursor:
    print(i)
# 关闭游标
cursor.close()
# 关闭连接
db.close()
