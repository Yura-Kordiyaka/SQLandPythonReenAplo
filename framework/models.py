from abc import ABC, abstractmethod
import mysql.connector
import json

import pymysql


class Model(ABC):
    @abstractmethod
    def mysqlconnect(cls):
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password="root",
            db='test',
        )
        return conn

    def print_info(self, name):
        cur = self.mysqlconnect().cursor()
        cur.execute("select * from " + name)
        output = cur.fetchall()
        print(output)

    def search_by(self, name, id):
        cur = self.mysqlconnect().cursor()
        cur.execute("select * from " + name + " where id = "+str(id))
        output = cur.fetchall()
        print(output)
    @abstractmethod
    def add(self,name,val):
       pass
