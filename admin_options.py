import customtkinter as ctk
import tkinter as tk
from tkinter import StringVar
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import eca
import grades
import users
import password
import visualizers

import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import tkinter.filedialog as tkFileDialog
import tkinter.font as tkFont

def perform_action(action_number):
    if action_number == 1:
        Add.new_user()
    elif action_number == 3:
        Edit.edit_menu()
    elif action_number == 4:
        Edit.edit_grades()
    elif action_number == 5:
        visualizers.visualisers()

def admin_options():
    customtkinter.set_appearance_mode('System')
    customtkinter.set_default_color_theme('blue')

    root = customtkinter.CTk()
    root.title("Student LogIn System")
    root.geometry("400x350")
    root.resizable(False, False)
    command_var = StringVar()

    label = customtkinter.CTkLabel(root, text="What would you like to do?", font=('Helvetica', 14))
    label.pack(pady=20)
    button1 = customtkinter.CTkButton(root, text="Add New User", command=lambda: perform_action(1))
    button1.pack(pady=10)
    button3 = customtkinter.CTkButton(root, text="Edit User Details", command=lambda: perform_action(3))
    button3.pack(pady=10)
    button4 = customtkinter.CTkButton(root, text="Edit Student Grades", command=lambda: perform_action(4))
    button4.pack(pady=10)
    button5 = customtkinter.CTkButton(root, text="Analytics", command=lambda: perform_action(5))
    button5.pack(pady=10)

    root.mainloop()
    root.destroy()

class Edit:
    @staticmethod
    def edit_grades():
        def submit_form():
            id = entry_name.get()
            subject = activity_var.get()
            new_data = Edit.custom_change("Grades")
            obj_grades = grades.Grades()
            obj_grades.edit_student_grades(id, subject, new_data)
        
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")

        root = customtkinter.CTk()
        root.title("Student ECA Activities Submission Form")

        label_name = customtkinter.CTkLabel(master=root, text="Student ID:")
        label_name.grid(row=0, column=0, padx=20, pady=10)
        entry_name = customtkinter.CTkEntry(master=root, width=200)
        entry_name.grid(row=0, column=1, padx=20, pady=10)

        label_activities = customtkinter.CTkLabel(master=root, text="Select Activity:")
        label_activities.grid(row=2, column=0, padx=20, pady=10)

        activity_var = customtkinter.StringVar(value="Select an activity")

        dropdown_activities = customtkinter.CTkOptionMenu(
            master=root, 
            variable=activity_var,
            values=["Select an activity", "FOD", "FOM", "IT", "English", "Maths"]
        )
        dropdown_activities.grid(row=2, column=1, padx=20, pady=10)

        button_submit = customtkinter.CTkButton(master=root, text="Submit", command=submit_form)
        button_submit.grid(row=3, column=0, columnspan=2, pady=20)

        root.mainloop()

    @staticmethod
    def edit_menu():
        customtkinter.set_appearance_mode('System')
        customtkinter.set_default_color_theme('blue')

        root = customtkinter.CTk()
        root.title("Student LogIn System")
        root.geometry("400x350")
        root.resizable(1000, 750)

        def on_submit():
            id = student_id_entry.get()
            selected_option = option_menu.get()
            print(f"User ID: {id}, Selected Option: {selected_option}")
            obj_users = users.Users()
            if selected_option == "Email":
                new = Edit.custom_change("Email")
                obj_users.access_user_details(id, "email")
            elif selected_option == "Role":
                new = Edit.custom_change("Role")
                obj_users.access_user_details(id, "role")
            elif selected_option == "City":
                new = Edit.custom_change("City")
                obj_users.access_user_details(id, "city")
            elif selected_option == "Password":
                Edit.pass_change(id)
        
        student_id_label = customtkinter.CTkLabel(root, text="Student ID:")
        student_id_label.pack(pady=10)

        student_id_entry = customtkinter.CTkEntry(root)
        student_id_entry.pack(pady=10)

        student_id_label = customtkinter.CTkLabel(root, text="Choose a given option to make changes:")
        student_id_label.pack(pady=10)

        options = ["Email", "Role", "City", "Password"]
        option_menu = customtkinter.CTkOptionMenu(root, values=options)
        option_menu.pack(pady=10)

        submit_button = customtkinter.CTkButton(root, text="Submit", command=on_submit)
        submit_button.pack(pady=20)

        root.mainloop()

    @staticmethod
    def custom_change(field):
        customtkinter.set_appearance_mode('System')
        customtkinter.set_default_color_theme('green')
        root = customtkinter.CTk()
        root.title("Change " + field)
        root.geometry("400x350")
        root.resizable(1000, 750)

        def on_confirm():
            new_email = email_entry.get()
            print(f"New {field}: {new_email}")
            result_label.configure(text=field + " Confirmed", fg="green")
            return new_email

        email_label = customtkinter.CTkLabel(master=root, text="New Email ID:")
        email_label.pack(pady=10)

        email_entry = customtkinter.CTkEntry(master=root)
        email_entry.pack(pady=10)

        confirm_button = customtkinter.CTkButton(root, text="Confirm", command=on_confirm)
        confirm_button.pack(pady=20)

        result_label = customtkinter.CTkLabel(root, text="")
        result_label.pack(pady=10)

        root.mainloop()

    @staticmethod
    def pass_change(id):
        customtkinter.set_appearance_mode('System')
        customtkinter.set_default_color_theme('green')

        root = customtkinter.CTk()
        root.title("Student LogIn System")
        root.geometry("600x450")
        root.resizable(1000, 750)

        def on_submit():
            new_password = new_password_entry.get()
            confirm_password = confirm_password_entry.get()
            obj_password = password.Self_Password()
            obj_password.change_password_verify(id, new_password, confirm_password)
            
        new_password_label = customtkinter.CTkLabel(root, text="New Password:")
        new_password_label.pack(pady=10)

        new_password_entry = customtkinter.CTkEntry(root, show="*")
        new_password_entry.pack(pady=10)

        confirm_password_label = customtkinter.CTkLabel(root, text="Confirm Password:")
        confirm_password_label.pack(pady=10)

        confirm_password_entry = customtkinter.CTkEntry(root, show="*")
        confirm_password_entry.pack(pady=10)

        submit_button = customtkinter.CTkButton(root, text="Submit", command=on_submit)
        submit_button.pack(pady=20)

        result_label = customtkinter.CTkLabel(root, text="")
        result_label.pack(pady=10)

        root.mainloop()

