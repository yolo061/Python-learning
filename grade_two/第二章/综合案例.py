'''
要求将前文的数据存入数据库中，并读取内容，记录"curedIncr"
'''

from pymysql import Connection, NULL
import json


class MysqlConn:
    conn = NULL
    cursor = NULL
    # 初始化就要获得链接和游标
    def __init__(self):
        self.__mysql_connector()
        self.__get_cursor()

    def __mysql_connector(self):
        self.conn = Connection(
            host='localhost',
            # 或者127.0.0.1
            port=3306,
            user='root',
            password='raojiarui0601',
            autocommit=True # 自动提交
        )
        self.conn.select_db('python')

    def __get_cursor(self):
        self.cursor = self.conn.cursor()

    def connect_close(self):
        self.conn.close()

    def detail_function(self,sql):
        try :
            self.cursor.execute(sql)
        except Exception as e:
            # print(e)
            pass

    def query(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def delete_all(self):
        self.cursor.execute("DELETE FROM test_2")

    def get_data_count(self):
        return self.cursor.execute("SELECT * FROM test_2")

if __name__ == '__main__':
    mysql = MysqlConn()
    # 首先创建表，检查表的存在性
    sql = '''
          CREATE TABLE test_2 ( 
              id   INT AUTO_INCREMENT PRIMARY KEY, 
              date varchar(50) UNIQUE NOT NULL , 
              data INT         NOT NULL
          ); 
          '''
    # 设置日起值为UNIQUE，避免出现重复
    try:
        mysql.detail_function(sql)
    except Exception as e:
        print(f"创建表失败: {e}")

    # 将数据读出来，使用字典存储
    result = dict()
    with open("data/world_total_data.json") as f:
        data = json.load(f)
        data = data.get("RECORDS", [])

    for i in data:
        result[i["dateId"]] = i["curedIncr"] # 将数据都存入字典当中
    # 获取所有的key值
    keys = list(result.keys())
    for i in keys:
        data = int(result[i])
        sql = f"INSERT INTO test_2 (date,data) VALUES ('{i}',{data})"
        mysql.detail_function(sql)

    # 执行查询才做
    count = mysql.get_data_count()
    index = 0
    length = 5
    while index < (count / length):
        results = mysql.query(f"SELECT * FROM test_2 ORDER BY data DESC LIMIT {index*length},{length}")
        index += 1
        print(f"第{index}次查询结果:")
        for r in results:
            print(f"id={r[0]}\tdate={r[1]}\tdata={r[2]}")
        print()


    ans = int(input("是否初始化表，非0表示删除:\n",))
    if (ans):
        mysql.delete_all()

    mysql.connect_close()
