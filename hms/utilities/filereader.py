class FileReader():

    def get_username(self):
        my_file = open("/Users/tamasdober/Documents/maszek/hmsPythonSelenium/hms/tests/test_data.txt", "r")
        username = my_file.readline()
        my_file.close()
        return username

    def get_password(self):
        my_file = open("/Users/tamasdober/Documents/maszek/hmsPythonSelenium/hms/tests/test_data.txt", "r")
        my_file.readline()
        password = my_file.readline()
        my_file.close()
        return password
