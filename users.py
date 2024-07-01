import os
import pandas as pd
import random
import string
from tkinter import messagebox

class Users:
    def __init__(self):
        try:
            self.users = pd.read_csv("data/users.csv")
        except FileNotFoundError:
            print("User details file missing!")

    def list_users(self):
        print(self.users)

    def input_new_user(self, f_name, l_name, email, role, city):
        id = self.unique_id_generator()
        if not all([f_name, l_name, email, role, city, id]):
            print("One of the user details is missing! Please try again!")
            messagebox.showinfo("Alert", "One of the user details is missing! Please try again!")
            return None

        self.info = {"id": id, "first_name": f_name, "last_name": l_name, "email": email, "role": role, "city": city}
        self.new_user_main()
        self.generate_password(id)
        return id

    def new_user_main(self):
        if self.info.get("id").strip():
            self.write_new_user()
        else:
            print("New user cannot be added, please try again!")
            messagebox.showinfo("Alert", "New user cannot be added, please try again!")

    def generate_password(self, id):
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        data = {"id": id, "password": password}
        password_df = pd.DataFrame(data=[data])
        password_df.to_csv("data/passwords.csv", mode="a", index=False, header=False)
        print("Password generated successfully!")
        messagebox("Alert", f"Password generated successfully! NEW PASSWORD {password}")
        

    def write_new_user(self):
        if os.path.exists("data/users.csv"):
            new_user = pd.DataFrame(data=[self.info])
            new_user.to_csv("data/users.csv", mode="a", index=False, header=False)
            print("User added successfully!")
            messagebox("Alert", "User added successfully!")
        else:
            print("User details file missing! Can't add to a non-existing file")

    def unique_id_generator(self):
        id_checker = self.users
        unique_id = ''
        id_check = True
        char = string.ascii_uppercase + string.digits
        for _ in range(12):
            unique_id += ''.join(random.choice(char))
        for i in id_checker.iterrows():
            a = i[1]["id"]
            if a == unique_id:
                id_check = False
                break
        if id_check:
            return unique_id
        else:
            return None

    def access_user_details(self, user_id, field, new_data):
        user_found = False
        for index, row in self.users.iterrows():
            if row['id'] == user_id:
                user_found = True
                print("User Found!")
                print(self.users.iloc[index])
                self.update_user_details(index, field, new_data)
        if not user_found:
            print("User ID not found.")

    def update_user_details(self, index, column, new_data):
        self.users.at[index, column] = new_data
        if os.path.exists("data/users.csv"):
            self.users.to_csv("data/users.csv", index=False)
            print("User detail successfully updated")
            messagebox("Alert", "User added successfully!")
            print(self.users.iloc[index])
        else:
            print("User details file missing! Can't edit from non-existing file")

    def remove_users(self):
        user_id = input("Enter the user ID: ")
        user_found = False
        for index, row in self.users.iterrows():
            if row['id'] == user_id:
                user_found = True
                if os.path.exists("data/users.csv"):
                    self.users = self.users.drop(index)
                    self.users.to_csv("data/users.csv", index=False)
                    print("User removed successfully")
                    break
                else:
                    print("User details file missing! Can't remove from non-existing file")
                    break
        if not user_found:
            print("User ID not found.")
