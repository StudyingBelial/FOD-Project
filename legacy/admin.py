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

# Adding a label for the admin options
label = customtkinter.CTkLabel(root, text="What would you like to do?", font=('Helvetica', 14))
label.pack(pady=20)

# Creating buttons for admin actions
button1 = customtkinter.CTkButton(root, text="Add New User", command=lambda: perform_action(1))
button1.pack(pady=10)
button2 = customtkinter.CTkButton(root, text="Import Database", command=lambda: perform_action(2))
button2.pack(pady=10)
button3 = customtkinter.CTkButton(root, text="Edit User Details", command=lambda: perform_action(3))
button3.pack(pady=10)
button4 = customtkinter.CTkButton(root, text="Edit Student Grades", command=lambda: perform_action(4))
button4.pack(pady=10)
button5 = customtkinter.CTkButton(root, text="Analytics", command=lambda: perform_action(5))
button5.pack(pady=10)

# Run the main loop
root.mainloop()