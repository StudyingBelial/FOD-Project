import pandas as py
import os

class Data_Handler:
    def __init__(self):
        while True:
            print("What is the type of file you would like to add")
            print("1. Users")
            print("2. ECA")
            print("3. ID and Passwords")
            print("4. Grades")
            try:
                file_type = int(input("Choose the number: "))
            except ValueError:
                os.system('cls')
                print("Please enter the number corresponding to the option!")
            else:
                print("Note that the file should be .csv and should be in the same directory. So don't type .csv")
                file_name = input("Please enter the file name: ")
                file_name = file_name + ".csv"
                if os.path.exists(file_name):
                    match file_type:
                        case 1:
                            Data_Handler.Users(file_name)
                        case 2:
                            break
                        case 3:
                            break
                        case 4:
                            break
                        case _:
                            os.system('cls')
                            print("The picked option is out of scope. Please try again!")
                else:
                    print("The file entered does not exist! Please Try Again!")
    
    @staticmethod
    def Users(file_name):
        file = pd.read_csv(file_name)
        header_list = list(file.columns)
        users_header_list = ["id","first_name","last_name","email","role","city"]
        if (header_list == users_header_list):
            print("The importing data set is valid and will be added!")
        else:
            if len(header_list) == len(users_header_list):
                pass 
