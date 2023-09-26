import json


def add_time_start():
    f = open("config.json")

    data_dir = json.load(f)["base_dir_files_user_slot"]
