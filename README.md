Application Management Script
Overview
This Python script is a simple command-line interface application for managing user options. It provides functionality for logging into a system, changing directories, listing files, and running scripts. It also includes a welcome message and a thank you message when exiting.

Features
Display Patterns: Prints a vertical 'N' pattern within a centered box.
Welcome Messages: Displays welcome messages for different modes (DBSERVER and APPSERVER).
Option Handling: Allows users to choose between logging into a system, changing directories, listing files, running a toolkit, or exiting the application.
Error Handling: Displays an error message for invalid options.
Functions
print_vertical_nn_centered_box_pattern(): Prints a vertical 'N' pattern centered inside a box.
print_welcome(): Displays a decorative welcome message.
print_welcome_message(): Displays a welcome message specifically for DBSERVER.
print_appserver_welcome_message(): Displays a welcome message specifically for APPSERVER.
print_thank_you_message(): Displays a thank you message when exiting the application.
print_invalid_option_message(): Displays a message when an invalid option is selected.
handle_option(): Handles user options for logging in, changing directories, listing files, running toolkits, and exiting.
main(): Entry point of the script, displaying the initial menu and calling appropriate functions based on user selection.
Usage
Run the Script: Execute the script using Python 3.x.
python script_name.py
Select Options: Follow the on-screen prompts to choose between available options:

1. DBSERVER: Displays the DBSERVER welcome message and presents additional options.
2. APPSERVER: Displays the APPSERVER welcome message and presents additional options.
3. Exit: Displays a thank you message and exits the application.
Available Options:

1. Login on Algomox: Attempts to switch user to 'algomox'.
2. Change Directory: Changes the current working directory to the user's home directory.
3. List out the files: Lists files in the current directory.
4. Run the files: Executes a specified toolkit file.
5. Exit: Exits the application.
Dependencies
Python 3.x: Ensure Python 3.x is installed on your system.
Notes
Permissions: The script uses subprocess.run(['su', 'algomox']) to switch users, which may require appropriate permissions.
Toolkit Execution: Ensure the toolkit file has execute permissions and is located in the correct directory.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Contributions and improvements are welcome. Please submit issues or pull requests on the GitHub repository.
