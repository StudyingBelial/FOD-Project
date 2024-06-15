import csv
import datetime

class Users:
    def __init__(self):
        self.f_name = input("First Name: ")
        self.l_name = input("Last Name: ")
        self.number = input("Phone Number: ")
        self.role = input("Role: ")

    def generate_unique_id():
        now = datetime.datetime.now()
        
        random_id = now.strftime("%Y%f")
        unique_id = self.f_name.lower()+self.l_name.lower()+random_id
        return unique_id