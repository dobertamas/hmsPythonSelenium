class File_Reader():

    def get_username(self):
        my_file = open("test_data.txt", "r")
        username = my_file.readline()
        print(username)
        my_file.close()
        return username

    def get_password(self):
        my_file = open("test_data.txt", "r")
        my_file.readline()
        password = my_file.readline()
        print(password)
        my_file.close()
        return password
