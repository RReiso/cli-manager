from menu_item import MenuItem
from datetime import datetime
import utils
import os
from dotenv import load_dotenv
load_dotenv()


class ReminderItem(MenuItem):
    description = "Set a reminder"

    def __init__(self):
        self.REMINDER_WEBHOOK_URL = os.getenv("REMINDER_WEBHOOK_URL")

    def run(self):
        reminder = input("Reminder: ")

        while True:
            reminder_datetime = utils._get_datetime()
            now = datetime.now()
            diff_days = (reminder_datetime.date() - now.date()).days

            # check if datetime is in the future but not more than one month ahead (=> Zap error)
            if now >= reminder_datetime:
                print("Please, set a future date and time!")
            elif diff_days > 30:
                print("Dates cannot be more than a month in the future")
            else:
                break

        message = {"reminder": reminder, "date_time": reminder_datetime}

        utils._send_msg_to_webhook(message, self.REMINDER_WEBHOOK_URL)
        return utils.TaskStatus.SUCCESS
