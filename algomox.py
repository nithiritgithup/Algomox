import os
import subprocess


def print_vertical_nn_centered_box_pattern():
    n_pattern = []

    for row in range(7):
        line = ""
        for column in range(7):
            if column == 0 or column == 6 or column == row:
                line += "*"
            else:
                line += " "
        n_pattern.append(line)

    box_width = len(n_pattern[0]) * 2 + 4
    box_height = len(n_pattern) + 2

    padding = (box_width - len(n_pattern[0]) * 2 - 2) // 2

    print('+' + '-' * (box_width - 2) + '+')

    for i in range(len(n_pattern)):
        print('|' + ' ' * padding + n_pattern[i] + ' ' + n_pattern[i] + ' ' * padding + '|')

    print('+' + '-' * (box_width - 2) + '+')


def print_welcome():
    print("\n" + "*" * 80)
    print("*" + " " * 78 + "*")
    print("*" + " " * 10 + "Welcome to the Application".center(58) + "*")
    print("*" + " " * 78 + "*")
    print("*" * 80)
    print()


def print_welcome_message():
    border = '*' * 50
    message = 'Welcome to the DBSERVER'

    print(border)
    print('*' + ' ' * (len(border) - 2) + '*')
    print('*' + message.center(len(border) - 2) + '*')
    print('*' + ' ' * (len(border) - 2) + '*')
    print(border)

def print_appserver_welcome_message():
    message = "Welcome to the APPSERVER"
    border_length = len(message) + 4
    border = "*" * border_length

    print(border)
    print("*" + message.center(border_length - 2) + "*")
    print(border)

def print_thank_you_message():
    message = "Thank you for visiting our page"
    border_char = "="
    padding = 4
    border_length = len(message) + padding * 2
    border = border_char * border_length

    print(border)
    print(f"{border_char}{' ' * (border_length - 2)}{border_char}")
    print(f"{border_char}{' ' * padding}{message}{' ' * padding}{border_char}")
    print(f"{border_char}{' ' * (border_length - 2)}{border_char}")
    print(border)

def print_invalid_option_message():
    message = "Invalid option. Please select 1, 2, or 3."
    border_char = "*"
    padding = 2
    border_length = len(message) + padding * 2 + 4
    border = border_char * border_length

    print(border)
    print(f"{border_char} {border_char * (border_length - 2)} {border_char}")
    print(f"{border_char} {message.center(border_length - 4)} {border_char}")
    print(f"{border_char} {border_char * (border_length - 2)} {border_char}")
    print(border)


def handle_option():
    while True:
        print("\n" + "*" * 80)
        print("*" + " " * 78 + "*")
        print("*" + " " * 10 + "Option for available".center(58) + "*")
        print("*" + " " * 78 + "*")
        print("*" * 80)
        print()
        print("1. Login on algomox")
        print("2. Change Directory")
        print("3. List out the files")
        print("4. Run the files")
        print("5. Exit")
        opt = input("Select option: ")

        if opt == '1':
            print("\n" + "!" * 80)
            print("!" + " " * 78 + "!")
            print("!" + " " * 10 + "Welcome to the Algomox".center(58) + "!")
            print("!" + " " * 78 + "!")
            print("!" * 80)
            print()
            subprocess.run(['su', 'algomox'])
            print("\n" + "°" * 80)
            print("°" + " " * 78 + "°")
            print("°" + " " * 10 + "You are successfully logged into Algomox".center(58) + "°")
            print("°" + " " * 78 + "°")
            print("°" * 80)
            print()
        elif opt == '2':
            print("\n" + "#" * 80)
            print("#" + " " * 78 + "#")
            print("#" + " " * 10 + "Now we are changing the directory".center(58) + "#")
            print("#" + " " * 78 + "#")
            print("#" * 80)
            print()
            os.chdir(os.path.expanduser("~"))
        elif opt == '3':
            print("\n" + "$" * 80)
            print("$" + " " * 78 + "$")
            print("$" + " " * 10 + "Listing out the Algomox files directory".center(58) + "$")
            print("$" + " " * 78 + "$")
            print("$" * 80)
            print()
            print("\n".join(os.listdir()))
        elif opt == '4':
            print("\n" + "*" * 80)
            print("*" + " " * 78 + "*")
            print("*" + " " * 10 + "Now we can run the Toolkit of the Algomox".center(58) + "*")
            print("*" + " " * 78 + "*")
            print("*" * 80)
            print()
            toolkit = input("Enter the toolkit name: ")
            subprocess.run(['./' + toolkit])
        elif opt == '5':
            print("\n" + "~" * 80)
            print("~" + " " * 78 + "~")
            print("~" + " " * 10 + "Thank you for visiting my application By Nithyananthan_techie".center(58) + "~")
            print("~" + " " * 78 + "~")
            print("~" * 80)
            print()
            break
        else:
            print("\n" + "=" * 80)
            print("=" + " " * 78 + "=")
            print("=" + " " * 10 + "Wrong option".center(58) + "=")
            print("=" + " " * 78 + "=")
            print("=" * 80)
            print()


def main():
    print_vertical_nn_centered_box_pattern()
    print_welcome()

    while True:
        print("********** Welcome to the Options Menu **********")
        print("*                                               *")
        print("*               Option for available            *")
        print("*                                               *")
        print("*************************************************")

        print("1. DBSERVER")
        print("2. APPSERVER")
        print("3. Exit")
        opt = input("Select option: ")

        if opt == '1':
            print_welcome_message()
            handle_option()
        elif opt == '2':
            print_appserver_welcome_message()
            handle_option()
        elif opt == '3':
            print_thank_you_message()
            break
        else:
            print_invalid_option_message()


if __name__ == "__main__":
    main()
