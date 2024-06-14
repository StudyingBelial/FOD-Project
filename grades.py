import csv

class grades:
    @staticmethod
    def list_grades(self):
        with open("grades.csv", mode = r, newline='') as file:
            grades = csv.reader(file)
            print("|    Student ID  |    FOD    |    FOM   |   Maths   |   English |   IT  |")
            for details in grades:
                print(f"|   {details[0]}  |   {details[1]}  |   {details[2]}  |   {details[3]}  |   {details[4]}  |   {details[5]}  |")
    
    def grade_adder(self):
        with open("grader.csv", mode = a, newline='') as grade_file:
            adder = csv.writer(grade_file)
            id = input("Enter the user ID: ")
            fod = input("Enter FOD Grades: ")
            fom = input("Enter FOM Grades: ")
            maths = input("Enter Maths Grades: ")
            english = input("Enter English Grades: ")
            it = input("Enter IT Grades: ")
            adder.writerow([id,fod,fom,maths,english,it])

    def grade_modifier_verify(self):
        prompt_id = input("Please Enter the Student ID: ")
        vaid_user = False
        with open("grades.csv", mode = r, newline='') as file:
            grades = csv.reader(file)
            for id in grades:
                if (id == prompt_id):
                     valid_user = True
                     break
                else:
                    valid_user = False
        if (valid_user == False):
            print("The Student ID does not exist!")
        else:
            if(valid_user == True):
                subject = input ("Enter the Subject to modify: ")
            else:
                pass

        if (valid_user == True):
            marks = input("Please enter new marks: ")
            if (subject == "fod"):
                grade_editer(prompt_id, 1, marks)
            else:
                if (subject == "fom"):
                    grade_editer(prompt_id, 2, marks)
                else:
                    if (subject == "maths"):
                        grade_editer(prompt_id, 3, marks)
                    else:
                        if (subject == "english"):
                            grade_editer(prompt_id, 4, marks)
                        else:
                            if (subject == "it"):
                                grade_editer(prompt_id, 5, marks)
                            else:
                                print("Please enter valid subject!")

    def grade_editer(self, id ,subject, marks):
        with open("grades.csv", mode = r,newline='') as file:
            with open("temp_grades.csv", mode = w, newline='') as temp_file:
                temp = csv.writer(temp_file)
                grades = csv.reader(file)
                for details in grades:
                    if(details[0] == id):
                        details[subject] == marks
                    temp.writerow()

        with open("grader.csv", mode = w, newline='') as grade_file:
            with open("temp_grades.csv", mode = r, newline='') as temp_file:
                temp = csv.reader(temp_file)
                adder = csv.writer(grade_file)
                for details in temp:
                    adder.writerow(details)