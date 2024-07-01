import pandas as pd

def access_user_details():
    user_id = input("Enter the user ID: ")
    df = pd.read_csv('data/users.csv')
    user_found = False
    for index, row in df.iterrows():
        if row['id'] == user_id:
            user_found = True
            print("User Found!")
            print(df.iloc[index])
            print("first_name , last_name , email , role , city")
            field = input("What would you like to change: ")
            if (field =="first_name" or field =="last_name" or field =="email" or field =="role" or field =="city" ):
                new_data = input("Enter the new value: ")
                update_user_details(index, field, new_data)
            else:
                print("Please enter a valid field!")
                break
        if ((not user_found) and index == (len(df)-1)):
            print("User ID not found.")
            break

def update_user_details(index, column, new_data):
    df = pd.read_csv('data/users.csv')
    df.at[index, column] = new_data
    df.to_csv('data/users.csv', index=False)
    print("User Detail Successfully Updated")
    print(df.iloc[index])


access_user_details()