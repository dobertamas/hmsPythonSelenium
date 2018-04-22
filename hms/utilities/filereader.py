import os
import json


class FileReader:

    @staticmethod
    def get_path():
        script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
        rel_path = "config.json"
        abs_file_path = os.path.join(script_dir, rel_path)
        return abs_file_path

    @staticmethod
    def get_username():
        abs_file_path = FileReader.get_path()
        with open(abs_file_path) as config_file:
            config = json.load(config_file)
            return config['LOCAL_TDOBER']['USERNAME']

    @staticmethod
    def get_password():
        with open(FileReader.get_path()) as config_file:
            config = json.load(config_file)
            return config['LOCAL_TDOBER']['PASSWORD']
