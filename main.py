# This is pre-in-dev 1

import time
from time import sleep
from datetime import date
from sensitive import password_test, save_current_data, check_usaa_balance, calculate_remaining_today, calculate_net_worth
from system_commands import clear_screen, bash_command

clear_screen()
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
today = date.today()
current_date = today.strftime("%m/%d/%Y")
wrong_user_count = 0
authenticated = False

while not authenticated:
    incorrect_multiplier = 5
    user = input("Username: ")
# "YourName" is your name, but of course this login method will change in the near future
    if user == "YourName":
        log_in = password_test()
        authenticated = True
    else:
        print(f"""I do not recognise you, "{user}", go away!""")
        wrong_user_count += 1
        seconds_to_wait = wrong_user_count * incorrect_multiplier
        print(f"Waiting {seconds_to_wait} seconds before retry allowed...")
        sleep(seconds_to_wait)
        clear_screen()


if log_in == "passed":
    clear_screen()
    print(f"Welcome back, {user}!")

# --------------------INSIDE THE APP TERMINAL--------------------

    while True:
        command = input("> ").lower()
        clear_screen()

        if command == "save":
            save_current_data()
        elif command == "--help":
            print(f"""List of commands:

save  -  This will allow you to save a .json file with a line of text in it.
You can give it both a [name].json and the text to be inserted within "".

:  -  This will allow you to run a shell command.

[bank]  -  Type the name of a bank to retrieve its balance.

today  -  Will show today's remaining miscellaneous spending amount.

net worth -  Will calculate and display your current net worth.

exit  -  Closes the application.

--help  -  This will pull up the help menu you're seeing now.

NOTE: This terminal is NOT case-sensitive.""")
        elif command == ":":
            shell_command = input("root@kali:~#")
            bash_command(shell_command)
# Random examples of banks, such as Chase, BoA, Cap1, etc.
        elif command == "chase":
            check_chase_balance()
        elif command == "boa":
            # --------------------THIS NOTE IS CENSORED TO THE PUBLIC--------------------
            print("Repeat USAA cmd for BoA here when possible.")
        elif command == "today":
            print(calculate_remaining_today())
        elif command == "net worth":
            calculate_net_worth()
        elif command == "exit":
            break
        else:
            print(f""""{command}" is not a valid command.
Let's try something like this: --help""")

else:
    print(f"Too many incorrect password attempts for {user}")
    exit()
