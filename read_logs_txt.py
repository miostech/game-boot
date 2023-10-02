import datetime
import winreg

import accounts_manager
import add_start_process
import create_user_data
import diff_time
from tabulate import tabulate
from termcolor import colored  # Import the termcolor module for colored text
import json

import get_user_to_play
import read_file_cfg
import read_ppx
import update_registry


def custom_format_table(data):
    """
    Custom function to format and print a table using to tabulate library.

    Args:
        data (list of lists): The data to be displayed in the table.

    Example Usage:
        custom_format_table(data)
    """

    print(tabulate(data, headers="firstrow", tablefmt="grid"))


def read_logs(idx):
    """
    Reads log entries from a log file and analyzes them.

    The function reads log entries from "slot_log_1.txt", calculates the time difference between each log entry's timestamp
    and the current time, and checks if any log entry falls within the last 10 minutes. It also counts the occurrences
    of log entries containing "kicked!" or "kicked". If the count of such entries is greater than 10, it suggests
    changing the account; otherwise, it indicates that the account is okay.

    Example Usage:
        read_logs()
    """

    dir_logs = None

    f = open("config.json")

    dir_logs = json.load(f)

    dir_logs = dir_logs["base_dir_users_logs"]

    with open(dir_logs + "slot_log_" + str(idx) + ".txt", "r") as r:
        lines = r.readlines()
        date_time_now = datetime.datetime.now()
        list_lasted_10_minutes = []
        list_lasted_30_minutes = []

        # Iterate through log entries in reverse order
        for line in reversed(lines):
            date_end = line[0:19]
            dif = diff_time.diff_time_logs(date_end, date_time_now)
            if dif < 30:  # 19407 seconds is approximately 5 hours and 23 minutes
                list_lasted_30_minutes.append(line)
            if dif < 10:
                list_lasted_10_minutes(line)

        count_kicked = 0
        count_error = 0
        count_client_start = 0
        count_client_ban = 0
        count_done = 0

        # Count occurrences of "kicked!" or "kicked" in recent log entries
        for item in list_lasted_30_minutes:
            if "kicked!" in item or "kicked" in item:
                count_kicked += 1
            if "Client started!" in item or "Client started" in item:
                count_client_start += 1

        for item in list_lasted_10_minutes:
            if "Client Error" in item or "Client Error!" in item:
                count_error += 1

        for item in lines:
            if "Account Banned!" in item or "Account Banned" in item:
                count_client_ban += 1

        for item in lines:
            if "Alchemist quest done! Exitting.." in item or "Alchemist quest done Exitting.." in item:
                count_done += 1

        #user_to_add = get_user_to_play.get_user_to_play()

        if count_kicked > 10:
            print(colored("Need to change the account", "red"))
            print(colored(("Count of kicked: " + str(count_kicked)), "red"))
            read_ppx.change_proxy(idx, "")

        elif count_error > 0:
            print("Change proxy")
            read_ppx.change_proxy(idx, "")
            with open(dir_logs + "slot_log_" + str(idx) + ".txt", "w") as w:
                w.write("")
                w.close()
            add_start_process.start_process(idx)

        elif count_client_start > 1:
            print("Change proxy cause client start error")
            read_ppx.change_proxy(idx, "")

        elif count_client_ban > 0:
            email_user_to_ban = read_file_cfg.return_user_slot(idx)

            accounts_manager.account_ban(email_user_to_ban)

            user = get_user_to_play.get_user_to_play()

            read_file_cfg.update_user_slot(idx, user)

            read_ppx.change_proxy(idx, user["password_proxy"])

            update_registry.update_values("slot" + str(idx), user["last_auth"], user["first_char"])

            accounts_manager.account_run(user["email"])

            add_start_process.start_process(idx)

        elif count_done > 0:
            email_user_to_done = read_file_cfg.return_user_slot(idx)

            accounts_manager.account_done(email_user_to_done)

            user = get_user_to_play.get_user_to_play()

            read_file_cfg.update_user_slot(idx, user)

            read_ppx.change_proxy(idx, user["password_proxy"])

            update_registry.update_values("slot" + str(idx), user["last_auth"], user["first_char"])

            accounts_manager.account_run(user["email"])

            add_start_process.start_process(idx)
        else:
            print("Account is okay")


def read_logs_2(idx):
    """
    Reads log entries from a log file and analyzes them.

    The function reads log entries from "slot_log_1.txt", calculates the time difference between each log entry's timestamp
    and the current time, and checks if any log entry falls within the last 10 minutes. It also counts the occurrences
    of log entries containing "kicked!" or "kicked". If the count of such entries is greater than 10, it suggests
    changing the account; otherwise, it indicates that the account is okay.

    Example Usage:
        read_logs()
    """

    dir_logs = None

    f = open("config.json")

    dir_logs = json.load(f)

    dir_logs = dir_logs["base_dir_users_logs"]

    with open(dir_logs + "slot_log_" + str(idx) + ".txt", "r") as r:
        lines = r.readlines()
        date_time_now = datetime.datetime.now()
        list_lasted_10_minutes = []
        list_lasted_30_minutes = []

        # Iterate through log entries in reverse order
        for line in reversed(lines):
            date_end = line[0:19]
            dif = diff_time.diff_time_logs(date_end, date_time_now)
            if dif < 30:  # 19407 seconds is approximately 5 hours and 23 minutes
                list_lasted_30_minutes.append(line)
            if dif < 10:
                list_lasted_10_minutes.append(line)

        count_kicked = 0
        count_error = 0
        count_client_start = 0
        count_client_ban = 0

        # Count occurrences of "kicked!" or "kicked" in recent log entries
        for item in list_lasted_30_minutes:
            if "kicked!" in item or "kicked" in item:
                count_kicked += 1
            if "Client started!" in item or "Client started" in item:
                count_client_start += 1

        for item in list_lasted_10_minutes:
            if "Client Error" in item or "Client Error!" in item:
                count_error += 1

        for item in lines:
            if "Account Banned!" in item or "Account Banned" in item:
                count_client_ban += 1

        #user_to_add = get_user_to_play.get_user_to_play()

        if count_kicked > 10:
            print(colored("Need to change the account", "red"))
            print(colored(("Count of kicked: " + str(count_kicked)), "red"))
            read_ppx.change_proxy(idx, "")
            with open(dir_logs + "slot_log_" + str(idx) + ".txt", "w") as w:
                w.write("")
                w.close()

        elif count_error > 0:
            print("Change proxy")
            read_ppx.change_proxy(idx, "")
            with open(dir_logs + "slot_log_" + str(idx) + ".txt", "w") as w:
                w.write("")
                w.close()
            add_start_process.start_process(idx)

        elif count_client_start > 1:
            print("Change proxy cause client start error")
            read_ppx.change_proxy(idx, "")
            with open(dir_logs + "slot_log_" + str(idx) + ".txt", "w") as w:
                w.write("")
                w.close()

        else:
            print("Account is okay")