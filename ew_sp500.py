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

stocks = pd.read_csv('sp_500_stocks.csv')
