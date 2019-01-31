import pymysql.cursors
import os
from package.config import MYSQL_CONFIG


class MySqlWorker(object):

    def __init__(self):

        self.host = MYSQL_CONFIG['host']
        self.database = MYSQL_CONFIG['db']
        self.user = MYSQL_CONFIG['user']
        self.password = MYSQL_CONFIG['pwd']
        self.charset='utf8mb4'
        self.cursorclass=pymysql.cursors.DictCursor

    def __enter__(self):

        conn = pymysql.connect(host=self.host,
                               database=self.database,
                               user=self.user,
                               password=self.password,
                               charset=self.charset,
                               cursorclass=self.cursorclass,
                               autocommit=True
                               )

        self.conn = conn
        self.cr = self.conn.cursor()
        return self.cr

    def __exit__(self, exc_type, exc_val, exc_tb):

        self.cr.close()
        self.conn.close()



