from datetime import date, time, datetime
import math
import re
from calendar import monthrange
import traceback


def get_date():
    while True:
        the_date_in = input("Enter a date in MM/DD/YYYY format: ")
        the_date_in = re.sub("\s", "", the_date_in)
        split_date = the_date_in.split("/")
        if not len(split_date) == 3:
            print("Error, improper formatting for the date. Please try again.")
            continue
        if check_for_non_numbers(split_date):
            continue
        month, day, year = map(int, split_date)
        if year < 38:
            year += 2000
            print(f"Assuming you meant {year}...")
        elif year < 1970:
            print(
                f"Error, this program does not support a year as low as {year}. Please try again"
            )
            continue
        elif year > 2038:
            print(
                f"Error, this program does not support a year as high as {year}. Please try again"
            )
            continue
        if month < 1 or month > 12:
            print(
                "Error: month must be a whole number between 1 and 12. Please try again."
            )
            continue
        max_date = monthrange(year, month)[1]
        if day < 1 or day > max_date:
            print(
                f"Error: date must be a whole number between 1 and the max date for this month/year ({max_date}). Please try again."
            )
            continue

        return date(year, month, day)


def check_for_non_numbers(split_input):
    Error = False
    for num in split_input:
        try:
            int(num)
        except:
            print(f'Error: "{num}" is not a whole number. Please try again.')
            Error = True
            break
    return Error


def get_time():
    while True:
        the_time_in = input(
            "Enter a time in H:M format\nNOTE: You must either put the hour in 24 hour time (0-23) or add pm to the end of the time\n"
        )
        formatted_input = re.sub("P|p|A|a|M|m|\s", "", the_time_in)
        split_time = formatted_input.split(":")
        if not len(split_time) == 2:
            print("Error, improper formatting of time. Please try again.")
            continue
        if check_for_non_numbers(split_time):
            continue
        hour, minute = map(int, split_time)
        if "pm" in the_time_in.lower():
            hour += 12
        return time(hour, minute)


def time_until_str(target_datetime):
    seconds = (target_datetime - datetime.now()).total_seconds()
    if seconds >= 172800:
        return f"in {round(seconds/86400)} days"
    if seconds >= 86400:
        return "in a day"
    if seconds >= 7200:
        return f"in {round(seconds/3600)} hours"
    if seconds >= 3600:
        return "in an hour"
    if seconds >= 120:
        return f"in {round(seconds/60)} minutes"
    if seconds > 0:
        return "in a minute"
    if seconds <= -172800:
        return f"{abs(round(seconds/86400))} days ago"
    if seconds <= -86400:
        return "in a day"
    if seconds <= -7200:
        return f"{abs(round(seconds/3600))} hours ago"
    if seconds <= 3600:
        return "in an hour"
    if seconds <= -120:
        return f"{abs(round(seconds/60))} minutes ago"
    if seconds <= 0:
        return f"a minute ago"
    return f"Error, {seconds} not defined"


if __name__ == "__main__":
    try:
        target = datetime.combine(get_date(), get_time())
        print(
            "---------------------RESULT----------------------------------------------"
        )
        print(
            "Input to Discord:              Example Result (what discord will display):"
        )
        print(
            f"<t:{math.trunc(target.timestamp())}:R>               {time_until_str(target)}"
        )  # 4 minutes ago\in 4 minutes")
        print(
            f"<t:{math.trunc(target.timestamp())}:d>               {target.strftime('%m/%d/%Y')}"
        )  # 08/20/2021")
        print(
            f"<t:{math.trunc(target.timestamp())}:D>               {target.strftime('%B %d, %Y')}"
        )  # August 20, 2021")
        print(
            f"<t:{math.trunc(target.timestamp())}:t>               {target.strftime('%I:%M %p')}"
        )  # 8:49 PM")
        # print(f"<t:{math.trunc(target.timestamp())}:T>               {target.strftime('%-I:%M:%S %p')}") # 8:49:00 PM")
        print(
            f"<t:{math.trunc(target.timestamp())}:f>               {target.strftime('%B %d, %Y %I:%M %p')}"
        )  # August 20, 2021 8:49 PM")
        print(
            f"<t:{math.trunc(target.timestamp())}:F>               {target.strftime('%A, %B %d, %Y %I:%M %p')}"
        )  # Friday, August 20, 2021 8:49 PM")
    except KeyboardInterrupt:
        print("\nKeyboard Interrupt (ctrl+c), program shutting down")
    except Exception as e:
        print("\nHmm, you ran into an error I haven't found yet")
        print(
            "DM @[DSI] Pas2704#1283 on discord with a screenshot of the following so I can make a fix:"
        )
        print(
            "------------------------------------------------------------------------------------------"
        )
        print(repr(e))
        traceback.print_exc()
        print(
            "------------------------------------------------------------------------------------------"
        )
    finally:
        exit = input("Enter to Exit")
