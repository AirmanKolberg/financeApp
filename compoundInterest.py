# I'm working on some compound interest stuff in my free time
# However, it isn't completed, yet.  When it is, I will be
# adding it to the finance app framework, but until then,
# my works on the matter will be found in separate .py files!

from compound_interest_functions import future_value

options = """value  -  See the value of any dollar amount over time
--help  -  Shows this option menu"""
print(f'Welcome to the Compound Interest Calculator!  Here are your options:\n{options}')
choice = input('> ').lower()

if choice == 'value':
    future_value()
elif choice == '--help':
    print(options)
else:
    print(f'{choice} is not a valid command.  Please try again.')
