import pymysql
from common.handle_config import read_config


class MySQLHandler():

    def __init__(self):
        '''连接数据库'''
        self.connect = pymysql.connect(host=read_config.get("mysql", "host"),
                                       port=read_config.getint("mysql", "port"),
                                       user=read_config.get("mysql", "user"),
                                       password=read_config.get("mysql", "password"),
                                       db=read_config.get("mysql", "db"),
                                       charset="utf8",
                                       cursorclass=pymysql.cursors.DictCursor
                                       )

        self.cursor = self.connect.cursor()  # 创建游标对象

    def find_all(self, sql):
        '''返回所有数据'''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def find_one(self, sql):
        '''返回第一条数据'''
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def find_count(self, sql):
        '''返回查询到的数据个数'''
        result = self.cursor.execute(sql)
        return result

    # def update(self, sql):
    #     '''增删改操作'''
    #     self.cursor.execute(sql)
    #     self.connect.commit()

    def close(self):
        '''断开游标，关闭连接'''
        self.cursor.close()
        self.connect.close()


# if __name__ == '__main__':
#     sql = "select id from organizationtable where OrgName = 'api测试001'"
#     a = MySQLHandler().find_all(sql)
#     print(a)
