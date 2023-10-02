import json


def account_ban(email):
    f = open("accounts_logs.json")
    fj = json.load(f)

    for item in fj:
        if item["email"] == email:
            item["used"] = 3
            break

    with open("accounts_logs.json", "w") as file:
        json.dump(fj, file)


def account_done(email):
    f = open("accounts_logs.json")
    fj = json.load(f)

    for item in fj:
        if item["email"] == email:
            item["used"] = 2
            break

    with open("accounts_logs.json", "w") as file:
        json.dump(fj, file)


def account_run(email):
    f = open("accounts_logs.json")
    fj = json.load(f)

    for item in fj:
        if item["email"] == email:
            item["used"] = 1
            break

    with open("accounts_logs.json", "w") as file:
        json.dump(fj, file)


def init_day():
    f = open("accounts_logs.json")
    fj = json.load(f)

    for item in fj:
        if item["used"] == 2:
            item["used"] = 0
            break

    with open("accounts_logs.json", "w") as file:
        json.dump(fj, file)
