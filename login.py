from admin_dashboard import verify
from student_dashboard import verify

id = input("User ID: ")
password = input("Password: ") #REQUIRES EXCEPTION HANDELLING

with open("passwords.txt", 'r') as password_file:
    for i in range(len(password_file)):
        read_id = password_file.readline()
        read_password = password_file.readline()
        if (id == read_id and password == read_password):
            verify.is_admin(id)
            verify.is_student(id)
        else:
            print("Invalid ID or Passoword!")