import pymysql

class Database:
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='empo',
            charset='utf8mb4'

        )
        
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    def execute_query(self, query, params=()):
        self.cursor.execute("SET NAMES utf8mb4")
        self.cursor.execute(query, params)
        self.conn.commit()
        return self.cursor

    def close(self):
        self.cursor.close()
        self.conn.close()

