class verify:
    @staticmethod
    def is_admin(id):
        runner = true
        with open("users.txt", 'r') as file:
            while (runner):
                read_id = file.readline()
                read_name = file.readline()
                read_number = file.readline()
                read_user = file.readline()
                if (id == read_id and read_user == "admin"):
                    print(f"WELCOME {read_name}. Here is your admin controls")