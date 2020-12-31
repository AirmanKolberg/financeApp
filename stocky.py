# This app trades stocks
# This in-dev version, whilst operable,
# is just for testing purposes.

import pandas as pd
import requests
import math
from time import sleep
from datetime import date, datetime
from os import system
import calendar
from system_commands import bash_command, clear_screen
from secrets import api_token, stocks_dictionary


def check_prices(stock_or_all, price_or_shares2buy):
    if price_or_shares2buy.lower() == 'price':
        price_or_shares2buy = 'Stock Price'
    elif price_or_shares2buy.lower() == 'shares2buy':
        price_or_shares2buy = 'Shares to Buy'
    else:
        print(f"{price_or_shares2buy} is neither 'prices', nor 'shares2buy', sorry.")
        return
    stocks = pd.read_csv('stocks_list.csv')
    my_columns = ['Ticker', 'Stock Price', 'Shares to Buy']

    def chunks(lst, n):
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    symbol_groups = list(chunks(stocks['Ticker'], 100))
    symbol_strings = []
    for i in range(0, len(symbol_groups)):
        symbol_strings.append(','.join(symbol_groups[i]))

    final_dataframe = pd.DataFrame(columns=my_columns)

    for symbol_string in symbol_strings:
        batch_api_call_url = f"https://cloud.iexapis.com/stable/stock/market/batch?symbols={symbol_string}&types=quote&token={api_token}"
        data = requests.get(batch_api_call_url).json()
        for symbol in symbol_string.split(','):
            final_dataframe = final_dataframe.append(
                pd.Series([symbol,
                           data[symbol]['quote']['latestPrice'],
                           'N/A'],
                          index=my_columns),
                ignore_index=True)

    portfolio_size = 6000

    # The following lines are unnecessary unless the user inputs portfolio_size
    # try:
    #     val = float(portfolio_size)
    # except ValueError:
    #     portfolio_size = input("That's not a number, please try again.\nEnter the value of your portfolio: ")
    #     val = float(portfolio_size)

    position_size = float(portfolio_size) / len(final_dataframe.index)
    for i in range(0, len(final_dataframe['Ticker'])):
        final_dataframe.loc[i, 'Shares to Buy'] = math.floor(position_size / final_dataframe['Stock Price'][i])

    if stock_or_all.lower() == 'all':
        return final_dataframe
    else:
        return final_dataframe.iloc[stocks_dictionary[f'{stock_or_all}']][f'{price_or_shares2buy}']


def get_date():
    current_date = date.today().strftime("%d %B %Y")
    return current_date


def get_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    return current_time


def get_weekday():
    day_of_the_week = calendar.day_name[date.today().weekday()]
    return day_of_the_week


def get_hour():
    if int(get_time()[0]) == 0:
        hour = int(get_time()[1])
    else:
        hour = int(get_time()[0:2])
    return hour


# Invert both booleans when debugging (to True/False)
weekend = True
market_open = False
money = 6000


class Stock:
    def __init__(self, symbol, num_of_shares, price_at_sale):
        self.symbol = symbol
        self.num_of_shares = num_of_shares
        self.price_at_sale = price_at_sale

    def buy_shares(self, num_to_buy, price_per_share):
        self.num_of_shares = num_to_buy
        cost = num_to_buy * price_per_share
        self.price_at_sale = price_per_share
        return cost

    def sell_shares(self, price_per_share):
        earnings = self.num_of_shares * price_per_share
        self.num_of_shares = 0
        self.price_at_sale = price_per_share
        return earnings


    def value(self, current_value):
        share_value = self.num_of_shares * current_value
        return share_value


TSLA = Stock('TSLA', 0, 0)
RTX = Stock('RTX', 0, 0)
HON = Stock('HON', 0, 0)
KBR = Stock('KBR', 0, 0)
AAPL = Stock('AAPL', 0, 0)


