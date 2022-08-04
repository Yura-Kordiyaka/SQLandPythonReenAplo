from models.plant import Plant
from models.employee import Employee
from models.salon import Salon
import pymysql

from Controller import Controller

while True:
    print(
        "Choose a menu item by number: \n" +
        "1. Add new Plant \n" +
        "2. Add new Employee \n" +
        "3. Add new Salon\n" +
        "4. Get plant by id \n" +
        "5. Get employee by id \n" +
        "6. Get salon by id\n"
    )
    menu_flag = int(input("Your choose: "))
    start = Controller()
    start.general(menu_flag)
