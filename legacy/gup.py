import customtkinter
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import tkinter.filedialog as tkFileDialog
import tkinter.font as tkFont

customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('green')

root=customtkinter.CTk()
root.title("Student LogIn System")
root.geometry("400x350")
root.resizable(1000, 750)

def login(id, password, remember):
    print(id, password, remember)

frame=customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=60,fill="both",expand=True)

label= customtkinter.CTkLabel(master=frame, text="Login")
label.pack( pady=12,padx=10)

entry1=customtkinter.CTkEntry(master=frame , placeholder_text="ID" )
id = entry1.pack(pady=12,padx=10)

entry2=customtkinter.CTkEntry(master=frame , placeholder_text="Password" , show="*" )
password = entry2.pack(pady=12,padx=10)

checkbox=customtkinter.CTkCheckBox(master=frame,text="Remember Me")
remember = checkbox.pack(pady=12,padx=10)

button=customtkinter.CTkButton ( master=frame, text="Login", command=lambda: login(id, password, remember))
button.pack(pady=12,padx=10)

root.mainloop()

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