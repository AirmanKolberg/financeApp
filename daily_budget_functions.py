from os import system


def clear_screen():
    _ = system('clear')


def solve_for_a(b, c, x, y, z):
    a = (x - (y * c) - (z + b)).__round__(2)
    print(f'a = ${a}')


def solve_for_b(a, c, x, y, z):
    b = (x - (y * c) - (z + a)).__round__(2)
    print(f'b = ${b}')


def solve_for_c(a, b, x, y, z):
    c = ((x - (a + b + z)) / y).__round__(2)
    print(f'c = ${c}')


def determine_if_value_is_number(input_value, num_type):
    number_determined = False
    while not number_determined:
        try:
            if num_type == 'float':
                float(input_value)
            elif num_type == 'int':
                int(input_value)
            else:
                clear_screen()
                print("ERROR: Make sure 'float' or 'int' selected as second input.")
                exit()
            clear_screen()
            number_determined = True
        except ValueError:
            input_value = input('Try again, but with a number.\n>')
    if num_type == 'float':
        return float(input_value)
    else:
        return int(input_value)
