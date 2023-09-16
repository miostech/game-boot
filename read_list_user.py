#  lets read a file .txt where contais one list with users and passwords, and split by "|" and save in a list
#  and after that, we will read a file .txt where contais one list with users and passwords, and split by "|" and save in a list
import update_registry
import create_user_data
import read_ppx


def read_file_txt():
    with open("gerAccounts (2).txt", "r") as r:
        lines = r.readlines()
        lines = lines[0:60]
        for idx, line in enumerate(lines):
            line = line.split("|")
            print("-------------")
            print("email", line[3])
            print("password", line[4])
            print("account", line[5])
            print("proxy", line[17])
            print("last_auth", line[18])
            print("first_run", line[19])
            print("-------------")
            create_user_data.create_user(str(idx + 1), line[3], line[4], line[5], line[19])
            update_registry.update_values(("slot" + str(idx + 1)), line[18], line[19])
            read_ppx.read_file_ppx(str(idx + 1), line[17])
            break


read_file_txt()

