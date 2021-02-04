import pandas as pd
from generalFunctions import verify_float, verify_yes_or_no, clear_screen


def export_monthly_bills(bill_name_list, amount_list):
    framework = {'Bill Name': bill_name_list,
                 'Amount': amount_list,
                 }

    df = pd.DataFrame(framework, columns=['Bill Name', 'Amount'])
    df.to_csv('monthlyBills.csv')


def create_monthly_bills_list():
    clear_screen()
    bills_dictionary = dict()
    print("Here we will cover all of your monthly bills.  Please insert them one at a time.")

    done_adding_bills = False
    while not done_adding_bills:
        bill_name = input('Insert bill name: ')
        bill_amount = verify_float(input('Insert bill amount: '))
        bills_dictionary[bill_name]=bill_amount

        adding_another = verify_yes_or_no(input('Add another?\n').lower())
        if not adding_another:
            done_adding_bills = True
        else:
            pass

    bill_name_list = list()
    amount_list = list()
    for i in bills_dictionary:
        bill_name_list.append(i)
        amount_list.append(bills_dictionary[i])

    export_monthly_bills(bill_name_list, amount_list)
