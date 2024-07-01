import customtkinter
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
import tkinter.filedialog as tkFileDialog
import tkinter.font as tkFont


import pandas as pd


class Login:
    def __init__(self, id, password):
        self.id = id
        self.password = password
        self.password_file = pd.DataFrame()
        try:
            self.password_file = pd.read_csv("data/passwords.csv")
        except FileNotFoundError:
            print("User Authentication file is missing!")
        else:
            user_found = False
            for index, id, password in self.password_file.itertuples():
                if (self.id == id and password == password):
                    user_found = True
                    print("Login Successful!")
            if not user_found:
                print("Wrong ID or Password!")
                messagebox.showinfo("Alert", "Wrong ID or Password!")

    def user_config(self):
        print("user config")
        try:
            users = pd.read_csv("data/users.csv")
            print("verified users file")
        except FileNotFoundError:
            print("User details file missing!")
        try:
            print("reading file")
            with open("data/current_config.txt", mode = "w") as file:
                for index, row in users.iterrows():
                    if row['id'] == self.id:
                        file.write(row["id"]+"\n")
                        file.write(row["first_name"]+"\n")
                        file.write(row["email"]+"\n")
                        file.write(row["role"]+"\n")
                        return row["role"]
        except FileNotFoundError:
            print("User Configuration Files does not exist!")

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

root=customtkinter.CTk()
root.title("Student LogIn System")
root.geometry("400x350")
root.resizable(1000, 750)

role_var = tk.StringVar() #variable

def login(input_id, input_password, remember):
    id = input_id.get()
    password = input_password.get()
    if id and password:
        login_obj = Login(id, password)
        role = login_obj.user_config()
        if role:
            role_var.set(role)
            root.destroy()
            root.quit()
    else:
        print("Cannot leave any of the fields empty!")
        tkMessageBox.showinfo("Alert", "Cannot leave any of the fields empty!")

def login_screen():
    frame=customtkinter.CTkFrame(master=root)
    frame.pack(pady=20,padx=60,fill="both",expand=True)

    label= customtkinter.CTkLabel(master=frame, text="Login")
    label.pack( pady=12,padx=10)

    entry1=customtkinter.CTkEntry(master=frame , placeholder_text="ID" )
    entry1.pack(pady=12,padx=10)

    entry2=customtkinter.CTkEntry(master=frame , placeholder_text="Password" , show="*" )
    entry2.pack(pady=12,padx=10)

    checkbox=customtkinter.CTkCheckBox(master=frame,text="Remember Me")
    checkbox.pack(pady=12,padx=10)

    button=customtkinter.CTkButton ( master=frame, text="Login", command=lambda: login(entry1, entry2, checkbox))
    button.pack(pady=12,padx=10)

    root.mainloop()
    button_command = button.cget("command")
    return str(button_command.__name__)


def main():
    login_screen()
    role = role_var.get()
    return role

if __name__ == "__main__":
    role = main()
    print(f"Role: {role}")