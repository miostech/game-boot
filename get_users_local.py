import read_file_cfg
import read_ppx
import update_registry
import json

def get_users():
    config_users = []
    id = 1
    for item in range(1, 61):
        try:
            print(item)
            info_slot = read_file_cfg.return_all_info_user_slot(item)

            info_last, info_first = update_registry.return_last_auth_and_first_char("slot" + str(item))

            info_proxy = read_ppx.return_proxy_by_idx(item)
            print(info_slot)
            print(info_last)
            print(info_first)
            print(info_proxy)
            if info_slot["mail"] is not None or info_slot["mail"] != "":
                config_users.append({
                    "id": 0,
                    "used": 0,
                    "email": info_slot["mail"],
                    "password": info_slot["pass"],
                    "account": info_slot["account"],
                    "server": 6,
                    "first_char": info_first[0],
                    "last_auth": info_last[0],
                    "password_proxy": info_proxy,
                    "logs": [],
                    "total_cor": 0
                })
        except Exception as ex:
            print(ex)
    data_save = json.dumps(config_users, indent=4)

    with open("accounts_logs.json", "w") as r:
        r.write(data_save)
        r.close()


get_users()