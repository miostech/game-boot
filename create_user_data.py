import json


def create_user(slot, email, password, account, first_char):
    user_data = "user_slot_data" + str(slot)
    f = open("config.json")

    fj = json.load(f)["base_dir_files_user_slot"]

    with open(fj + user_data + ".cfg", "w") as w:
        w.write("mail=" + email + "\n")
        w.write("pass=" + password + "\n")
        w.write("account=" + account + "\n")
        w.write("region=" + "5" + "\n")
        w.write("server=" + "0" + "\n")
        w.write("channel=" + "0" + "\n")
        w.write("char=" + "\n")
        w.write("chr_names=-,,,," + "\n")
        w.write("settings=1" + "\n")
        w.write("last_ch=0" + "\n")
        w.write("last_player=" + first_char + "\n")
        w.write("use_2fa=0" + "\n")
        w.close()
