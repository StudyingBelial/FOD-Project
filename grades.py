import csv
import pandas as pd

class Grades:
    def list_grades(self):
        self.grades = pd.read_csv("data/grades.csv")
        print(self.grades)

    @staticmethod
    def add_student_grades(id):
        fod = float(input("FOD Grades: "))
        fom = float(input("FOM Grades: "))
        it = float(input("IT Grades: "))
        english = float(input("English Grades: "))
        maths = float(input("Maths Grades: "))
        marks = {"id":id,"fod":fod, "fom":fom,"it":it,"english":english, "maths":maths}
        df = pd.DataFrame(data = marks)
        df.to_csv("data/grades.csv", mode = "a", header = False)

    
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