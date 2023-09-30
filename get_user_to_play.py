import json


def get_user_to_play():

    f = open("config.json")

    data = json.load(f)["base_dir_users_logs"]

    print(data)

    users = open("accounts_logs.json")

    data_users = json.load(users)

    print(data_users)

    for item in data_users:
        if item["used"] == 0:
            return item
    return None
