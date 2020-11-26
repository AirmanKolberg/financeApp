from time import sleep
import time
from datetime import date
from secrets import usaa_username, usaa_password

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

def check_usaa_balance():
    driver = webdriver.Firefox()
    driver.get('https://www.usaa.com/')
    driver.minimize_window()
    sleep(3)
    bot = driver.find_element_by_class_name('profileWidget-buttonLeft')
    bot.click()
    sleep(3)
    username = driver.find_element_by_id('j_usaaNum')
    password = driver.find_element_by_id('j_usaaPass')
    username.clear()
    password.clear()
    username.send_keys(usaa_username)
    password.send_keys(usaa_password)
    password.send_keys(Keys.RETURN)
    sleep(2)
    email_select = driver.find_element_by_id('id9-EMAIL1')
    email_select.click()
    sleep(1)
    button = driver.find_element_by_id('idc')
    button.click()

# The remainder of this page has not been submitted
# I will further review and carefully submit information as I go,
# So long as I first skim through it to scrub/edit personal information
