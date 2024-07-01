import pandas as pd
import os

class Verify:
    @staticmethod
    def is_admin(id):
        users = pd.read_csv("data/users.csv")
        for i in users.itertuples():
            read_id = i[1]
            read_user = i[5]
            if (id == read_id and read_user == "Admin"):
                    print("WELCOME!. Here is your admin controls")
                    break

class Admin_Master_Controls:
    def choose(self):
        while True:
            print("What would you like to do?")
            print("1. Add Individual Users")
            print("2. Import Data Base")
            print("3. Edit User Details")
            print("4. Edit Student Grades")
            print("5. Analytics")
            try:
                nav = int(input("Choose the number: "))
            except ValueError:
                os.system('cls')
                print("Please enter the number corresponding to the option!")
            else:
                match nav:
                    case 1:
                        break
                    case 2:
                        break
                    case 3:
                        break
                    case 4:
                        break
                    case 5:
                        break
                    case _:
                        os.system('cls')
                        print("The picked option is out of scope. Please try again!")

    


    # Example usage:
    # user_mgmt = UserManagement("data/users.csv")
    # print(user_mgmt.access_row(1))
    # print(user_mgmt.access_column('email'))
    # user_mgmt.edit_row(1, {'first_name': 'John', 'last_name': 'Doe'})
    # user_mgmt.edit_column('city', ['New York', 'Los Angeles', 'Chicago'])
    #verify.is_admin("7YT1E51QH77")
    #verify.edit_user_details()
    # users = pd.read_csv("data/users.csv")
    # print(users.loc[0:3]['id'])

obj = Admin_Master_Controls
obj.choose()