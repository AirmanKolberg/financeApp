from system_commands import clear_screen, bash_command
from time import sleep
from maths import find_line_of_search_result_in_file
from username_converter import username_dictionary

list_of_usernames = open("username_list.py", "r")
num_of_lines_in_username_list = 0
content = list_of_usernames.read()
line_divider = content.split("\n")


for i in line_divider:
    if i:
        num_of_lines_in_username_list += 1


def create_new_user():
    clear_screen()
    print("""Welcome new user to my financial app, "The Financial Framework"!
    
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

    user_number = int(num_of_lines_in_username_list) + 1
    bash_command(f"""echo "user_{str(user_number)} = ['{new_username}', '{new_password}']" >> username_list.py""")
    bash_command(f"echo '{new_username}' >> {new_username}_data_file.txt")
    bash_command(f"echo '{new_password}' >> {new_username}_data_file.txt")


def test_if_username_is_legit(username):
    try:
        f = open(f"{username}_data_file.py")
        auth = 'legit'
    except IOError:
        auth = 'not_legit'
    return auth


def password_test(username):
    retry_count = 2
    password = input("Password: ")

    while retry_count > 0:
        user_id = username_dictionary.get(username)
        user_id_num = int(user_id[-1:])
        bash_command('rm temp_app_auth.py')
        bash_command("echo 'import username_list' >> temp_app_auth.py")
        bash_command("echo '' >> temp_app_auth.py")
        bash_command(f"echo 'current_user = username_list.user_{user_id_num}' >> temp_app_auth.py")
        from temp_app_auth import current_user as user_list
        current_password = user_list[1]

        if password == current_password:
            print('Password correct!')
            sleep(1)
            return "passed"
        else:
            retry_count -= 1
            print(f"Have another go, or {retry_count + 1}!")
            password = input("Password: ")
    else:
        return "failed"


def find_user_id_number(username):
    clear_screen()
    user_number = find_line_of_search_result_in_file('username_list.py', f'{username}', 1)
    user_id = f'user_{user_number}'
    return user_id


def change_password(username):
    clear_screen()
    from temp_app_auth import current_user as user_list

    correct_password = user_list[1]
    passed_old_pass = False
    old_password = input("""Please first confirm your old password:
> """)
    while not passed_old_pass:
        if old_password == correct_password:
            passed_old_pass = True
        else:
            print(f"'{old_password}' is not your current password, please try again.")
            old_password = input('> ')

    while True:
        new_password = input("""Please select a new password:
> """)
        sure = input(f"""You've selected "{new_password}" (without outer quotes) as your new password!  Ready to save?
> """).lower()
        if sure == "yes":
            bash_command(f"sed -i 's/{old_password}/{new_password}/g' username_list.py")
            bash_command(f"sed -i 's/{old_password}/{new_password}/g' {username}_data_file.py")
            print(f"You password's been changed to '{new_password}', {username}!")
            break
        elif sure == "no":
            new_password = input("""Please try again with a new password:
> """)
        else:
            print("Just yes or no, please.  Please try again.")
            sure = input('> ')
