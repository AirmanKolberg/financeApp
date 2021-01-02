# This is just a test for now, but
# I may be re-writing the entire
# mainframe of this app.

from time_date import calculate_days_between, convert_date_to_list_of_integers
from secrets import *

while True:
    command = input('>').lower()
    if command == 'check bank one':
        check_bank_one()
    elif command == 'total':
        total_cash_on_hand()
    else:
        print(f"'{command}' not recognised, please try again.")
