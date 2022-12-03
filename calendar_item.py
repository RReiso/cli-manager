from menu_item import MenuItem
from datetime import datetime
import utils
import os
from dotenv import load_dotenv
load_dotenv()


class CalendarItem(MenuItem):
    description = "Create a calendar event"

    def __init__(self):
        self.CALENDAR_WEBHOOK_URL = os.getenv("CALENDAR_WEBHOOK_URL")

    def run(self):
        while True:
            calendar_datetime = utils._get_datetime()
            now = datetime.now()

            if now > calendar_datetime:
                print("Please, set a future date and time!")
            else:
                break

        description = input("Description: ")
        message = {"date_time": calendar_datetime, "description": description}

        utils._send_msg_to_webhook(message, self.CALENDAR_WEBHOOK_URL)
