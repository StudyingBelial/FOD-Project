import grades
import os
import pandas as pd
import time
import random
import string

class Users:
    def __init__(self):
        try:
            self.users = pd.read_csv("data/users.csv")
        except FileNotFoundError:
            print("User details file missing!")

    def list_users(self):
        print(self.users)

    def input_new_user(self):
        f_name = input("First Name: ")
        l_name = input("Last Name: ")
        email = input("Email: ")
        role = input("Role: ")
        city = input("City: ")
        id = self.unique_id_generator()
        self.info = {"id": id,"full_name":f_name, "last_name":l_name,"email":email,"role":role, "city":city}

    def new_user_main(self):
        if self.info.get("id").strip():
            ########################INCOMPLETE
            self.write_new_user()
        else:
            print("New user cannot be added, please try again!")
            return None
            
        # for value in self.info.values():
        #     if(value == ""):
        #         print("Cannot enter blank details while creating a new user!")
        #         print("Please try again!")
        #         return None
        role = self.info.get("role")
        if role == "Student":
            id = self.info.get("id")
            Grades.add_student_grades(id)
        elif role == "Teacher":
            # code here for Teacher
            pass
        elif role == "Admin":
            # code here for Admin
            pass
        else:
            print("The entered role is not valid")

    def write_new_user(self):
        if os.path.exists("data/users.csv"):
            new_user = pd.DataFrame(data = self.info)
            new_user.to_csv("data/users.csv", mode = "a")
            print("User Added Successfully!")
        else:
            print("User details file missing! Can't add to a non-existing file")
            

    def unique_id_generator(self):
        id_checker = self.users
        unique_id = ''
        id_check = True
        char = string.ascii_uppercase + string.digits
        for i in range (12):
            unique_id = unique_id + ''.join(random.choice(char))
        for i in id_checker.iterrows():
            a = i[1]["id"]
            if (a == unique_id):
                id_check = False
                break
            if id_check:
                return unique_id
            else:
                print("Failed to Generate User ID! Please try again later!")
                return None

    def access_user_details(self):
        user_id = input("Enter the user ID: ")
        user_found = False
        for index, row in self.users.iterrows():
            if row['id'] == user_id:
                user_found = True
                print("User Found!")
                print(self.users.iloc[index])
                print("first_name , last_name , email , role , city")
                field = input("What would you like to change: ")
                if (field =="first_name" or field =="last_name" or field =="email" or field =="role" or field =="city" ):
                    new_data = input("Enter the new value: ")
                    update_user_details(index, field, new_data)
                else:
                    print("Please enter a valid field!")
                    break
            if ((not user_found) and index == (len(self.users)-1)):
                print("User ID not found.")
                break

    def update_user_details(self, index, column, new_data):
        self.users.at[index, column] = new_data
        if os.path.exists("data/users.csv"):
            self.users.to_csv('data/users.csv', index=False)
            print("User Detail Successfully Updated")
            print(self.users.iloc[index])
        else:
            print("User details file missing! Can't edit from non-existing file")
            

# obj = Users
# obj.entering_new_user()
# info = {"first_name":"aarya", "last_name":"bhandari","email":"email","role":"role", "city":"city"}
# Users.adding_user(info, 12345)
print(Users.unique_id_generator())
