import pandas as pd
import os
import tkinter.messagebox as messagebox

def parser():
    eca = pd.read_csv("data/eca.csv")
    students = pd.read_csv("data/student_id.csv")
    new_data = pd.DataFrame()
    new_data['id'] = students['id']
    new_data['eca'] = eca['eca']
    new_data.to_csv("data/eca.csv", index=False)
    print(new_data)

class Eca:
    def __init__(self):
        try:
            self.eca = pd.read_csv("data/eca.csv")
        except FileNotFoundError:
            print("ECA details file missing!")

    def print_eca(self):
        print(self.eca)

    def access_user_details(self, id, eca):
        user_id = id
        user_found = False
        for index, row in self.eca.iterrows():
            if row['id'] == user_id:
                user_found = True
                self.update_user_details(index, "eca", eca)
        if ((not user_found) and index == (len(self.eca)-1)):
            print("User ID not found.")
            messagebox.showinfo("Alert", "User ID not found.")

    def update_user_details(self, index, column, new_data):
        self.eca.at[index, column] = new_data
        if os.path.exists("data/eca.csv"):
            self.eca.to_csv('data/eca.csv', index=False)
            print("User Detail Successfully Updated")
            tkMessageBox.showinfo("Alert", "User Detail Successfully Updated")
            print(self.eca.iloc[index])

    def creating_eca(self, id):
        print("Hiking , Football , Volleyball , Table Tennis , Hiking")
        field = input("Choose: ")
        if (field =="Hiking" or field =="Football" or field =="Volleyball" or field =="Table Tennis" or field =="Hiking" ):
            choice = input("Enter the changed ECA: ")
            new_data = {'id': field, 'eca': choice}
            self.eca = self.eca.append(new_data, ignore_index=True)
            self.eca.to_csv('data/eca.csv', index=False)
            print("User Detail Successfully Added")
            tkMessageBox.showinfo("Alert", "User Detail Successfully Added")
        else:
            print("Please enter a valid ECA!")
            tkMessageBox.showinfo("Alert", "Please enter a valid ECA!")