class FileReader:

    @staticmethod
    def get_username():
        my_file = open("/Users/tamasdober/Documents/maszek/hmsPythonSelenium/hms/tests/test_data.txt", "r")
        username = my_file.readline()
        my_file.close()
        return username

    @staticmethod
    def get_password():
        my_file = open("/Users/tamasdober/Documents/maszek/hmsPythonSelenium/hms/tests/test_data.txt", "r")
        my_file.readline()
        password = my_file.readline()
        my_file.close()
        return password
