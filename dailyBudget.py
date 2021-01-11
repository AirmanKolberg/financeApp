from daily_budget_functions import *
# from debugging_variables import *

variables_list = ['a', 'b', 'c', 'x', 'y', 'z']


def reset_variable(variable):
    if variable in variables_list:
        variable_verified = True
    else:
        print(f'{variable} is an invalid variable.  Please pick a, b, c, x, y, or z.')
        variable_verified = False
    if variable_verified:
        new_value = input(f'Set new value for {variable}: ')
        if variable != 'y':
            new_variable = determine_if_value_is_number(new_value, 'float')
        else:
            new_variable = determine_if_value_is_number(new_value, 'int')
        return new_variable


# ----------Comment out these next sections during debugging----------
total_cash = input('How much liquid money do you have?\n>')
x = determine_if_value_is_number(total_cash, 'float')

days_until_next_pay = input("How many days until next income date?\n>")
y = determine_if_value_is_number(days_until_next_pay, 'int')

bills = input('How much is coming out in bills over those days?\n>')
z = determine_if_value_is_number(bills, 'float')

spendable_today = input('How much do you have to spend today?\n>')
a = determine_if_value_is_number(spendable_today, 'float')

savings = input('How much is in savings?\n>')
b = determine_if_value_is_number(savings, 'float')

daily_spending_budget = input("What's your daily spending allowance?\n>")
c = determine_if_value_is_number(daily_spending_budget, 'float')
# --------------------------------------------------------------------

terminal_message = """Type one of the following letters to solve for it:
a = amount spendable today
b = amount saved for car
c = maximum daily spending limit

Or type "set [variable]" (no quotes) to set the value of that variable.
IE - set b
"""

while True:
    print(terminal_message)
    command = input('>').lower()
    if command == 'a':
        solve_for_a(b=b, c=c, x=x, y=y, z=z)
    elif command == 'b':
        solve_for_b(a=a, c=c, x=x, y=y, z=z)
    elif command == 'c':
        solve_for_c(a=a, b=b, x=x, y=y, z=z)
    elif command[:4] == 'set ':
        if command[4:] == 'a':
            a = reset_variable(command[4:])
        elif command[4:] == 'b':
            b = reset_variable(command[4:])
        elif command[4:] == 'c':
            c = reset_variable(command[4:])
        elif command[4:] == 'x':
            x = reset_variable(command[4:])
        elif command[4:] == 'y':
            y = reset_variable(command[4:])
        elif command[4:] == 'z':
            z = reset_variable(command[4:])
        else:
            print("Invalid 'set' command.")
    else:
        clear_screen()
        print(f"'{command}' not recognised, please try again.\n")
