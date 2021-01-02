# Again, just a test to potentially
# replace the old mainframe

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
from time import sleep

start_date = [2021, 1, 8]
spendable = 1000
saved_for_car = 30000

bank_one_user = 'secret'
bank_one_pass = 'secret'
bank_two_user = 'secret'
bank_two_pass = 'secret'


class Account:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def change_value_by(self, change):
        self.value += change
        print(f'{self.name} current value: ${self.value}')

    def set_value(self, new_value):
        self.value = new_value
        print(f'{self.name} current value: ${self.value}')


bank_one = Account('USAA', 354.37)
bank_two = Account('BoA', 0)


# Conformed to the 2015 15" MacBook Pro Retina display
def check_bank_one():
    firefox = webdriver.Firefox()
    firefox.get('https://www.usaa.com/')
    firefox.find_element_by_class_name('profileWidget-buttonLeft').click()
    username = firefox.find_element_by_id('j_usaaNum')
    password = firefox.find_element_by_id('j_usaaPass')
    username.clear()
    password.clear()
    username.send_keys(bank_one_user)
    password.send_keys(bank_one_pass)
    password.send_keys(Keys.RETURN)
    firefox.maximize_window()
    sleep(5)
    pyautogui.click(x=1070, y=706)
    sleep(9)
    pyautogui.click(x=1200, y=100)
    sleep(5)
    pyautogui.click(x=437, y=478, clicks=2)
    sleep(1)
    pyautogui.click(x=437, y=478, button='right')
    sleep(1)
    pyautogui.click(x=478, y=540)
    sleep(1)
    pyautogui.click(x=190, y=560, button='right')
    pyautogui.click(x=242, y=588)
    sleep(1)
    pyautogui.click(x=615, y=700)
    sleep(2)
    pyautogui.click(x=85, y=12)
    sleep(1)
    pyautogui.click(x=115, y=215)
    pyautogui.click(x=1000, y=600)
    pyautogui.click(x=600, y=630, button='right')
    sleep(1)
    pyautogui.click(x=679, y=733)
    sleep(1)
    pyautogui.click(x=1075, y=720, clicks=2)
    sleep(4)
    pyautogui.click(x=715, y=702)
    sleep(1)
    value_found = False
    while not value_found:
        account_value = input('Account value: ')
        try:
            float(account_value)
            value_found = True
        except ValueError:
            print(f"{account_value} is not a number, please try again.")
    firefox.close()
    bank_one.set_value(account_value)


def total_cash_on_hand():
    total_value = bank_one.value + bank_two.value
    print(f'Total cash on hand: ${total_value}')
