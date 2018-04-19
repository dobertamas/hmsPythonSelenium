import os


class FileReader:

    @staticmethod
    def get_path():
        script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
        rel_path = "../tests/test_data.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        return abs_file_path

    @staticmethod
    def get_username():
        # my_file = open(abs_file_path, "r")
        abs_file_path = FileReader.get_path()
        with open(abs_file_path) as my_file:
            username = my_file.readline()
            return username

    @staticmethod
    def get_password():
        # my_file = open("/Users/tamasdober/Documents/maszek/hmsPythonSelenium/hms/tests/test_data.txt", "r")
        with open(FileReader.get_path()) as my_file:
            my_file.readline()
            password = my_file.readline()
            return password
