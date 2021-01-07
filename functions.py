import pandas as pd
from secrets import *
from datetime import date, datetime

today = str(date.today())
now = datetime.now()
date_list = []
time_list = []


# Work on this bit later
def export_csv():
    date_list.append(today)
    time_list.append(now)
    output = {'Date': date_list,
              'Time': time_list
              }

    df = pd.DataFrame(output, columns=['Date', 'Time'])
    df.to_csv('financeData.csv')
