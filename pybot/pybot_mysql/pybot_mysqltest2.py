
import pymysql
# 连接MySQL数据库
connection = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='wxc7586637039',
    db='guest',
    charset='utf8mb4'#,
    #cursorclass=pymysql.cursors.DictCursor
    )
# 通过cursor创建游标
cursor = connection.cursor()
# 创建sql 语句，并执行
sql = "INSERT INTO `users` (`email`, `password`) VALUES ('huzhiheng@itest.info', '123456')"
cursor.execute(sql)
# 提交SQL
connection.commit()
#不管你使用的是什么工具或库，连接数据库这一步必不可少。host为数据库的主机IP地址，port为MySQL的默认端口号，user为数据的用户名，password为数据库的登录密码，db为数据库的名称。

#cursor()方法创建数据库游标。

#execute()方法执行SQL语句。

#commit()将数据库的操作真正的提交到数据。
