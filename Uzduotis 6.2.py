import datetime
import calendar


class Anniversary:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.anniversary = datetime.datetime(year, month, day)

    def time_past_since(self):
        now = datetime.datetime.now()
        date_diff = now - self.anniversary
        year_p = round(date_diff.days / 365)
        month_p = (date_diff.days / 365) * 12
        hours_p = date_diff.days * 24
        minutes_p = round(date_diff.total_seconds() / 60)
        seconds_p = round(date_diff.total_seconds())
        return f"""
Has passed {year_p} year since the anniversary,
{month_p} months,
{date_diff.days} days,
{hours_p} hours,
{minutes_p} minutes,
{seconds_p} seconds"""

    def leap_or_not(self):
        if calendar.isleap(self.year):
            return f"{self.year} is leap year"
        else:
            return f"{self.year} is not leap"

    def minus_days(self, number_of_days):
        print(self.anniversary - datetime.timedelta(days=number_of_days))

    def plus_days(self, number_of_days):
        print(self.anniversary + datetime.timedelta(days=number_of_days))


anniversary = Anniversary(2000, 6, 10)
anniversary.leap_or_not()
print(anniversary.time_past_since())
print(anniversary.leap_or_not())
print(anniversary.minus_days(20))
print(anniversary.plus_days(20))
