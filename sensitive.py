from time import sleep
import time
from datetime import date

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
today = date.today()
current_date = today.strftime("%m/%d/%Y")

# Set the following as variables in this comment's place

liquid_assets = [checking_account, savings_account, crypto_portfolio, cash]
short_term_liabilities = [goldmann_credit, trumps_border_wall,  cap1_black_card]
long_term_liabilities = [auto_loan, mansion_loan]
personal_assets = [angus_young_signature, catamaran_72]

net_worth = liquid_assets + personal_assets + short_term_liabilities + long_term_liabilities
all_data = f"""{current_date} @ {current_time}//  Liquid Assets: {liquid_assets}, Personal Assets: {personal_assets}, Short-Term Liabilities: {short_term_liabilities}, Long-Term Liabilities: {long_term_liabilities}"""

# The remainder of this page has not been submitted
# I will further review and carefully submit information as I go,
# So long as I first skim through it to scrub/edit personal information
