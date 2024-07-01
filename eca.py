import pandas as pd

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

    def access_user_details(self):
        user_id = input("Enter the user ID: ")
        user_found = False
        for index, row in self.eca.iterrows():
            if row['id'] == user_id:
                user_found = True
                print("User Found!")
                print(self.eca.iloc[index])
                print("Hiking , Football , Volleyball , Table Tennis , Hiking")
                field = input("What would you like to change: ")
                if (field =="Hiking" or field =="Football" or field =="Volleyball" or field =="Table Tennis" or field =="Hiking" ):
                    new_data = input("Enter the changed ECA: ")
                    self.update_user_details(index, field, new_data)
                else:
                    print("Please enter a valid ECA!")
                    break
            if ((not user_found) and index == (len(self.eca)-1)):
                print("User ID not found.")
                break

    def update_user_details(self, index, column, new_data):
        self.eca.at[index, column] = new_data
        self.eca.to_csv('data/users.csv', index=False)
        print("User Detail Successfully Updated")
        print(self.eca.iloc[index])