import pandas as pd

class Login:
    def __init__(self):
        self.password_file = pd.DataFrame()
        while True:
            self.id = input("User ID: ")
            self.password = input("Password: ")
            if self.id.strip() and self.password.strip():
                break
            else:
                print("Cannot leave any of the fields empty!")
        try:
            self.password_file = pd.read_csv("data/passwords.csv")
        except FileNotFoundError:
            print("User Authentication file is missing!")
        else:
            user_found = False
            for i in self.password_file.itertuples():
                if (self.id == i[1] and self.password == i[2]):
                    user_found = True
                    print("Welcome!")
                    break #USE TO CALL OPENER FUNCTION
            if not user_found:
                print("Wrong ID or Password!")


obj = Login()