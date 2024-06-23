import csv
import pandas as pd

class Grades:
    def __init__(self):
        self.grades = pd.read_csv("data/grades.csv")

    def list_grades(self):
        print(self.grades)
    
    def calculator(self):
        new_data = pd.DataFrame()
        new_data = self.grades.copy()
        #print(new_data)
        new_data["total"] = new_data["fom"]+new_data["fod"]+new_data["it"]+new_data["english"]+new_data["maths"]
        new_data["percentage"] = (new_data["total"]/5)
        print(new_data)

obj =  Grades()
obj.calculator()