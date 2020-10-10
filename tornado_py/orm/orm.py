# -*- coding: UTF-8 -*

import MySQLdb

# 建立和数据库的连接
db = MySQLdb.connect(host="localhost", user="root", passwd="root123", db="vending_machine", charset='utf8')
# 获取操作游标
cursor = db.cursor()
# SQL 查询语句
sql = "SELECT * FROM USER WHERE USER_ID == 666666"
# 执行sql
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for test_id in results:
        t_id = test_id[0]
        # 打印结果
        print "ID=" + t_id
except:
    print "Error: unable to fecth data"
# 关闭连接，释放资源
db.close()
