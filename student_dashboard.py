import pandas as pd

class verify:
    @staticmethod
    def is_student(id):
        users = pd.read_csv("data/users.csv")
        for i in users.itertuples():
            read_id = i[1]
            read_user = i[5]
            if (id == read_id and read_user == "Student"):
                    print("WELCOME!. Here is your admin controls")
                    break

                
#verify.is_admin("7YT1E51QH77")