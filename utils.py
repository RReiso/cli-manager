from dateutil.parser import parse
import requests
from requests.exceptions import HTTPError
from colors import bcolors
from enum import Enum


def _get_datetime():
    date_time = ""
    while not date_time:
        date_time = input("Date and time: ")
        if _is_date(date_time):
            date_time = parse(date_time)
        else:
            date_time = ""
    return date_time


def _is_date(string):
    try:
        parse(string)
        return True
    except ValueError:
        return False


def _send_msg_to_webhook(message, url):
    try:
        res = requests.post(url, data=message)
        # If the response was successful, no Exception will be raised
        res.raise_for_status()

        print(f"{bcolors.GREEN}Success!" + bcolors.ENDC)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')


class TaskStatus():
    SUCCESS = 0
    FAIL = 1
