import time
from datetime import date

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
today = date.today()
current_date = today.strftime("%Y|%m|%d")
year_now = today.strftime("%Y")
month_now = today.strftime("%m")
day_now = today.strftime("%d")


def count_days_since_today(init_year, init_month, init_day):
    initial_date = date(int(init_year), int(init_month), int(init_day))
    present_date = date(int(year_now), int(month_now), int(day_now))
    date_difference = present_date - initial_date
    return int(date_difference.days)


def count_days_from_today(future_year, future_month, future_day):
    initial_date = date(int(year_now), int(month_now), int(day_now))
    final_date = date(int(future_year), int(future_month), int(future_day))
    date_difference = final_date - initial_date
    return int(date_difference.days)


def add_numbers_in_list(list_of_numbers):
    total = 0
    for i in list_of_numbers:
        total += i
    return total


def find_line_of_search_result_in_file(file_name, string_to_search, num_of_results_to_display):
    line_number = 0
    list_of_results = []
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            line_number += 1
            if string_to_search in line:
                list_of_results.append(line_number)
    return list_of_results[(num_of_results_to_display - 1)]
