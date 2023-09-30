import datetime
import json


def start_process(idx):
    f = open("config.json")
    fj = json.load(f)
    base_dir = fj["base_dir_start_process"]
    with open(base_dir + "StartStopMgr.cfg", "w") as file:
        now = datetime.datetime.now()
        file.writelines("start:{0}:{1}:{2}".format(idx, now.hour, now.minute))
        file.close()


def start_init_process():
    f = open("config.json")
    fj = json.load(f)
    base_dir = fj["base_dir_start_process"]
    with open(base_dir + "StartStopMgr.cfg", "w") as file:
        now = datetime.datetime.now()
        for idx in range(1, 31):
            file.writelines("start:{0}:{1}:{2} \n".format(idx, now.hour, now.minute + idx))
        file.close()
