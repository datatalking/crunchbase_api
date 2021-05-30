# SOURCE https://rapidapi.com/blog/crunchbase-api-python-automated-sales-pipeline/
# FILENAME cruchbase_to_csv.py

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import json
import requests
import csv
from datetime import datetime, date, time timedelta, timezone


def main():
    cruchbase_data_grab():


def trigger_api(since_time):
    """A method to pull crunchbase data since specified time"""
    querystring = { "updated_since": str(since_time),
                    "sort_order":"updated_at ASC"}

    headers = {
        'x-rapidapi-host':"crunchbase-crunchbase-v1.p.rapidapi.com",
        'x-rapidapi-key': RAPIDAPI_KEY
    }
    url = "https://crunchbase-crunchbase-v1.p.rapidapi.com/odm-organizations"

    response = requests.request("GET", url, headers=headers,
                                params=querystring)
    if (200 == response.status_code):
        return json.loads(response.text)
    else:
        return None

    current_date = datetime.combine(date.today(), time(0, 0, 0))

    yesterday_date = current_date - timedelta(days=1)

    yday_timestamp_utc = int(yesterday_date.replace(tzinfo=timezone.utc).timestamp())

    print(yday_timestamp_utc)

    api_response = trigger_api(yday_timestamp_utc)


# Press the green button in the gutter to run the script.



def functions_inside_cruchbase_to_csv():
    print(cruchbase_data_grab.__doc__)
    print(print_hi().__doc__)


def cruchbase_data_grab():
    """A rest api from rapidAPI to extract json from cruchbase datacenter"""
    print("this function will prompt the user if they want to change the date since")



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.





if __name__ == '__main__':
    RAPIDAPI_KEY = "<YOUR_RAPID_KEY>"
    print_hi('PyCharm')
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
