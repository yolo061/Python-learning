from pymysql import Connection, NULL

class MysqlConn:
    conn = NULL
    def __mysql_connector(self):
        self.conn = Connection(
            host='localhost',
            # 或者127.0.0.1
            port=3306,
            user='root',
            password='raojiarui0601',
        )

    def select_database(self,name):
        self.conn.select_db(name)

    def get_cursor(self):
        self.__mysql_connector()
        return self.conn.cursor()

    def close(self):
        self.conn.close()



if __name__ == '__main__':
    mysql = MysqlConn()
    cursor = mysql.get_cursor()
    # 选择数据库
    mysql.select_database('python')
    # 执行查询语句

    times = int(180 / 5)
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