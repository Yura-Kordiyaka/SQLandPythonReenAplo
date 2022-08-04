import pymysql

from framework.models import Model


class Salon(Model):
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
        inser_plant = """insert into salon  (id,location,salon_name,director_id)  VALUES (%s, %s, %s, %s) """
        cur.execute(inser_plant, val)
        cur2.commit()
