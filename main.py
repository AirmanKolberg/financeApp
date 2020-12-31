# This is pre-in-dev 1
# I am missing a lot of bank information on here, but fear not!
# I am tirelessly (when I can) working on moving all of the
# sensitive material into one file, and make this as simple
# and autonomous as possible.  Give me a break, being a 
# stay-at-home step dad to a 4-year-old girl is quite time-
# consuming!  lol

# NOTE: Re-write values as Class Objects for simplified code

from time import sleep
from system_commands import *
from maths import *
from important_functions import *

clear_screen()
wrong_user_count = 0
# ------------------------------'failed' to 'passed', False to True for debugging------------------------------
log_in = 'failed'
user = 'h@ck3r'
authenticated = False

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

    main_menu()

else:
    print(f"Too many incorrect password attempts for {user}")
    exit()
