import datetime

import create_user_data
import diff_time
from tabulate import tabulate
from termcolor import colored  # Import the termcolor module for colored text
import json

import get_user_to_play
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

    The function reads log entries from "logs1.txt", calculates the time difference between each log entry's timestamp
    and the current time, and checks if any log entry falls within the last 10 minutes. It also counts the occurrences
    of log entries containing "kicked!" or "kicked". If the count of such entries is greater than 10, it suggests
    changing the account; otherwise, it indicates that the account is okay.

    Example Usage:
        read_logs()
    """

    dir_logs = None

    f = open("config.json")

    dir_logs = json.load(f)["base_dir_users_logs"]

    with open(dir_logs + "logs" + str(idx) + ".txt", "r") as r:
        lines = r.readlines()
        date_time_now = datetime.datetime.now()
        list_lasted_10_minutes = []

        # Iterate through log entries in reverse order
        for line in reversed(lines):
            date_end = line[0:19]
            dif = diff_time.diff_time_logs(date_end, date_time_now)
            if dif < 119407:  # 19407 seconds is approximately 5 hours and 23 minutes
                list_lasted_10_minutes.append(line)

        count_kicked = 0
        count_error = 0

        # Count occurrences of "kicked!" or "kicked" in recent log entries
        for item in list_lasted_10_minutes:
            if "kicked!" in item or "kicked" in item:
                count_kicked += 1

        for item in list_lasted_10_minutes:
            if "Client Error" in item or "Client Error!" in item:
                count_error += 1

        user_to_add = get_user_to_play.get_user_to_play()

        if count_kicked > 1000:
            print(colored("Need to change the account", "red"))
            print(colored(("Count of kicked: " + str(count_kicked)), "red"))
            read_ppx.change_proxy(idx, "")

            # TODO final system
            #if user_to_add is not None:
            #    password_proxy = user_to_add["password_proxy"]
            #    read_ppx.read_file_ppx(idx, password_proxy)
            #    with open(dir_logs + "logs" + str(idx) + "_test.txt", "w") as remove_logs:
            #        remove_logs.write("")
            #        remove_logs.close()
                #update_registry.check_if_error("slot" + str(idx))

        elif count_error > 0:
            print("Change proxy")
            read_ppx.change_proxy(idx, "")

        else:
            print("Account is okay")