class Add:
    @staticmethod
    def new_user_grades(id):
        def submit_marks():
            fod = entry_fod.get()
            fom = entry_fom.get()
            it = entry_it.get()
            english = entry_english.get()
            maths = entry_maths.get()

            print("FOD marks:", fod)
            print("FOM marks:", fom)
            print("IT marks:", it)
            print("English marks:", english)
            print("Maths marks:", maths)

            obj_grades = grades.Grades.add_student_grades(id, fod, fom, it, english, maths)
            root.destroy()
            root.quit()

        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")

        root = customtkinter.CTk()
        root.title("Admin Marks Submission Form")

        label_fod = customtkinter.CTkLabel(master=root, text="FOD Marks:")
        label_fod.grid(row=1, column=0, padx=20, pady=10)
        entry_fod = customtkinter.CTkEntry(master=root, width=200)
        entry_fod.grid(row=1, column=1, padx=20, pady=10)

        label_fom = customtkinter.CTkLabel(master=root, text="FOM Marks:")
        label_fom.grid(row=2, column=0, padx=20, pady=10)
        entry_fom = customtkinter.CTkEntry(master=root, width=200)
        entry_fom.grid(row=2, column=1, padx=20, pady=10)

        label_it = customtkinter.CTkLabel(master=root, text="IT Marks:")
        label_it.grid(row=3, column=0, padx=20, pady=10)
        entry_it = customtkinter.CTkEntry(master=root, width=200)
        entry_it.grid(row=3, column=1, padx=20, pady=10)

        label_english = customtkinter.CTkLabel(master=root, text="English Marks:")
        label_english.grid(row=4, column=0, padx=20, pady=10)
        entry_english = customtkinter.CTkEntry(master=root, width=200)
        entry_english.grid(row=4, column=1, padx=20, pady=10)

        label_maths = customtkinter.CTkLabel(master=root, text="Maths Marks:")
        label_maths.grid(row=5, column=0, padx=20, pady=10)
        entry_maths = customtkinter.CTkEntry(master=root, width=200)
        entry_maths.grid(row=5, column=1, padx=20, pady=10)

        button_submit = customtkinter.CTkButton(master=root, text="Submit", command=submit_marks)
        button_submit.grid(row=6, column=0, columnspan=2, pady=20)

        root.mainloop()

    @staticmethod
    def new_user():
        def submit_form():
            first_name_value = first_name.get()
            last_name_value = last_name.get()
            email_value = email.get()
            role_value = role.get()
            city_value = city.get()

            print("First Name:", first_name_value)
            print("Last Name:", last_name_value)
            print("Email:", email_value)
            print("Role:", role_value)
            print("City:", city_value)

            obj_users = users.Users()
            id = obj_users.input_new_user(first_name_value, last_name_value, email_value, role_value, city_value)
            if role_value == "Student":
                Add.new_user_grades(id)
            root.destroy()
            root.quit()

        customtkinter.set_appearance_mode('System')
        customtkinter.set_default_color_theme('green')

        root = customtkinter.CTk()
        root.title("System (ADMIN)")
        root.geometry("500x350")
        root.resizable(1000, 750)

        def create_form_entry(label_text, row):
            label = customtkinter.CTkLabel(root, text=label_text)
            label.grid(row=row, column=0, padx=10, pady=5)

            entry = customtkinter.CTkEntry(root)
            entry.grid(row=row, column=1, padx=10, pady=5)
            return entry

        first_name = create_form_entry("First Name", 0)
        last_name = create_form_entry("Last Name", 1)
        email = create_form_entry("Email", 2)
        role = create_form_entry("Role", 3)
        city = create_form_entry("City", 4)

        submit_button = customtkinter.CTkButton(root, text="Submit", command=submit_form)
        submit_button.grid(row=5, column=0, columnspan=2, pady=20)

        root.mainloop()

def main():
    admin_options()

if __name__ == "__main__":
    main()
