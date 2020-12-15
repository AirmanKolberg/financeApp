# This will eventually become an Equal-Weight S&P 500 Index
# Eventually I will be working on an app within the 
# Finance App mainframe that will buy/sell/trade stocks in
# the background, just for funzies, as the kids say.
# At least that's what I imagine they say, I like to think
# I'm hip, yo.

import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math
from secrets import IEX_CLOUD_API_TOKEN

stocks = pd.read_csv('sp_500_stocks.csv')

symbol = 'AAPL'
api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote/?token={IEX_CLOUD_API_TOKEN}'

data = requests.get(api_url).json()
# The next command could also be
# print(data.status_code)
# or something to that effect as well.
# Or just nix everything in the () save
# 'data', it's just something with which
# I'm playing right now.
print(data['companyName'])
