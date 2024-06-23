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

    def add_user():
        f_name =input("First Name: ")
        l_name =input("Last Name: ")
        email = input("Email: ")
        role = input("Role: ")
        city = input("City: ")
        id = unique_id_generator()
        print(id)

    @staticmethod
    def unique_id_generator():
        unique_id = ''
        char = string.ascii_uppercase + string.digits
        print(char)
        for i in range (12):
            unique_id = unique_id + ''.join(random.choice(char))
        print(unique_id)

Users.unique_id_generator()