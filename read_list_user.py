#  lets read a file .txt where contais one list with users and passwords, and split by "|" and save in a list
#  and after that, we will read a file .txt where contais one list with users and passwords, and split by "|" and save in a list


def read_file_txt():
    with open("gerAccounts (2).txt", "r") as r:
        lines = r.readlines()
        lines = lines[0:60]
        for line in lines:
            line = line.split("|")
            print("-------------")
            print("email", line[3])
            print("password", line[4])
            print("account", line[5])
            print("proxy", line[17])
            print("last_auth", line[18])
            print("first_run", line[19])
            print("-------------")


read_file_txt()

