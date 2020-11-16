from system_commands import clear_screen, bash_command

load_file = open("username_list.py", "r")
num_of_lines = 0
content = load_file.read()
line_divider = content.split("\n")

for i in line_divider:
    if i:
        num_of_lines += 1


def create_new_user():
    clear_screen()
    print("""Welcome new user to my financial app, "The Money Manager"!
    
This app shows passwords in plain text as you're typing, because that's my preference.
If you do not like that, this program is open-source, change that yourself.  I believe
that there should be some moderate level of difficulty when accessing financial
information, but at the same time, it shouldn't be exorbitantly difficult.\n""")
    new_username = input("""Please type in your username!  Note; this is case-sensitive.
> """)
    name_available = False
    while not name_available:
        try:
            f = open(f"{new_username}_data_file.py")
            new_username = input(f"""Oh no!  {new_username} is already in use!  Please try for another:
> """)
        except IOError:
            print("That username is not yet in use!")
            name_available = True

    certain = False
    while not certain:
        consent = input(f"""Are you sure you want '{new_username}' (without quotes) as your username?
(yes or no)
> """).lower()
        if consent == "yes":
            certain = True
        elif consent == "no":
            clear_screen()
            new_username = input("""What would you like your new case-sensitive username to be?
> """)
        elif consent == "exit":
            break
        else:
            clear_screen()
            print(f"'{consent}' is not a valid input, please try again.")

    clear_screen()
    password_set = False
    new_password = input(f"""Nice to meet you, {new_username}!  Please pick a password:
> """)
    while not password_set:
        confirm_password = input(f"""I got "{new_password}" (without the outer quotes), is that right?
(yes or no)
> """).lower()
        if confirm_password == "yes":
            clear_screen()
            print(f"""Username: {new_username}
Password: {new_password}
It is very lovely to meet you.  Please save your login credentials above!""")
            password_set = True
        elif confirm_password == "no":
            clear_screen()
            new_password = input("""Try again, input your password:
> """)
        else:
            print(f""""{confirm_password}" is neither yes, nor no.  Please try again.""")

    user_number = int(num_of_lines) + 1
    bash_command(f"""echo "user_{str(user_number)} = ['{new_username}', '{new_password}']" >> username_list.py""")
    bash_command(f"touch {new_username}_data_file.py")


def load_user_session(username):
    try:
        f = open(f"{username}_data_file.py")
        auth = 'legit'
    except IOError:
        auth = 'not_legit'
    return auth


# Create a function to change the password to the main app
