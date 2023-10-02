# Script Description:
# This script reads and manipulates configuration data from a JSON file ("config.json") and a configuration file
# ("user_slot_data1.cfg"). It updates the "mail" value in the configuration file and prints the updated configuration.

import json  # Import the json module for working with JSON files
import os  # Import the os module for file path manipulation
import tabulate  # Import to tabulate module for pretty printing
from termcolor import colored  # Import the termcolor module for colored text


def read_file_cfg():
    """
    Read and manipulate configuration data from files.

    This function performs the following tasks:
    1. Reads configuration data from a JSON file ("config.json").
    2. Constructs a file path based on the JSON data.
    3. Reads configuration settings from a configuration file ("user_slot_data1.cfg").
    4. Prints the "mail" setting from the configuration file.
    5. Updates the "mail" setting in the configuration file.
    6. Prints the updated configuration.

    Example Usage:
        read_file_cfg()
    """

    # Step 1: Read configuration data from "config.json"
    with open("config.json", "r") as r:
        data = json.load(r)
        base_dir = data["base_dir_files_user_slot"]

    # Step 2: Construct a file path based on the JSON data
    dir_file = os.path.join(base_dir, "user_slot_data1.cfg")

    # Step 3: Read configuration settings from "user_slot_data1.cfg"
    config_data = {}
    with open("user_slot_data1.cfg", 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=')
                config_data[key.strip()] = value.strip()

    # Step 3: Print the "mail" setting from the configuration file
    print("Current 'mail' setting:", config_data["mail"])

    # Step 4: Print the configuration as table
    print("Current configuration:")
    data_list = [config_data]
    table = tabulate.tabulate(data_list, headers="keys", tablefmt="grid")
    print(colored(table, "blue"))

    # Step 5: Update the "mail" and "pass" and "account" setting in the configuration file

    with open("accounts_logs.json", "r") as r:
        data = json.loads(r.read())
        data = data["account_1"]
        config_data["mail"] = data["email"]
        config_data["pass"] = data["password"]
        config_data["account"] = data["account"]

    # Step 6: Update the "mail" setting in the configuration file
    with open("user_slot_data1.cfg", 'w') as file:
        print("Updating 'mail' setting...")
        print("New 'mail' setting:", config_data["mail"])
        for key, value in config_data.items():
            file.write('%s=%s\n' % (key, value))

    # Step 6: Print the updated configuration
    print("Updated configuration:")
    data_list_new = [config_data]
    table = tabulate.tabulate(data_list_new, headers="keys", tablefmt="grid")
    print(colored(table, "green"))


def return_user_slot(idx):
    f = open("config.json", "r")
    fj_config = json.load(f)
    base_dir = fj_config["base_dir_files_user_slot"]
    dir_file = os.path.join(base_dir, "user_slot_data" + str(idx) + ".cfg")
    user_data = {}

    with open(dir_file, "r") as user:
        for line in user:
            if '=' in line:
                key, value = line.strip().split('=')
                user_data[key.strip()] = value.strip()
    print(user_data["mail"])
    return user_data["mail"]


def update_user_slot(idx, user):
    f = open("config.json", "r")
    fj_config = json.load(f)
    base_dir = fj_config["base_dir_files_user_slot"]
    dir_file = os.path.join(base_dir, "user_slot_data" + str(idx) + ".cfg")

    config_data = {}

    with open(dir_file, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=')
                config_data[key.strip()] = value.strip()

    config_data["mail"] = user["email"]
    config_data["pass"] = user["password"]
    config_data["account"] = user["account"]
    with open(dir_file, 'w') as file:
        print("Updating 'mail' setting...")
        print("New 'mail' setting:", config_data["mail"])
        for key, value in config_data.items():
            file.write('%s=%s\n' % (key, value))


def return_all_info_user_slot(idx):
    f = open("config.json", "r")
    fj_config = json.load(f)
    base_dir = fj_config["base_dir_files_user_slot"]
    dir_file = os.path.join(base_dir, "user_slot_data" + str(idx) + ".cfg")
    user_data = {}

    with open(dir_file, "r") as user:
        for line in user:
            if '=' in line:
                key, value = line.strip().split('=')
                user_data[key.strip()] = value.strip()
    print(user_data["mail"])
    return user_data