def compound_interest(principle, interest, time_years):
    amount = principle * (pow((1 + interest / 100), time_years))
    interest_compounded = amount - principle
    return interest_compounded


def future_value():
    amount = int(input('Insert the dollar value today:\n'))
    interest_rate = int(input('Insert the interest on this amount over time:\n'))
    time_to_grow = int(input('Finally, the time to grow:\n'))
    interest_gained = compound_interest(amount, interest_rate, time_to_grow)
    print(f'The real value of your ${amount} today, is really ${round((amount + interest_gained), 2)}.')
    retry = input('Go again?\n').lower()
    finished = False
    while not finished:
        if retry == 'yes':
            future_value()
        elif retry == 'no':
            break
        else:
            retry = input(f'{retry} is not a valid input.  Yes or no?\n')
