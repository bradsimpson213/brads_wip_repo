from time import sleep
from new_years import new_years_logo
from datetime import datetime, timedelta
import os


class Countdown:
    def __init__(self, logo=new_years_logo):
        os.system("cls")
        self.__event = input("What event are we counting down to? ")
        self.__datetime = None
        self.__logo = logo
        self.run_timer()


    def set_datetime(self):
        new_date = input("Enter the countdown date in MM:DD:YYYY: ")
        month, day, year = new_date.split(':')
        new_time = input("Enter the countdown time in 24hr HH:MM format: ")
        hour, minute = new_time.split(':')
        self.__datetime = datetime(int(year), int(month), int(day), int(hour), int(minute))


    def run_timer(self):
        self.set_datetime()
        os.system("cls")

        while True:
            now = datetime.now()
            time_left = self.__datetime - now

            if time_left <= timedelta(0):
                print(self.__logo)
                break
 
            days = time_left.days
            seconds = time_left.seconds
            hours, seconds = divmod(seconds, 3600)
            minutes, seconds = divmod(seconds, 60)

            countdown_display = f"Time remaining until {self.__event}: {days} days, {hours:02d}:{minutes:02d}:{seconds:02d}"
            print(countdown_display, end="\r")
        
            sleep(1)
        

Countdown()
