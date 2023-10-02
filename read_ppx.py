import json
import os
import random
from bs4 import BeautifulSoup
import subprocess


def read_file_ppx(index_to_change=1, new_password="Test123"):
    with open("1.ppx", "r") as r:
        data = r.read()
        with open("1.xml", "w") as w:
            w.write(data)
            w.close()
            with open("1.xml", "r") as r_1:
                data_to_read = r_1.read()
                bs_data = BeautifulSoup(data_to_read, "xml")
                proxy_list_tag = bs_data.findAll("Proxy")
                proxy_tag = None
                for label in proxy_list_tag:
                    label_index = label.find("Label")
                    if label_index.string == str(index_to_change):
                        proxy_tag = label
                        break
                auth_tag = proxy_tag.find("Authentication")
                password_tag = auth_tag.find("Password")
                password_tag.string = new_password.replace("\n", "")
                print(password_tag)
                with open("1.xml", "w") as w_2:
                    w_2.write(str(bs_data))
                    w_2.close()
                    with open("1.xml", "r") as r_2:
                        data_to_ppx = r_2.read()
                        with open("1.ppx", "w") as w_3:
                            w_3.write(data_to_ppx)
                            w_3.close()
                            print("done")
                            r_2.close()
                            r_1.close()
                            r.close()
                            #subprocess.call("", shell=True)


def change_proxy(index_to_change=1, new_password="Test123"):
    f = open("config.json")

    config_data = json.load(f)["base_dir_proxy"]

    with open(config_data + "1.ppx", "r") as r:
        data = r.read()
        with open(config_data +"1.xml", "w") as w:
            w.write(data)
            w.close()
            with open(config_data +"1.xml", "r") as r_1:
                data_to_read = r_1.read()
                bs_data = BeautifulSoup(data_to_read, "xml")
                proxy_list_tag = bs_data.findAll("Proxy")
                proxy_tag = None
                for label in proxy_list_tag:
                    label_index = label.find("Label")
                    if label_index.string == str(index_to_change):
                        proxy_tag = label
                        break
                auth_tag = proxy_tag.find("Authentication")
                password_tag = auth_tag.find("Password")

                get_co = password_tag.string.split("-")[1][:2]
                get_co = str(get_co).upper()

                with open(get_co + ".txt", "r+") as rd:
                    read_proxys = rd.readlines()

                    pr = None
                    sort = random.randint(0, len(read_proxys))

                    for idx, line in enumerate(read_proxys):
                        if sort == idx:
                            pr = line
                            lines = read_proxys
                            del lines[idx]
                            rd.seek(0)
                            rd.truncate()
                            rd.writelines(lines)
                            break


                password_tag.string = pr.replace("\n", "")
                print(password_tag)
                with open(config_data + "1.xml", "w") as w_2:
                    w_2.write(str(bs_data))
                    w_2.close()
                    with open(config_data + "1.xml", "r") as r_2:
                        data_to_ppx = r_2.read()
                        with open(config_data + "1.ppx", "w") as w_3:
                            w_3.write(data_to_ppx)
                            w_3.close()
                            print("done")
                            r_2.close()
                            r_1.close()
                            r.close()
    os.system("start " + config_data + "1.ppx")


def return_proxy_by_idx(idx):
    with open("1.ppx", "r") as r:
        data = r.read()
        with open("1.xml", "w") as w:
            w.write(data)
            w.close()
            with open("1.xml", "r") as r_1:
                data_to_read = r_1.read()
                bs_data = BeautifulSoup(data_to_read, "xml")
                proxy_list_tag = bs_data.findAll("Proxy")
                proxy_tag = None
                for label in proxy_list_tag:
                    label_index = label.find("Label")
                    if label_index.string == str(idx):
                        proxy_tag = label
                        break
                auth_tag = proxy_tag.find("Authentication")
                password_tag = auth_tag.find("Password")
                return password_tag.string