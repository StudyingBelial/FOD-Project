import csv
import pandas as pd
import os
import tkinter.messagebox as tkMessageBox

class Grades:
    def __init__(self):
        try:
            self.grades = pd.read_csv("data/grades.csv")
        except FileNotFoundError:
            print("Grades Files for students does not exist!")

    def list_grades(self):
        print(self.grades)

    @staticmethod
    def add_student_grades(id, fod, fom, it, english, maths):
        marks = {"id": [id], "fod": [fod], "fom": [fom], "it": [it], "english": [english], "maths": [maths]}
        df = pd.DataFrame(data=marks)
        file_path = "data/grades.csv"
        if os.path.exists(file_path):
            df.to_csv(file_path, mode="a", header=False, index=False)
        else:
            print("Grades file for students does not exist! Cannot write to a non-existing file")
            tkMessageBox("Alert","Grades file for students does not exist! Cannot write to a non-existing file")  

    @staticmethod
    def edit_student_grades(id, column, new_grade):
        if column in self.grades.columns:
            self.grades.loc[self.grades['id'] == id, column] = new_grade
            self.grades.to_csv("data/grades.csv", index=False)
            print("Grades updated successfully.")
            tkMessageBox("Alert","Grades updated successfully.")
        else:
            print("Invalid column name.")

    def calculator(self):
        self.grades = pd.read_csv("data/grades.csv")
        new_data = pd.DataFrame()
        new_data = self.grades.copy()
        #print(new_data)
        new_data["total"] = new_data["fom"]+new_data["fod"]+new_data["it"]+new_data["english"]+new_data["maths"]
        new_data["percentage"] = (new_data["total"]/5)
        print(new_data)

    @staticmethod
    def student_id(): #unusuable
        users = pd.read_csv("data/users.csv")
        id = pd.DataFrame(columns=["id"])
        for i in range(len(users)):
            if users.iloc[i]['role'] == "Student":
                student_id_df = pd.DataFrame([[users.iloc[i]['id']]], columns=["id"])
                id = pd.concat([id, student_id_df], ignore_index=True)
        id.to_csv("data/student_id.csv", index = False, header=False)


    @staticmethod
    def grade_file_use(): #unusuable
        grade = pd.read_csv("data/grades.csv")
        id = pd.read_csv("data/student_id.csv")
        grade.pop("id")
        id["fod"] = grade ["fod"]
        id["fom"] = grade ["fom"]
        id["it"] = grade ["it"]
        id["english"] = grade ["english"]
        id["maths"] = grade ["maths"]
        id.to_csv("grades.csv", index = True)
        print(id)