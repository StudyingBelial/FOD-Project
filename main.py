import customtkinter
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import tkinter.filedialog as tkFileDialog
import tkinter.font as tkFont

import login
import admin_options
import password
import grades
import student_dashboard
import eca

def main():
    role = str(login.main())
    print(f"Logged in as: {role}")
    role = "Admin"
    if role == "Admin":
        admin_options.main()
    elif role == "Student" or role == "Teacher":
        student_dashboard.main()
    else:
        print("User Data Error! Please Try Again Later")

if __name__ == "__main__":
    main()