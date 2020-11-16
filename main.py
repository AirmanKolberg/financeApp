# This is pre-in-dev 1
# I am missing a lot of bank information on here, but fear not!
# I am tirelessly (when I can) working on moving all of the
# sensitive material into one file, and make this as simple
# and autonomous as possible.  Give me a break, being a 
# stay-at-home step dad to a 4-year-old girl is quite time-
# consuming!  lol

from time import sleep
from sensitive import password_test, check_usaa_balance
from system_commands import clear_screen, bash_command
import budget_bug
from maths import current_date, current_time
from important_functions import create_new_user, load_user_session

clear_screen()
wrong_user_count = 0
# ------------------------------'failed' to 'passed', False to True for debugging------------------------------
log_in = 'failed'
user = 'h@ck3r'
authenticated = False

while not authenticated:
    print("""Welcome to "The Money Manager"!""")
    granted_entry = False
    while not granted_entry:
        entry_point = input("""Are you returning user?  (Yes or No, non-case-sensitive)
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
    auth = load_user_session(user)

    if auth == "legit":
        log_in = password_test()
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

today  -  Will show today's remaining miscellaneous spending amount.

budget  -  Runs the Budget Bugger application.

clear  -  Clears the screen.

exit  -  Closes the application.  This command will be universal
amongst all applications within this framework, to include the
framework itself.

--help  -  This will pull up the help menu you're seeing now.

NOTE: This terminal is NOT case-sensitive.""")
        elif command == ":":
            shell_command = input("root@kali:~#")
            bash_command(shell_command)
        elif command == "today":
            print(calculate_remaining_today())
        elif command == "budget":
            budget_bug.budget_bugger()
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
