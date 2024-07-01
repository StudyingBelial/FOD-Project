import pandas as pd
import os
import tkinter.messagebox as tkMessageBox
class Self_Password:
    def __init__(self):
        try:
            self.password_file = pd.read_csv("data/passwords.csv")
        except FileNotFoundError:
            print("User Authentication file is missing!")
            tkMessageBox("Alert","User Authentication file is missing!")

    def change_password_verify(self, id, new_p, con_p):
        self.id = id
        new_password = new_p
        confirm_password = con_p
        user_found = False
        for index, row in self.password_file.iterrows():
            if self.id == row["id"]:
                user_found = True
                if new_password != confirm_password:
                    print("Unmatching Passwords! Please Try again")
                    tkMessageBox("Alert","Unmatching Passwords! Please Try again")
                    continue
                else:
                    if " " in new_password:
                        print("Cannot have white spaces in a password. Please Try again!")
                        tkMessageBox("Alert","Cannot have white spaces in a password. Please Try again!")
                    else:
                        self.password_changer(index, new_password)

    def password_changer(self, index, new_password):
        self.password_file.at[index, "password"] = new_password
        if os.path.exists("data/passwords.csv"):
            self.password_file.to_csv("data/passwords.csv", index=False)
            print("Password Successfully Changed")
            tkMessageBox("Alert","Password Successfully Changed")
            print(self.password_file.iloc[index])
        else:
            print("User details file missing! Can't edit from non-existing file")
            tkMessageBox("Alert","User details file missing! Can't edit from non-existing file")

class Admin_Password_Controls(Self_Password):
    def change_password_verify(self):
        while True:
            id = input("User ID: ")
            if not id:
                print("Cannot leave the ID field empty!")
                continue
            else:
                break
        user_found = False
        for index, row in self.password_file.iterrows():
            if id == row["id"]:
                user_found = True
                for attempt in range(3):
                    new_password = input("New Password: ")
                    confirm_password = input("Confirm Password: ")
                    if new_password != confirm_password:
                        print("Unmatching Passwords! Please Try again")
                        continue
                    else:
                        if " " in new_password:
                            print("Cannot have white spaces in a password. Please Try again!")
                            continue
                        else:
                            self.password_changer(index, new_password)
                            break
                else:
                    print("Maximum attempts reached. Please try again later.")
        if not user_found:
            print("Wrong ID or Password!")