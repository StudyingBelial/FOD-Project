import pandas as pd
import csv
import numpy as np
import time

class Users:
    def list_users():
        users = pd.read_csv("data/users.csv")
        print(users)

    def add_user():
        f_name =input("First Name: ")
        l_name =input("Last Name: ")
        email = input("Email: ")
        role = input("Role: ")
        city = input("City: ")
        id = f_name[0].lower() + l_name[0].lower() + str(int(time.time()))
        print(id)