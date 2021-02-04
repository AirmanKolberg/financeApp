from os import system


def clear_screen():
    _ = system('clear')


def bash_command(user_in):
    _ = system(user_in)


def verify_float(potential_number):
    try:
        the_float = float(potential_number)
    except ValueError:
        potential_number = input(f'{potential_number} is not a number, please try again: ')
        return verify_float(potential_number)
    else:
        return the_float


def verify_yes_or_no(response):
    if response == 'yes':
        return True
    elif response == 'no':
        return False
    else:
        return verify_yes_or_no(input(f"{response} is neither 'yes' nor 'no', please try again: ").lower())
