from system_commands import bash_command, clear_screen
from maths import count_days_since_today
from bugger_file import my_data

# This will not be updated until further notice
# May discontinue and replace

clear_screen()
days_since_start = count_days_since_today(my_data[0], my_data[1], my_data[2])
num_of_weeks = int(days_since_start / 7)


def budget_bugger():

    print('Welcome to Budget Bug!')
    my_current_data = my_data

    def update_data_sheet(rolling, weekly, discrepancy):
        my_current_data[rolling] = my_current_data[weekly] + (my_current_data[weekly] * num_of_weeks) - my_current_data[discrepancy]

    def update_all():
        update_data_sheet(7, 3, 11)
        update_data_sheet(8, 4, 12)
        update_data_sheet(9, 5, 13)
        update_data_sheet(10, 6, 14)

    def save_data():
        update_all()
        bash_command(f"rm bugger_file.py && echo 'my_data = {my_current_data}' >> bugger_file.py")

    while True:
        command = input('> ').lower()
        if command == "show all":
            update_all()
            print(f"""Weekly food remaining: ${my_current_data[7]}
Weekly iPad fund remaining: ${my_current_data[8]}
Weekly misc remaining: ${my_current_data[9]}
Savings fund: ${my_current_data[10]}""")
        elif command == "--help":
            print("""--help  -  Brings you here.
            
show all  -  Shows all remaining balances.

transaction  -  The section of the portal to input transactions.

save  -  Saves all current data.
            
exit  -  Exits this application.""")
        elif command == "transaction":
            while True:
                selection = input("""Transaction from which account?
                - Food
                - iPad stuff
                - Misc
                - Savings
                > """).lower()
                clear_screen()
                if selection == "food":
                    to_sum = float(input("What are we taking from the food fund? "))
                    before = int(my_current_data[11])
                    my_current_data[11] = before + to_sum
                    break
                elif selection == "ipad":
                    to_sum = float(input("What are we taking from the pot fund? "))
                    before = int(my_current_data[12])
                    my_current_data[12] = before + to_sum
                    break
                elif selection == "misc":
                    to_sum = float(input("What are we taking from the misc fund? "))
                    before = int(my_current_data[13])
                    my_current_data[13] = before + to_sum
                    break
                elif selection == "savings":
                    to_sum = float(input("What are we taking from the savings fund? "))
                    before = int(my_current_data[14])
                    my_current_data[14] = before + to_sum
                    break
                elif selection == "exit":
                    break
                else:
                    print(f"{selection} is not valid.  Try again or 'exit', no quotes.")
        elif command == "save":
            save_data()
        elif command == "exit":
            save_data()
            print("Everything is saved.  Budget Bug Bye-Bye!")
            break
        else:
            print(f"{command} is not a valid command.  Perhaps try '--help' (no quotes).")
