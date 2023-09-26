import winreg
from winreg import *
import os


def update_values(slot, last_auth, first_char, is_alert="0"):
    directory = os.path.join(r'SOFTWARE\WOW6432Node\SageUserData\slot_run_states', slot)
    key = OpenKey(HKEY_LOCAL_MACHINE, directory, 0,
                  KEY_SET_VALUE)
    #SetValueEx(key, "is_alert", 1, REG_SZ, is_alert)
    SetValueEx(key, "last_auth", 1, REG_SZ, last_auth)
    SetValueEx(key, "first_char", 1, REG_SZ, first_char)


def check_if_error(slot):
    directory = os.path.join(r'SOFTWARE\WOW6432Node\SageUserData\slot_run_states', slot)
    key = OpenKey(HKEY_LOCAL_MACHINE, directory, 0,
                  KEY_READ)
    response = winreg.QueryValueEx(key, 'is_alert')
    print("here")
    print(response[0])
    return response[0]