def buy_all_shares():
    price_check = check_prices('all', 'price')
    money = 6000
    money -= TSLA.buy_shares(price_check['Shares to Buy'][0], price_check['Stock Price'][0])
    print(f"Bought {price_check['Shares to Buy'][0]} share(s) of TSLA for ${price_check['Stock Price'][0]}.")
    money -= RTX.buy_shares(price_check['Shares to Buy'][1], price_check['Stock Price'][1])
    print(f"Bought {price_check['Shares to Buy'][1]} share(s) of RTX for ${price_check['Stock Price'][1]}.")
    money -= HON.buy_shares(price_check['Shares to Buy'][2], price_check['Stock Price'][2])
    print(f"Bought {price_check['Shares to Buy'][2]} share(s) of HON for ${price_check['Stock Price'][2]}.")
    money -= KBR.buy_shares(price_check['Shares to Buy'][3], price_check['Stock Price'][3])
    print(f"Bought {price_check['Shares to Buy'][3]} share(s) of KBR for ${price_check['Stock Price'][3]}.")
    money -= AAPL.buy_shares(price_check['Shares to Buy'][4], price_check['Stock Price'][4])
    print(f"Bought {price_check['Shares to Buy'][4]} share(s) of AAPL for ${price_check['Stock Price'][4]}.")
    return money
    sleep(60)


def assess_asset(stock, stock_int, money=money):
    old_price = stock.price_at_sale
    price_check = check_prices('all', 'price')
    potential_loss = stock.value(price_check['Stock Price'][stock_int]) - (stock.num_of_shares * old_price)
    potential_profit = stock.value(price_check['Stock Price'][stock_int]) - (stock.num_of_shares * old_price)
    if potential_loss >= -0.01 * stock.value(price_check['Stock Price'][stock_int]) and stock.num_of_shares == 0:
        money -= stock.buy_shares(price_check['Stock Price'][stock_int], price_check['Stock Price'][stock_int])
        print(f"Bought {price_check['Shares to Buy'][stock_int]} share(s) of {str(stock)} at ${price_check['Stock Price'][stock_int]} each at {get_time()}.")
    elif potential_profit >= 0.01 * stock.value(price_check['Stock Price'][stock_int]) and stock.num_of_shares != 0:
        money += stock.sell_shares(price_check['Stock Price'][stock_int])
        print(f"Sold {price_check['Shares to Buy'][stock_int]} share(s) of {str(stock)} at ${price_check['Stock Price'][stock_int]} (from ${old_price}) each at {get_time()}.")
        stock.num_of_shares = 0
    else:
        print(f"{stock} assessed at {get_time()}, no action required.")


object_list = [TSLA, RTX, HON, KBR, AAPL]

message_1 = f"Starting with $6,000 on {get_date()} at {get_time()}."

# --------------------TERMINAL BEGINS HERE--------------------

clear_screen()
print(message_1)

while True:
    today = get_weekday()
    while today != 'Saturday' and today != 'Sunday':
        hour = get_hour()
        while 7 <= hour < 15:
            if TSLA.num_of_shares == 0 and RTX.num_of_shares == 0 and HON.num_of_shares == 0 and KBR.num_of_shares == 0 and AAPL.num_of_shares == 0:
                money = buy_all_shares()
                message_2 = f"Cash on hand: ${money.__round__(2)}"
                print(message_2)
                hour = get_hour()

            identifier = -1
            for stocks in object_list:
                identifier += 1
                assess_asset(stocks, identifier)
            sleep(60)
            hour = get_hour()
        today = get_weekday()
        sleep(60)
    print(f"""It's the weekend, market is closed.
Money at close: ${money}""")

    # Put a for loop here, you dirty, rotten bastard!

    price_check = check_prices('all', 'price')
    tsla_value = TSLA.value(price_check['Stock Price'][0])
    rtx_value = RTX.value(price_check['Stock Price'][1])
    hon_value = HON.value(price_check['Stock Price'][2])
    kbr_value = KBR.value(price_check['Stock Price'][3])
    aapl_value = AAPL.value(price_check['Stock Price'][4])
    print(f'Portfolio at close: ${(money + tsla_value + rtx_value + hon_value + kbr_value + aapl_value).__round__(2)}\n')
    print(f"""TSLA: ${tsla_value}
RTX: ${rtx_value}
HON: ${hon_value}
KBR: ${kbr_value}
AAPL: ${aapl_value}""")
    sleep(21600)    # 6 hours
    today = get_weekday()
