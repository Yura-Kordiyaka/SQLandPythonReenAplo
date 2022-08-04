import pymysql

from framework.models import Model
import mysql.connector
from mysql.connector import Error
import pandas as pd


class Employee(Model):
    def mysqlconnect(cls):
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password="root",
            db='test',
        )

        return conn

    def add(self, name, val):
        cur2 = self.mysqlconnect()
        cur = cur2.cursor()
        inser_employeees = """insert into employees  (id,email,user_name,department_type,department_id)  VALUES (%s, %s, %s, %s,%s) """
        cur.execute(inser_employeees, val)
        cur2.commit()
