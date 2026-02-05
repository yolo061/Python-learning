from pymysql import Connection, NULL

class MysqlConn:
    conn = NULL
    def mysql_connector(self):
        self.conn = Connection(
            host='localhost',
            # 或者127.0.0.1
            port=3306,
            user='root',
            password='raojiarui0601',
            # autocommit=True # 自动提交
        )
        return self.conn

    def select_database(self,name):
        self.conn.select_db(name)

    def get_cursor(self):

        return self.conn.cursor()

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()



if __name__ == '__main__':
    mysql = MysqlConn()
    conn = mysql.mysql_connector()
    cursor = mysql.get_cursor()
    # 选择数据库
    mysql.select_database('python')
    # 添加数据
    try :
        cursor.execute("INSERT INTO test_1(NAME, AGE) VALUES ('dwx',19)")
        '''
        仅执行sql语句，数据库不会发生更改，即需要通过确认，才能发生更改
        '''
        conn.commit()
    except Exception as e:
        print(e)
    # 执行查询语句,此处要重新获得游标不然还是得到的是插入前的游标
    cursor = mysql.get_cursor()
    count_all = cursor.execute("SELECT * FROM test_1")
    times = int(count_all / 5)
    count = 0
    while count < times:
        cursor.execute("SELECT * FROM test_1  LIMIT %d , 5" % (count * 5))
        # ORDER BY age DESC 这里是先对年龄进行排序，再进行分页的
        count += 1
        results = cursor.fetchall()
        # 得到的结果为元组
        print(f"第{count}次查询得到的结果为:")
        for i in results:
            print(f"id = {i[0]}\tname = {i[1]}\tage = {i[2]}")
        print()

    # 关闭数据库的链接
    mysql.close()