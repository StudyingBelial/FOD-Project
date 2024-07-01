import pandas as pd

class verify:
    @staticmethod
    def is_admin(id):
        users = pd.read_csv("data/users.csv")
        for i in users.itertuples():
            read_id = i[1]
            read_user = i[5]
            if (id == read_id and read_user == "Admin"):
                    print("WELCOME!. Here is your admin controls")
                    break
    
    @staticmethod
    def access_user_details():
        exist = False
        id = ()
        exist, id = verify.exist_user()
        if exist:
            print("ID: ", id[1])
            print("First Name: ", id[2])
            print("Last Name: ", id[3])
            print("Email: ", id[4])
            print("Role: ", id[5])
            print("City: ", id[6])
            return True, id
        else:
            print("The given User ID does not exist!")
            return False, id

    @staticmethod
    def edit_user_details():
        exist = False
        id = ()
        exist, id = verify.access_user_details()
        id = list(id)
        id.pop(0)
        if exist:
            change_data = pd.DataFrame(data = {"id": [id[0]],"first_name": [id[1]],"last_name": [id[2]] ,"email" : [id[3]],"role" : [id[4]],"city" : [id[5]]})
            print(change_data)
            

    @staticmethod
    def exist_user():
        exist = False
        users = pd.read_csv("data/users.csv")
        chg_id = input("Enter the user ID: ")
        for i in users.itertuples():
            read_id = i[1]
            if (chg_id == read_id):
                    exist = True
                    break
        return exist, i


#verify.is_admin("7YT1E51QH77")
#verify.edit_user_details()
users = pd.read_csv("data/users.csv")

print(users.loc[0:3]['id'])