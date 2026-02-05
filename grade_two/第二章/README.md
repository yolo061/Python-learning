# SQL

## MySQL的安装

## DBeaver连接mysql

## SQL基础(结构化查询语言)
+ 数据定义:DDL
  + 库的创建删除、表的创建删除等
+ 数据操纵:DML
  + 新增数据、删除数据、修改数据等
+ 数据控制：DCL
  + 新增用户、删除用户、密码修改、权限管理等
+ 数据查询：DQL
  + 基于需求查询和计算数据

### SQL语句的特点
+ 大小写不敏感
+ 可以单行或者多行书写，以';'结束
+ SQL支持注释:
  + 单行注释: -- 注释内容
  + 单行注释: # 注释内容
  + 多行注释: /* 注释内容 */

### DDL - 库管理
+ SHOW DATABASES; 查看数据库
+ USE 数据库名称; 使用数据库
+ CREATE DATABASE 数据库名称 (可选)[CHARSET UTF8]; 创建数据库
+ DROP DATABASE 数据库名称; 删除数据库
+ SELECT DATABASE(); 查看当前使用的数据库
### DDL - 表管理
+ SHOW TABLES; 查看表
+ DROP TABLE 表名称; 删除表
+ DROP TABLE IF EXISTS 表名称; 删除表
+ CREATE TABLE 表名称(
    列名称 列类型,
    列名称 列类型,
    ......
  ); 创建表
  + 列的类型有:
    + int 
    + float
    + varchar
    + date 日期类型
    + timestamp 时间戳
### DML
+ 数据插入INSERT
  + INSERT INTO 表[(列1,列2,......,列N)] VALUES (值1,值2,...,值N) [,(值1,值2,...,值N),(值1,值2,...,值N),...,(值1,值2,...,值N)];
+ 数据删除DELETE 
  + 基础语法:
  + DELETE FROM 表名称[WHERE 条件判断];
+ 数据更新UPDATE
  + 基础语法:
  + UPDATE 表名称 SET 列 = 值 [WHERE 条件判断];

### DQL-基础数据查询
+ 基础语法:
+ SELECT 字段列表 FROM 表
+ 过滤查询:
+ SELECT 字段列表 FROM 表 [WHERE 条件判断];

### DQL-分组聚合
+ 基础语法:
+ SELECT 字段 | 聚合函数 FROM 表 [WHERE 条件] GROUP BY 列;
  + 聚合函数:
  + SUM(列) 求和
  + AVG(列) 求平均值
  + MIN(列) 求最小值
  + MAX(列) 求最大值
  + COUNT(列|*) 求数量

### DQL-结果排序
+ 对查询结果使用ORDER BY 关键字
+ 基础语法:
  + SELECT 列 | 聚合函数 | * FROM 表 WHERE ... GROUP BY ... ORDER BY ... [ASC | DESC] 升序排序 | 降序排序
  + 默认升序 ASC

### DQL-结果分页限制
+ 基本语法:
+ SELECT 列 | 聚合函数 | * FROM 表 WHERE ... GROUP BY ... ORDER BY ... [ASC | DESC] LIMIT n[,m];
+ LIMIT n[,m]的意思是：
  + 只有n，表示展示n条数据
  + 当还有n,m时，表示从第n条(不包括)开始取m条

## Python操作MySQL