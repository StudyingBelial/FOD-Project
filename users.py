import grades

import pandas as pd
import csv
import numpy as np
import time
import random
import string

class Users:
    def list_users():
        users = pd.read_csv("data/users.csv")
        print(users)

    def entering_new_user():
        f_name = input("First Name: ")
        l_name = input("Last Name: ")
        email = input("Email: ")
        role = input("Role: ")
        city = input("City: ")
        id = Users.unique_id_generator()
        info = {"id": id,"full_name":f_name, "last_name":l_name,"email":email,"role":role, "city":city}

        if id == "":
            return None
        else:
            Users.adding_user(info)

        for value in info.values():
            if(value == ""):
                print("Cannot enter blank details!")
                print("Please try again")
                break
            else:
                if(role == "Student"):
                    Grades.add_student(id)
                else:
                    if(role == "Teacher"):
                        pass#code here
                    else:
                        if(role == "Admin"):
                            pass#code here
                        else:
                            print("The entered role is not valid")

    @staticmethod
    def adding_user(info):
        user = pd.read_csv("data/users.csv")
        print(user)
        new_user = pd.DataFrame(data = info)
        addition = pd.concat([user, new_user])

    @staticmethod
    def unique_id_generator():
        unique_id = ''
        id_check = True
        char = string.ascii_uppercase + string.digits
        for i in range (12):
            unique_id = unique_id + ''.join(random.choice(char))
        id_checker = pd.read_csv("data/users.csv")
        for i in id_checker.iterrows():
            a = i[1]["id"]
            if (a == unique_id):
                id_check = False
        if id_check:
            return unique_id
        else:
            return None
            

# obj = Users
# obj.entering_new_user()
# info = {"first_name":"aarya", "last_name":"bhandari","email":"email","role":"role", "city":"city"}
# Users.adding_user(info, 12345)
print(Users.unique_id_generator())
