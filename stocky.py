# This app trades stocks
# This in-dev version, whilst operable,
# is just for testing purposes.

import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math
from secrets import IEX_CLOUD_API_TOKEN

stocks = pd.read_csv('my_stocks.csv')

symbol = 'AAPL'
api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote/?token={IEX_CLOUD_API_TOKEN}'

data = requests.get(api_url).json()
# The next command could also be
# print(data.status_code)
# or something to that effect as well.
# Or just nix everything in the () save
# 'data', it's just something with which
# I'm playing right now.
print(data['latestPrice'])

my_columns = ['Ticker', 'Stock Price', 'Market Capitalisation', 'Number of Shares to Buy']
final_dataframe = pd.DataFrame(columns=my_columns)

final_dataframe.append(
    pd.Series(
    [
        symbol,
        data['latestPrice'],
        data['marketCap'],
        'N/A'
    ],
    index = my_columns
    ),
    ignore_index=True
)

print(final_dataframe)