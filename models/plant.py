import pymysql

from framework.models import Model


class Plant(Model):

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
        inser_plant = """insert into plants  (id,location,plants_name,director_id)  VALUES (%s, %s, %s, %s) """
        cur.execute(inser_plant, val)
        cur2.commit()
    # def print_info(self):
    #     name = input("name : ")
    #     cur = self.mysqlconnect().cursor()
    #     cur.execute("select * from " + name)
    #     output = cur.fetchall()
    #     print(output)

    # def __init__(self, id, location, name, director_id):
    #     self.id = id
    #     self.location = location
    #     self.name = name
    #     self.director_id = director_id

    # def print_information(self):
    #     name = input("Select table")
    #     mycursor = self.connect().cursor()
    #
    #     sql = "SELECT * FROM " + name
    #
    #     mycursor.execute(sql)
    #
    #     myresult = mycursor.fetchall()
    #
    #     for x in myresult:
    #         print(x)
