# This is pre-in-dev 1
# I am missing a lot of bank information on here, but fear not!
# I am tirelessly (when I can) working on moving all of the
# sensitive material into one file, and make this as simple
# and autonomous as possible.  Give me a break, being a 
# stay-at-home step dad to a 4-year-old girl is quite time-
# consuming!  lol

from time import sleep
from system_commands import *
import budget_bug
from maths import *
from important_functions import *

clear_screen()
wrong_user_count = 0
# ------------------------------'failed' to 'passed', False to True for debugging------------------------------
log_in = 'passed'
user = 'h@ck3r'
authenticated = True

while not authenticated:
    print("""Welcome to "The Financial Framework"!""")
    granted_entry = False
    while not granted_entry:
        entry_point = input("""Are you a returning user?  (Yes or no)
> """).lower()
        clear_screen()
        if entry_point == "yes":
            granted_entry = True
        elif entry_point == "no":
            create_new_user()
            granted_entry = True
        elif entry_point == "exit":
            break
        else:
            print(f"'{entry_point}' is neither yes, nor no, please try again.")

    incorrect_multiplier = 5

    user = input("Username: ")
    auth = test_if_username_is_legit(user)

    if auth == "legit":
        log_in = password_test(user)
        authenticated = True
    else:
        print(f"""I do not recognise you, "{user}", please type carefully!""")
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
            bash_command(f"echo '{current_date}@{current_time}' >> randomSave.txt")
        elif command == "--help":
            print(f"""List of commands:

save  -  This will take all of the current data and store it with a time/date stamp.

:  -  This will allow you to run a shell command.

[bank]  -  Type the name of a bank to retrieve its balance.

budget  -  Runs the Budget Bugger application.

clear  -  Clears the screen.

new pass  -  Select this option to choose a new password for your
Financial Framework username.

exit  -  Closes the application.  This command will be universal
amongst all applications within this framework, to include the
framework itself.

--help  -  This will pull up the help menu you're seeing now.

NOTE: This terminal is NOT case-sensitive.""")
        elif command == ":":
            use_terminal()
        elif command == "chase":
            check_chase_balance()
        elif command == "budget":
            budget_bug.budget_bugger()
        elif command == "new pass":
            change_password(user)
        elif command == "clear":
            clear_screen()
        elif command == "exit":
            break
        else:
            print(f""""{command}" is not a valid command.
Let's try something like this: --help""")

else:
    print(f"Too many incorrect password attempts for {user}")
    exit()
