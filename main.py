# Project Description:
# This script is part of a larger project and is designed to run a game. It utilizes command-line arguments for
# configuration and interacts with other modules for reading configuration files and logs.

import argparse  # Import the argparse module for command-line argument parsing
import time
import winreg

import get_user_to_play
import read_file_cfg  # Import a module for reading configuration files
import read_logs_txt  # Import a module for reading log files
import read_ppx  # Import a module for reading ppx files
import update_registry


def run_game():
    """
    Placeholder function for running the game. Modify this function to implement the actual game logic.
    """
    print("Running game")


if __name__ == '__main__':

    # Create an argument parser for processing command-line arguments
    parser = argparse.ArgumentParser(
        prog='game_boot',  # Program name displayed in help messages
        description='Process some integers.',  # Description displayed in help messages
        epilog='Enjoy the program!')  # Epilog displayed in help messages

    # Define a command-line argument "--run" with choices "all" or "1"
    parser.add_argument("--run",
                        choices=["all", "1"],
                        help="Run the game",  # Help message for the argument
                        action="store",  # Store the argument value
                        default="--run",  # Default value if the argument is not provided
                        required=False)  # Argument is not required

    # Parse the command-line arguments
    args = parser.parse_args()

    # Print the value of the "--run" argument
    print(args.run)

    # Call functions from other modules to read configuration files and logs
    #read_file_cfg.read_file_cfg()  # Function for reading configuration files
    #read_logs_txt.read_logs()  # Function for reading log files
    #read_ppx.read_file_ppx()  # Function for reading ppx files

    while True:
        for item in range(1, 60):
            #verify_contains_error = update_registry.check_if_error("slot" + str(item))
            #if verify_contains_error == "1":
            #    print("Change a proxy and play")
            #    user = get_user_to_play.get_user_to_play()
            #    read_ppx.read_file_ppx(item, user["password_proxy"])
            print("CHANGE SLOT " + str(item))
            read_logs_txt.read_logs(item)
        time.sleep(10)
