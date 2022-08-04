from framework.models import Model
from models.plant import Plant

from models.employee import Employee
from models.salon import Salon


class Controller():

    def general(self, choose):
        if choose == 1:
            id = int(input("id : "))
            location = input("location : ")
            plants_name = input("plants name : ")
            director_id = int(input("director id : "))
            record = (id, location, plants_name, director_id)
            plant = Plant()
            plant.add("plants", record)
        elif choose == 2:
            id = int(input("id : "))
            email = input("email : ")
            user_name = input("user_name : ")
            department_type = input("department_type : ")
            department_id = input("department_id : ")
            record = (id, email, user_name, department_type, department_id)
            emplo = Employee()
            emplo.add("employees", record)
        elif choose == 3:
            id = int(input("id : "))
            location = input("location : ")
            salon_name = input("salon name : ")
            director_id = int(input("director id : "))
            record = (id, location, salon_name, director_id)
            salon = Salon()
            salon.add("salon", record)
        elif choose == 4:
            n = int(input("id = "))
            plant = Plant()
            plant.search_by("plants", n)
        elif choose == 5:
            n = int(input("id = "))
            emplo = Employee()
            emplo.search_by("employees", n)
        elif choose == 6:
            n = int(input("id = "))
            salon = Salon()
            salon.search_by("salon", n)
