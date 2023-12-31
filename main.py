# Project Description:
# This script is part of a larger project and is designed to run a game. It utilizes command-line arguments for
# configuration and interacts with other modules for reading configuration files and logs.

import argparse  # Import the argparse module for command-line argument parsing
import datetime
import time
import winreg

import accounts_manager
import add_start_process
import add_time_start
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
    init_day = False

    while True:
        dt = datetime.datetime.now()
        for item in range(1, 31):
            if dt.hour < 21:
                print("execute slot " + str(item))
                read_logs_txt.read_logs(item)
            else:
                print("Stop at 1am")
            if init_day is True and dt.hour == 1:
                init_day = True
                accounts_manager.init_day()
                add_start_process.start_init_process()
            if dt.hour == 2:
                init_day = False
            time.sleep(60)
