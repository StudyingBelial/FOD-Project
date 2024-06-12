import csv

class grades:

    def list_grades(self):
        with open("grades.csv", mode = r) as file:
            grades = csv.reader(file)
            print("|    Student ID  |    FOD    |    FOM   |   Maths   |   English |   IT  |")
            for details in grades:
                print(f"|   {details[0]}  |   {details[1]}  |   {details[2]}  |   {details[3]}  |   {details[4]}  |   {details[5]}  |")
    
    def grade_adder(self):
        with open("grader.csv", mode = a) as file:
            adder = csv.writer(file)
            id = print("Enter the user ID: ")
            fod = print("Enter FOD Grades: ")
            fom = print("Enter FOM Grades: ")
            maths = print("Enter Maths Grades: ")
            english = print("Enter English Grades: ")
            it = print("Enter IT Grades: ")
            adder.writerow([id,fod,fom,maths,english,it])